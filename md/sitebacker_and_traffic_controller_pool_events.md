

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

# SiteBacker and Traffic Controller Pool Events

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create an
Event

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/events

**Parameters** : None

**Body** : Must include an EventInfo DTO.

**Response** : If task completes, Status Code 201 is returned with a Location
Header containing a URI, and the GUID for the created event in the body
content.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content. 

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

  * If the poolRecord is not a pool record in the pool.

  * If the pool contains both A and AAAA record types.

JSON Example: Create a SB / TC Event

{  
"poolRecord": "1.2.3.4",  
"type": "NORMAL",  
"start": "2018-10-02T12:00:00Z",  
"repeat": "WEEKLY",  
"end": "2020-12-31T23:59:59Z",  
"notify": "ALWAYS"  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get Events
for a Pool

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/events

**Parameters** :

Get events parameters

Parameter |  Description |  Type  
---|---|---  
q |  Specify query operators to filter the returned result. Valid operators are:

  * poolRecord - The CNAME, IPv4, or IPv6 for the pool record. This will only return events for the specified pool record.

|  String  
offset |  The position in the list for the first returned element (0 based). The default value is   
0. |  Integer  
limit |  The maximum number of rows requested. The default value is 100. |  Integer  
sort |  The sort column used to order the list. Sort columns are:

  * START â the start date for the event.
  * END â the end date for the event.

Note that if you get all events in a pool, they will be primarily sorted by
pool record.  
This sort is a secondary sort. |  String  
reverse |  Whether the list is ascending (false) or descending (true). The default value is   
false. |  Boolean  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
EventInfoList DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

  * If the poolRecord is not a pool record in the pool.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get a Single
Event

**Method and URI** :

GET
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/events/{guid}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
EventInfo DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

  * If the poolRecord is not a pool record in the pool.

  * If the {guid} is not a guid for an event for the pool record.

  * If the pool contains both A and AAAA record types.

JSON Example: Get a SB / TC Event Response

{  
"queryInfo": {  
"reverse": false,  
"limit": 100  
},  
"resultInfo": {  
"totalCount": 1,  
"offset": 0,  
"returnedCount": 1  
},  
"events": [  
{  
"id": "0608452906095FDE",  
"poolRecord": "1.2.3.4",  
"type": "ACTIVE",  
"start": "2018-10-02T12:00:00Z",  
"end": "2020-12-31T23:59:00Z",  
"repeat": "WEEKLY",  
"notify": "ALWAYS"  
}  
]  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update an
Event

**Method and URI** :

PUT
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/events/{guid}

**Parameters** : None

**Body** : Must include an EventInfo DTO

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

  * If the {guid} is not a guid for an event in the pool.

  * If the pool contains both A and AAAA record types.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update an Event

**Method and URI** :

PATCH
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/events/{guid}

**Parameters** : None

**Body** : Must include an EventInfo DTO.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

  * If the {guid} is not a guid for an event in the pool.

  * If the pool contains both A and AAAA record types.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete an
Event

**Method and URI** :

DELETE
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/events/{guid}

**Parameters** : None

**Body** : None

**Response** : If delete completes immediately, Status Code 204 with no
content in the body is returned.

  * If delete happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

  * If the {guid} is not a guid for an event in the pool.

## _Pool Event DTOs_

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)EventInfo DTO

The EventInfo DTO contains the data to create, get, or update a pool event.

EventInfo DTO Structure

Field |  Description |  Type  
---|---|---  
**id** |  The internal id for this event. Returned by GET. |  String. Always returned by GET, ignored if present on POST, PUT, or PATCH.  
**poolRecord** |  The pool record associated with this event. This must be a FQDN if the pool record is a CNAME or reference to another pool, or an IPv4 or IPv6 address. |  String. Required for POST, ignored if present on PUT or PATCH, returned by GET.  
**type** |  Indicates what will happen when the event is triggered. Valid values are:

  * NORMAL - treat as normal pool record.
  * ACTIVE - force the record to be active.
  * ACTIVE_TEST - force the record to be active and run a probe test, but do not act on the result.
  * INACTIVE - force the record to be inactive.
  * INACTIVE_TEST - force the record to inactive and run a probe test, but do not act on the result.

|  String. One of the valid values. Required.  
**start** |  Start date and time for the event. |  String. Date/time in ISO 8601 format. Must be in the future.  
**repeat** |  How frequently events are triggered. Valid values are DAILY, WEEKLY, FORTNIGHTLY, MONTHLY. |  String. If not specified, event does not repeat.  
**end** |  The date to stop triggering events. |  String. Date in ISO 8601 format after the start date/time. Only allowed if repeat is specified.  
**notify** |  Indicates when to notify after an event is triggered. Valid values are: NEVER - do not send a notification. ERROR - only send notification on error. ALWAYS - send notification on success or error. |  String. If not specified, defaults to ERROR.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)EventInfoList
DTO

This is used to return the list of all events for a pool record.

EventInfo List DTO

Field |  Description |  Type  
---|---|---  
events |  The list of returned events. Each entry in the list matches the EventInfo DTO described above. |  List of EventInfo DTO.  
queryInfo/q |  The query used to construct the list. |  String.  
queryInfo/sort |  The sort column used to order the list. |  String  
queryInfo/reverse |  Whether the list is ascending (false) or descending (true). |  Boolean  
queryInfo/limit |  The maximum number of rows requested. |  Integer  
resultInfo/totalCount |  Count of all events in the system for the specified query. |  Integer  
resultInfo/offset |  The position in the list for the first returned element (0 based). |  Integer  
resultInfo/returnedCount |  The number of records returned. |  Integer

