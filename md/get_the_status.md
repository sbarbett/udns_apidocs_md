

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

# Get the Status

The Get Status call provides a simple way to determine if the REST API is
running, and to make sure you are connecting to the UltraDNS Portal with
proper authorization.

**Method and URI** :

GET https://api.ultradns.com/status

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a Get
Status DTO containing the status response message.

**Errors** : An error is returned under the following conditions:

  * None

![](../Resources/Images/Rest-API_User_Guide/Get the Status.png)

Get Status with Status Response Message

### Get Status DTO

The following table shows the structure of the DTO returned by a request for
status.

Get Status DTO

Attribute |  Description |  Type  
---|---|---  
**message** |  Contains any message from the server about the result of your request. |  String  
  
JSON Example: Status

{  
"message": "Good"  
}

