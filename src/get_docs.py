import requests
import os
import re
import argparse
import json

# Base URL for UltraDNS docs
BASE_URL = "https://docs.ultradns.com"

# URL of the JavaScript file containing the API documentation paths
JS_FILE_URL = f"{BASE_URL}/Content/REST%20API/Data/Tocs/MSP_User_Guide_Chunk0.js"

def fetch_js_file():
    """Fetch the JavaScript file and extract the JSON-like structure."""
    response = requests.get(JS_FILE_URL)
    response.raise_for_status()
    content = response.text

    # Extract the define({...}) block content
    match = re.search(r"define\((\{.*\})\);", content, re.DOTALL)
    if not match:
        raise ValueError("Could not extract JSON data from JS file.")

    js_data = match.group(1)

    # Convert JavaScript-style object to valid JSON:
    # 1. Convert property names to quoted strings
    json_data = re.sub(r'([{,])\s*([a-zA-Z]+):', r'\1"\2":', js_data)
    
    # 2. Convert single quotes around keys to double quotes
    json_data = re.sub(r"'([^']+)'(?=\s*:)", r'"\1"', json_data)
    
    # 3. Convert single quotes around values to double quotes, including empty strings
    json_data = re.sub(r':\s*\'([^\']*)\'', r': "\1"', json_data)
    
    # 4. Handle arrays with proper quoting, including empty strings
    def fix_array_contents(match):
        array_content = match.group(1)
        # Handle empty strings in arrays
        fixed_content = re.sub(r"'([^']*)'", r'"\1"', array_content)
        return ': [' + fixed_content + ']'
    
    json_data = re.sub(r':\s*\[([^\]]+)\]', fix_array_contents, json_data)
    
    # 5. Remove trailing commas
    json_data = re.sub(r',\s*([}\]])', r'\1', json_data)
    
    try:
        return json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Processed JSON data: {json_data[:500]}...")  # Print part of processed data for debugging
        raise

def construct_urls(data):
    """Construct the full URLs and corresponding filenames."""
    urls = []
    
    for uri, meta in data.items():
        if uri == "___":  # Ignore the general REST API entry
            continue
        
        full_url = f"{BASE_URL}/Content/REST%20API{uri}"
        title = meta["t"][0]  # Extract the title

        # Format filename: lowercase, replace spaces and special characters
        filename = title.lower()
        filename = filename.replace(" ", "_")
        filename = filename.replace("/", "_")
        filename = filename.replace("(", "")
        filename = filename.replace(")", "")
        filename = filename.replace("â", "a")  # Handle special characters
        filename = re.sub(r'[^\w\-_.]', '_', filename)  # Replace any other special chars
        filename = filename + ".htm"
        
        urls.append((full_url, filename))
    
    return urls

def save_html(url, output_path):
    """Fetch the HTML from the given URL and save it to the specified path."""
    response = requests.get(url)
    response.raise_for_status()

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(response.text)

def main():
    parser = argparse.ArgumentParser(description="Scrape UltraDNS REST API documentation.")
    parser.add_argument("-o", "--output", type=str, default="./html", help="Output directory for HTML files.")
    args = parser.parse_args()

    # Ensure output directory exists
    os.makedirs(args.output, exist_ok=True)

    print(f"Fetching JavaScript index from {JS_FILE_URL}...")
    data = fetch_js_file()

    print("Constructing URLs...")
    urls = construct_urls(data)

    for url, filename in urls:
        output_path = os.path.join(args.output, filename)
        print(f"Fetching {url} -> {output_path}")
        
        try:
            save_html(url, output_path)
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")

    print("Scraping completed.")

if __name__ == "__main__":
    main()
