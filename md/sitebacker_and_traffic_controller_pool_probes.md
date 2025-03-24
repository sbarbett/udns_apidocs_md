

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

# SiteBacker and Traffic Controller Pool Probes

As of August 27th, 2018, new region names have been added for SiteBacker and
Traffic Controller Pool Probe calls. These new region names are not
(currently) replacing the previous region names, however, we do recommend you
begin to utilize these new region names, as the old region names will
eventually not be valid. These new regions provide greater customization and
granularity when establishing probe locations to desired regions, or returning
more specific probe regions when querying.

Functionally, you can use the old region names along with the new region names
without triggering an error. We are supporting backward compatibility through
the REST API. This means that you can provide the new region name
North_America_East on a POST call, but on a GET call, that same new region
name North_America_East is returned as the old region name New_York.

Eventually, the REST API will no longer accept the old region names, nor will
it return the old region names as a response. Please begin to use the new
region names as we begin to transition these changes through the REST API.

ProbeType SiteBacker Agent - Updated Region/Agent Names below lists the new
region names along with the locations that are incorporated with the new
region name.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create a
Probe

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/probes

**Parameters** : None

**Body** : Must include Probe Info DTO

**Response** : If task completes, Status Code 201 is returned with a Location
Header containing a URI, and the GUID for the created probe in the body
content.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

  * If the pool contains both A and AAAA record types.

JSON Example: Create a SiteBacker / Traffic Controller Probe â Pool Level

{  
"type": "HTTP",  
"interval": "ONE_MINUTE",  
"agents": [  
"Palo_Alto",  
"NEW_YORK"  
],  
"threshold": 2,  
"details": {  
"transactions": [  
{  
"method": "GET",

"protocolVersion": "HTTP/1.0",  
"url": "http://www.google1.com/",  
"transmittedData": "",  
"limits": {  
"connect": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
},  
"run": {  
"warning": 60,  
"critical": 60,  
"fail": 60  
}  
},  
"followRedirects": true  
}  
]  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get Probes

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/probes

**Parameters** :

Get probes parameters

Parameter |  Description |  Type  
---|---|---  
**q** |  The query used to construct the list. Query operators are:

  * **type** \- Valid values are RECORD, POOL, or ALL. Default value is ALL, unless poolRecord is specified.
  * **poolRecord** -If you only want to get probes for a single pool record, specify either the IPv4, IPv6, or CNAME as a FQDN for the pool record. If not specified, type of RECORD is assumed.

|  String  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a Probe
Info List DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get a Probe

**Method and URI** :

GET
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/probes/{guid}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a Probe
Info DTO  in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

  * If the {guid} is not a guid for a probe for the pool or a pool record.

JSON Example: Get a Sitebacker / Traffic Controller Pool Probe via id

{  
"id": "060844D2F8B23F19",  
"poolRecord": "1.1.1.1",  
"type": "HTTP",  
"interval": "ONE_MINUTE",  
"agents": [  
"DALLAS",  
"AMSTERDAM",  
"ASIA",  
"NEW_YORK"  
],  
"threshold": 2,  
"details": {  
"transactions": [  
{  
"method": "GET",

"protocolVersion": "HTTP/1.0",  
"url": "http://www.google1.com/",  
"transmittedData": "",  
"limits": {  
"connect": {  
"fail": 20  
},  
"run": {  
"fail": 60  
}  
},  
"followRedirects": true  
}  
]  
}  
}

JSON Example: Get a SiteBacker / Traffic Controller Pool HTTP Probe with
Custom Header

{

"probes": [

{

"id": "06084E33F90E7BA6",

"type": "HTTP",

"interval": "FIFTEEN_MINUTES",

"agents": [

"AMSTERDAM",

"EUROPE_WEST"

],

"threshold": 2,

"details": {

"transactions": [

{

"method": "GET",

"url": "https://microsoft.com/",

"transmittedData": "fgf",

"limits": {

"connect": {

"fail": 20

},

"run": {

"fail": 60

}

},

"followRedirects": true,

"expectedResponse": "2XX|3XX",

"protocolVersion": "HTTP/1.0"

}

]

},

"headers": {

"X-Custom-Header": [

"value1",

"value2"

],

"queryInfo": {

"reverse": false,

"limit": 100

},

"resultInfo": {

"totalCount": 3,

"offset": 0,

"returnedCount": 3

}

}

}

}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get
SiteBacker Agents for account

This call allows users to query for supported agents for an account

SiteBacker Agent DTO

Field |  Description |  Type  
---|---|---  
name |  Name of the agent. |  String  
location |  SB Agent location. |  String  
description |  SB Agent description. |  String  
  
  
SiteBacker AgentList DTO

Field |  Description |  Type  
---|---|---  
**agents** |  List of all the supported SiteBacker Agents. |  List of SiteBacker Agents  
  
  
ProbeType SiteBacker Agent - Updated Region/Agent Names

Field |  New Regions |  Sites Associated to the Regions  
---|---|---  
**regionName** |  ASIA |  Tokyo, Taipei, Singapore, Hong Kong, Sydney  
CHINA |  Beijing, Hong Kong Note: Reliable results only to China based hosts.  
EUROPE_EAST |  Amsterdam, Frankfurt, Stockholm  
EUROPE_WEST |  London, Dublin, Paris, Madrid  
NORTH_AMERICA_CENTRAL |  Chicago, Denver, Dallas, Minneapolis  
NORTH_AMERICA_EAST |  New York, Washington D.C., Atlanta, Miami, Toronto  
NORTH_AMERICA_WEST |  Seattle, San Jose, Los Angeles, Phoenix, Vancouver  
SOUTH_AMERICA |  Sao Paolo, Colombia, Miami  
  
**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/agents

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
SiteBacker AgentList DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If an invalid method or URI is provided.

JSON Example: Get SiteBacker Agents

{  
"agents": [  
{  
"name": "North America Central",  
"description": "(Chicago, Denver, Dallas)"  
"location": "USCENTRAL"  
},  
{  
"name": "Europe East",  
"description": "(Amsterdam, Frankfurt, Stockholm)",  
"location": "EUEAST"  
},  
{  
"name": "Europe West",  
"description": "(London, Dublin, Paris, Madrid)",  
"location": "EUWEST"  
},  
{  
"name": "South America",  
"description": "(Sao Paulo,Columbia, Miami)",  
"location": "SAMERICA"  
},  
{  
"name": "Asia",  
"description": "(Tokyo, Taipei, Singapore, Hong Kong, Sydney)",  
"location": "ASIA"  
},  
{  
"name": "China",  
"description": "(Beijing, Hong Kong) Note: Reliable results only within
China",  
"location": "CHINA"  
},  
{  
"name": "North America West",  
"description": "(Seattle, San Jose, Los Angeles, Phoenix, Vancouver)",  
"location": "USWEST"  
},  
{  
"name": "North America East",  
"description": "(New York, Washington D.C., Atlanta, Miami, Toronto)",  
"location": "USEAST"  
}  
]  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update a
Probe

**Method and URI** :

PUT
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/probes/{guid}

**Parameters** : None

**Body** : Must include a Probe Info DTO .

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

  * If the {guid} is not a guid for a probe for the pool or a pool record.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update a Probe

**Method and URI** :

PATCH
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/probes/{guid}

**Parameters** : None

**Body** : Must include a Probe Info DTO , or a [JSON PATCH DTO](Making
Updates via JSON PATCH.htm#_Ref399931231).

**Patchable Objects for SB/TC** :

  * biz.neustar.ultra.rest.dto.ProbeInfo

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If {ownerName} does not exist.

  * If you don't have permission to read this zone.

  * If you don't have permissions to access the pool.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If the {guid} is not a defined guid for a probe for the pool or a pool record.

  * If both A and AAAA record types are included in the same pool.

JSON Example: Partially Updating a Probe with new and old regions response

{  
"probes": [  
{  
"id": "060844D2F8B23F19",  
"poolRecord": "1.1.1.1",  
"type": "HTTP",  
"interval": "ONE_MINUTE",  
"agents": [  
"DALLAS",  
"AMSTERDAM",  
"ASIA",  
"NEW_YORK"  
],  
"threshold": 2,  
"details": {  
"transactions": [  
{  
"method": "GET",  
"protocolVersion": "HTTP/1.0",  
"url": "http://www.google1.com/",  
"transmittedData": "",  
"limits": {  
"connect": {  
"fail": 20  
},  
"run": {  
"fail": 60  
}  
},  
"followRedirects": true  
}  
]  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete a
Probe

**Method and URI** :

DELETE
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/probes/{guid}

**Parameters** : None

**Body** : None

**Response** : If delete completes, Status Code 204 is returned with no
content in the body.

  * If delete happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.
  * If you don't have permission to read this zone.
  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.
  * If you don't have permissions to access the pool.
  * If the {guid} is not a guid for a probe for the pool or a pool record.

## Probe Info DTO

Probes are defined in their own endpoints, relative to the pool for pool-level
probes, and relative to the records for record-level probes.

Each of the probe types has a different details section. In a ProbeInfo DTO
(shown below), the structure of the details section must match the structure
associated with the value in the type field.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Custom HTTP
Probe Headers

Configuring HTTP Probe Headers allows you to tailor monitoring to your
specific needs and allows you to test server configurations for accurate
results and mimic real user traffic to improve monitoring accuracy. Probe
Headers consist of a key:value pair, and each Probe can only consist of 5
configured headers.

Use the List of HTTP Header Fields link to view the various types of Probe
Headers that are available.

##### Known Issues and Limitations

**HTTP/1**

For HTTP/1 multi-valued probe headers, the list of values will be sent as
"key": ["val1", "val2"]. We are aware that some servers may expect the values
to be sent as a string resembling "key": "val1, val2". In these instances, the
probe header can be configured as a single value, such as: "key": ["val1,
val2"].

If a server expects the values to be sent as "key": "val1" and "key": "val2",
the probe may fail because a single header is being sent with multiple values.

**HTTP/2**

For HTTP/2 multi-valued probe headers, the list of values will be sent as
"key": "val1" "key": "val2". We are aware that some servers may expect the
values to be sent as a string resembling "key": "val1, val2". In these
instances, the probe header can be configured as a single value, such as:
"key": ["val1, val2"].

##### Restrictions

The following restrictions apply to the design and length of the HTTP Probe
Headers:

  * Duplicate Key values are not allowed.

  * Each header Key length cannot exceed 50 characters.

  * Each header Value length cannot exceed 512 characters.

  * Each total header length (Key + Value) cannot exceed 562 characters.

  * The total character length of all 5 headers cannot exceed 2810 characters.

  * The Key value only supports alphanumeric characters, hyphens ( - ), and underscores ( _ ).

The following Header types are not allowed due to potential conflicts with
protocol-level operations and/or security concerns:

  * Host

  * Connection

  * Content-Length

  * Cookie

  * :method

  * :authority

  * :scheme

  * :path

probeInfo DTO structure

Field |  Description |  Type  
---|---|---  
id |  The internal id for this probe. Returned by GET. |  String. Always returned by GET. Ignored if present on POST, PUT, or PATCH.  
poolRecord |  The pool record associated with this probe.

  * Returned by GET when returning a record-level probe.
  * Left blank when creating a pool-level probe.
  * Specified when creating a record-level probe.

|  String. Sometimes returned by GET, required for POST when creating a
record-level probe. Ignored if present on PUT or PATCH.  
type |  Type of the probe. Valid values are:

  * HTTP
  * PING
  * FTP
  * TCP
  * SMTP
  * SMTP_SEND
  * DNS

|  String. Required, no default value.  
headers  |  Used to create a list of custom probe headers when type = HTTP. Headers are provided as key:value pairs.  Key is required, but value can be empty.  List of [HTTP Header Fields](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields). |  String displayed as a key:value pair. Only used if **type=http**.  Optional.   
interval |  Length of time between probes in minutes. Value values are HALF_MINUTE, ONE_MINUTE, TWO_MINUTES, FIVE_MINUTES, TEN_MINUTES, and FIFTEEN_MINUTES. |  String. If not specified, defaults to FIVE_MINUTES.  
agents |  Locations that will be used for probing. One or more values must be specified. Valid values are NEW_YORK, PALO_ALTO, DALLAS, and AMSTERDAM.  See ProbeType SiteBacker Agent - Updated Region/Agent Names for the new agent names. |  Array of Strings. Required, no default value.  
threshold |  Number of agents that must agree for a probe state to be changed. |  Integer, from 1 to the number of agents specified. Required.  
details |  Probe type-specific information. |  Map of the type-specific fields for a probe. See below.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Probe Info
List DTO

This is used to return a list of Probes for a Pool or a Pool Record.

ProbeInfo List DTO Structure

Field |  Description |  Type  
---|---|---  
probes |  The list of all probes. |  List of  Probe Info DTOs  
queryInfo/q |  The query used to construct the list. |  String  
queryInfo/sort |  The sort column used to order the list. |  String  
queryInfo/reverse |  Whether the list is ascending (false) or descending (true). |  Boolean  
queryInfo/limit |  The maximum number of rows requested. |  Integer  
resultInfo/totalCount |  Count of all events in the system for the specified query. |  Integer  
resultInfo/offset |  The position in the list for the first returned element (0 based). |  Integer  
resultInfo/returnedCount |  The number of records returned. |  Integer  
  
JSON Example: HTTP Probe with Custom Headers

{

"type": "HTTP",

"headers": {

"Accept-Language": [

"en-US",

],

JSON Example: Probe Info List with two TCP Probes

{  
"probes": [  
{  
"type": "TCP",  
"interval": 5,  
"agents": [  
"NEW_YORK",  
"DALLAS"  
],  
"threshold": 1,  
"details": {  
"port": 1024,  
"controlIP": "1.2.3.4",  
"limits": {  
"connect": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
},  
"avgConnect": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
},  
}  
}  
},  
{  
"type": "TCP",  
"interval": 5,  
"agents": [  
"NEW_YORK",  
"DALLAS"  
],  
"threshold": 1,  
"details": {  
"port": 2048,  
"controlIP": "1.2.3.4",  
"limits": {  
"connect": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
},  
"avgConnect": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
},  
}  
}  
}  
],  
"queryInfo": {  
"q":"",  
"sort": "type",  
"reverse": false,  
"limit": 100  
},  
"resultInfo": {  
"totalCount": 2,  
"offset": 0,  
"returnedCount": 2  
}  
}

## _Probe Details DTOs_

The below DTOs provide the data and structure needed for the details field of
the Probe Info DTO . The Details DTOs you will use is determined by the type
of the probe identified.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)HTTP Probe
Details DTO

HTTP Probe Details DTO structure

Field |  Description |  Type  
---|---|---  
transactions |  List of http requests sent for a single probe. |  Array of transaction info structures.  
transactions/method |  HTTP method. Valid values are GET or POST. |  String. Required.  
transactions/protocolVersion |  HTTP protocol version. Valid values are: 

  * HTTP/1.0
  * HTTP/1.1
  * HTTP/2 

Note: HTTP probes will only correctly work if the indicated server supports the configured HTTP protocol version, otherwise the probe will fail.  |  String. Optional.   
transactions/url |  URL to probe. |  String. Required.  
transactions/transmittedData |  Data to send to URL. |  String. Optional.  
transactions/followRedirects |  Indicates whether or not to follow redirects. |  Boolean. Optional, defaults to false.  
transactions/expectedResponse |  The Expected Response code for probes to be returned as Successful. Valid values are:

  * 2XX: Probe will pass for any code between 200-299.
  * 3XX: Probe will pass for any code between 300-399.
  * 2XX|3XX: Probe will pass for any code between 200-399.
  * Any combination of HTTP codes between 100-599 separated by â | â For example:
    * 201|302 
    * 301|202|401
    * 501|201|404|301

|  String. Optional. By default, probes will be passed for 2XX HTTP code.  
transactions/limits |  Determine the cutoffs for sending notification or failing the probe. |  httpLimitInfo structure.  
transactions/limits/connect |  |   
transactions/limits/connect/warning |  How long the probe stays connected to the resource to trigger a warning (maximum 20 seconds).  |  Integer. Optional, only used for Traffic Controller Pools.  
transactions/limits/connect/critical |  How long the probe stays connected to the resource to trigger a critical warning (maximum 20 seconds).  |  Integer. Optional, only used for Traffic Controller Pools.  
transactions/limits/connect/fail |  How long the probe stays connected to the resource to trigger a fail (maximum 20 seconds).  |  Integer. Optional.  
transactions/limits/avgConnect |  |   
transactions/limits/avgConnect/warning |  Mean connect time over the five most recent probes run on each agent to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
transactions/limits/avgConnect/critical |  Mean connect time over the five most recent probes run on each agent to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
transactions/limits/avgConnect/fail |  Mean connect time over the five most recent probes run on each agent to trigger a fail. |  Integer. Optional, only used for Traffic Controller Pools.  
transactions/limits/run |  |   
transactions/limits/run/warning |  How long the probe should run to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
transactions/limits/run/critical |  How long the probe should run to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
transactions/limits/run/fail |  How long the probe should run to trigger a fail. |  Integer. Optional.  
transactions/limits/avgRun |  |   
transactions/limits/avgRun/warning |  Mean run time over the five most recent probes run on each agent to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
transactions/limits/avgRun/critical |  Mean run time over the five most recent probes run on each agent to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
transactions/limits/avgRun/fail |  Mean run time over the five most recent probes run on each agent to trigger a fail. |  Integer. Optional, only used for Traffic Controller Pools.  
transactions/limits/searchString |  |   
transactions/limits/searchString/warning |  If left blank, the HTTP probe verifies that the server responds to the request with a successful HTTP response (normally a Status Code 200). If specified, the probe searches the response's body only; it does not search the status line and headers. If the probe does not find the string within the response, the probe attempts to match it as a regular expression.  |  String. Optional, only used for Traffic Controller Pools.  
transactions/limits/searchString/critical |  If left blank, the HTTP probe verifies that the server responds to the request with a successful HTTP response (normally a Status Code 200). If specified, the probe searches the response's body only; it does not search the status line and headers. If the probe does not find the string within the response, the probe attempts to match it as a regular expression.  |  String. Optional, only used for Traffic Controller Pools.  
transactions/limits/searchString/fail |  If left blank, the HTTP probe verifies that the server responds to the request with a successful HTTP response (normally a Status Code 200). If specified, the probe searches the response's body only; it does not search the status line and headers. If the probe does not find the string within the response, the probe attempts to match it as a regular expression.  |  String. Optional.  
totalLimits |  The total amount of time spent on all http transactions. |  httpTotalLimit structure.  
totalLimits/warning |  Run time for all steps in the sequence of an HTTP transactional probe for a warning to be generated. |  Integer. Optional, only used for Traffic Controller Pools.  
totalLimits/critical |  Run time for all steps in the sequence of an HTTP transactional probe for a critical warning to be generated. |  Integer. Optional, only used for Traffic Controller Pools.  
**totalLimits/fail** |  Run time for all steps in the sequence of an HTTP transactional probe for the probe to fail. |  Integer. Optional.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Ping Probe
Details DTO

Ping Probe Details DTO structure

Field |  Description |  Type  
---|---|---  
packets |  Number of ICMP packets to send. |  Integer, defaults to 3.  
packetSize |  Size of packets in bytes. |  Integer, defaults to 56.  
limits |  Determine the cutoffs for sending a notification or failing the probe. |  pingLimitInfo structure.  
limits/lossPercent |  |   
limits/lossPercent/warning |  Percentage of packets lost to trigger a SiteBacker/Traffic Controller warning event. For example, 5 would indicate that packet loss > 5% would trigger a probe failure. 0 always fails the probe; 100 ensures the probe succeeds.  |  Integer. Optional, only used for Traffic Controller Pools.  
limits/lossPercent/critical |  Percentage of packets lost to trigger a SiteBacker/Traffic Controller critical warning event. For example, 5 would indicate that packet loss > 5% would trigger a probe failure. 0 always fails the probe; 100 ensures the probe succeeds.  |  Integer. Optional, only used for Traffic Controller Pools.  
limits/lossPercent/fail |  Percentage of packets lost to trigger a SiteBacker/Traffic Controller failure event. For example, 5 would indicate that packet loss > 5% would trigger a probe failure. 0 always fails the probe; 100 ensures the probe succeeds.  |  Integer. Optional.  
limits/total |  |   
limits/total/warning |  Run time for all pings to complete for a warning to be generated. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/total/critical |  Run time for all pings to complete for a critical warning to be generated. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/total/fail |  Run time for all pings to complete for a failure to be generated. |  Integer. Optional  
limits/average |  |   
limits/average/warning |  Mean connect time over the five most recent probes run on each agent to trigger a warning. |  Integer, optional, only used for Traffic Controller Pools.  
limits/average/critical |  Mean connect time over the five most recent probes run on each agent to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/average/fail |  Mean connect time over the five most recent probes run on each agent to trigger a failure. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run |  |   
limits/run/warning |  How long the probe should run to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run/critical |  How long the probe should run to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run/fail |  How long the probe should run to trigger a failure. |  Integer. Optional.  
limits/avgRun |  |   
limits/avgRun/warning |  Mean run time over the five most recent probes run on each agent to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgRun/critical |  Mean run time over the five most recent probes run on each agent to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgRun/fail |  Mean run time over the five most recent probes run on each agent to trigger a failure. |  Integer. Optional, only used for Traffic Controller Pools.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)FTP Probe
Details DTO

FTP Probe Details DTO structure

Field |  Description |  Type  
---|---|---  
port |  Which Port to connect to. |  Integer between 1 and 65535. Defaults to 21.  
passiveMode |  Whether or not to use FTP Passive mode. |  Boolean, defaults to false.  
username |  Username for FTP service. |  String. Optional.  
password |  Password for FTP service. |  String. Optional.  
path |  Path to check for a file. |  String  
limits |  Determine the cutoffs for sending a notification or failing the probe. |  ftpLimitInfo structure.  
limits/connect |  |   
limits/connect/warning |  How long the probe stays connected to the resource to trigger a warning (maximum 20 seconds).  |  Integer. Optional, only used for Traffic Controller Pools.  
limits/connect/critical |  How long the probe stays connected to the resource to trigger a critical warning (maximum 20 seconds).  |  Integer. Optional, only used for Traffic Controller Pools.  
limits/connect/fail |  How long the probe stays connected to the resource to trigger a failure (maximum 20 seconds).  |  Integer. Optional.  
limits/avgConnect |  |   
limits/avgConnect/warning |  Mean connect time over the five most recent probes run on each agent to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgConnect/critical |  Mean connect time over the five most recent probes run on each agent to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgConnect/fail |  Mean connect time over the five most recent probes run on each agent to trigger a failure. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run |  |   
limits/run/warning |  How long the probe should run to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run/critical |  How long the probe should run to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run/fail |  How long the probe should run to trigger a failure. |  Integer. Optional.  
limits/avgRun |  |   
limits/avgRun/warning |  Mean run time over the five most recent probes run on each agent to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgRun/critical |  Mean run time over the five most recent probes run on each agent to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgRun/fail |  Mean run time over the five most recent probes run on each agent to trigger a failure. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/searchString |  |   
limits/searchString/warning |  If blank, the FTP probe verifies that the server responds to the request with a successful response. If specified, the probe searches the response's body. If the probe does not find the string within the response, the probe attempts to match it as a regular expression.  |  String. Optional, only used for Traffic Controller Pools.  
limits/searchString/critical |  If blank, the FTP probe verifies that the server responds to the request with a successful response. If specified, the probe searches the response's body. If the probe does not find the string within the response, the probe attempts to match it as a regular expression.  |  String. Optional, only used for Traffic Controller Pools.  
limits/searchString/fail |  If blank, the FTP probe verifies that the server responds to the request with a successful response. If specified, the probe searches the response's body. If the probe does not find the string within the response, the probe attempts to match it as a regular expression.  |  String. Optional.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)TCP Probe
Details DTO

TCP Probe Details DTO structure

Field |  Description |  Type  
---|---|---  
port |  Which Port to connect to. |  Integer between 1 and 65535. Required.  
controlIP |  Provides a control mechanism that allows the web administrators to stop the TCP port on the control system.  |  String, IP address. Optional.  
limits |  |   
limits/connect |  |   
limits/connect/warning |  How long the probe stays connected to the resource to trigger a warning (maximum 20 seconds).  |  Integer. Optional, only used for Traffic Controller Pools.  
limits/connect/critical |  How long the probe stays connected to the resource to trigger a critical warning (maximum 20 seconds).  |  Integer. Optional, only used for Traffic Controller Pools.  
limits/connect/fail |  How long the probe stays connected to the resource to trigger a failure (maximum 20 seconds).  |  Integer. Optional.  
limits/avgConnect |  |   
limits/avgConnect/warning |  Mean connect time over the five most recent probes run on each agent to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgConnect/critical |  Mean connect time over the five most recent probes run on each agent to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgConnect/fail |  Mean connect time over the five most recent probes run on each agent to trigger a failure. |  Integer. Optional, only used for Traffic Controller Pools.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)SMTP Probe
Details DTO

SMTP Probe Details DTO structure

Field |  Description |  Type  
---|---|---  
port |  The Port that will be connected to. |  Integer between 1 and 65535. Defaults to 25.  
limits |  |   
limits/connect |  |   
limits/connect/warning |  How long the probe stays connected to the resource to trigger a warning (maximum 20 seconds).  |  Integer. Optional, only used for Traffic Controller Pools.  
limits/connect/critical |  How long the probe stays connected to the resource to trigger a critical warning (maximum 20 seconds).  |  Integer. Optional, only used for Traffic Controller Pools.  
limits/connect/fail |  How long the probe stays connected to the resource to trigger a failure (maximum 20 seconds).  |  Integer. Optional.  
limits/avgConnect |  |   
limits/avgConnect/warning |  Mean connect time over the five most recent probes run on each agent to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgConnect/critical |  Mean connect time over the five most recent probes run on each agent to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgConnect/fail |  Mean connect time over the five most recent probes run on each agent to trigger a failure. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run |  |   
limits/run/warning |  How long the probe should run to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run/critical |  How long the probe should run to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run/fail |  How long the probe should run to trigger a fail. |  Integer. Optional.  
limits/avgRun |  |   
limits/avgRun/warning |  Mean run time over the five most recent probes run on each agent to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgRun/critical |  Mean run time over the five most recent probes run on each agent to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgRun/fail |  Mean run time over the five most recent probes run on each agent to trigger a failure. |  Integer. Optional, only used for Traffic Controller Pools.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)SMTP_SEND
Probe Details DTO

SMTP Send Probe Details DTO structure

Field |  Description |  Type  
---|---|---  
port |  The Port that will be connected to. |  Integer between 1 and 65535. Defaults to 25.  
from |  Email address that will send the message. |  String. Email address. Required.  
to |  Email address that will receive the message. |  String. Email address. Required.  
message |  Email message body. |  String. Optional.  
limits |  |   
limits/connect |  |   
limits/connect/warning |  How long the probe stays connected to the resource to trigger a warning (maximum 20 seconds).  |  Integer. Optional, only used for Traffic Controller Pools.  
limits/connect/critical |  How long the probe stays connected to the resource to trigger a critical warning (maximum 20 seconds).  |  Integer. Optional, only used for Traffic Controller Pools.  
limits/connect/fail |  How long the probe stays connected to the resource to trigger a failure (maximum 20 seconds).  |  Integer. Optional.  
limits/avgConnect |  |   
limits/avgConnect/warning |  Mean connect time over the five most recent probes run on each agent to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgConnect/critical |  Mean connect time over the five most recent probes run on each agent to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgConnect/fail |  Mean connect time over the five most recent probes run on each agent to trigger a failure. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run |  |   
limits/run/warning |  How long the probe should run to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run/critical |  How long the probe should run to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run/fail |  How long the probe should run to trigger a fail. |  Integer. Optional.  
limits/avgRun |  |   
limits/avgRun/warning |  Mean run time over the five most recent probes run on each agent to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgRun/critical |  Mean run time over the five most recent probes run on each agent to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgRun/fail |  Mean run time over the five most recent probes run on each agent to trigger a failure. |  Integer. Optional, only used for Traffic Controller Pools.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)DNS Probe
Details DTO

DNS Probe Details DTO structure

Field |  Description |  Type  
---|---|---  
port |  The Port that should be used for DNS lookup. |  Integer between 1 and 65535. Defaults to 53.  
tcpOnly |  Indicates whether or not the probe should use TCP only, or first UDP then TCP. |  Boolean. Defaults to false.  
type |  Select which kind of record should be checked for. Valid values are NULL, AXFR, or any Resource Record Type. |  String. Defaults to NULL.  
ownerName |  Selects the name that should be queried. |  String. Defaults to blank.  
limits |  |   
limits/run |  |   
limits/run/warning |  How long the probe should run to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run/critical |  How long the probe should run to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/run/fail |  How long the probe should run to trigger a fail. |  Integer. Optional.  
limits/avgRun |  |   
limits/avgRun/warning |  Mean run time over the five most recent probes run on each agent to trigger a warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgRun/critical |  Mean run time over the five most recent probes run on each agent to trigger a critical warning. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/avgRun/fail |  Mean run time over the five most recent probes run on each agent to trigger a failure. |  Integer. Optional, only used for Traffic Controller Pools.  
limits/response |  |   
limits/response/warning |  Match exactly the records with single field responses (that is: A, AAAA, CNAME, DNAME, NS, MB, MD, MF, MG, MR, PTR) to trigger a warning. Match HINFO records partially and without considering case. Match partially for types with multiple field responses, and join all fields separated by spaces (for example, use 10 mail.example.com. to test a response to an MX record with a preference of 10 and target host of mail.example.com.).  |  String. Optional, only used for Traffic Controller Pools.  
limits/response/critical |  Match exactly the records with single field responses (that is: A, AAAA, CNAME, DNAME, NS, MB, MD, MF, MG, MR, PTR) to trigger a critical warning. Match HINFO records partially and without considering case. Match partially for types with multiple field responses, and join all fields separated by spaces (for example, use 10 mail.example.com. to test a response to an MX record with a preference of 10 and target host of mail.example.com.).  |  String. Optional, only used for Traffic Controller Pools.  
limits/response/fail |  Match exactly the records with single field responses (that is: A, AAAA, CNAME, DNAME, NS, MB, MD, MF, MG, MR, PTR) to trigger a failure. Match HINFO records partially and without considering case. Match partially for types with multiple field responses, and join all fields separated by spaces (for example, use 10 mail.example.com. to test a response to an MX record with a preference of 10 and target host of mail.example.com.).  |  String. Optional.  
  
JSON Example: HTTP Probe Info

{  
"type": "HTTP",  
"poolRecord": "1.1.1.1",  
"interval": "ONE_MINUTE",  
"agents": [  
"NEW_YORK",  
"DALLAS"  
],  
"threshold": 1,  
"details": {  
"transactions": [  
{  
"method": "POST",  
"protocolVersion": "HTTP/1.0",  
"url": "https://www.cnn.com/",  
"transmittedData": "foo=bar",  
"followRedirects": true,  
"expectedResponse": "2XX",  
"limits": {  
"connect": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
},  
"avgConnect": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
},  
"run": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
},  
"avgRun": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
},  
"searchString": {  
"warning": "missing",  
"critical": "uh-oh",  
"fail": "bad"  
}  
}  
},  
{  
"method": "GET",

"protocolVersion": "HTTP/1.0",  
"url": "https://www.bing.com/",  
"followRedirects": false,  
"expectedResponse":"201|301",  
"limits": {  
"connect": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
},  
"avgConnect": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
},  
"run": {  
"critical": 20,  
"fail": 20  
},  
"avgRun": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
},  
"searchString": {  
"warning": "missing",  
"critical": "uh-oh",  
"fail": "bad"  
}  
}  
}  
],  
"totalLimits": {  
"warning": 20,  
"critical": 20,  
"fail": 20  
}  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)SiteBacker
Agent / Probes

The following table lists the IP addresses that are used for probing actions
performed by Traffic Management (Sitebacker and Traffic Controller) pools. It
may be necessary to modify firewall or security policies to allow traffic from
these addresses.

IP Probes Expansion by Region

IP Probes by Region Available 2019  
---  
Region |  IPv4 |  IPv6  
**North America â East** |  156.154.35.153 156.154.35.154 156.154.37.153 156.154.37.154 156.154.119.153 156.154.119.154 |  2610:a1:3008:128::153 2610:a1:3008:128::154 2610:a1:3010:128::153 2610:a1:3010:128::154 2610:a1:3044:128::153 2610:a1:3044:128::154  
North America â West |  156.154.36.153 156.154.36.154 156.154.38.153 156.154.38.154 156.154.41.153 156.154.41.154 |  2610:a1:300c:128::153 2610:a1:300c:128::154 2610:a1:3014:128::153 2610:a1:3014:128::154 2610:a1:3020:128::153 2610:a1:3020:128::154  
North America â Central |  156.154.39.153 156.154.39.154 156.154.39.156 156.154.40.153 156.154.40.154 156.154.40.156 |  2610:a1:301c:128::153 2610:a1:301c:128::154 2610:a1:301c:128::156 2610:a1:3018:128::153 2610:a1:3018:128::154 2610:a1:3018:128::156  
Europe - East |  156.154.76.153 156.154.76.154 156.154.77.153 156.154.77.154 156.154.85.153 156.154.85.154 |  2610:a1:302c:128::153 2610:a1:302c:128::154 2610:a1:3028:128::153 2610:a1:3028:128::154 2610:a1:3040:128::153 2610:a1:3040:128::154  
Europe â West |  156.154.78.153 156.154.78.154 156.154.80.153 156.154.80.154 |  2610:a1:3030:128::153 2610:a1:3030:128::154 2610:a1:3038:128::153 2610:a1:3038:128::154  
South America |  156.154.122.153 156.154.123.153 |  2610:a1:304c:128::153 2610:a1:3048:128::153  
Asia |  156.154.99.153 156.154.99.154 156.154.180.153 156.154.180.154 156.154.181.153 156.154.181.154 156.154.182.153 203.119.15.153 203.119.15.154 |  2610:a1:305c:128::153 2610:a1:3054:128::153 2610:a1:3054:128::154 2610:a1:3058:128::153 2610:a1:3058:128::154 2610:a1:3068:128::153 2610:a1:3068:128::154 2610:a1:3070:128::153 2610:a1:3070:128::154  
China |  156.154.62.153 156.154.62.154 156.154.63.153 156.154.63.154 |  2610:a1:3074:128::153 2610:a1:3074:128::154 2610:a1:3078:128::153 2610:a1:3078:128::154

