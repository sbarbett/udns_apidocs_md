

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

# Get the API Version

The API Version call provides the version of the REST API currently in
production.

This call does not require an Authorization header to be specified, which
allows it to be used to verify that there are no networking issues between a
client and the REST API server.

**Method and URI** :

GET https://api.ultradns.com/version

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
Version DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * None

### Version DTO

This is the structure returned by a request for the API version.

Version DTO

Field |  Description |  Type  
---|---|---  
  
**version** |  Contains the version of the server. If the server cannot determine its version, it will return the string "Unknown". The format of the version string is:   
_Major.Minor.BugFix-buildId (example: 1.9.0-20140403224104.2beec3b)_ |    
String  
  
JSON Example: Version

{  
"version": "1.9.0-20140403224104.2beec3b"  
}

