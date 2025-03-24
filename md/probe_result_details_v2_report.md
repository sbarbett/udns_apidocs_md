

Skip To Main Content

Account

Settings

* * *

Logout

[](../News and Updates.htm)

  * placeholder

Account

Settings

* * *

Logout

Filter:

  * All Files

Submit Search

## Probe Result Details v2 Report

Unlike the Probe Result Details Report which is already documented, the
**Probe Result Details v2 Report** has been streamlined to not require as many
mandatory fields to generate the request for the report, and subsequently, the
return of the report When a Probe Result Details v2 Report is requested, the
detailed report is returned to the user immediately.

_Please note that the /v2/ path is required in the Method and URI to correctly
utilize this report._

### Requesting Probe Result Details v2 Report

**Method and URI** :

GET https://api.ultradns.com/v2/reports/traffic_services/probe_result/details

**Parameters** : Must include Probe Result Details v2 Query Parameters.

### Probe Result Details v2 Query Parameters

Probe Result Details v2 Query Parameters

Field |  Description |  Type  
---|---|---  
accountName |  **Required**. The Account for which the Probe Result Details Report is being requested. |  String.  
zoneName |  **Optional**. The Zone under the account for which the Probe Result Details Report is being requested. |  String.  
poolName |  **Optional**. The Pool under the Zone, and under the Account specified for which the Probe Result Summary Report is being requested. |  String.  
trafficServicePoolType |  **Optional**. The type of Pool for which the Probe Result Summary Report is being requested. If not specified, value will be ALL. | 

  * SIMPLE_LOAD_BALANCING
  * SIMPLE_FAILOVER
  * TRAFFIC_CONTROLLER
  * SITE_BACKER
  * ALL

  
poolRecord |  **Optional**. The record within the pool for which the report is being requested. |  String.  
poolRecordType |  **Optional**. The type of record within the pool for which the report is being requested.  If not specified, this will be ALL.  | 

  * A
  * AAAA
  * CNAME
  * ALL

  
poolProbeRegion |  **Optional**. The region from which the pool record was probed for report is being requested.  If not specified, this will be ALL.  | 

  * NORTH_AMERICA_EAST
  * NORTH_AMERICA_WEST
  * NORTH_AMERICA_CENTRAL
  * EUROPE_EAST
  * EUROPE_WEST
  * SOUTH_AMERICA
  * ASIA
  * CHINA
  * ALL

  
probeResultType |  **Optional**. The type of probe result to view in the report being requested. If not specified, this will be ALL. | 

  * ALL
  * SUCCESS
  * FAILURE

  
reportStartDateTime |  **Optional**. The reportStartDateTime in ISO 8601 UTC (yyyy-MM-ddTHH:mm:ss.SSSZ) for the period for which the Probe Result Details Report is being requested. StartDateTime must not be more than three (3) months old. The date range (begin â end date) for the report cannot be greater than seven (7) days. If not specified, this will be set to last twenty four (24) hours. |  Date-time.  
reportEndDateTime |  **Optional**. The reportEndDateTime in ISO 8601 UTC (yyyy-MM-ddTHH:mm:ss.SSSZ) for the period for which the Probe Result Details Report is being requested. The date range (begin â end date) cannot be greater than seven (7) days. |  Date-time.  
limit |  Optional. The number of rows per page for paginated responses. The default is 1,000 if not specified. The maximum value that can be provided for the limit is 1,000. |  Integer.  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with the
Probe Result Details v2 Output DTO and the following data:

Response Body |  Description |  Type  
---|---|---  
sbTcProbeDetailsRow |  The list of Probe Result Details. |  Array.  
sbTcprobeDetailsCount |  The number of Rows in the report. |  Long.  
  
  
**Errors** : An error code is returned under the following conditions:

  * If the reportEndDateTime is earlier than the reportStartDateTime.

  * If the duration between reportStartDateTime and reportEndDateTime exceeds 7 days.

  * If the reportStartDateTime is older than 6 months.

  * If the {accountName } cannot be accessed by the current userName.

### Probe Results Details v2 Output DTO

Probe Result Details v2 Output DTO

Field |  Description |  Type  
---|---|---  
accountName |  The Account associated to the Probe Result Details row. |  String.  
zoneName |  The Zone associated to the Probe Result Details row. |  String.  
poolName |  The Pool associated to the Probe Result Details row. |  String  
trafficServicePoolType |  The Pool type associated to the Probe Result Details row. | 

  * SIMPLE_LOAD_BALANCING
  * SIMPLE_FAILOVER
  * TRAFFIC_CONTROLLER
  * SITE_BACKER

  
probeResultType |  The probeResultType from the request. Value of ALL if both a Success and Failure Probe Result Details Report is being requested. | 

  * SUCCESS
  * FAILURE
  * ALL

  
poolRecord |  The record within the pool that was probed. |  String.  
poolRecordType |  The type of the record within the pool that was probed. | 

  * A
  * AAAA
  * CNAME

  
poolProbeRegion |  The region from which the pool record was probed. | 

  * NORTH_AMERICA_EAST
  * NORTH_AMERICA_WEST
  * NORTH_AMERICA_CENTRAL
  * EUROPE_EAST
  * EUROPE_WEST
  * SOUTH_AMERICA
  * ASIA
  * CHINA

  
probeLogTime |  The Date and Time when probing began for the record from the probe region. |  Date-Time.  
probeResult |  The response for the probe that determined the probe result. |  String.  
probeType |  The type of method that was used for probing. |  String.  
statusCount |  The number of times this result was received for this probe request. |  Integer.  
  
JSON Example: Probe Result Details Report v2 Response

{

"sbTcProbeDetailsRow": [

{

"accountName": "javauie2e",

"zoneName": "e2e-slb.com.",

"poolName": "slbpool1.e2e-slb.com.",

"trafficServicePoolType": "SIMPLE_LOAD_BALANCING",

"probeResultType": "ALL",

"probeLogTime": "2016-06-14T00:00:00.000Z",

"poolRecord": "74.125.138.99",

"poolRecordType": "A",

"poolProbeRegion": "US-EAST",

"probeResult": "Success",

"probeType": "HTTP",

"statusCount": 4,

},

{

"accountName": "javauie2e",

"zoneName": "e2e-slb1.com.",

"poolName": "slbpool1.e2e-slb1.com.",

"trafficServicePoolType": "SITE_BACKER",

"probeResultType": "FAILURE",

"probeLogTime": "2016-06-14T00:00:00.000Z",

"poolRecord": "74.125.138.99",

"poolRecordType": "A",

"poolProbeRegion": "US-EAST",

"probeResult": "Success",

"probeType": "HTTP",

"statusCount": 4

}

],

"sbTcProbeDetailsCount": 5479

}

Response Link Headers

Field |  Description  
---|---  
Link |  **Relative URL to next page of report if available** : GET <v2/reports/traffic_services/probe_result/details?accountName=GTV8& cursorOperation=NEXT&limit=50>; rel="next" **Relative URL to previous page of report if available** : <v2/reports/traffic_services/probe_result/details?accountName=GTV8& cursorOperation=PREVIOUS&limit=50>; rel="previous"  
  
![](../../Resources/Images/Rest-API_User_Guide/Making Updates via JSON PATCH_73x84.png) |  If a Reportâs Results exceed 1,000 records per page, you can use the âNext / Previousâ header command to search the additional results.  
---|---

