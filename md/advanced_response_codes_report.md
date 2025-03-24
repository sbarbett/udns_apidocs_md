

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

## Advanced Response Codes Report

The Advanced Response codes report shows the DNS return codes for zones. This
report can indicate a trend in DNS return codes, or pinpoint where or when
specific DNS return codes began occurring in responses.

### Requesting Advanced Reponse Codes Report

**Method and URI** :

POST
https://api.ultradns.com/reports/dns_resolution/advanced_response_codes?offset={offset}&limit={limit}

  
**Parameters** : Can include the following:

### Advanced Response Codes Parameters

Advanced Response Codes Parameters DTO

Parameter |  Description |  Type  
---|---|---  
offset |  This field is optional.  If not specified, initial records will always be returned specified to limit. This parameter allows pagination on the reporting records retrieved. The offset will be the integer value that specifies the position of first result to be retrieved. Specify offset as 0 for first results to be retrieved. |  Integer. Optional.  
limit |  This field is optional.  If not specified, the total number of records returned in the response will be equal to the default value 1000. This parameter allows pagination on the reporting records retrieved. The maximum number of results to be retrieved in a single response is 10,000 records. |  Integer. Optional.  
  
**Body** : Must contain Advanced Response Codes DTO

**Response** : If task completes, Status Code 201 is returned with a requestId
in the response body.

**Errors** : An error code is returned under the following conditions:

  * Error Code 401 â âUnauthorized. Token not found, expired or invalid.â

  * Error Code 400 â âreportEndDate is before reportStartDate.â

  * Error Code 400 â âDate provided is not in a valid format.â

  * Error Code 400 â âAccount name not provided.â

  * Error Code 400 â âreportStartDate / reportEndDate is a future date.â

  * Error Code 400 â âOffset value is a negative value.â

  * Error Code 400 â âreportStartDate is older than 90 days.â

### Advanced Response Codes Report DTO

Advanced Response Codes DTO

Field |  Description |  Type  
---|---|---  
accountName |  The name of the account. |  String. Required.  
zoneName |  The results of the one zone being returned.

  * When not specified, all zones under the account will be queried for reporting.
  * Wildcards in the zone name are currently not supported.
  * Zone names with and without a DOT(.) at the end are supported.

|  String. Optional  
reportStartDate |  The reportStartDate must be supplied in the ISO 8601 UTC format (yyyy-MM-dd).

  * The maximum number of days between the reportStartDate and reportEndDate cannot exceed 90 days. 
  * If not provided, will default to yesterdayâs date.
  * The reportStartDate must be before or the same as the reportEndDate.
  * The reportStartDate cannot be more than 90 days prior to the current date.
  * The reportStartDate cannot be a future date.

|  Date. Optional  
reportEndDate |  The reportEndDate must be supplied in the ISO 8601 UTC format (yyyy-MM-dd).

  * The maximum number of days between the reportStartDate and reportEndDate cannot exceed 90 days. 
  * If not provided, will default to yesterdayâs date.

|  Date. Optional.  
  
JSON Example: Requesting Advanced Response Codes Report

JSON Example: Requesting Advanced Response Codes Report ```json {
"advancedResponseCodes": { "accountName": "teamrest", "reportStartDate":
"2017-05-20", "reportEndDate": "2017-07-20", "zoneName": "apexcnamedemo1.com."
} } ```

### Retrieving Advanced Response Codes Report

**Method and URI** :

GET https://api.ultradns.com/requests/{requestID}

**Parameters** : Must contain a ReportRequest DTO.

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
Advanced Response Codes Report Output DTO in the response body. Each value is
comma-separated.

**Errors** : An error code is returned under the following conditions:

  * Error Code 401 â âUnauthorized. Token not found, expired or invalid.â

  * Error Code 404 â âNo report with the given ID was requested before.â

### Report Request ID DTO

The requestID is a randomly generated ID of letters and numbers sent to the
user after the successful request for a report.

ReportRequest DTO

Field |  Description |  Type  
---|---|---  
**requestID** |  The requestID that is provided to the user once a request for a report has been made.

  * For the Projected Query Volumes report, the requestID will have the following prefix: PQV.

|  String.  
  
JSON Example: Request ID return

Status 201 Created  
  
{  
  
"requestId": "PQV-d5a4c7ce"  
  
}

Advanced Response Codes Report Output DTO

Response Body |  Description |  Type  
---|---|---  
responseCount |  The total sum of all of the returned âcountâ fields returned as an integer value. (i.e. refusedCount, notimpCount, nxdomainCount etc) |  Long.  
reportStartDate |  The date from which the report aggregation begins for the zone. |  Date.  
reportEndDate |  The date on which the aggregation ends for the zone |  Date.  
refusedCount |  The total count of Queries refused. |  Long.  
notimpCount |  The total count of Not implemented results. |  Long.  
nxdomainCount |  The total count of Non-existent domains returned. |  Long.  
servfailCount |  The total count of Server failures returned.. |  Long.  
formerrCount |  The total count of Format errors returned. |  Long.  
noerrorCount |  The total count of No errors returned. |  Long.  
accountName |  The name of the Account being queried. |  String.  
zoneName |  The Zone Name being queried.  |  String.  
  
JSON Example: Retrieving Advanced Response Codes Report

JSON Example: Retrieving Advanced Response Codes Report ```json [ {
"responseCount": 1, "reportStartDate": "2016-03-29", "reportEndDate":
"2016-03-29", "refusedCount": 0, "notimpCount": 0, "nxdomainCount": 0,
"servfailCount": 1, "formerrCount": 0, "noerrorCount": 0, "accountName":
"teamrest", "zoneName": "apexcnamedemo1.com." } ] ```

.CSV Example: Advanced Response Codes Report

Total Response Count,Report Start Date,Report End Date,Refused Count,Not
Implemented Count,Nxdomain Count,Service fail Count,Formerr Count,No Error
Count,Account Name,Zone Name

11084,2018-02-20,2018-05-07,0,0,0,0,0,11084,GTV8,gmon-a.invalid.

