

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

# Health Status Summary Report

The Health Status Summary Report API call returns a condensed summary of the
health status for all of the accounts that a user has access to, that contains
a count of the validation results for each of the following status/category
types.

  1. **OK** \- The number of validations passed for domains.

  2. **ERROR** \- The number of validations failed and the domains are most likely not configured properly for that condition.

  3. **WARNING** \- The number of validations generated warnings and the domains may be misconfigured for that condition; however, it still may function.

  4. **BEST_PRACTICE** \- The number of validations that indicated the domains configuration falls outside the RFC guidelines or recommended best practice for that condition.

  5. **INFO** \- The number of validations yields information, as there is no pass or fail results expected. 

  6. **NA** \- The number of validations cannot run because another required test failed or not applicable.

**Method and URI** :

GET https://api.ultradns.com/v1/dns_configuration/health_status/summary

**Body** : None

**Parameters** : Must include Health Status Summary Report Query Parameters.

## Health Status Summary Report Query Parameters

Field |  Description |  Type  
---|---|---  
**q** |  **Optional**. This search string will be matched with account name and domain name (with OR condition). The matching entries will be returned in the report. Special characters need to be URL encoded. Example URL encoded â âtest @ & # accountâ would be âtest%20%40%20%26%20%23%20accountâ Default value will be null and summary for all objects (zones and accounts) available for the user. |  String  
**category** |  **Optional**. The category of health check results. The following categories are possible:

  * **ALL** (default)
  * **NS**
  * **SOA**
  * **MX**
  * **DNSSEC**
  * **DOMAIN**

|  Enum  
  
**Response** : Status Code 200 OK is returned with the
HealthStatusSummaryReport DTO.

**Errors** : An error is returned under the following conditions:

  * If an unauthorized user tries to call this API.

  * If invalid values for query parameters q and category are provided by user.

## HealthStatusSummaryReport DTO

Field |  Description |  Type  
---|---|---  
**okCount** |  The count of total OK health check results. |  Long  
**errorCount** |  The count of total ERROR health check results. |  Long  
**warningCount** |  The count of total WARNING health check results. |  Long  
**bestPracticeViolationCount** |  The count of total health check results related to BEST_PRACTICE violations. |  Long  
**infoCount** |  The count of total INFO health check results. |  Long  
**naCount** |  The count of total NA health check results. |  Long  
  
JSON Example: Health Status Summary Report Response

JSON Example: Health Status Summary Report Response ```json { "okCount": 1000,
"errorCount": 200, "warningCount": 234, "bestPracticeViolationCount": 325,
"infoCount": 102, "naCount": 47 } ```

