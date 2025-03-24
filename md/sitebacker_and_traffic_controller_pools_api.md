

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

# SiteBacker and Traffic Controller Pools API

SiteBacker (SB) and Traffic Controller (TC) pools provide advanced services
above what is possible with an RD Pool. Records in a SB or TC pool can have
probes attached to them, which verify the functionality of the servers over a
variety of protocols. Records that fail to return proper responses within the
expected time frame can result in a notification and/or the removal of the
records from the pool. If all records in a pool fail to respond to their
probes, SB and TC pools can be configured to return backup records instead.

SiteBacker and Traffic Controller pools can use the A or AAAA rrtype value.
Please note however, that a SiteBacker and/or Traffic Controller pool cannot
contain both A and AAAA records; individual pools need to be created to
support each of the rrtype values.

While SiteBacker and Traffic Controller pools can intermix CNAME records with
A or AAAA records, it isn't legal to specify a SiteBacker or Traffic
Controller pool of type CNAME. Instead, CNAME records can refer to other SB,
TC, RD, Directional pools, or can be references to standard RRSets inside or
outside of the zone.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Profiles

All pools are implemented as additional information added to [Resource Record
Sets](Resource Record Sets.htm#_Ref442345895) (RRSets). This additional
information is specified in a section with the label profile. Every profile
contains an entry with the label @context. The value of @context is a URI that
uniquely identifies the type of the pool.

The URI for a SiteBacker Pool is
[http://schemas.ultradns.com/SBPool.jsonschema.](http://schemas.ultradns.com/RDPool.jsonschema)

The URI for a Traffic Controller Pool is
[http://schemas.ultradns.com/TCPool.jsonschema.](http://schemas.ultradns.com/RDPool.jsonschema)

### SiteBacker Profile Fields

The other fields in the profile for a SiteBacker Pool are:

SiteBacker Pool Fields

Field |  Description |  Type  
---|---|---  
description |  An optional description of the SiteBacker pool. |  String. Less than 255 characters.  
runProbes |  Indicates whether or not the probes are run for this pool. |  Boolean. If not specified, defaults to true.  
actOnProbes |  Indicates whether or not pool records will be enabled (true) or disabled (false) when probes are run. |  Boolean. If not specified, defaults to true.  
order |  Indicates the order of the records returned by the resolver for the SiteBacker pool. Valid values are FIXED, RANDOM, and ROUND_ROBIN. |  String.  If not specified, defaults to ROUND_ROBIN.  
maxActive |  Specifies the maximum number of active servers in a pool and determines when SiteBacker takes backup servers offline. For example, consider a pool with six servers. Setting Max Active to 4 means SiteBacker takes two servers offline and sends the four active records in the answer. |  Integer.  Value from 1 to the number of records in the pool. If not specified, defaults to â1.â  
failureThreshold |  The minimum number of records that must fail for a pool to be labeled 'FAILED'. If the number of failed records in the pool is greater than or equal to the 'Failure Threshold' value, the pool will be labeled FAILED. For example, a pool with six priority records, one all-fail record, and the Failure Threshold value is set to four (4). If four or more priority records are not available to serve, the pool will be labeled FAILED, and the all-fail record will be served. |  Long.  Valid value between 0 and the number of priority records in the pool.  If not specified, defaults to null. Note: For value â0â or ânull,â the failure-threshold logic will be disabled.  
maxServed |  Determines the number of record answers for each query. This is typically All Active records or a sub set of Max Active. |  Integer. Value from 1 to maxActive. If not specified, defaults to maxActive.  
status |  Returned for all SiteBacker and/or Traffic Controller GET calls. Returns the following results:

  * **OK** â If the number of records serving is equal to the Max Active value, and all the active records are top priority records. For example, if a pool has a Max Active of 1 and the Priority 1 record is serving.
  * **WARNING** â If the number of records serving is equal to the Max Active value, and the active records are not top priority records. For example, if a pool has a Max Active of 1 and the Priority 1 records is not serving and the Priority 2 record is serving.
  * **CRITICAL** â If the number of records serving is less than the Max Active value, or the All Fail record is being served. For example, if a pool has a Max Active of 2, and only one record is serving.
  * **FAILED** â If the FailureThreshold value is â0â or null, and no records are serving, and there is no All Fail record configured.

OR

  * If the number of priority records not available to serve equals or exceeds the FailureThresholdâs value. (For example, if the Failure Threshold value is 3, and there are 3 or more Priority Records that are not available to serve.)

|  String. Ignored if present on PUT or PATCH, returned by GET.  
rdataInfo |  One entry for each entry in rdata. Metadata for each rdata. |  Array of rdataInfo structures, in order matching the rdata entries in the main body. See below for rdataInfo structure.  
backupRecords |  List of backup records for the SiteBacker pool. Specifies the records to be served if all other records fail. There can be one or more A records used as backup records, or a single CNAME record. |  Array of backupRecordInfo structures. Optional.  
backupRecords/backupRecord |  An entry in the list backupRecords list. |  backupRecordInfo structure.  
backupRecords/backupRecord/rdata |  The IPv4 address or CNAME for the backup record. |  String. rdata string (for SiteBacker and Traffic Controller, a valid IPv4 address or CNAME).  
backupRecords/backupRecord/failoverDelay |  Specifies the time, from 0â30 minutes, that SiteBacker waits after detecting that the pool record has failed before activating primary records.  |  Integer. If not specified, defaults to â0.â  
backupRecords/backupRecord/restorationDelay |  Specifies the time SiteBacker waits after detecting that the failed recordâthat was failed-over fromâis no longer in a failure state and will now failback to. 

  * A value of 0 minutes indicates **immediate** failback.
  * If left empty, inherits the failoverDelay value.
  * Acceptable values between 0-30 (min). 

|  Integer. If not specified, defaults to **failoverDelay** value.  
backupRecords/backupRecord/availableToServe |  Indicates whether the pool is active and available to serve records. |  Boolean.  
  
RDataInfo Fields

Field |  Description |  Type  
---|---|---  
state |  The current state of the pool record. Valid values are NORMAL, ACTIVE, and INACTIVE. |  String. Defaults to NORMAL.  
runProbes |  Indicates whether or not probes are run for this pool record. |  Boolean. Defaults to true.  
priority |  Indicates the serving preference for this pool record. |  Integer.  
failoverDelay |  Specifies the time, from 0â30 minutes, that SiteBacker waits after detecting that the pool record has failed before activating secondary records.  |  Integer. If not specified, defaults to 0 (activate the secondary records immediately).   
restorationDelay |  Specifies the time SiteBacker waits after detecting that the failed recordâthat was failed-over fromâis no longer in a failure state and will now failback to. 

  * A value of 0 minutes indicates **immediate** failback.
  * If left empty, inherits the failoverDelay value.
  * Acceptable values between 0-30 (min). 

|  Integer. If not specified, defaults to **failoverDelay** value.  
threshold |  Specifies how many probes must agree before the record state is changed.  |  Integer.  
weight |  Determines the traffic load to send to each server in the Traffic Controller pool.  |  Even integers from â2â to â100.â If not specified, defaults to â2.â Only applies to a record in a Traffic Controller pool. Ignored if present in a POST/PUT/PATCH to a SiteBacker Pool.  
availableToServe |  Indicates whether the pool is active and available to serve records. Applies to JSON response, not JSON request. |  Boolean. Defaults to true.  
status |  Returned for all SiteBacker and/or Traffic Controller GET calls.  Returns the following results: 

  * OK â If the number of records serving is equal to the Max Active value, and all the active records are top priority records. For example, if a pool has a Max Active of 1 and the Priority 1 record is serving. 
  * WARNING â If the number of records serving is equal to the Max Active value, and the active records are not top priority records. For example, if a pool has a Max Active of 1 and the Priority 1 record is not serving and the Priority 2 record is serving.
  * CRITICAL â If the number of records serving is less than the Max Active value, or if the All Fail record is being served. For example, if a pool has a Max Active of 2, and only one record is serving.
  * FAILED â If no records are serving, and there is no All Fail record configured.

|  String.  
type |  Indicates the type of record and/or pool type for the pools in the zone. |  String. Abbreviated Record/Pool type.  
  
JSON Example: SiteBacker RRSet with Profile"ttl": 120,

"rdata": [

"7.7.7.7",

"testrd.dollytest6.com.",

"testsf.dollytest6.com.",

"testslb1.dollytest6.com.",

"testtc.dollytest6.com.",

"xyz.com."

],

"profile": {

"@context": "http://schemas.ultradns.com/SBPool.jsonschema",

"description": "testsb.dollytest6.com.",

"runProbes": true,

"actOnProbes": true,

"order": "ROUND_ROBIN",

"maxActive": 1,

"maxServed": 0,

"status": "OK",

"rdataInfo": [

{

"state": "NORMAL",

"runProbes": true,

"priority": 1,

"failoverDelay": 0,

"restorationDelay": 0,

"threshold": 1,

"availableToServe": false,

"type": "A"

},

{

"state": "NORMAL",

"runProbes": true,

"priority": 1,

"failoverDelay": 0,

"restorationDelay": 0,

"threshold": 1,

"availableToServe": false,

"type": "RD"

},

{

"state": "NORMAL",

"runProbes": true,

"priority": 1,

"failoverDelay": 0,

"restorationDelay": 0,

"threshold": 1,

"availableToServe": false,

"type": "SF"

},

{

"state": "NORMAL",

"runProbes": true,

"priority": 1,

"failoverDelay": 0,

"restorationDelay": 0,

"threshold": 1,

"availableToServe": false,

"type": "SLB"

},

{

"state": "NORMAL",

"runProbes": true,

"priority": 1,

"failoverDelay": 0,

"restorationDelay": 0,

"threshold": 1,

"availableToServe": true,

"type": "TC",

"status": "OK"

},

{

"state": "NORMAL",

"runProbes": true,

"priority": 1,

"failoverDelay": 0,

"restorationDelay": 0,

"threshold": 1,

"availableToServe": false,

"type": "CNAME"

}

],

"backupRecords": [

{

"rdata": "4.4.4.4",

"failoverDelay": 0,

"restorationDelay": 0,

"type": "A",

"availableToServe": false

}

}

}

]

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Traffic
Controller Profile Fields

Traffic Controller pools have very similar fields in their profile to those of
the Site Backer pools. The differences are:

  * The URI @context is "http://schemas.ultradns.com/TCPool.jsonschemaâ.

  * maxServed is not allowed (only one record is ever served at a time in a Traffic Controller pool).

  * Order is not allowed (again, only one record is ever served at a time).

  * maxActive is replaced with maxToLB. The maximum value is the number of pool records. If it is not specified, it defaults to 0.

  * backupRecords is replaced by backupRecord, which is a single backupRecordInfo structure. As in SiteBacker, backupRecord is optional.

JSON Example: Traffic Controller RRSet with Profile

{  
"ttl": 300,  
"rdata": [  
"1.2.3.4",  
"a.domain.name.",  
"9.8.7.6",  
"30.40.50.60"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/TCPool.jsonschema",  
"description": "STRING",  
"runProbes": true,  
"actOnProbes": true,  
"maxToLB": 3,  
"failureThreshold": 0,  
"rdataInfo": [  
{  
"state": "NORMAL",  
"runProbes": true,  
"priority": 1,  
"failoverDelay": 0,

"restorationDelay": 0,  
"threshold": 1,  
"weight": 2,  
"availableToServe": true,

"type": "RD"  
},  
{  
"state": "NORMAL",  
"runProbes": true,  
"priority": 2,  
"failoverDelay": 0,  
"restorationDelay": 0,  
"threshold": 1,  
"weight": 2,  
"availableToServe": true,

"type": "A"  
},  
{  
"state": "NORMAL",  
"runProbes": true,  
"priority": 3,  
"failoverDelay": 0,

"restorationDelay": 0,  
"threshold": 1,  
"weight": 2,  
"availableToServe": true,

"type": "SF"  
},  
{  
"state": "NORMAL",  
"runProbes": true,  
"priority": 4,  
"failoverDelay": 0,

"restorationDelay": 0,  
"threshold": 1,  
"weight": 2,  
"availableToServe": true,

"type": "SLB"  
}  
],  
"backupRecord": {  
"rdata": "9.8.7.6"  
}  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get a
SiteBacker or Traffic Controller Pool

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/{rrType}/{ownerName}

**Parameters** : None.

**Body** : None.

**Response** : If task completes, Status code 200 OK is returned with
SiteBacker Profile Fields and/or Traffic Controller Profile Fields in the body
content.

**Errors** : An error is returned under the following conditions:

  * If this URI does not refer to a SB/TC pool.

  * If you do not have permission to access this SB/TC pool.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get All
SiteBacker and Traffic Controller Pools

**Method and URI** :

To get SiteBacker Pools:

GET https://api.ultradns.com/zones/{zoneName}/rrsets/?q=kind:SB_POOLS

To get Traffic Controller Pools:

GET https://api.ultradns.com/zones/{zoneName}/rrsets/?q=kind:TC_POOLS

To get both SiteBacker and Traffic Controller Pools together:

GET https://api.ultradns.com/zones/{zoneName}/rrsets/?q=kind:SB_POOLS,TC_POOLS

**Parameters** : None.

**Body** : None.

**Response** : If task completes, Status code 200 OK is returned with
SiteBacker Profile Fields and/or Traffic Controller Profile Fields in the body
content.

**Errors** : An error is returned under the following conditions:

  * If this URI does not refer to an SB/TC pool.

  * If you do not have permission to access this SB/TC pool.

![](../Resources/Images/Rest-API_User_Guide/Introduction_70x82.png) |  Users should provide a maximum limit of 1000 when requesting to get all SB/TC pools. If the limit is greater than 1000, the following error message will be returned:  
---|---  
  
{  
errorCode: 22000  
errorMessage: "Invalid Page Limit, the maximum number of records that can be
retrieved are restricted to 1000."  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create
SiteBacker or Traffic Controller Pools

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/rrsets/{rrType}/{ownerName}

**Parameters** : None

**Body** : Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288) with SiteBacker/TrafficController pool profile info,
or a [JSON PATCH DTO](Making Updates via JSON PATCH.htm#_Ref399931231).

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you donât have permission to read this zone.

  * If type is invalid.

  * If {ownerName} is not valid.

  * If invalid data was submitted in the body around any validation error for Failure Threshold.

  * If both A and AAAA record types are included in the same pool.

![](../Resources/Images/Rest-API_User_Guide/Introduction_76x89.png) |  Users should provide a FailureThreshold value between zero and âXâ when creating SB/TC pools, where the value X is the total number of priority records. If the provided value is less than zero or greater than X, the following error message will be returned: {  
"errorCode": 2951,  
"errorMessage": "Invalid Failure Threshold. Failure threshold value should be
from 0 to 1."  
}  
---|---  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update
SiteBacker or Traffic Controller Pools

**Method and URI** :

PUT https://api.ultradns.com/zones/{zoneName}/rrsets/{rrType}/{ownerName}

**Parameters** : None

**Body** : Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288) with SiteBacker/TrafficController pool profile info,
or a [JSON PATCH DTO](Making Updates via JSON PATCH.htm#_Ref399931231).

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to update records.

  * If type is invalid.

  * If {ownerName} does not exist.

  * If both A and AAAA record types are included in the same pool.

![](../Resources/Images/Rest-API_User_Guide/Introduction_70x82.png) |  Users can delete a specific record from a DIR pool by sending a PUT request, without providing that record in the input.  
---|---  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update SiteBacker or Traffic Controller Pools

**Method and URI** :

PATCH https://api.ultradns.com/zones/{zoneName}/rrsets/{rrType}/{ownerName}

**Parameters** : None

**Body** : Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288) with SiteBacker/TrafficController pool profile info,
or a [JSON PATCH DTO](Making Updates via JSON PATCH.htm#_Ref399931231).

**Patachable Objects for SiteBacker and Traffic Controller** :

  * biz.neustar.ultra.rest.dto.SiteBackerPoolProfile

  * biz.neustar.ultra.rest.dto.TCPoolProfile

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If {ownerName} does not exist.

  * If you don't have permission to partial update SB/TC pool.

  * If both A and AAAA record types are included in the same pool.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete
SiteBacker or Traffic Controller Pools

**Method and URI** :

DELETE https://api.ultradns.com/zones/{zoneName}/rrsets/{type}/{ownerName}

**Parameters** : None

**Body** : None

**Response** : If delete happens immediately, Status Code of 204 is returned
with no body content.

  * If delete happens in the background, a Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.  

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to delete records.

  * If type is invalid.

  * If ownerName does not exist.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get Probe
Alerts

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/alerts

**Parameters** : None.

**Body** : None.

**Response** : If task completes, Status Code 200 OK is returned with an Alert
Data List DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If you don't have permissions to access alerts.

  * If this URI does not refer to an SB/TC pool.

  * If you do not have permission to access this SB/TC pool.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Alert Data
DTO

The API call /alerts returns all probing errors for the current user. This
data is returned as AlertData DTOs in an AlertDataList.

AlertData DTO Structure

Field |  Description |  Type  
---|---|---  
poolRecord |  The pool record that triggered the alert. |  String  
probeType |  The name of the probe type. |  String  
  
  
  
  
probeStatus |  The status determined by the probe. Valid values are:

  * OK
  * WARNING
  * CRITICAL
  * FAILED

|  
  
  
  
String  
  
alertDate |  The date the alert occurred. |  String,   
date/time formatted in ISO 8601 format.  
failoverOccurred |  Flag to indicate if failover occurred. |  Boolean  
ownerName |  The ownerName of the pool that alerted. |  String  
status |  Status of the probe. Valid values are Active and Inactive. |  String  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Alert Data
List DTO

AlertData List DTO Structure

Field |  Description |  Type  
---|---|---  
alerts |  The list of all alerts. |  List of Alert Data DTO  
queryInfo/q |  The query used to construct the list. |  String  
queryInfo/sort |  The sort column used to order the list. |  String  
queryInfo/reverse |  Whether the list is ascending (false) or descending (true). |  Boolean  
queryInfo/limit |  The maximum number of rows requested. |  Integer  
resultInfo/totalCount |  Count of all events in the system for the specified query. |  Integer  
resultInfo/offset |  The position in the list for the first returned element (0 based). |  Integer  
resultInfo/returnedCount |  The number of records returned. |  Integer  
  
JSON Example: AlertDataList

{  
"alerts": [  
{  
"status": "Active",  
"ownerName": "host1.example-zone.com.",  
"poolRecord": "172.16.8.1",  
"alertDate": "2014-04-01T08:05:42Z",  
"probeStatus": "FAILED",  
"probeType": "DNS",  
"failoverOccurred": true  
},  
{  
"status": "Active",  
"ownerName": "h.testzone.com.",  
"poolRecord": "1.2.3.4",  
"alertDate": "2014-04-01T17:24:33Z",  
"probeStatus": "FAILED",  
"probeType": "HTTP",  
"failoverOccurred": true  
}  
],  
"queryInfo": {  
"q": "",  
"sort": "alertDate",  
"reverse": false,  
"limit": 100  
},  
"resultInfo": {  
"totalCount": 2,  
"offset": 0,  
"returnedCount": 2  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)TTL Records
Consistency in SiteBacker/Traffic Controller Pool Records

Per [RFC 2181](https://tools.ietf.org/html/rfc2181#section-5.2), the Time To
Live (TTL) of all Resource Records in an RRSet must be the same value.
Whenever any existing SiteBacker / Traffic Controller Pool record TTL is
modified using a partial update (PATCH) request, all other existing SiteBacker
/ Traffic Controller Pool records will also be updated with the modified TTL
value. There will be an audit event for each SiteBacker / Traffic Controller
Pool record modification.

Below is an example scenario of the new TTL function for SiteBacker / Traffic
Controller pools.

If there is an existing SiteBacker / Traffic Controller pool with two records:

  * Record one â Points to 1.1.1.1 with a TTL value of 400

  * Record two â Points to 1.2.3.4 with a TTL value of 86400

If the TTL value for Record one (1.1.1.1) is updated using the partial update
request to change the value from 400 to 500, then the additional record(s)
must be updated as well. In this scenario, Record two (1.2.3.4) will be
altered from a TTL value of 86400 to 500.

