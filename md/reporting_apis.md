

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

# Reporting APIs

This document details the Neustar UltraDNS Reporting Service API which allows
you to generate a multitude of Reports for various report types and date
configurations.

## Overview

The Reporting Service is a RESTful web service that provides you access to
UltraDNS reports via an API interface. The reporting data retrieved is
returned in response to Reporting service API calls.

### Authorization

The Authorization process is outlined by the following scenarios, and is based
upon the type of report that is being requested.

  1. If the report requested is a Standard report, you do not need to have advanced reporting authorization set at the user account level.

  2. If the report requested is an Advanced report, then the userâs account will be checked for the Advanced reporting authorization before continuing.

  3. If the report requested is for an account that the user belongs to, the user will be granted access to the report.

  4. If the report requested is for an account that the user has access to, the user will be granted access to the report.

  * Once a specific user has been authorized for a specified report, no additional authorizations will be required when retrieving information for the report, until a new report is requested.

Advanced reporting allows you to analyze time data to the minute, and location
data to the client Class C address level. By comparison, the standard
reporting package restricts analysis to only the hour and country level.

## Available Reports

Report Name |  Description |  Report Type |  Output Format  
---|---|---|---  
Projected Query Volume (PQV) Report |  The Projected Query Volumes report provides a snapshot of projected monthly volumes based on 7 and 30 day average query amounts. The details returned by the Projected Query Volume Report for a user that has access to multiple accounts will be consolidated across all of these accounts. |  Standard |  JSON / CSV  
Zone Query (Usage) Volume (ZQV) Report |  The Zone Query Volume report provides aggregated zone query volumes for multiple zones on a monthly basis. The data can be compiled up to 13 months. |  Standard |  JSON / CSV  
Synchronous Zone Query Volume Report |  The Synchronous Zone Query Volume Report provides aggregated zone query volumes for multiple zones within a 7 day period. |  Standard |  JSON  
Zone Daily Query (ZDQV) Report |  The Zone Daily Query Report provides zone query daily volume usage in aggregate for up to 60 days.  This information provides detailed data that may be used to support aggregate monthly totals used for billing, or for the generation of a GUI with daily data. |  Standard |  JSON / CSV  
Host Query Volume (HQV) Report |  The Host Query Volume Report provides aggregated host query volumes for one or multiple hosts within a zone. It is intended to be a âdrill downâ report, designed to get more granular information on a host basis from the Zone Query Volume Report. |  Standard |  JSON / CSV  
Probe Result Summary Report |  The Probe Result Summary Report provides a summary of probe results associated to traffic service pools under a given zone for a given period of time (Max of 7 days at a time). |  Standard |  JSON   
Probe Result Details Report |  The Probe Result Details Report provides specific probe results obtained while probing a given Simple monitoring or Simple Failover traffic service pool under a given zone for a given period of time (Max of 7 days at a time). |  Standard |  JSON  
Audit Log Report  |  The Audit Log Report provides up to 6 months of audit logs of activities. These activities involve DNS configuration changes (like create/update/delete of zones, records, pools), login, account/user related operations etc. |  Standard |  JSON  
Raw Query (RQR) Report |  The Raw Query report includes copious data for both queries and responses. This report can provide details for query and response troubleshooting. |  Standard |  JSON / CSV  
Advanced Response Codes (ARC) Report |  The Advanced Response Codes report shows the DNS return codes for zones. This report can indicate a trend in DNS return codes, or pinpoint where or when specific DNS return codes began occurring in responses. |  Standard |  JSON / CSV  
Client IP Directional Response Counts (CIPDRC) Report  |  The Client IP Directional Response Counts Report displays the number of responses sent to Client IPs. |  Standard |  JSON / CSV  
Host Directional Response Counts (HDRC) Report  |  The Host Directional Response Counts Report displays the number of responses sent for hosts from a specified region. |  Standard |  JSON / CSV  
Country Code Directional Response Counts (CCDRC) Report |  The Country Code Directional Response Counts Report displays the country codes from which the DNS queries originate. |  Standard |  JSON / CSV  
Usage Summary Report |  The Usage Summary Report displays peak data statistics for an account for the last thirty-six months. |  Standard |  JSON / CSV  
Usage Summary Daily Report  |  The Usage Summary Daily Report displays peak data statistics for an account for the month specified. The Usage Summary Daily Report will be available for last thirteen months. |  Standard  |  JSON / CSV  
Probe Result Summary Report  |  The Probe Result Summary Report returns the basic Traffic Service Probe results for an account, by displaying the successes and failures of probes during a set time period. |  Standard |  JSON  
Probe Result Details Report |  The Probe Result Details Report displays the detailed results of Traffic Service Probe results for an account, by displaying the transmitted probe details. |  Standard |  JSON  
Audit Log Report |  The Audit Log Report returns the events captured in the Audit Log for an account. These can include actions taken for a Zone or Record (add / delete / update), the creation of a user, and even the tracking of Change Comments added to an operation. |  Standard |  JSON / CSV  
Probe Result Summary v2 Report |  Probe Result Summary v2 Report returns the same results as the v1 report, but with less requirements required to generate and return the report details.  |  Standard |  JSON  
Probe Result Details v2 Report |  The Probe Result Details v2 Report returns the same results as the v1 report, but with less requirements required to generate and return the report details. |  Standard |  JSON  
Failover Report |  The Failover Report displays the details for failover and/or failback events that occurred for an account. |  Standard |  JSON  
Account Health Report |  The Account Health Report returns a list of health status checks for the accounts that the user has access to, which pertain to best practices and enabled features. |  Standard |  JSON  
Health Status Summary Report |  The Health Status Summary Report provides a quick health status check that identifies the number of possible policy and or configuration violations for your account(s).  |  Standard |  JSON  
Health Status Details Report  |  The Health Status Details Report returns the number of validation errors, warnings, and/or best practice violations for domains within accounts that you have access to. |  Standard |  JSON  
  
## Returning Reporting Results

Given the possibility of report sizes and the speed in which the results could
be returned, reports will be returned in an asynchronous fashion. Any data
that is retrieved in order to produce the report will be internally stored,
and then provided once the user requests the API call to return the report
data via a GET call using a Report Request ID.

![](../../Resources/Images/Rest-API_User_Guide/Introduction_65x76.png) |  The Request ID will be distinguishable for each Report type being requested via the prefix supplied in front of the Request ID being returned. For example, Projected Query Volume report returns a âPQVâ prefix, while Zone Query Volume will return a âZQVâ prefix.   
---|---  
  
The data being held for a query request will be stored and accessible for 60
calendar days from the initial request date. The Report Request ID will only
be valid for the 60 days. After which, a new report request will need to be
submitted, at which time a new Report Request ID will be provided to the user
to obtain the newly requested information.

### Reporter Service Report Properties

Reporter Service Report Properties

Report Name |  Max Limit |  Default Limit |  Max Date Range |  Max Number of Days in Past Allowed  
---|---|---|---|---  
Probe Summary Report |  2000 |  25 |  7 Days |  6 Months (185 Days)  
Probe Details Report |  2000 |  25 |  7 Days |  6 Months (185 Days)  
Projected Query Volume Report |  **NA** |  **NA** |  **NA** |  **NA**  
Zone Query Volume Report |  100,000 |  1,000 |  13 Months |  13 Months  
Synchronous Zone Query Volume Report |  100,000 |  1,000 |  7 Days |  7 Days  
Zone Daily Query Volume Report |  **NA** |  **NA** |  62 Days |  13 Months  
Host Query Volume Report |  100,000 |  1,000 |  7 days |  90 Days  
Audit Report |  250 |  50 |  6 Months |  6 Months  
Raw Query Report |  10,000 |  1,000 |  90 Days |  90 Days  
Advanced Response Codes Report |  10,000 |  1,000 |  90 Days |  90 Days  
Client IP Directional Response Counts Report |  10,000 |  1,000 |  90 Days |  90 Days  
Host Directional Response Counts Report |  10,000 |  1,000 |  90 Days |  90 Days  
Country Code Directional Response Counts Report |  100,000 |  100,000 |  90 Days |  90 Days  
Usage Summary Report |  **NA** |  **NA** |  36 Months |  36 Months  
Probe Result Summary Report  |  1,000 |  1,000 |  7 Days |  6 Months  
Probe Result Details Report |  1,000 |  1,000 |  7 Days |  6 Months  
Audit Log Report |  250 |  50 |  6 Months |  6 Months  
Probe Result Summary v2 Report |  1,000 |  1,000 |  7 Days |  60 Days  
Probe Result Details v2 Report |  1,000 |  1,000 |  7 Days |  60 Days  
Failover Report |  10,000 |  1,000 |  30 Days |  90 Days  
Account Health Report |  10,000 |  1,000 |  N/A |  N/A  
Health Status Summary Report |  10,000 |  1,000 |  N/A |  N/A  
Health Status Details Report  |  100,000 |  1,000 |  N/A |  N/A  
  
The following report figure is a representation of the fields that will be
displayed in the JSON format that is returned upon using the Report ID to
request the data.

## URLs

Use the following base URLs for running REST API calls against the appropriate
UltraDNS environment:

  * Production API: <https://api.ultradns.com>/reports

All of the URI constructs provided in this document use the Production URL.

## Calling the APIs

The UltraDNS APIs accept requests and return responses in JSON format. The
default response format is JSON. A response format of .csv is available on
specific reports, which are noted in this guide.

Controlling the format of the request and response is done by supplying the
"Content-type" and "Accept" HTTP headers respectively, specifying
application/json for the value in either header (or both). Keep in mind that
you do not have to specify JSON for a response.

![](../../Resources/Images/Rest-API_User_Guide/Introduction_71x83.png) |  We use the Postman REST Client to provide example screen shots in this document. Postman is a freely-available REST client that allows you to save and organize frequently-used queries for later use. It can be obtained at [http://www.getpostman.com/](http://www.getpostman.com/)  
---|---  
  
## Responses to API Calls

All operations return a response, and all responses have a response code (HTTP
Status Code). The code number returned depends on the kind of operation you
sent, (GET, POST) and the status of the operation (OK, Created).

Successful Response Codes are returned as follows:

  * Status Code 200 is typically returned for a request (GET) of information and notes the call was Successful, signified by an âOKâ response. If the call was a GET, you should also receive a DTO containing the information you requested.

  * Status Code 201 is typically returned for a POST call and indicates that the object was Created.

If an error condition occurs, you will you will receive a 400 or 500 series
(4xx or 5xx) HTTP Status Code along with an HTTP body containing a specific
UltraDNS error code and a description of the error. For example:

[  
{  
"errorCode": 404,  
"errorMessage":"No report with the given ID was requested  
before."  
}  
]

### Response Link Headers

When using Query Parameters for certain reports, a Response Link Header may be
returned to indicate that the maximum number of results exceeds the specified
query parameter. In these situations, a link header indicating ânextâ will
be provided in the response to allow you to retrieve the next set of report
results. Additionally, a âpreviousâ link will be returned as well to
return to the previous set of report results.

When using the Link Header, you must re-perform the POST call for the Report
along with the original body content (if any was specified) along with your
new query parameters. Each subsequent request will need to be made as a POST
first before retrieving your report details.

