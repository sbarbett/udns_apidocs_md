

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

## Failover Report

The Failover Report displays the details for failover and/or failback events
that occurred for an account, within a provided time frame as well as the
reason the event occurred. When a Failover Report is requested, the report is
returned to the user immediately.

### Requesting Failover Report

**Method and URI** :

GET https://api.ultradns.com/reports/traffic_services/failover_report

**Parameters** : Must include Failover Query Parameters.

### Failover QueryParameters

Failover Query Parameters

Field |  Description |  Type  
---|---|---  
accountName |  **Required**. The Account for which the Failover Report is being requested |  String.  
zoneName |  **Optional**. The Zone under the account for which the Failover Report is being requested. |  String.  
poolName |  **Optional**. The Simple Load Balancing Pool under the Zone, and under the Account specified for which the Failover Report is being requested. |  String.  
poolRecord |  **Optional**. The record within the pool for which the report is being requested. |  String.  
poolRecordType |  **Optional**. The type of record within the pool for which the report is being requested. If not specified, this will be ALL. | 

  * A
  * AAAA
  * CNAME
  * ALL

  
trafficServicePoolType |  **Optional**. The type of Pool for which the Failover Report is being requested. If not specified, value will be ALL | 

  * SIMPLE_LOAD_BALANCING
  * SIMPLE_FAILOVER
  * TRAFFIC_CONTROLLER
  * SITE_BACKER
  * ALL

  
reportStartDateTime |  **Optional**. The reportStartDateTime in ISO 8601 UTC (yyyy-MM-ddTHH:mm:ss.SSSZ) for the period for which the Failover Report is being requested. StartDateTime must not be more than three (3) months old. The date range (begin â end date) for the report cannot be greater than thirty (30) days. If not specified, this will be set to last twenty four (24) hours. |  Date-time.  
reportEndDateTime |  **Optional**. The reportEndDateTime in ISO 8601 UTC (yyyy-MM-ddTHH:mm:ss.SSSZ) for the period for which the Failover Report is being requested. The date range (begin â end date) cannot be greater than thirty (30) days |  Date-time.  
limit |  **Optional**. The number of rows per page for paginated responses. The default is 1,000 if not specified. The maximum value that can be provided for the limit is 1,000. |  Integer.  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with the
Failover Report Output DTO and the following data:

Response Body |  Description |  Type  
---|---|---  
probeResultDetails |  The list of Failover records. |  Array.  
probeResultDetailsCount |  The number of Rows in the report. |  Long.  
  
  
**Errors** : An error code is returned under the following conditions:

  * If the reportEndDateTime is earlier than the reportStartDateTime.

  * If the duration between reportStartDateTime and reportEndDateTime exceeds 30 days.

  * If the reportStartDateTime is older than 3 months.

  * If the {accountName} cannot be accessed by the current userName.

### Failover Report Output DTO

Failover Report Output DTO

Field |  Description |  Type  
---|---|---  
accountName |  The Account associated to the Failover row. |  String.  
zoneName |  The Zone associated to the Failover row. |  String.  
poolName |  The Pool associated to the Failover row. |  String  
poolRecord |  The record within the pool that was probed. |  String.  
poolRecordType |  The type of the record within the pool that was probed. | 

  * A
  * AAAA
  * CNAME

  
poolRecordState |  The state of the record associate to the Failover row. | 

  * ACTIVE
  * INACTIVE

  
poolRecordStatus |  The status of the pool record associated to the Failover row. |  String.  
failoverReason |  The reason for the failover event. |  String.  
allFailRecord |  The All Fail record indicator. | 

  * True
  * FALSE

  
trafficServicePoolType |  The Pool type associated to the Failover row. | 

  * SIMPLE_LOAD_BALANCING
  * SIMPLE_FAILOVER
  * TRAFFIC_CONTROLLER
  * SITE_BACKER

  
failoverTime |  The Date and Time when probing began for the record from the probe region. |  Date-Time.  
  
JSON Example: Failover Response

{

"failoverRecordCount": 1000,

"failoverRecords": [

{

"failoverTime": "2020-0929T08:56:14",

"accountName": "javauie2e",

"zoneName": "regex.com.",

"poolName": "200.regex.com.",

"poolRecord": "75.125.23.76",

"poolRecordState": "ACTIVE",

"failoverReason": "Probe Success",

"allFailRecord": true,

"poolRecordStatus": "ok",

"trafficServicePoolType": "SITEBACKED",

"poolRecordType": "A",

},

{

"failoverTime": "2020-0929T08:58:14",

"accountName": "javauie2e",

"zoneName": "regex.com.",

"poolName": "201.regex.com.",

"poolRecord": "74.125.23.76",

"poolRecordState": "INACTIVE",

"failoverReason": "Probe Failure",

"allFailRecord": true,

"poolRecordStatus": "ok",

"trafficServicePoolType": "TRAFFIC_CONTROLLER",

"poolRecordType": "A",

}

]

}

Response Link Headers

Field |  Description  
---|---  
Link |  **Relative URL to next page of report if available** : GET <v2/reports/traffic_services/probe_result/failover_report?accountName=GTV8& cursorOperation=NEXT&limit=50>; rel="next" **Relative URL to previous page of report if available** : <v2/reports/traffic_services/probe_result/failover_report?accountName=GTV8& cursorOperation=PREVIOUS&limit=50>; rel="previous"  
  
![](../../Resources/Images/Rest-API_User_Guide/Making Updates via JSON PATCH_73x84.png) |  If a Reportâs Results exceed 1,000 records per page, you can use the âNext / Previousâ header command to search the additional results.  
---|---

