

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

## Audit Log Report

Unlike the [Projected Query Volume Report](Projected Query Volume Report.htm),
[Zone Query Volume Report](Zone Query Volume Report.htm), and the [Reporting
APIs](Reporting APIs.htm), the Audit Log Report does not require the usage of
the Report RequestID to generate the request for the report, and subsequently
the return of the report. When an Audit Log Report is requested, the detailed
report is returned to the user immediately.

![](../../Resources/Images/Rest-API_User_Guide/Introduction_66x77.png) |  The Audit Log Report can be returned in a .CSV format, but will require an additional step beyond the default JSON requirements. In the header section, you will need to include the additional field: **Accept: text/csv**.   
---|---  
  
### Requesting Audit Log Report

**Method and URI** :

GET
https://api.ultradns.com/reports/dns_configuration/audit?filter=any_search_param&limit=any_integer

**Parameters** : Must contain a Audit Log Query Parameters.

### Audit Log Query Parameters DTO

Audit Log Query Parameters

Field |  Description |  Type  
---|---|---  
**filter** |  Defines the filter criteria for Audit Log.

  * **accounts** â Comma-separated list of account names. Default value is **None** , which will return ALL accounts of the logged in user.
  * **users** \- Comma-separated list of user names. Default value is **None** , which will return ALL users.
  * **change_type** â The type of change to display. Valid values of change_type can be obtained using Audit Log Query Filters. Default value is None, which will return all change_type values.
  * **object_type** â The type of object to display. Valid values of object_type can be obtained using Audit Log Query Filters. Default value is None, which will return all object_type values.
  * **object_name** â The name of the object. Default value is None, which will return all object_name values.
  * **parent_name** â The name of the parent object. Default value is **None** , which will return all parent_name values. 
  * **date_range** â The specific date range to filter the results by. Date ranges can be provided in the following format:
    * 15m = 15 minutes from the current date.
    * 5h = 5 hours from the current date.
    * 30d = 30 days from the current date.
    * 5w = The last 5 weeks from the current date.
    * 1month = The last calendar month from the current date.
    * {start_date â {end_date} = Provide a specific date range in GMT format. (yyyyMMddHHmmss) 
  * **change_comment** \- The text fragment of Change Comments search for. Special characters need to be URL encoded. 
    * When using a colon (:) as a search paramter for the Audit Log Report, â/: â (slash colon) is required instead of just a colon ( **:** ). 
    * Search criteria is case sensitive, and will be returned on a partial match (all records containing your search criteria will be returned).
    * Example URL encoded - "Special change @ & # comment" would be Special%20change%20%40%20%26%20%23%20comment

|  String.  
**limit** |  Allows for pagination of the Audit records received. Maximum value for results received is 250. Minimum is 1. Default value is 50. |  Integer.  
  
**Body** : None

**Response** : If task completes, Status Code 200 OKis returned with an Audit
Log Response Parameters,and a response header containing the Link Header
having URLS of nextand previous pages as applicable.

### Audit Log Response DTO

Audit Log Response Parameters

Field |  Description |  Type  
---|---|---  
objectType |  The type of the object that is being audited. |  String.  
changeType |  Audited action. |  String.  
object |  The name of the object that is being audited. |  String.  
user |  The name of the user who performed the action. |  String.  
ipAddress |  IP address of user or logic who performed the action. |  String.  
changeTime |  Date and Time when action was performed. |  String.  
account |  Account name from which audit was done. |  String.  
parent |  The name of the parent object. |  String.  
detail |  The detail of the audit record. |  AuditLogDetail.  
changeComment |  The details of the most recent comment provided. |  String.  
  
Audit Log Detail Parameters

Field |  Description |  Type  
---|---|---  
**changes** |  The list of details of changes that take place by CRUD operation. |  List of Audit Log Change Detail Parameters.  
  
Audit Log Change Detail Parameters

Field |  Description |  Type  
---|---|---  
name |  The name of the attribute that was added/updated/deleted. |  String.  
from |  The attribute "from" represents the old value of attribute "name" in case of update/delete operation. |  String.  
to |  The attribute "to" represents the new value of attribute "name" in case of update/add operation. |  String.  
  
Response Headers

Field |  Description  
---|---  
Link |  **Relative URL to next page of report if available** : <v1/reports/dns_configuration/audit?filter=filter_spec&cursor=cursor_spec&Limit=limit_spec&cursorOperation=NEXT>; rel="next" **Relative URL to previous page of report if available** : <v1/reports/dns_configuration/audit?filter=filter_spec&cursor=cursor_spec&Limit=limit_spec&cursorOperation=PREVIOUS>; rel="previous"  
Limit |  The limit specified in audit log query parameter  
Results |  Total rows in the report page  
  
JSON Example: Audit Log Query Parameters Successful Response

{

"auditRecords":[

{

"objectType": "TXT"

"changeType": "MODIFY"

"object": "date.gmon-a.invalid."

"user": "gmonitor"

"ipAddress": "209.173.57.233"

"changeTime": "2016-06-12 21:48:02.0"

"account": "GTV8"

"parent": null

"detail": {

"changes": [

{

"name": "Comments"

"from": "Mon Jun 13 03.15.02 2016"

"to": "Mon Jun 13 03.18.02 2016"

}

],

"others": [0]

}

}

]

}

**Errors** : An error code is returned under the following conditions:

  * If the âlimitâ value is not between 0 and 250.

  * If the âfilterâ parameterâs value is syntactically incorrect. The value must be a sequence of âkey:valueâ pair where each pair is separated by â::â.

  * If invalid filter âkeyâ is supplied in the request.

  * If the date range provided in the filter value is not in the format of âyyyyMMddHHmmssâ.

  * If the start date given in the date range is greater than the end date.

  * If the logged in user is not authorized for the accounts given in the filter parameter.

JSON Example: Audit Log Example Requests

**Example - List latest 50 Audit Records**

GET https://api.ultradns.com/reports/dns_configuration/audit HTTP/1.1

  * If filter query parameter is not given then by default last 24h audit records are returned.

  * The records retrieved will be sorted in DESC order

  * The default values of limit is 50.

**Example â List latest 250 Audit Records**

GET https://api.ultradns.com/reports/dns_configuration/audit?limit=250

**Example â List Audit Records for a specific date range**

GET
https://api.ultradns.com/reports/dns_configuration/audit?filter=date_range:20160302290813-20160402193020

**Example â List Audit Records for a specific User**

GET https://api.ultradns.com/reports/dns_configuration/audit?filter=users:ABLE

**Example â List Audit Records for a specific object name**

GET
https://api.ultradns.com/reports/dns_configuration/audit?filter=object_name:127.0.0.1

**Example â List Audit Records for a specific object name and change type**

GET
https://api.ultradns.com/reports/dns_configuration/audit?filter=object_name:127.0.0.1::change_type:ZONE_TRANSFER_FAILURE

**Example â List Audit Records for a specific parent name**

GET
https://api.ultradns.com/reports/dns_configuration/audit?filter=parent_name:test-
domain.com.

**Example â List Audit Records for a specific parent name and change type**

GET
https://api.ultradns.com/reports/dns_configuration/audit?filter=parent_name:test-
domain.com.::change_type:ZONE_TRANSFER_FAILURE

### AXFR Failure Reporting Audit Log

The **AXFR Failure Reporting API** allows you to generate detailed reports on
Zone Transfer Failures (AXFR) across your authoritative DNS zones. This API is
designed to help DNS administrators and operators who utilize DNS redundancy
or manage multiple zones, providing visibility into transfer failures that
could impact zone propagation and redundancy.

The primary filter parameter used in this API is **change_type:
ZONE_TRANSFER_FAILURE**. The following Method examples returns the following
details:

  * **Date Range** : 03/26/2024 â 09/23/2024

  * **Change Type** : Zone_Transfer_Failure

  * Returned result **limit** : 50

**Method and URI** :

GET https://api.ultradns.com/reports/dns_configuration/audit?
filter=date_range:20240326183000-20240923133537::change_type:ZONE_TRANSFER_FAILURE&limit=50

**Body:** None

**Parameters** : Must contain an Audit Log Query Parameters DTO.

**Response** : If task completes, Status Code 200 OK is returned with an Audit
Log Response DTO, and a response header containing the Link Header having URLS
of next and previous pages as applicable.

**Errors** : An error code is returned under the following conditions:

  * If the âlimitâ value is not between 0 and 250.

  * If the âfilterâ parameterâs value is syntactically incorrect. The value must be a sequence of âkey:valueâ pair where each pair is separated by â :: â(colon).

  * If invalid filter âkeyâ is supplied in the request.

  * If the date range provided in the filter value is not in the format of â**yyyyMMddHHmmss** â.

  * If the start date given in the date range is greater than the end date.

  * If the logged in user is not authorized for the accounts given in the filter parameter.

JSON Example: AXFR Failure Reporting Audit Log Response

JSON Example: AXFR Failure Reporting Audit Log Response ```json {
"auditRecords": [ { "objectType": "PRIMARY_NAMESERVER", "changeType":
"ZONE_TRANSFER_FAILURE", "object": "44.194.226.84", "user": "neustar1",
"ipAddress": "23.21.206.251", "changeTime": "2024-09-23 11:19:00.0",
"account": "GTV8", "parent": "10records-50.invalid.", "detail": { "others": [
{ "name": "Failure Reason", "value": "Connection timed out" } ] } } ] } ```

### Audit Log Query Filters

**Method and URI** :

GET https://api.ultradns.com/reports/dns_configuration/audit/filters

**Parameters** : The following Query Parameter will be used:

Audit Log Query Parameter

Field |  Description |  Type  
---|---|---  
**dateRange** |  The specific date range to filter the results by. Date ranges can be provided in the following format:

  * 15m = 15 minutes from the current date.
  * 5h = 5 hours from the current date.
  * 30d = 30 days from the current date.
  * 5w = The last 5 weeks from the current date.
  * 1month = The last calendar month from the current date.

{start_date â {end_date} = Provide a specific date range in GMT format. (yyyyMMddHHmmss) **Example** : 20160321123010 - 20160401113312 |  String.  
  
**Body** : None

**Response** : If task completes, Status code 200 OK is returned with an Audit
Log Query Filter Parameters.

### Audit Log Query Filter Response DTO

Audit Log Query Filter Parameters

Field |  Description |  Type  
---|---|---  
key |  Key for audit url. These keys could be value of object_type, change_type etc. |  String.  
url |  The example audit url to search records based the given key. |  String.  
  
JSON Example: Audit Log Query Filters Response

{

"filters": [

"objectTypes": [

{

"key": "A"

"url": "/reports/dns_configuration/audit?filter=object_type:A"

},

{

"key": "SOA"

"url": "/reports/dns_configuration/audit?filter=object_type:SOA"

},

{

"key": "NS"

"url": "/reports/dns_configuration/audit?filter=object_type:NS"

}

],

"changeTypes": [

{

"key": "ADD"

"url": "/reports/dns_configuration/audit?filter=change_type:ADD"

},

{

"key": "FAILED_LOGIN"

"url": "/reports/dns_configuration/audit?filter=change_type  
  
:FAILED_LOGIN"

}

],

"users": [

{

"key": "gmonitor"

"url": "/reports/dns_configuration/audit?filter=user:gmonitor"

},

{

"key": "ketkitest"

"url": "/reports/dns_configuration/audit?filter=user:ketkitest"

},

{

"key": "sswamy"

"url": "/reports/dns_configuration/audit?filter=user:sswamy"

}

],

"accounts": [

{

"key": "GTV8"

"url": "/reports/dns_configuration/audit?filter=account:GTV8"

},

{

"key": "sswamy"

"url": "/reports/dns_configuration/audit?filter=account:sswamy"

}

]

]

}

**Errors** : An error code is returned under the following conditions

  * Invalid X-User {userName} supplied in the request header. This user is not linked with any account.â

