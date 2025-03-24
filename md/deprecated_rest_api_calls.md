

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

# Deprecated REST API Calls

This section is intended to keep our customers informed of our Deprecated REST
API calls, so that users can track which API calls have been deprecated and
utilize the recommended alternative API call(s). Additionally, this list will
coincide with customer notifications to further prevent disruptions in your
service or saved scripts.

The table below outlines the REST API calls that have been deprecated and are
no longer supported by our REST API.

Version / Date |  Deprecated REST API Call |  Alternate API Call  
---|---|---  
3.61.0 12/01/2022 |  **Probe Result Summary Report -v1** GET https://api.ultradns.com//v1/reports/traffic_services/probe_result/summary  **Probe Details Report Report -v1** GET https://api.ultradns.com/v1/reports/traffic_services/probe_result/details  |  [Probe Result Details v2 Report](Reports/Probe Result Details v2 Report.htm) [Probe Result Summary v2 Report](Reports/Probe Result Summary v2 Report.htm)  
  
  
  
  
3.57.0 09/30/2022 |  **List Metadata for Zones â v1 / v2 Offset Pagination Method** GET https://api.ultradns.com/v1/zones GET https://api.ultradns.com/v2/zones GET https://api.ultradns.com/zones  _***Please Note, performing any of the above listed API calls will return the Cursor-Based behavior response, instead of an Error 301.***_ |  [List Metadata for Zones v3 - Cursor Based](Zone API/Zone API.htm#List)  
**Get Zones of an Account (Deprecated 2022-09-30)** GET https://api.ultradns.com/accounts/{accountName}/zones _***Please Note, this call will return an Error 301 if performed.***_ |  [List Metadata for Zones v3 - Cursor Based](Zone API/Zone API.htm#List)

