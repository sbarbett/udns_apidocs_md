

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

# Simple Load Balancing (SLB) Pool API

Simple Load Balancing Pools are used to define a pool of up to five (5) IPv4 A
records (Primary Records pool), an HTTP(S) monitor, and a backup (All Fail)
IPv4 address. One resource record will be served based on the Response Method
configured.

Simple Load Balancing supports the usage of IPv6 addresses, using the AAAA
record type. You will need to alter the API calls to match the AAAA record
type when trying to use an IPv6 address instead of an IPv4 address.

An additional limitation is that you are not able to mix and match IPv4 and
IPv6 addresses in the rdata field of the body of a call. You must keep these
record types consistent throughout the call.

The following is the list of available IPv6 formats that are accepted:

IPv6 Address Format |  Example  
---|---  
IPv6 Full Notation |  â2001:0db8:0a0b:12f0:0000:0000:0000:0001â  
Compressed |  â2001:db8:a0b:12f0::1â "2610:a1:1059:0:0:0:0:35"  
  
When using Simple Load Balancing, the defined monitor (probe) sends HTTP(S)
GET or POST requests from four locations towards the target addresses once
every five minutes. Optionally, the request to the target system can include
HTTP(S) request data and/or the HTTP response data can be searched for
specific content. If no search string is specified, the probe of the target is
considered as successful if any non-error HTTP response from the target is
received. The availability of the target system is evaluated upon receipt of
each successful or unsuccessful probe result from each location.

If the monitor (probe) detects that a record in the Primary Records pool is
unreachable, that record will not be served unless the record's Forced State
is set to Forced Active. If the record's Forced State is set to Forced
Inactive, a record will not be served regardless of the pool probe status.

Serving Preference determines if records will be selected from the Primary
Records pool or from the All Fail Record.

  1. **Auto Select** (default): Serving method switches from serving Primary Records, to All Fail Record based upon probe results, and the Forced State of the Primary Records.

  2. **Serve Primary** : Only the Primary Records are served based upon the probe results and the Forced State of the Primary Records.

  3. **Serve All Fail** : Only the All Fail Record will be served, ignoring the probe results and the Forced State of the Primary Records.

**Note:**

  * Auto Select and Serve Primary will also take into account the Response Method that has been established (if applicable) when determining which records get served.

  * It may take up to 15 seconds to see the updated value after a switching between Auto Select/Serve Primary and Serve All Fail.

## Calling the APIs

In this document you will find descriptions of the Data Transfer Objects
(DTOs) and the various available services. In all cases, you will receive a
2xx HTTP response code in response to a successful service call. If an error
condition occurs, you will receive an HTTP response code in the 4xx or 5xx
range, with a HTTP body that indicates the error condition such as:

<errors>  
<code>AccountNotFound<code>  
<message>Account not found with ID: abc123xyz</message>  
</errors>

The UltraDNS APIs can accept requests and send responses in both XML and JSON
formats. The client can control the format of the request and the response, by
supplying the "Content-Type" and "Accept" HTTP headers respectively, as well
as supplying either an **"application/xml"** or **"application/json"** for the
value in either header. The default response format is JSON.

## Modifications of Existing DTOs and Parameters

Pools are implemented as additional information added to RRSets. A SLBPool DTO
has a section called âprofile.â The profile contains information that is
outside the typical boundaries of various DNS specifications.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Profile
Information for Simple Load Balancing Pools

A profile is simply a JSON Map. All profiles must contain a key called
@context. This is a JSON-LD reference to a schema ([http://json-ld.org/). The
schema describes the custom data that is used in the profile
fields.](http://json-ld.org/)

The schema name for SLB Pools is set to
[http://schemas.ultradns.com/SLBPool.jsonschema.](http://schemas.ultradns.com/SLBPool.jsonschema)

The other fields in the profile for a SLB Pool are:

SLB Pool Profile Information

Field |  Description |  Type  
---|---|---  
description |  An optional description of the Simple Load Balancing field. |  String. Less than 255 characters. Optional.  
rdataInfo |  The data used to describe the pool records. |  Array of RData Info DTO. Required  
responseMethod |  The method used to select which record is returned from the primary record pool. |  Required. One of the following:

  * **PRIORITY_HUNT** â The sequence of the records listed in the primary record pool determines the priority. The first record listed is the highest priority record. Once a record starts being served, it will always be served until the probe detects a failure on this record or the record is FORCED_INACTIVE. The top priority record is always returned among all the set of primary records where the following conditions are satisfied:
    1. Record forcedState is set to FORCED_ACTIVE.
    2. Pool Probe is determined to be passing successfully for the record (based upon Threshold configuration), and the record forced state is NOT_FORCED and probingEnabled at this record level is set to true.
  * **RANDOM** â A random record is returned from the following set of primary records.
    1. Pool Probe is determined to be passing successfully (based upon Threshold configuration), and the record forced state is NOT_FORCED and probingEnabled at this record level is set to true.
    2. Record forcedState is set to FORCED_ACTIVE.
  * **ROUND_ROBIN** \- A record is returned in rotation from the following set of records.
    1. Pool Probe is determined to be passing successfully (based upon Threshold configuration), and the record forced state is NOT_FORCED and probingEnabled at this record level is set to true.
    2. If record forcedState is set to FORCED_ACTIVE.

  
allFailRecord |  Information for the backup record. |  An All Fail Record DTO. Required.  
monitor |  Information for the probe / monitor. |  A Monitor DTO. Required.  
regionFailureSensitivity |  Specifies the sensitivity to the number of regions that must fail probing (Low or High) in order for the backup record to become active. |  Required. One of either:

  * **LOW** â All 4 regions have to fail.
  * **HIGH** â 2 or more regions have to fail.

  
servingPreference |  Allows users to specify which set of records to serve, from the Simple Load Balancing Pool. Possible choices are:

  * AUTO_SELECT
  * SERVE_PRIMARY
  * SERVE_ALL_FAIL

|  Required. One of :

  * **AUTO_SELECT** â The pool can switch from serving from the primary record set, to an All Fail record OR, from an All Fail record to the primary record set automatically, based upon the probe results and other record forcedState settings.
  * **SERVE_PRIMARY** â Only a record in the primary pool will be served. There is no fail over to the âAll failâ record. 
  * **SERVE_ALL_FAIL** â Only the All Fail Record will be served..

  
status |  Ignored if sent on Create or Update. Returned when list of RRSets is returned. |  One of either:

  * **OK** \- Priority record(s) are being served.
  * **WARNING** â One of the priority records is not being served due to the monitor detecting a failure, but there is still a priority record to be served.
  * **CRITICAL** â The backup All Fail record is being served due to the monitor detecting a failure.

This is a pool level setting that is determined based upon the number of
records available to be served. The number of records available to be served
is determined by the probe results from various regions.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)RData Info
DTO

RData Info DTO

Field |  Description |  Type  
---|---|---  
rdataInfo/description |  An optional description of the record in the live pool. |  String. Less than 255 characters. Optional.  
rdataInfo/forcedState |  The Forced State of the record that indicates whether the record needs to be: force served, forced to be inactive, or the force status not being set all. Defaults to NOT_FORCED.  |  Optional. Valid values are one of the following:

  * FORCED_ACTIVE
  * FORCED_INACTIVE
  * NOT_FORCED (default)

  
rdataInfo/probingEnabled |  Can be set at the record level to indicate whether probing is required (true) or not (false) for the given record.  Defaults to true at the record level. |  true or false.  
rdataInfo/availableToServe |  Indicates whether the record is available to be served (true) or not (false), based upon the probe results or the forced state of the record. Applies to JSON response, not JSON request. |  true or false.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)All Fail
Record DTO

All Fail Record DTO

Field |  Description |  Type  
---|---|---  
allFailRecord/rdata |  BIND data for the backup record. |  IPv4 or IPv6 address. Required.  
allFailRecord/description |  An optional description for the backup record. |  String. Less than 255 characters. Optional.  
allFailRecord/serving |  Serving status of the AllFail Record. This is a response only attribute. true = serving  
false = not serving |  true of false  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Monitor DTO

Monitor DTO

Field |  Description |  Type  
---|---|---  
monitor/method |  The HTTP method used to connect to the monitored URL. |  Required. One of either:

  * GET
  * POST
  * PUT

  
monitor/url |  The monitored URL. |  Required. A full URL including protocol, host, and URI. Valid protocols are http and https.   
monitor/transmittedData |  If a monitor is sending a POST, the data that is sent as the body of the request. |  String. Less than 255 characters. Optional.  
monitor/searchString |  If supplied, the string that is checked against the returned data from the request. The monitor fails if the search string is not present. |  String. Less than 255 characters. Optional.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create a
Simple Load Balancing Pool

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/rrsets/{type}/{newPoolName}

**Parameters** : None

**Body** : Must include Profile Information for Simple Load Balancing Pools.

**Response** : If task completes, Status Code 201 is returned with a [Task
DTO](Tasks.htm#_Ref396227604) in the body content.

**Errors** : An error is returned under the following conditions:

  * If {taskId} does not exist.

  * If you do not have permission to read {taskId}.

The {newPoolName} can either be a Fully Qualified Domain Name, or a Relative
Domain Name.

The below JSON example demonstrates creating a new pool along with five (5)
records, along with the All Fail record.

JSON Example: Create SLB Pool IPv4 Address

{  
"ttl": 333,  
"rdata": [  
"1.1.1.1",  
"2.2.2.2",  
"3.3.3.3",  
"4.4.4.4",  
"5.5.5.5"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/SLBPool.jsonschema",  
"description": "SLB Pool description",  
"rdataInfo": [  
{  
"description": "1",  
"forcedState": "NOT_FORCED",  
"probingEnabled": true  
},  
{  
"description": "2",  
"forcedState": "FORCED_ACTIVE",  
"probingEnabled": false  
},  
{  
"description": "3",  
"forcedState": "FORCED_INACTIVE",  
"probingEnabled": true  
},  
{  
"description": "4",  
"forcedState": "NOT_FORCED",  
"probingEnabled": true  
},  
{  
"description": "5",  
"forcedState": "NOT_FORCED",  
"probingEnabled": true  
}  
],  
"responseMethod": "PRIORITY_HUNT",  
"allFailRecord": {  
"rdata": "6.6.6.6",  
"description": "Backup Record"  
},  
"monitor": {  
"method": "POST",  
"url": "https://www.google.com",  
"transmittedData": "q=something",  
"searchString": "UltraDNS"  
},  
"regionFailureSensitivity": "LOW",  
"servingPreference": "AUTO_SELECT"  
}  
}

  * Simple Load Balancing Pools (SLB) can only be defined for RRSets of type A (1). It is an error to define a SLB Pool for other RRSets. 

  * It is also an error to define a SLB pool with no records, or with more than five (5) records.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)List Simple
Load Balancing Pools

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/?q=kind:SLB_POOLS  

**Parameters** :

The âqâ parameter for GET /v1/zones/{zoneName}/rrsets and GET
/zones/{zoneName}/rrsets/{type} recognize a new attribute called âkind.â
The valid values for kind are:

Value |  Meaning  
---|---  
ALL |  All pools and records (such as RECORDS, and POOLS).  
RECORDS |  Only resource records.  
POOLS |  All Pools  
RD_POOLS |  Only RD Pools.  
DIR_POOLS |  Only Directional Pools.  
SF_POOLS |  Only Simple Monitor / Failover Pools.  
SLB_POOLS |  Only Simple Load Balancing Pools.  
  
  * These values can be comma-separated.

  * If kind is not specified, it will default to the value ALL.

  * This list is subject to change as new pool types are defined.

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an RData
Info DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If you do not have access to the zoneName.

  * If the zoneName is invalid.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)How Simple
Load Balancing Pools are Displayed

When an owner that represents a SLB Pool is returned, the profile information
must be included.

If SLB Pools are included in a list with other RRSet types, the SLB Pools are
placed at the end of the list. If the list is paginated, the SLB Pools are
returned after the pages with all other record types listed.

The hierarchy for the display order is as follows:

  1. Standard RRSets, RD Pools, and DIR Pools intermixed.

  2. All SF Pools

  3. All SLB Pools.

JSON Example: Displaying SLB Pools IPv4

STATUS 200 OK  
{  
"zoneName": "primary-example.com.",  
"rrSets": [  
{  
"ownerName": "primary-example.com.",  
"rrtype": "A (1)",  
"ttl": 333,  
"rdata": [  
"1.1.1.1",  
"2.2.2.2",  
"3.3.3.3",  
"4.4.4.4",  
"5.5.5.5"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/SLBPool.jsonschema",  
"description": "SLB Pool description",  
"rdataInfo": [  
{  
"description": "1",  
"forcedState": "NOT_FORCED",  
"probingEnabled": true,  
"availableToServe": true  
},  
{  
"description": "2",  
"forcedState": "FORCED_ACTIVE",  
"probingEnabled": false,  
"availableToServe": true  
},  
{  
"description": "3",  
"forcedState": "FORCED_INACTIVE",  
"probingEnabled": true  
"availableToServe": false,  
},  
{  
"description": "4",  
"forcedState": "NOT_FORCED",  
"probingEnabled": true,  
"availableToServe": true  
},  
{  
"description": "5",  
"forcedState": "NOT_FORCED",  
"probingEnabled": true,  
"availableToServe": true  
}  
],  
"responseMethod": "PRIORITY_HUNT",  
"allFailRecord": {  
"description": "Backup Record"  
"serving": false  
"rdata": "6.6.6.6",  
},  
"monitor": {  
"method": "POST",  
"url": "https://www.google.com",  
"transmittedData": "q=something",  
"searchString": "UltraDNS"  
},  
"regionFailureSensitivity": "LOW",  
"status":"OK"  
"servingPreference": "AUTO_SELECT",  
}  
}  
]  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update Simple
Load Balancing Pools

For full updates (PUT), the SLB Pool profile must be fully specified. Modify
both the Pool Configuration and Records / Backup Record.

**Method and URI** :

PUT https://api.ultradns.com/zones/{zoneName}/rrsets/{type}/{existingPoolName}

  * The {existingPoolName} can either be a Fully Qualified Domain Name, or a Relative Domain Name.

  
![](../Resources/Images/Rest-API_User_Guide/Introduction.png) |  When performing a PUT request on a Simple Load Balancing pool, if the Transmitted Data is being completed as a GET call, you will need to remove the information inside the â â of the Transmitted Data section. Otherwise, you will encounter an error. "monitor": {  
"method": "PUT",  
"url": "http://www.google.com",  
"transmittedData": " ",  
"searchString": "UltraDNS"  
}  
---|---  
  
JSON Example: Full Update IPv4

{  
"ttl": 333,  
"rdata": [  
"1.1.1.1",  
"2.2.2.2",  
"3.3.3.3",  
"5.5.5.5"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/SLBPool.jsonschema",  
"description": "SLB Pool description",  
"rdataInfo": [  
{  
"description": "1"  
"forcedState": "NOT_FORCED"  
"probingEnabled": true  
},  
{  
"description": "2"  
"forcedState": "FORCED_ACTIVE"  
"probingEnabled": false  
},  
{  
"description": "3"  
"forcedState": "FORCED_INACTIVE"  
"probingEnabled": true  
},  
{  
"description": "5"  
"forcedState": "NOT_FORCED"  
"probingEnabled": true  
}  
],  
"responseMethod": "RANDOM",  
"allFailRecord": {  
"rdata": "7.7.7.7",  
"description": "Backup Record"  
},  
"monitor": {  
"method": "POST",  
"url": "http://www.google.com",  
"transmittedData": "q=something",  
"searchString": "UltraDNS"  
},  
"regionFailureSensitivity": "HIGH"  
"servingPreference": "SERVE_PRIMARY"  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Adding a
Record into a Simple Load Balancing Pool

The Adding-Record (AR) operation is a special case of the general SLB Partial
Update Pool steps outlined in this guide, and it follows the same URL and
content format as shown below.

**Method and URI** :

PATCH
https://api.ultradns.com/zones/{zoneName}/rrsets/{type}/{existingPoolName}

  * The {existingPoolName} can either be a Fully Qualified Domain Name, or a Relative Domain Name.

There are two ways to perform this action: Either use a body of [Resource
Record Set (RRSet) DTO](Resource Record Sets.htm#_Ref462834288) or use a body
of the [JSON PATCH DTO](Making Updates via JSON PATCH.htm#_Ref399929538)

  * If using the RRSet DTO method, the body contains the fields that need to be partially updated, which are structurally similar to what is used in Creating a Pool.

JSON Example: Update Pool via JSON Patch

{  
"rdata": ["1.1.1.2"],  
"profile": {  
"rdataInfo": [  
{  
"description": "desc",  
"forcedState": "NOT_FORCED"  
}  
]  
}

  * If using the JSON Patch DTO, the following two methods need to be done in the same PATCH location.

JSON Example: Partial Update Record via JSON Patch

(**Content Type: application/json-patch+json**)

[  
{"op": "add", "path": "/rdata/-", "value": "1.1.1.2"},  
{"op": "add", "path": "/profile/rdataInfo/-", "value": {  
"description": "desc",  
"probingEnabled": true  
"forcedState": "Not_Forced"  
}  
}  
]

  * Both of the above examples achieve the same result on an existing SLB pool.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Remove a
Record in an Simple Load Balancer Pool

JSON Example: Remove a Record in an SLB Pool

[  
{"op": "remove", "path": "/rdata/0"},  
{"op": "remove", "path": "/profile/rdataInfo/0"}  
]

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Updating One
or More Configurations in an SLB Pool

JSON Example: Update Pool Level Configurations

[  
{"op": "replace", "path": "/profile/description", "value": "Pool Level Desc
B"}  
{"op": "replace", "path": "/profile/allFailRecord/rdata", "value": "1.1.1.1"},  
{"op": "replace", "path": "/profile/responseMethod", "value": "ROUND_ROBIN"},  
{"op": "replace", "path": "/profile/monitor/url", "value":
"http://www.twitter.com"}  
{"op": "replace", "path": "/profile/regionFailureSensitivity", "value": "LOW"}  
{"op": "replace", "path": "/profile/servingPreference", "value":
"SERVE_ALL_FAIL"}  
]

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete a
Simple Load Balancing Pool

**Method and URI** :

DELETE
https://api.ultradns.com/zones/{zoneName}/rrsets/{type}/{existingPoolName}

**Parameters** : None

**Body** : None

**Response** : If delete happens immediately, Status Code of 204 is returned
with no body content.

**Errors** : An error is returned under the following conditions:

  * If {taskId} does not exist.

  * If {zoneName} is not a valid ZoneName.

    * The {existingPoolName} can either be a Fully Qualified Domain Name, or a Relative Domain Name.

    * The delete endpoints are not affected by the addition of SLB pools, and will remain the same as the other types of pools.

