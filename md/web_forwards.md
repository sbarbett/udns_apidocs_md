

Skip To Main Content

Account

Settings

* * *

Logout

[](News and Updates.htm)

  * placeholder

Account

Settings

* * *

Logout

Filter:

  * All Files

Submit Search

# Web Forwards

UltraDNS Web Forwarding services allow you to redirect HTTP traffic from one
target to another. Forwarding services are invaluable tools for companies that
own or acquire multiple brands or have purchased many variations of their
domain names to protect their brand identity.

## Web Forwards DTOs

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)WebForward
DTO

The WebForward DTO creates, modifies, or retrieves a Web Forward.

Web Forward DTO

Attribute |  Description |  Type/ Restrictions  
---|---|---  
guid |  System-generated unique identifier for this object. |  Returned for Get Web Forwardscall.  
Required for Update and Partial Update of Web Forwards.  
requestTo |  Specifies the URL to be redirected. The anchor character (#) is supported when creating a unique record. For example,  _sub.abc.com/index.html_ and _sub.abc.com/index.html#anchor_ will be recognized and allowed. |  Required for creation. Must be a valid URL. Only http:// is acceptable. The page portion of the URL is optional.  
defaultRedirectTo |  URL destination of the redirect.  |  Required for creation.  
Either http:// or https:// are acceptable.  
defaultForwardType |  Type of forward. Valid values include:

  * Framed
  * HTTP_301_REDIRECT
  * HTTP_302_REDIRECT
  * HTTP_303_REDIRECT
  * HTTP_307_REDIRECT

|  Required for creation.  
records |  Present if you are using advanced web forward to specify where to forward, based on custom headers. |  Array.  
relativeForwardType |  The Type of relative forward. Valid values include:

  * PARAMETER â Parameter is appended to the target path.
  * PATH â Path is appended to the target path.
  * PARAMETER_AND_PATH â Both the Path and Parameter are appended to the target path.

|  String.  
records/redirectTo |  URL destination of the redirect. |  Required on create (if records are present). Must be a valid URL. Can include a port number.   
Either http:// or https:// are acceptable.  
records/forwardType |  Type of forward. Valid values include:

  * Framed
  * HTTP_301_REDIRECT
  * HTTP_302_REDIRECT
  * HTTP_303_REDIRECT
  * HTTP_307_REDIRECT

|  Required on create (if records are present).  
records/priority |  Order for a record to match. Lower numbers have higher priority. |  Positive integer. Required on create (if records are present).  
records/rules |  Array of one or more rules. |  Array Required on create (if records are present).  
records/rules/header |  Name of the header to match. |  String Required on create (if records are present). Must be a header returned by the Get Custom HTTP Headers of Accountcall.  
records/rules/matchCriteria |  Type of match to perform. Valid values include:

  * BEGINS_WITH
  * CONTAINS
  * ENDS_WITH
  * MATCHES

|  Required on create (if records are present).  
records/rules/value |  Expected header value. |  String Required on create (if records are present).  
records/rules/caseInsensitive |  Flag to indicate if the match takes case into account (true) or not (false). |  Boolean If not present, defaults to false.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)WebForwardList
DTO

The webForwardList is returned for the list of web forwards.

WebForwardList DTO

Attribute |  Description |  Type  
---|---|---  
webForwards/webForward |  One of the returned webForwards. Structure matches the webForward DTO described above. |  Web Forward DTO  
queryInfo/q |  The query used to construct the list. |  String  
queryInfo/sort |  The sort column used to order the list. |  String  
queryInfo/reverse |  Whether the list is ascending (false) or descending (true). |  Boolean  
queryInfo/limit |  The maximum number of rows requested. |  Integer  
resultInfo/totalCount |  Count of all zones in the system for the specified query. |  Integer  
resultInfo/offset |  The position in the list for the first returned element (0 based). |  Integer  
resultInfo/returnedCount |  The number of records returned. |  Integer  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Custom Header
List DTO

The Custom Header List returns the list of custom headers that are or have
been defined for an account.

Custom header List DTO

Attribute |  Description |  Type  
---|---|---  
**names** |  An array of the custom header names. |  Array  
  
JSON Example: Custom Header List

{  
"names":  
[  
" ",...  
]  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Web Forward
Create DTO

The REST API returns the guid when you create a web forward.

Web Forward Create DTO

Attribute |  Description |  Type  
---|---|---  
**guid** |  The unique identifier for the web forward. |  String  
  
JSON Example: Web Forward Create

{  
"guid": "0909433CB37A13A8"  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Add Custom
HTTP Header to Account

**Method and URI** :

POST https://api.ultradns.com/accounts/{accountName}/customheaders

**Parameters** : None

**Body** : Must include a Custom Header List DTO.

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If you don't have permission to create custom headers.

  * If you don't have permission to access the specified account or the account doesn't exist.

  * If the custom header already exists.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get Custom
HTTP Headers of Account

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/customheaders

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a Custom
Header List DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If you don't have permission to access the specified account.

  * If the account doesn't exist.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete Custom
HTTP Header of Account

**Method and URI** :

DELETE
https://api.ultradns.com/accounts/{accountName}/customheaders/{headerName}

**Parameters** : None

**Body** : None

**Response** : If delete completes, Status Code 204 is returned with no
content in the body.

**Errors** : An error is returned under the following conditions:

  * If you don't have permission to delete custom headers.

  * If you don't have permission to access the specified account, or if the account doesn't exist.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create Web
Forwards

**Method and URI:**

POST https://api.ultradns.com/zones/{zoneName}/webforwards

**Parameters** : None

**Body** : Must include a WebForward DTO.

**Response** : If task completes, Status Code 201 is returned with a Web
Forward Create DTO in the body content.

**Errors** : An error is returned under the following conditions:: An error is
returned under the following conditions:

  * If you don't have permission to create web forwards.

  * If a web forwards already exsists for the <zone name>.

JSON Example: Create Web Forwards

{  
"requestTo": "a.demo-kb-1.com",  
"defaultRedirectTo": "https://b.demo-kb-1.co.us",  
"defaultForwardType": "HTTP_301_REDIRECT",  
"records": [  
{  
"redirectTo": "c.demo-kb-1.com.in",  
"forwardType": "HTTP_301_REDIRECT",  
"priority": 1,  
"rules": [  
{  
"header":"Accept",  
"matchCriteria": "CONTAINS",  
"value": "kb",  
"caseInsensitive": false  
}  
]  
}  
]  
}

JSON Example: Create Web Forwards with anchor character (#)

In the following example, duplicate Web Forward records are created, however,
one record is created using the anchor character (#). In this scenario, an
error would not occur as the records are not duplicates due to the handling of
the anchor character (#) making the record unique.

{

"requestTo":"a.demo-kb-1.com/index.html",

"defaultRedirectTo":"https://b.demo-kb-1.co.us",

"defaultForwardType":"HTTP_301_REDIRECT"

}

JSON Example: Create Web Forwards with anchor character (#) ```json {
"requestTo": "a.demo-kb-1.com/index.html#anchor", "defaultRedirectTo":
"https://b.demo-kb-1.co.us", "defaultForwardType": "HTTP_301_REDIRECT" } ```

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get Web
Forwards

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/webforwards

**Parameters** : You can include the following:

Web Forwards Parameters

Parameter |  Description |  Type  
---|---|---  
q |  The query used to construct the list. Query operators are:

  * type - Valid values include:
    * HTTP_301_REDIRECT
    * HTTP_302_REDIRECT
    * HTTP_303_REDIRECT
    * HTTP_307_REDIRECT
  * Advanced
    * advanced - Valid values are either true or false.
    * name - Valid values include any string, and will map to anything in either the host or the target.

|  String  
offset |  The position in the list for the first returned element (0 based) Default value is 0. |  Integer  
Limit |  The maximum number of rows requested. Default value is 100. |  Integer  
sort |  The sort column used to order the list. Valid sort values are:

  * REQUEST_TO (this is the default)
  * REDIRECT_TO
  * TYPE
  * DOMAIN
  * ADVANCED

|  String  
reverse |  Whether the list is ascending (false) or descending (true). Default value is false. |  Boolean  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
WebForwardList DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If you don't have permission to list web forwards.

JSON Example: Get Web Forwards

{  
"queryInfo": {  
"sort": "REQUEST_TO",  
"reverse": false,  
"limit": 100  
},  
"resultInfo": {  
"totalCount": 3,  
"offset": 0,  
"returnedCount": 3  
},  
"webForwards": [  
{  
"guid": "0909433CB37A13A8",  
"requestTo": "a.demo-kb-1.com",  
"defaultRedirectTo": "http://b.demo-kb-1.co.us",  
"defaultForwardType": "HTTP_301_REDIRECT",  
"records": [  
{  
"redirectTo": "http://c.demo-kb-1.com.in/",  
"forwardType": "HTTP_302_REDIRECT",  
"priority": 1,  
"rules": [  
{  
"header": "Accept",  
"matchCriteria": "CONTAINS",  
"value": "kb",  
"caseInsensitive": false  
}  
]  
},  
{  
"redirectTo": "https://c.demo-kb-1.com.in/",  
"forwardType": "HTTP_302_REDIRECT",  
"priority": 2,  
"rules": [  
{  
"header": "Accept",  
"matchCriteria": "CONTAINS",  
"value": "kb",  
"caseInsensitive": false  
}  
]  
}  
]  
},  
{  
"guid": "0908433BB29E91EB",  
"requestTo": "www.demo-kb-1.com/community1/investors-foundation",  
"defaultRedirectTo": "http://b1.demo-kb-1.co.us",  
"defaultForwardType": "HTTP_301_REDIRECT"  
},  
{  
"guid": "0908433BB29D85C2",  
"requestTo": "www.demo-kb-1.com/community/investors-foundation",  
"defaultRedirectTo": "http://b1.demo-kb-1.co.us",  
"defaultForwardType": "HTTP_301_REDIRECT"  
}  
]  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update Web
Forward

**Method and URI** :

PUT https://api.ultradns.com/zones/{zoneName}/webforwards/{guid}

**Parameters** : None

**Body** : Must include a WebForward DTO.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If you don't have permission to update web forwards.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update Web Forwards

The Partial Update Web Forward is a PATCH or JSON PATCH call and is generated
as follows:

**Method and URI** :

PATCH https://api.ultradns.com/zones/{zoneName}/webforwards/{guid}

**Parameters** : None

**Body** : For standard XML or JSON calls, you must include a WebForward DTO.

For JSON PATCH formatted updates, the body must include a [JSON PATCH
DTO](Making Updates via JSON PATCH.htm#_Ref399931231).

**Patchable Objects for Web Forward:**

  * biz.example.ultra.rest.dto.WebForward

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If the {zoneName} is not valid.

  * If you don't have permission to update web forwards.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete Web
Forwards

**Method and URI** :

DELETE https://api.ultradns.com/zones/{zoneName}/webforwards/{guid}

**Parameters** : None

**Body** : None

**Response** : If delete completes, Status Code 204 is returned with no
content in the body.

**Errors** : An error is returned under the following conditions:

  * If you don't have permission to delete web forwards.

  * If the {guid} is not valid.

