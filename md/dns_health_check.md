

Skip To Main Content

Account

Settings

* * *

Logout

[](News and Updates.htm)

  * placeholder

Account

Settings

* * *

Logout

Filter:

  * All Files

Submit Search

# DNS Health Check

The DNS Health Check is a feature that performs various kinds of checks on a
zone that can identify Account Security issues, as well as DNS
misconfigurations. The tests or checks that are executed by the DNS Health
Check system and returned in this report include the following categories and
validations.

  1. **NS Validations**

  2. **SOA Validations**

  3. **MX Validations**

  4. **DNSSEC Validation**

  5. **Domain Validations**

## Execute DNS Health Check

This API call initiates the health check for the given zone name specified as
{zoneName} in the url.

**Method and URI** :

POST https://api.ultradns.com/v1/zones/<zoneName>/healthchecks

**Parameters** : None

**Body** : None

**Response** : If request is valid and accepted by health check system, Status
Code 202 ACCEPTED is returned and a response header containing the URI of
newly created report version.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} does not exist.

  * If unauthenticated user tries to call this API.

  * If user does not have permission to execute DNS health check.

### Response Headers

Field |  Description  
---|---  
location |  The URI of the newly created report version.  
  
## Get DNS Health Check Data

This API call returns the health check report for the given zone name
specified as {zoneName} in the URL. It can return a specific or the latest
version of the report based on the given version specified as {version} in the
URL.

The DNS Health Check maintains a maximum of two versions of the report (a
version of the current run, and one for the previous run). The specific
version as {version} is specified in the format YYYY-MM-DD-HH24:MI:SS.nnnZ.

**Method and URI** :

GET https://api.ultradns.com/v1/zones/<zoneName>/healthchecks/<version>

GET https://api.ultradns.com/v1/zones/<zoneName>/healthchecks/latest

**Parameters** : None

**Body** : None

**Response** : If request is valid and accepted by health check system, Status
Code 200 OK is returned with HealthCheckReport DTO.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} does not exist.

  * If there is no health check report available for {zoneName}.

  * If unauthenticated user tries to call this API.

  * If user requesting the health check does not have permission to retrieve health check report.

HealthCheckReport DTO

Field |  Description |  Type  
---|---|---  
version |  The version of the health check report. |  Timestamp in format YYYY-MM-DD-HH24:MI:SS.nnnZ  
checks |  The list of HealthCheckResultList. |  List of HealthCheckResultList DTO  
state |  The health check report generation state. It can contain one of the following values:

  * **IN_PROGRESS** â Health checks are in progress.
  * **COMPLETED** â Health checks are completed.
  * **FAILED** â Failed to perform health check completely and report is not complete.

|  Enum  
  
HealthCheckResultList DTO

Field |  Description |  Type  
---|---|---  
category |  The category of health check results. |  String.  
results |  The list of HealthCheckResult. |  List of HealthCheckResult DTOs  
status |  Displays the worst of the results received in this category. For example, if results[0] is OK and results[1] is WARNING, the overall status of this category will be WARNING. |  Enum  
state  |  The state of health check of this category. It can contain one of the following values:

  * **IN_PROGRESS** â Health checks are in progress.

  * **COMPLETED** â Health checks are completed.
  * **FAILED** â Failed to perform health check completely and report is not complete. 

|  Enum  
  
HealthCheckResult DTO

Field |  Description |  Type  
---|---|---  
name |  The name or short description of the health check. |  String.  
hint |  _Optional_. Contains hints to optimize or fix the DNS configuration. |  String.  
description |  The detailed description of the health check; why it is needed, and associated RFCs, if any. |  String.  
status |  The status of the Health Check. It can contain one of the following values:

  * **NOT_APPLICABLE** â If health check was not executed.
  * **OK** â Health Check result is optimal and all good.
  * **BEST_PRACTICE** â The health check indicates that the domainâs configuration falls outside of the RFC guidelines or recommended best practices. However, this does not imply a misconfiguration
  * **INFO** â No failure or success just information.
  * **WARNING** â The health check generated a warning and this domain may be misconfigured, however, it may still function.
  * **ERROR** â The health check has failed, and the domain is likely not configured properly for that condition.

|  Enum.  
messages |  The list of messages with status |  List of Message DTOs.  
  
Message DTO

Field |  Description |  Type  
---|---|---  
status |  The status associated with the message. It can contain one of the following values:

  * **OK**
  * **BEST_PRACTICE**
  * **INFO**
  * **WARNING**
  * **ERROR**

|  Enum.  
messages |  The message string. |  String.  
  
JSON Example: Health Check Data Response

JSON Example: Health Check Data Response ```json { "version":
"2021-03-10T18:06:49.790Z", "state": "COMPLETED", "checks": [ { "category":
"NS Validations", "state": "COMPLETED", "status": "OK", "results": [ { "name":
"Authoritative name servers have the same NS record list as the parent zone",
"description": " description ", "status": "OK", "messages": [ { "status":
"OK", "message": "The NS set from parent '['ns1.example.com.',
'ns2.example.com.', 'ns3.example.com.', 'ns4.example.com.']'
\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0and
NS set from zone '['ns1.example.com.', 'ns2.example.com.', 'ns3.example.com.',
'ns4.example.com.']' are same." } ] }, { "name": "All name servers respond",
"description": "description", "status": "OK", "messages": [ { "status": "OK",
"message": "Nameserver 'ns1.example.com.' responded." }, { "status": "OK",
"message": "Nameserver 'ns2.example.com.' responded." } ] }, { "name": "Name
servers answer authoritatively", "description": "description", "status": "OK",
"messages": [ { "status": "OK", "message": "Nameserver 'ns1.example.com.'
answers authoritatively" }, { "status": "OK", "message": "Nameserver
'ns2.example.com.' answers authoritatively" } ] }, { "name": "Name servers do
not announce open recursion", "description": "description", "status": "OK",
"messages": [ { "status": "OK", "message": "Nameserver 'ns1.example.com.' does
not allow open recursion" } ] } ] }, { "category": "SOA Validations", "state":
"COMPLETED", "status": "ERROR", "results": [ { "name": "SOA record exists for
zone", "description": "description", "status": "OK", "messages": [ { "status":
"OK", "message": "The SOA record for zone 'example.com.' exists." } ] }, {
"name": "SOA REFRESH is present and valid", "description": " description ",
"status": "BEST_PRACTICE", "messages": [ { "status": "BEST_PRACTICE",
"message": "The SOA refresh value of '900' for the zone 'example.com.' is not
within the range of best practice." } ] }, { "name": "SOA RETRY is present and
valid", "description": "description", "status": "OK", "messages": [ {
"status": "OK", "message": "The SOA retry value of '900' for the zone
'example.com.' is within the range of best practice." } ] }, { "name": "SOA
EXPIRE is present and valid", "description": "description", "status": "ERROR",
"messages": [ { "status": "ERROR", "message": "The SOA expire value of '1800'
for zone 'example.com.' is not within the common best practice." } ] }, {
"name": "SOA MINIMUM is present and valid", "description": "description",
"status": "BEST_PRACTICE", "messages": [ { "status": "BEST_PRACTICE",
"message": "The SOA minimum value of '60' for the zone 'example.com.' is not
within the range of best practice." } ] } ] }, { "category": "MX Validations",
"state": "COMPLETED", "status": "OK", "results": [ { "name": "Zone has MX
records", "description": "description", "status": "OK", "messages": [ {
"status": "OK", "message": "The zone 'example.com.' has '5' MX record." } ] }
] }, { "category": "DNSSEC Validations", "state": "COMPLETED", "status":
"INFO", "results": [ { "name": "Zone is signed", "description": "description",
"status": "INFO", "messages": [ { "status": "INFO", "message": "Zone
'example.com.' is not signed!" } ] } ] }, { "category": "Domain Validations",
"state": "COMPLETED", "status": "OK", "results": [ { "name": "no CNAME (only
our alias) at apex", "description": "description", "status": "OK", "messages":
[ { "status": "OK", "message": "The zone 'example.com.' does not has CNAME
record at apex." }, { "status": "OK", "message": "The SOA response for the
zone 'example.com.' does not has CNAME record in its answer section." } ] } ]
} ] } ```

## Get DNS Health Check Report Version List

This API call returns the versions of the DNS Health Check Report that is
available for the given zone name specified as {zoneName} in the URL.

**Method and URI** :

GET https://api.ultradns.com/v1/zones/<zoneName>/healthchecks/versions

**Parameters** : None

**Body** : None

**Response** : If request is valid and accepted by health check system, Status
Code 200 OK is returned with VersionList DTO.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} does not exist.

  * If unauthenticated user tries to call this API.

  * If user requesting the Health Check Report Version does not have necessary permissions.

VersionList DTO

Field |  Description |  Type  
---|---|---  
versions |  The list of available versions of the report. |  List of version(s) in the format âYYYY-MM-DD-HH24:MI:SS.nnnZâ.  
  
JSON Example: Health Check Report Version List Response

JSON Example: Health Check Report Version List Response ```json { "versions":
[ "2021-03-24T18:26:50.002Z", "2021-03-24T14:42:18.322Z" ] } ```

