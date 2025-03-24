

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

## Probe Result Summary Report -v1 Deprecated

Unlike the various reports already documented, the **Probe Result Summary
Report** does not require the usage of the Report RequestID to generate the
request for the report, and subsequently the return of the report. When a
Probe Result Summary Report is requested, the detailed report is returned to
the user immediately.

![](../../Resources/Images/Rest-API_User_Guide/Introduction_64x75.png) |  The version of the Probe Result Summary Report utilizing /v1 in the Method has been officially deprecated as of **2022-12-01**. We highly recommend that users begin to utilize the [Probe Result Summary v2 Report](Probe Result Summary v2 Report.htm) call as soon as possible to prevent any errors or confusion.  
---|---  
  
### Requesting Probe Result Summary Report

**Method and URI** :

GET https://api.ultradns.com/v1/reports/traffic_services/probe_result/summary

**Errors** : If /v1 is present, Error 301 will be returned, indicating this
API call is no longer supported.

  * [Deprecated REST API Calls](../Deprecated REST API Calls.htm)

