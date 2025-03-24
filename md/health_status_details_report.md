

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

# Health Status Details Report

The Health Status Details Report returns the number of validation errors,
warnings, and/or best practice violations for domains within accounts that you
have access to.

**Method and URI** :

GET https://api.ultradns.com/v1/dns_configuration/health_status/detail

**Body** : None

**Parameters** : Must include Health Status Detail Report Query Parameters.

## Health Status Detail Report Query Parameters

Field |  Description |  Type  
---|---|---  
q |  **Optional**. This search string will be matched with account name and domain name (with OR condition). The matching entries will be returned in the report.  Special characters need to be URL encoded.  Example URL encoded â âtest @ & # accountâ would be "test%20%40%20%26%20%23%20account" Default value will be null and returns entries for all objects (zones and accounts) available for the user.  |  String  
sort |  **Optional**. This is used to sort the results. The valid values are:

  * **healthScore** (default)
  * **zoneName**
  * **accountName**

|  String  
order |  **Optional**. This is used to get the results in an specified order. The valid values are:

  * **ASC** (default)
  * **DESC**

|  Enum  
category |  **Optional**. The category of health check results. The following categories are possible:

  * **ALL** (default)
  * **NS**
  * **SOA**
  * **MX**
  * **DNSSEC**
  * **DOMAIN**

|  Enum  
limit |  **Optional**. The number of rows per page for paginated responses. The default is 1000 if not specified. The maximum value for the limit is 1000 and minimum value is 1. |  Integer  
  
**Response** : Status Code 200 OK is returned with the
HealthStatusDetailReport DTO.

**Errors** : An error is returned under the following conditions:

  * If unauthorized user tries to call this API.

  * If invalid values for query parameters q, sort, order, category and limit are provided by user.

## HealthStatusDetailReport DTO

Field |  Description |  Type  
---|---|---  
healthStatusRecordsList |  The list of HealthStatusRecords. |  List of HealthStatusRecord DTO  
  
## HealthStatusRecord DTO

Field |  Description |  Type  
---|---|---  
zoneName |  The name of zone. |  String  
accountName |  The name of account. |  String  
okCount |  The count of total OK health check results. |  Long  
errorCount |  The count of total ERROR health check results. |  Long  
warningCount |  The count of total WARNING health check results. |  Long  
bestPracticeViolationCount |  The count of total health check results related to BEST_PRACTICE violations. |  Long  
infoCount |  The count of total INFO health check results. |  Long  
naCount |  The count of total NA health check results. |  Long  
healthScore |  The health score associated with the zone with a maximum value of 10.00 |  Float  
  
JSON Example: Health Status Detail Report Response

JSON Example: Health Status Detail Report Response ```json {
"healthStatusRecordsList": [ { "zoneName": "example.com.", "accountName":
"Account 1", "okCount": 10, "errorCount": 2, "warningCount": 2,
"bestPracticeViolationCount": 3, "infoCount": 5, "naCount": 3, "healthScore":
8.7 }, { "zoneName": "example2.com.", "accountName": "Account 2", "okCount":
9, "errorCount": 3, "warningCount": 3, "bestPracticeViolationCount": 2,
"infoCount": 4, "naCount": 4, "healthScore": 7.3 } ] } ```

## Response Link Headers

Field |  Description  
---|---  
Link |  **Relative URL to next page of report if available** : **GET** <v1/dns_configuartion/health_status/detail?q=zoneName&cursorOperation=NEXT&cursor=<value> &limit=1000>; rel="next"  **Relative URL to previous page of report if available** :  <v1/dns_configuartion/health_status/detail?q=zoneName&cursorOperation=PREVIOUS&cursor=<value> &limit=1000>; rel="previous"   
  
![](../../Resources/Images/Rest-API_User_Guide/Introduction_66x77.png) |  If a Reportâs Results exceed the default limit of 1,000 records per page, you can use the âNext / Previousâ header command to search the additional results.  
---|---

