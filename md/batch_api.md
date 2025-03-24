

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

# Batch API

The Batch API provides the ability to run multiple requests as a single unit.
The Rest API will always process the individual requests sequentially,
following the request order in the Batch API payload. The set of configuration
changes contained amongst all of the requests in the batch will be committed
to the UltraDNS configuration database, upon successful completion of all the
requests

If any request in the batch fails, the batch request ends and all of the
requests are then rolled back with an error message returned.

For instance, if there are four requests in a Batch API payload (A,B,C and D)
and one of the requests fails (request C), the REST API will rollback
everything contained in the Batch API request.

If your batch request contains GET calls only, using [Batch Query API](Batch
Query API.htm#_Ref471981146) is typically more appropriate because if does not
stop the execution when an individual call returns a 404 response status.

It is legal to put a single POST, PUT, PATCH, or DELETE call in a batch, but
it will have the same semantics as making the single call directly.

![](../Resources/Images/Rest-API_User_Guide/Introduction_65x75.png) |  The current size limit for a BATCH API request is 1,000 records. If the records exceed 1,000, a 4xx validation error message will be returned.   
---|---  
  
**Asynchronous (Async)**

Async is a new parameter that can be added to the method call for large Batch
API requests that might time out. When this value is set to true, the Batch
API will run the call as a background task, and provide an X-Task-ID that can
be used to retrieve the status of the task.

The default value for async is false, so unless it is set to true, Batch API
calls will run as normal.

![](../Resources/Images/Rest-API_User_Guide/Introduction_74x86.png) |  Depending on the size of your Batch (or Batch Query) request, and on the size of your UltraDNS dataset, the Batch request can take significant time to execute. In certain cases, its execution time may exceed the REST API service idle timeout, resulting in a 504 response status.  When Batch (or Batch Query) is run in an asynchronous mode (by providing HTTP parameter async=true), it is not subjected to the REST API service idle timeout. Therefore, the asynchronous method should be preferred for the larger, more complex requests..  
---|---  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create a
Batch Request

**Method and URI** :

POST https://restapi.ultradns.com/v1/batch

**Parameters** : None

**Body** : Requires the use of a Batch Request DTO.

**Response** : If task completes, Status code 200 OK is returned for the batch
call itself, and a Batch Response DTO in the body content.

NOTE: The Batch Response DTO contains individual status codes returned for
each call included in the batch.

**Errors** : An error is returned under the following conditions:

  * Error DTOs will be embedded in the response for invalid requests.

  * Error DTO returned when invalid methods or URIs are used.

JSON Example: Batch API Request

[  
{  
"method": "POST",  
"uri": "/v1/zones/example.invalid/rrsets/A/foo",  
"body": {  
"ttl": 300,  
"rdata": ["1.2.3.4"]  
}  
},  
{  
"method": "POST",  
"uri": "/v1/zones/example.invalid/rrsets/A/bar",  
"body": {  
"ttl": 300,  
"rdata": ["10.20.30.40"]  
}  
},  
{  
"method": "DELETE",  
"uri": "/v1/zones/example.invalid/rrsets/A/baz"  
}  
]

JSON Example: Batch API Response

[  
{  
"status": 201,  
"response": {  
"message": "SUCCESSFUL"  
}  
},  
{  
"status": 201,  
"response": {  
"message": "SUCCESSFUL"  
}  
},  
{  
"status": 204  
}  
]

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create a
Batch Request using Async

The async parameter, when added to the method, allows you to create a Batch
request and receive a taskID while the operation executes in the background
instead of receiving a 504 response status due to timeout.

**Method and URI** :

POST https://restapi.ultradns.com/v1/batch?async=true

**Body** : Requires the use of a Batch Request DTO .

Once your Batch request is completed, and you have used the X-Task-Id to
retrieve your result, your next step is to delete the task from the REST API.

Method and URI:

DELETE https://restapi.ultradns.com/v1/tasks/{X-Task-Id}

**Response** : If task completes, Status Code 204 is returned with no body
content.

JSON Example: Creating Batch Request for GlobalIP Groups with async=true

[  
{  
"method": "POST",  
"uri": "v1/accounts/teamrest/dirgroups/ip/foo",  
"body": {  
"name": "foo",  
"description": "Sample ip group for foo",  
"ips": [  
{  
"cidr": "172.0.0.0/29"  
},  
{  
"cidr": "172.0.0.8/29"  
},  
{  
"cidr": "172.0.0.16/29"  
}  
]  
}  
},  
{  
"method": "POST",  
"uri": "v1/accounts/teamrest/dirgroups/ip/bar",  
"body": {  
"name": "bar",  
"description": "Sample ip group for bar",  
"ips": [  
{  
"cidr": "172.0.0.24/29"  
},  
{  
"cidr": "172.0.0.32/29"  
}  
]  
}  
}  
]

**Response** : Status code 202 is returned with a Pending message and an
X-Task-Id in the header.

{  
"message": "Pending"  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get Task
Status of Async Batch Request via X-Task-Id

From the Headers section, use the X-Task-Id to check the status of your
pending Batch API call.

![](../Resources/Images/Rest-API_User_Guide/Batch API_740x141.png)

Async X-Task-Id in the Headers Section

**Method and URI** :

GET https://restapi.ultradns.com/v1/tasks/{X-Task-Id}

**Parameters** : None

**Body** : None

**Response** : If task completes, see the JSON example response below.

**Errors** : An error is returned under the following conditions:

  * If the X-Task-Id is not valid.

JSON Example: Response from X-Task-Id to retrieve Batch API request status

{  
"taskId": "30f976cf-0d7a-48d0-99a6-002eed41868d",  
"code": "COMPLETE",  
"message": "Batch operation completed.",  
"resultUri": /tasks/30f976cf-0d7a-48d0-99a6-002eed41868d/result"  
}

When the âcodeâ parameter returns a âCOMPLETEâ message, you can use
the âresultUriâ to check the result of your Batch request.

In the above example, two requests were made in the Batch request, so the
response will contain the status of both requests.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get Results
of Async Batch Request Using X-Task-Id

**Method and URI** :

GET https://restapi.ultradns.com/v1/tasks/{resultUri]/result

JSON Example: Response using resultUri to get the Batch API request

[  
{  
"status": 201,  
"response": {  
"message": "Successful"  
}  
}  
{  
"status": 201,  
"response": {  
"message": "Successful"  
}  
}  
]

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete a
Batch Request X-Task-Id

Once your Batch request is completed, and you have used the X-Task-Id to
retrieve your result, delete the task from the REST API.

**Method and URI** :

DELETE https://restapi.ultradns.com/v1/tasks/{X-Task-Id}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 204 is returned with no body
content.

**Errors** : An error is returned under the following conditions:

  * If the X-Task-Id is not valid.

### Batch Request DTO

A batch request is composed of a list of Batch Request DTOs. This is the
structure used to request batch changes via the API calls.

Batch Request DTO

Field |  Description |  Type  
---|---|---  
**method** |  The HTTP method that is used to submit this request. Valid values are POST, PUT, PATCH, and DELETE. GET is allowed, but is discouraged. |  String  
**uri** |  The path for the request, which includes any query parameters.  Note that this is absolute, and not relative. It must start with /v1. |  String  
**body** |  Required for calls that require a body, otherwise ignored. This is the body that would be submitted for the specified method and uri. |  Object  
  
### Batch Response DTO

This is the response sent for each of the Batch Request entries. Like the
Batch Request, it is composed of a list of Batch Response DTOs

Batch Response DTO

Field |  Description |  Type  
---|---|---  
status |  The HTTP status code returned for each call in this batch request. |  Integer  
response |  The body returned for each call in this batch request. For any 204 status responses (no content) that are returned for successful Delete calls, a response body will not be present. |  Object  
taskId |  Returned when a X-Task-ID is used to check the status of a Batch API call. (Retrieved from the Header section) |  String

