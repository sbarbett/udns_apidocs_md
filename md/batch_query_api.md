

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

# Batch Query API

Similar to the Batch API function, the Batch Query API provides the ability to
run multiple GET operations as a single unit. If any of the calls fail with a
response status other than a 404, the request will end and an error message
will be returned.

If all of the calls succeed, a success message will be returned. If a GET
response returns a 404 status, the other GET requests running will return data
(if there is data to provide).

**Asynchronous (Async)**

Async is a new parameter that can be added to the method call for large Batch
API requests that might time out. When this value is set to true, the Batch
API will run the call as a background task, and provide an X-Task-ID that can
be used to retrieve the status of the task once it has finished running.

The default value for async is false, so unless it is set to true, Batch API
calls will run as normal.

![](../Resources/Images/Rest-API_User_Guide/Introduction_80x93.png) |  Depending on the size of your Batch (or Batch Query) request, and on the size of your UltraDNS dataset, the Batch request can take significant time to execute. In certain cases, its execution time may exceed the REST API service idle timeout, resulting in a 504 response status.  When Batch (or Batch Query) is run in an asynchronous mode (by providing HTTP parameter async=true), it is not subjected to the REST API service idle timeout. Therefore, the asynchronous method should be preferred for the larger, more complex requests.  
---|---  
  
![](../Resources/Images/Rest-API_User_Guide/Introduction.png) |  The current size limit for a BATCH API request is 1,000 records. If the records exceed 1,000, a 4XX validation error message will be returned.   
---|---  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create a
Batch Query Request

**Method and URI** :

POST https://restapi.ultradns.com/v1/batch/query

**Parameters** : None

**Body** : Requires the use of a Batch Query Request DTO.

**Response** : If task completes, Status Code 200 OK is returned with a Batch
Query Response DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * Error DTOs will be embedded in the response for invalid requests.

  * Error DTO returned when invalid methods or URIs are used.

JSON Example: Batch Query Request

[  
{  
"method": "GET",  
"uri":"/v1/zones/zone.name./rrsets"  
},  
},  
{  
"method": "GET",  
"uri":"/v1/zones/zone.name./webforwards"  
},  
{  
"method": "GET",  
"uri":"/v1/zones/zone.name./mail/blocks"  
}  
]

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create a
Batch Query Request using Async

**Method and URI** :

POST https://restapi.ultradns.com/v1/batch/query?async=true

**Parameters** : None

**Body** : Requires the use of a Batch Query Request DTO.

**Response** : If task completes, Status Code 200 OK is returned with a Batch
Query Response DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * Error DTOs will be embedded in the response for invalid requests.

  * Error DTO returned when invalid methods or URIs are used.

JSON Example: Creating Batch Query request with async=true

[  
{  
"method": "GET",  
"uri": "/v1/accounts/teamrest/dirgroups/ip/foo"  
},  
{  
"method": "GET",  
"uri": "/v1/accounts/teamrest/dirgroups/ip/non-existing"  
},  
{  
"method": "GET",  
"uri": "/v1/accounts/teamrest/dirgroups/ip/bar"  
}  
]

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get Task
Status of Async Batch Query Request via X-Task-Id

If the response returns a âPendingâ message, the Headers section will
display an X-Task-Id. Use the X-Task-Id to check the status of your pending
Batch API call.

![](../Resources/Images/Rest-API_User_Guide/Batch Query API_740x141.png)

Batch Query Async X-Task-Id in the Headers Section

**Method and URI** :  

GET https://restapi.ultradns.com/v1/tasks/{X-Task-Id}

JSON Example: Response using the X-Task-Id to retrieve the status of the Batch
Query request

{  
"taskId": "30f976cf-0d7a-48d0-99a6-002eed41868d",  
"code": "COMPLETE",  
"message": "Batch operation completed.",  
"resultUri": /tasks/30f976cf-0d7a-48d0-99a6-002eed41868d/result"  
}

When the âcodeâ parameter returns a âCompleteâ message, you can then
use the âresultUriâ to check the result of your Batch request.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get Results
of Async Batch Query Request Using X-Task-Id

**Method and URI** :

GET https://restapi.ultradns.com/v1/tasks/{resultUri}/result

JSON Example: Response using resultUri to get the Batch Query API request

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
Batch Query Request Using X-Task-Id

Once your Batch Query request is completed, and you have used the X-Task-Id to
retrieve your result, your next step is to delete the task from the REST API.

**Method and URI** :

DELETE https://restapi.ultradns.com/v1/tasks/{X-Task-Id}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 204 is returned with no body
content.

**Errors** : An error is returned under the following conditions:

  * If the X-Task-Id is invalid.

### Batch Query Request DTO

A batch query request is composed of a list of Batch Query Requests DTOs. The
following table provides the structure required to submit a batch query
request.

Batch Query Request DTO

Field |  Description |  Type  
---|---|---  
method |  The HTTP method that is used to submit this request. Valid values are GET. Only GET is allowed for this API. |  String  
uri |  The path for the request, which includes any query parameters.  Note that this is absolute, and not relative. It must start with /v1. |  String  
body |  Required for calls that require a body, otherwise ignored. This is the body that would be submitted for the specified method and uri. |  String  
  
JSON Example: Batch Query Body Request

JSON Example: Batch Query Body Request ```json { "method": "GET", "uri":
"https://api.ultradns.com/zones/x.map.com./rrsets/TXT/foo.map.com", "body": {
"rdata": [ "ab12345" ] } } ```

### Batch Query Response DTO

The following table provides the response that is sent for each of the Batch
Query Request entries. Like the Batch request, the Batch Query response is
composed of a list of Batch Response DTOs.

Batch Query Response DTO

Field |  Description |  Type  
---|---|---  
status |  The HTTP status code returned for this batch query request. |  Integer  
response |  The body returned for this batch query request. For any 204 status responses (no content) that are returned, this data will not be present. |  Object  
  
JSON Example: Batch Query Response

[  
{  
"status": 200,  
"response": {  
"zoneName": "000-conversion-1.com.",  
"rrSets": [  
{  
"ownerName": "000-conversion-1.com.",  
"rrtype": "MX (15)",  
"ttl": 300,  
"rdata": [  
"10 crsmail.ultradns.net."  
]  
},  
{  
"ownerName": "000-conversion-1.com.",  
"rrtype": "NS (2)",  
"ttl": 86400,  
"rdata": [  
"udns1.ultradns.net.",  
"udns2.ultradns.net."  
]  
},  
{  
"ownerName": "000-conversion-1.com.",  
"rrtype": "SOA (6)",  
"ttl": 86400,  
"rdata": [  
"udns1.ultradns.net.raj\\\\.neustar.biz. 2016120726 10800 3600 2592000 86400"  
]  
}  
]  
}  
},  
{  
"status": 404,  
"response": [  
{  
"errorCode": 70002,  
"errorMessage": "Data not found."  
}  
]  
},  
{  
"status": 200,  
"response": {  
"queryInfo": {  
"sort": "REQUEST_TO",  
"reverse": false,  
"limit": 100  
},  
"resultInfo": {  
"totalCount": 1,  
"offset": 0,  
"returnedCount": 1  
},  
"webForwards": [  
{  
"guid": "090842F8ADF5DD6C",  
"requestTo": "owner1.000-conversion-1.com/index.html",  
"defaultRedirectTo": "http://owner2.000-conversion-1.com/index.jsp",  
"defaultForwardType": "HTTP_301_REDIRECT"  
}  
]  
}  
}  
]

JSON Example: Batch Query Response with async=true

[  
{  
"status": 200,  
"response": {  
"name": "foo",  
"description": "Sample ip group for foo",  
"ips": [  
{  
"cidr": "172.0.0.0/29"  
},  
{  
"cidr": "172.0.0.8/29"  
}  
],  
"recordCount": 0  
}  
},  
{  
"status": 404,  
"response": [  
{  
"errorCode": 80001,  
"errorMessage": "Cannot find any directional group for the given group name"  
}  
]  
},  
{  
"status": 200,  
"response": {  
"name": "bar",  
"description": "Sample ip group for bar",  
"ips": [  
{  
"cidr": "172.0.0.16/29"  
},  
{  
"cidr": "172.0.0.24/29"  
},  
{  
"cidr": "172.0.0.32/29"  
}  
],  
"recordCount": 0  
}  
}  
]

