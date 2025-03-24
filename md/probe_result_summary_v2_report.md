

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

## Probe Result Summary v2 Report

Unlike the Probe Result Summary Report, the Probe Result Summary version 2
Report has been streamlined to not require as many mandatory fields to
generate the request for the report, and subsequently, the return of the
report. When a Probe Result Summary v2 Report is requested, the detailed
report is returned to the user immediately.

_Please note that the /v2/ path is required in the Method and URI to correctly
utilize this report._

### Requesting Probe Result Summary v2 Report

**Method and URI** :

GET https://api.ultradns.com/v2/reports/traffic_services/probe_result/summary

**Parameters** : Must contain a Probe Results Summary v2 Query Parameters.

**Body** : None

### Probe Results Summary v2 Query Parameters

Probe Results Summary v2 Query Parameters

Field |  Description |  Type  
---|---|---  
accountName |  **Required**. The Account for which the Probe Result Summary Report is being requested. |  String.  
zoneName |  **Optional**. The Zone under the account for which the Probe Result Summary Report is being requested. |  String.  
poolName |  **Optional**. The Pool under the Zone, and under the Account specified for which the Probe Result Summary Report is being requested. |  String.  
trafficServicePoolType |  **Optional**. The type of Pool for which the Probe Result Summary Report is being requested. If not specified, value will be **ALL**. | 

  * SIMPLE_LOAD_BALANCING
  * SIMPLE_FAILOVER
  * TRAFFIC_CONTROLLER
  * SITE_BACKER
  * ALL

  
probeResultType |  **Optional**. The type of probe result to view in the report being requested. If not specified, this will be ALL.  | 

  * ALL
  * SUCCESS
  * FAILURE

  
poolRecord |  **Optional**. The record within the pool for which the report is being requested. |  String.  
poolRecordType |  **Optional**. The type of record within the pool for which the report is being requested. If not specified, this will be ALL.  | 

  * A
  * AAAA
  * CNAME
  * ALL

  
poolProbeRegion |  **Optional**. The region from which the pool record was probed for report is being requested. If not specified, this will be ALL.  | 

  * NORTH_AMERICA_EAST
  * NORTH_AMERICA_WEST
  * NORTH_AMERICA_CENTRAL
  * EUROPE_EAST
  * EUROPE_WEST
  * SOUTH_AMERICA
  * ASIA
  * CHINA
  * ALL

  
reportStartDateTime |  **Optional**. The StartDateTime in ISO 8601 UTC (yyyy-MM-ddTHH:mm:ss.SSSZ) for the period for which the Probe Result Summary Report is being requested. StartDateTime must not be more than three (3) months old. The date range (begin â end date) for the report cannot be greater than seven (7) days. If not specified, this will be set to last twenty four (24) hours. |  Date-time.  
reportEndDateTime |  **Optional**. The EndDateTime in ISO 8601 UTC (yyyy-MM-ddTHH:mm:ss.SSSZ) for the period for which the Probe Result Summary Report is being requested. The date range (begin â end date) cannot be greater than seven (7) days. |  Date-time.  
limit |  **Optional**. The number of rows per page for paginated responses. The default is 1,000 if not specified. The maximum value that can be provided for the limit is 1,000. |  Integer.  
  
  
**Response** : If task completes, Status code 200 OK is returned with a Probe
Result Summary v2 DTO and the following data:

Response Body |  Description |  Type  
---|---|---  
sbtcprobeSummaryRow |  The list of Probe Result Summaries. |  Array.  
sbtcprobeSummaryCount |  The number of Rows in the report. |  Long.  
  
  
**Errors** : An error code is returned under the following conditions:

  * If the reportEndDateTime is earlier than the reportStartDateTime.

  * If the duration between reportStartDateTime and reportEndDateTime exceeds 7 days.

  * If the reportStartDateTime is older than 3 months.

  * If the {accountName} cannot be accessed by the current userName.

### Probe Result Summary v2 Output DTO

Probe Result Summary v2 DTO

Field |  Description |  Type  
---|---|---  
accountName |  The Account associated to the Probe Result Summary row. |  String.  
zoneName |  The Zone associated to the Probe Result Summary row. |  String.  
poolName |  The Pool associated to the Probe Result Summary row. |  String.  
poolRecord |  The record within the pool that was probed. | String.  
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

  
successes |  The number of Probes that were successful for the associated Pool Name within the requested report period, from all probe regions for all records under the pool. |  Integer.  
failures |  The number of Probes that failed for the associated Pool Name within the requested report period, from all probe regions for all records under the pool. |  Integer.  
warnings |  The number of Probes that were in warning state for the associated Pool Name within the requested report period, from all probe regions for all records under the pool. |  Integer  
critical |  The number of Probes that were in critical state for the associated Pool Name within the requested report period, from all probe regions for all records under the pool. | Integer  
total |  The number of Probes that were executed for the associated Pool Name within the requested report period, from all probe regions for all records under the pool. |  Integer.  
successPercentage |  The percentage of Probes that were successful for the associated Pool Name within the requested report period, from all probe regions for all records under the pool. |  Integer  
failurePercentage |  The percentage of Probes that failed for the associated Pool Name within the requested report period, from all probe regions for all records under the pool. |  Integer  
warningPercentage |  The percentage of Probes that were in warning state for the associated Pool Name within the requested report period, from all probe regions for all records under the pool. |  Integer  
criticalPercentage |  The percentage of Probes that were in critical state for the associated Pool Name within the requested report period, from all probe regions for all records under the pool. |  Integer  
reportStartDateTime |  The StartDateTime from which the report was requested. |  Date-Time.  
reportEndDateTime |  The EndDateTime up to which the report was requested. |  Date-Time.  
trafficServicePoolType |  The Pool type associated to the Probe Result Summary row. | 

  * SIMPLE_LOAD_BALANCING
  * SIMPLE_FAILOVER
  * TRAFFIC_CONTROLLER
  * SITE_BACKER

  
  
JSON Example: Probe Result Summary v2 Report Response

JSON Example: Probe Result Summary v2 Report Response ```json {
"sbtcprobeSummaryRow": [ { "accountName": "javauie2e", "zoneName":
"slb.test.com.", "poolName": "test.slb.test.com.", "poolRecord":
"www.google.com.", "poolRecordType": "CNAME", "poolProbeRegion": "North
America Central", "successes": 60, "failures": 0, "warnings": 0, "critical":
0, "total": 60, "successPercentage": 100.0, "failurePercentage": 0.0,
"warningPercentage": 0.0, "criticalPercentage": 0.0, "startDateTime":
"2016-06-15T12:01:00.000Z", "endDateTime": "2016-06-15T12:59:00.000Z",
"trafficServicePoolType": "SIMPLE_LOAD_BALANCING" } ],
"sbtcprobeSummaryCount": 6 } ```

Response Link Headers

Field |  Description  
---|---  
Link |  **Relative URL to next page of report if available** : GET <v2/reports/traffic_services/probe_result/summary ?accountName=GTV8& cursorOperation=NEXT&limit=50>; rel="next" **Relative URL to previous page of report if available** : <v2/reports/traffic_services/probe_result/summary ?accountName=GTV8& cursorOperation=PREVIOUS&limit=50>; rel="previous"  
  
![](../../Resources/Images/Rest-API_User_Guide/Making Updates via JSON PATCH_68x78.png) |  If a Reportâs Results exceed 1,000 records per page, you can use the âNext / Previousâ header command to search the additional results.  
---|---

