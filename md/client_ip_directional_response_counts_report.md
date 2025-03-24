

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

## Client IP Directional Response Counts Report

The Client IP Directional Response Counts Report displays the number of
responses sent to Client IPs.

### Requesting Client IP Directional Response Counts Report

**Method and URI** :

POST
https://api.ultradns.com/reports/dns_resolution/directional_response_counts/client_ip?offset={offset}&limit={limit}

  
**Parameters** : Can include the following:

### Client IP Directional Response Counts Report Parameters

Client IP Directional Response Counts Report Parameters

Parameter |  Description |  Type  
---|---|---  
offset |  This field is optional.  If not specified, initial records will always be returned specified to the limit. This parameter allows pagination on the reporting records retrieved. The offset will be the integer value that specifies the position of first result to be retrieved. Specify offset as 0 for the first results to be retrieved. |  Integer. Optional.  
limit |  This field is optional.  If not specified, the total number of records returned in the response will be equal to the default value 1000. This parameter allows pagination on the reporting records retrieved. The maximum number of results to be retrieved in a single response is 10,000 records. |  Integer. Optional.  
  
**Body** : Must contain the Client IP Directional Response Counts Report DTO.

**Response** : If task completes, Status Code 201 is returned with a requestId
in the response body.

**Errors** : An error is returned under the following conditions:

  * Error Code 401 â Unauthorized. Token not found, expired or invalid.

  * Error Code 400 â When account name is not provided.

  * Error Code 400 â When Client Class C is not provided.

  * Error Code 400 â If date provided is not in valid format.

  * Error Code 400 â If reportEndDate is before reportStartDate. 

  * Error Code 400 â If reportStartDate or reportEndDate is a future date.

  * Error Code 400 â If reportStartDate is older than 90 days.

  * Error Code 400 â If offset is a negative value.

### Client IP Directional Response Counts Report DTO

Client IP Directional Response Counts Report DTO

Field |  Description |  Type  
---|---|---  
accountName |  The name of the account. |  String. Required.  
classCNetwork |  The Class C Network from which the dns queries originated. |  String. Required.  
zoneName |  The results for the one zone that is being returned.

  * Wildcards in the zone name are not currently supported.
  * Zone names with and without a DOT(.) at the end are supported.

|  String. Optional.  
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
  * The reportEndDate cannot be a future date.

|  Date. Optional.  
clientIP |  The Client IP from which the dns queries originated. |  String. Optional.  
country |  The country from which the dns queries originated.  |  String. Optional.  
region |  The region from which the dns queries originated. |  String. Optional.  
city |  The city from which the dns queries originated. |  String. Optional.  
  
JSON Example: Requesting Client IP Directional Response Counts Report

JSON Example: Requesting Client IP Directional Response Counts Report ```json
{ "clientIPDirectionalResponseCounts": { "accountName": "NameOfTheAccount",
"classCNetwork": "10.33.162.0", "reportStartDate": "2018-06-05",
"reportEndDate": "2018-09-01" } } ```

### Retrieving Client IP Directional Response Counts Report

**Method and URI** :

GET https://api.ultradns.com/requests/{requestID}

  
**Parameters** : ReportRequest DTO

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a list
of Client IP Directional Response Report Response DTO.

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

Client IP Directional Response Report Response DTO

Response Body |  Description |  Type  
---|---|---  
accountName |  The Account Name for which the report is being generated for. |  String.  
reportStateDate |  The start date that the report is being run from. |  Date.  
reportEndDate |  The end date that the report is being run to. |  Date.  
classCNetwork |  The Class C Network from which the dns queries originated. |  String.  
clientIP |  The Client IP from which the dns queries originated.  |  String.  
country |  The Country from which the dns queries originated. |  String.  
city |  The City (from the above country) from which the dns queries originated. |  String.  
region |  The Region from which the dns queries originated. |  String.  
authNode |  The Authoritative DNS Resolution Node from which the answers originated. These are displayed as airport codes that correspond to the node. |  String.  
responseCount |  The total response count grouped by classCNetwork, country, city, region, and authNode. |  Long  
  
### Response Link Headers

Response Links Headers

Field |  Description  
---|---  
Link |  **Relative URL to next page of report if available** : </v1/reports/dns_resolution/directional_response_counts/client_ip ?offset=8&limit=4>; rel="next"  **Relative URL to previous page of report if available** : </v1/reports/dns_resolution/directional_response_counts/client_ip?offset=0&limit=4>; rel="previous" When using the next or previous link header to retrieve report data, you must perform another POST call, and include the original body content (if any) and new query parameters (such as offset and limit).  When continuing to use subsequent Link Headers to retrieve additional results, you must continue to perform the POST call per link header to retrieve the next set of report details.  
Limit |  Specify the maximum number of records in requested response. Cannot be greater than maximum allowed limit. Currently maximum allowed limit is 100k.  
Results |  Total rows in the report response.  
  
JSON Example: Retrieving the Client IP Directional Response Counts Report

{

"accountName": "teamrest",

"reportStartDate": "2018-08-22",

"reportEndDate": "2018-09-01",

"classCNetwork": "10.33.162.0",

"clientIP": "10.33.162.158",

"country": "united states",

"city": "ashburn",

"region": "virginia",

"authNode": "IAD",

"responseCount": 300

},

{

"accountName": "teamrest",

"reportStartDate": "2018-08-22",

"reportEndDate": "2018-08-22",

"classCNetwork": "10.33.162.0",

"clientIP": "10.33.162.159",

"country": "united states",

"city": "frederick",

"region": "maryland",

"authNode": "IAD",

"responseCount": 100

},

JSON Example: Retrieving the Client IP Directional Response Counts Report
```json { "accountName": "teamrest", "reportStartDate": "2018-08-30",
"reportEndDate": "2018-08-30", "classCNetwork": "10.33.162.0", "clientIP":
"10.33.162.160", "country": "united states", "city": "baltimore", "region":
"maryland", "authNode": "IAD", "responseCount": 100 } ```

.CSV Example â Retrieving the Client IP Directional Response Counts Report

Account Name,Report Start Date,Report End Date,Class C Network,Client
IP,Country,City,Region,Authoritative DNS Node,Total Response Count

teamrest,2018-08-22,2018-09-01,10.33.162.0,10.33.162.158,united
states,ashburn,virginia,IAD,300

teamrest,2018-08-22,2018-08-22,10.33.162.0,10.33.162.159,united
states,frederick,maryland,IAD,100

teamrest,2018-08-30,2018-08-30,10.33.162.0,10.33.162.160,united
states,baltimore,maryland,IAD,100

