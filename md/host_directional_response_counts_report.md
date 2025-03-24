

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

## Host Directional Response Counts Report

The Host Directional Response Counts Report displays the number of responses
sent for hosts from a specified region.

The Host Directional Response Counts Report now contains two new parameters:
**zoneNames** and **wrap**. When these two features are provided, up to ten
million records can be returned, and will provide source ip details at the
host level. If wrap is not provided, the Host Directional Response Counts
Report will return the results as normal.

### Requesting Host Directional Response Counts Report

**Method and URI** :

POST  
  
https://api.ultradns.com/reports/dns_resolution/directional_response_counts/host?offset={offset}&limit={limit}

  
**Parameters** : Can include the following:

### Host Directional Response Counts Report Parameters

Host Directional Response Counts Report Parameters

Parameter |  Description |  Type  
---|---|---  
offset |  This field is optional.  If not specified, initial records will always be returned specified to the limit. This parameter allows pagination on the reporting records retrieved. The offset will be the integer value that specifies the position of first result to be retrieved. Specify offset as 0 for the first results to be retrieved. |  Integer. Optional.  
limit |  This field is optional.  If not specified, the total number of records returned in the response will be equal to the default value 1000. This parameter allows pagination on the reporting records retrieved. The maximum number of results to be retrieved in a single response is 10,000 records. |  Integer. Optional.  
  
**Body** : Must contain the Host Directional Response Counts Report DTO.

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

### Host Directional Response Counts Report DTO

Host Directional Response Counts Report DTO

Field |  Description |  Type  
---|---|---  
accountName |  The name of the account. |  String. Required.  
classCNetwork |  The Class C Network from which the dns queries originated. |  String. Optional.  
zoneName |  The results for the one zone that is being returned.

  * Wildcards in the zone name are not currently supported.
  * Zone names with and without a DOT(.) at the end are supported.

|  String. Required.  
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
hostName |  The results for the host that is being returned, if specified. (geo ip information)

  * Wildcards in the zone name are not currently supported.

|  String. Optional.  
country |  The country from which the dns queries originated.  |  String. Optional.  
region |  The region from which the dns queries originated. |  String. Optional.  
city |  The city from which the dns queries originated. |  String. Optional.  
zoneNames |  The list of zones for which the report is being generated. The maximum number of zones allowed in this field is 1,000. Either the zoneName or zoneNames parameter need to be included in the DTO body.  |  List <String>. Required.  
wrap |  The wrap parameter is used to return a large number of records in a single response. The maximum number of records that can be returned at once is ten million. If set to **True** , up to ten million records will be returned. If the response counts is larger than ten million, the Task-ID will return an Error. _Additionally, when set to True, the report will only be available in .CSV format_. If set to **False** , the existing behavior of _offset_ and _limit_ will apply. |  Boolean. Optional.  
  
JSON Example: Requesting Host Directional Response Counts Report

{

"hostDirectionalResponseCounts": {

"accountName": "NameOfTheAccount",

"classCNetwork": "10.33.162.0",

"zoneName": "apexcnamedemo.com."

"reportStartDate": "2018-06-05",

"reportEndDate": "2018-09-01"

}

}

### Retrieving Host Directional Response Counts Report

**Method and URI** :

GET https://api.ultradns.com/requests/{requestID}

  
**Parameters** : ReportRequest DTO

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a list
of Host Directional Response Report Response DTO.

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

Host Directional Response Report Response DTO

Response Body |  Description |  Type  
---|---|---  
accountName |  The Account Name for which the report is being generated for. |  String.  
reportStateDate |  The start date that the report is being run from. |  Date.  
reportEndDate |  The end date that the report is being run to. |  Date.  
classCNetwork |  The Class C Network from which the dns queries originated. |  String.  
zoneName |  The Zone that was queried from the given region (country + city + region combination). |  String.  
hostname |  The host that was queried from the given region (country + city + region combination) and the given authNode. |  String.  
country |  The Country from which the dns queries originated. |  String.  
city |  The City (from the above country) from which the dns queries originated. |  String.  
region |  The Region from which the dns queries originated. |  String.  
authNode |  The Authoritative DNS Resolution Node from which the answers originated. These are displayed as airport codes that correspond to the node. |  String.  
responseCount |  The total response count grouped by classCNetwork, country, city, region, and authNode. |  Long.  
hostType |  The type of the host.  This parameter will only be returned in the response if the **wrap** parameter is set to True in the request. |  Integer.  
sourceIP |  The SourceIP from which the dns queries originated. This parameter will only be returned in the response if the **wrap** parameter is set to True in the request. |  String.  
  
### Response Link Headers

Response Links Headers

Field |  Description  
---|---  
Link |  **Relative URL to next page of report if available** : </v1/reports/dns_resolution/directional_response_counts/host ?offset=8&limit=4>; rel="next"  **Relative URL to previous page of report if available** : </v1/reports/dns_resolution/directional_response_counts/host?offset=0&limit=4>; rel="previous" When using the next or previous link header to retrieve report data, you must perform another POST call, and include the original body content (if any) and new query parameters (such as offset and limit).  When continuing to use subsequent Link Headers to retrieve additional results, you must continue to perform the POST call per link header to retrieve the next set of report details.  
Limit |  Specify the maximum number of records in requested response. Cannot be greater than maximum allowed limit. Currently maximum allowed limit is 100k.  
Results |  Total rows in the report response.  
  
JSON Example: Retrieving the Host Directional Response Counts Report

JSON Example: Retrieving the Host Directional Response Counts Report ```json [
{ "accountName": "teamrest", "reportStartDate": "2018-10-03", "reportEndDate":
"2018-10-03", "classCNetwork": "10.33.162.0", "zoneName":
"apexcnamedemo.com.", "hostName": "a1.apexcnamedemo.com.", "country": "united
states", "city": "ashburn", "region": "virginia", "authNode": "IAD",
"responseCount": 100 } ] ```

.CSV Example: Retrieving the Host Directional Response Counts Report

Account Name,Report Start Date,Report End Date,Class C Network,Zone Name,Host
Name,Country,City,Region,Authoritative DNS Node,Total Response Count

teamrest,2018-10-03,2018-10-03,10.33.162.0, apexcnamedemo.com.,
a2.apexcnamedemo.com.,united states,ashburn,virginia,IAD,100

.CSV Example: Retrieving the Host Directional Response Counts Report using
WRAP

Account Name,Report Start Date,Report End Date,Class C Network,Zone Name,Host
Name,Country,City,Region,Authoritative DNS Node,Total Response Count, Host
Type, Source IP

AccountName,2021-02-22,2021-02-22,127.0.0.0,apexcnamedemo.com,,argentina,buenos
aires,ciudad de buenos aires,,0,0,127.0.0.1

AccountName,2021-02-18,2021-02-23,10.33.162.0,apexcnamedemo.com,,argentina,buenos
aires,ciudad de buenos aires,,0,0,10.33.162.159

