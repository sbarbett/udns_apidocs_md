import os
import argparse
from bs4 import BeautifulSoup
import re
import json
import html2text

def clean_text(text):
    """Clean up text content."""
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove spaces at start/end of lines
    text = text.strip()
    # Fix line wrapping for URLs
    text = re.sub(r'(\[.*?\])\s*\(([^\s)]+)\)', r'\1(\2)', text)
    # Ensure proper line breaks for paragraphs
    text = re.sub(r'([.!?])\s+([A-Z])', r'\1\n\n\2', text)
    return text

def extract_json(text):
    """Extract and format JSON from text."""
    try:
        # Remove any "JSON Example:" prefix
        text = re.sub(r'^.*?JSON.*?Example:?\s*', '', text, flags=re.IGNORECASE|re.MULTILINE)
        
        # Find the JSON content between the first { and last }
        start = text.find('{')
        end = text.rfind('}') + 1
        if start == -1 or end == 0:
            return None
            
        json_text = text[start:end]
        
        # Replace all newlines and extra spaces with a single space
        json_text = re.sub(r'\s+', ' ', json_text)
        
        # Parse and format the JSON
        parsed = json.loads(json_text)
        return json.dumps(parsed, indent=2)
    except (json.JSONDecodeError, IndexError):
        return None

def handle_code_blocks(element):
    """Convert code blocks and inline code."""
    if element.name in ['pre', 'code']:
        code = element.get_text().strip()
        
        # Check if this is a JSON example
        if '{' in code and '}' in code:
            try:
                # Try to extract and format JSON
                json_text = re.search(r'\{.*\}', code, re.DOTALL)
                if json_text:
                    json_text = json_text.group(0)
                    # Clean up the JSON text
                    json_text = re.sub(r'\s+', ' ', json_text)
                    # Parse and format the JSON
                    parsed = json.loads(json_text)
                    return f"\n```json\n{json.dumps(parsed, indent=2)}\n```\n"
            except (json.JSONDecodeError, AttributeError):
                pass
        
        # Handle regular code blocks
        if element.name == 'pre':
            # Try to detect the language
            code_class = element.get('class', [])
            lang = ''
            if code_class and any('language-' in c for c in code_class):
                lang = next(c.replace('language-', '') for c in code_class if 'language-' in c)
            elif any(keyword in code.lower() for keyword in ['function', 'var ', 'let ', 'const ', '=>']):
                lang = 'javascript'
            elif any(keyword in code.lower() for keyword in ['def ', 'class ', 'import ', 'from ']):
                lang = 'python'
            return f"\n```{lang}\n{code}\n```\n"
        return f"`{code}`"
    return None

def handle_lists(element):
    """Convert ordered and unordered lists."""
    if element.name == 'ul':
        items = []
        for li in element.find_all('li', recursive=False):
            item_text = convert_element_to_md(li)
            items.append(f"* {item_text}")
        return "\n".join(items) + "\n"
    elif element.name == 'ol':
        items = []
        for i, li in enumerate(element.find_all('li', recursive=False), 1):
            item_text = convert_element_to_md(li)
            items.append(f"{i}. {item_text}")
        return "\n".join(items) + "\n"
    return None

def handle_headers(element):
    """Convert header elements."""
    if element.name and element.name.startswith('h') and len(element.name) == 2:
        level = int(element.name[1])
        text = clean_text(element.get_text())
        return f"{'#' * level} {text}\n\n"
    return None

def handle_links(element):
    """Convert anchor tags to markdown links."""
    if element.name == 'a' and element.get('href'):
        text = clean_text(element.get_text())
        href = element['href']
        if not text:
            text = href
        return f"[{text}]({href})"
    return None

def handle_tables(element):
    """Convert HTML tables to markdown tables."""
    if element.name != 'table':
        return None
    
    markdown_table = []
    
    # Handle headers
    headers = []
    for th in element.find_all('th'):
        headers.append(clean_text(th.get_text()))
    
    if headers:
        markdown_table.append('| ' + ' | '.join(headers) + ' |')
        markdown_table.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')
    
    # Handle rows
    for tr in element.find_all('tr'):
        row = []
        for td in tr.find_all(['td', 'th']):
            cell_text = clean_text(td.get_text())
            row.append(cell_text)
        if row:  # Skip empty rows
            markdown_table.append('| ' + ' | '.join(row) + ' |')
    
    return '\n'.join(markdown_table) + '\n\n'

def convert_element_to_md(element):
    """Recursively convert an HTML element and its children to Markdown."""
    if isinstance(element, str):
        return clean_text(element)
    
    # Handle different element types
    for handler in [handle_code_blocks, handle_lists, handle_headers, handle_links, handle_tables]:
        result = handler(element)
        if result is not None:
            return result
    
    # Handle paragraphs
    if element.name == 'p':
        text = ''.join(convert_element_to_md(child) for child in element.children)
        return f"{text}\n\n"
    
    # Handle emphasis
    if element.name == 'em' or element.name == 'i':
        return f"_{convert_element_to_md(element.string)}_"
    if element.name == 'strong' or element.name == 'b':
        return f"**{convert_element_to_md(element.string)}**"
    
    # Handle line breaks
    if element.name == 'br':
        return '\n'
    
    # Handle horizontal rules
    if element.name == 'hr':
        return '---\n\n'
    
    # Recursively process child elements
    return ''.join(convert_element_to_md(child) for child in element.children)

def format_json_block(text):
    """Format a block of text containing JSON."""
    try:
        # Parse and format
        parsed = json.loads(text)
        formatted = json.dumps(parsed, indent=2)
        return formatted
    except json.JSONDecodeError:
        return text

def extract_json_example(element):
    """Extract a complete JSON example from a series of Code paragraphs."""
    if not element.find_previous_sibling('p', class_='Examples'):
        return None
        
    # Get all consecutive Code paragraphs
    json_lines = []
    current = element
    while current and current.get('class') == ['Code']:
        text = current.get_text().strip()
        if text:
            json_lines.append(text)
        current = current.find_next_sibling('p')
    
    # Join the lines and try to parse
    json_text = ''.join(json_lines)
    try:
        parsed = json.loads(json_text)
        return json.dumps(parsed, indent=2)
    except json.JSONDecodeError:
        return None

def html_to_md(html_content):
    """Convert HTML to Markdown."""
    soup = BeautifulSoup(html_content, 'html5lib')
    
    # Find and format JSON examples
    for p in soup.find_all('p', class_='Code'):
        if p.find_previous_sibling('p', class_='Examples'):
            formatted_json = extract_json_example(p)
            if formatted_json:
                # Replace all related Code paragraphs with the formatted JSON
                prefix = p.find_previous_sibling('p', class_='Examples').get_text().strip()
                new_p = soup.new_tag('p')
                new_p.string = f"{prefix}\n```json\n{formatted_json}\n```\n"
                p.replace_with(new_p)
                
                # Remove subsequent Code paragraphs that were part of this JSON
                current = new_p.find_next_sibling('p')
                while current and current.get('class') == ['Code']:
                    next_p = current.find_next_sibling('p')
                    current.decompose()
                    current = next_p
    
    # Convert HTML to markdown
    text = html2text.html2text(str(soup))
    return text

def convert_html_to_md(input_folder, output_folder):
    """Converts all HTML files in input_folder to Markdown and saves them in output_folder."""
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".htm"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace(".htm", ".md"))

            print(f"Converting: {input_path} → {output_path}")
            
            try:
                # Read the file in binary mode and decode with errors='ignore'
                with open(input_path, "rb") as f:
                    html_content = f.read().decode('utf-8', errors='ignore')

                md_content = html_to_md(html_content)

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(md_content)
                    
                print(f"✓ Successfully converted {filename}")
            except Exception as e:
                print(f"✗ Error converting {filename}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Convert HTML files to Markdown.")
    parser.add_argument("-i", "--input", type=str, default="./html", help="Input folder containing HTML files.")
    parser.add_argument("-o", "--output", type=str, default="./md", help="Output folder for Markdown files.")
    args = parser.parse_args()

    convert_html_to_md(args.input, args.output)
    print("\nConversion completed!")

if __name__ == "__main__":
    main()
