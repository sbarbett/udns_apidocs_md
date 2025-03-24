

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

## Projected Query Volume Report

### Requesting Projected Query Volume Report

**Method and URI** :

POST https://api.ultradns.com/reports/dns_resolution/projected_query_volume

**Parameters** : None

**Body** : Must contain a Projected Query Volume Sort DTO and Projected Query
Volume Sortable Columns.

### Projected Query Volume Report DTO

Projected Query Volume Sort DTO

Field |  Description |  Type  
---|---|---  
sortFields |  Contains a map of sortable columns and sort directions.  |  JSON  
accountName |  The account name for which the report is being run against. |  String.  
  
Projected Query Volume Sortable Columns

Sortable Column |  Description |  Sort Direction  
---|---|---  
month |  Current Month. |  ASC (Ascending) or   
  
DESC (Descending)  
currentDay |  Day of the Month |  ASC or DESC  
rspMtd |  MTD Responses. |  ASC or DESC  
rspMtd7dAvg |  Projected MTD Responses (7 day Average). |  ASC or DESC  
rspMtd30dAvg |  Projected MTD Responses (30 day Average). |  ASC or DESC  
ttlAvg |  Average TTL. |  ASC or DESC  
rspDaily |  Daily Responses. |  ASC or DESC  
  
![](../../Resources/Images/Rest-API_User_Guide/Introduction_57x66.png) |  For a list of field definitions, please refer to Projected Query Volumes Report DTOs.  
---|---  
  
  
  
JSON Example: Projected Query Volume Report with Sort Columns

{  
  
"projectedQueryVolume" : {  
  
"accountName" : "abc"  
  
},  
  
{  
  
"sortFields":  
  
{  
  
"rspDaily": "ASC",  
  
"ttlAvg": "DESC",  
  
"rspMtd": "ASC"  
  
}  
  
}

**Responses** : If task completes, Status Code 201 is returned with a
ReportRequest DTOin the response body.

**Errors** : An error code is returned under the following conditions:

  * Error Code 401 â âUnauthorized. Token not found, expired or invalid.â

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

### Retrieving Projected Query Volumes Reports

**Method and URI** :

GET https://api.ultradns.com/requests/{requestId}

**Parameters** : ReportRequest DTO

**Body** : None

**Responses** : If task completes, Status Code 200 OK is returned with
Projected Query Volumes Report DTOs in the response body. Each value is comma-
separated.

### Projected Query Volume Report Output DTO

Projected Query Volumes Report DTOs

Response Body |  Description |  Type  
---|---|---  
year |  Current year. |  Integer  
month |  Current Month. |  Month  
currentDay |  Day of the Month |  Short  
rspMtd |  MTD Responses. |  Long  
rspMtd7dAvg |  Projected MTD Responses (7 day Average). |  Long  
rspMtd30dAvg |  Projected MTD Responses (30 day Average). |  Long  
ttlAvg |  Average TTL. |  Long  
rspDaily |  Daily Responses. |  Long   
  
  
  
**Errors** : An error code is returned under the following conditions:

  * Error Code 401 â âUnauthorized. Token not found, expired or invalid.â

  * Error Code 404 â âNo report with the given ID was requested before.â

![](../../Resources/Images/Rest-API_User_Guide/Introduction_71x83.png) |  The Projected Query Volume Report may not be supplied immediately after providing the requestId. A status message will be returned, notifying you that the Report has not yet completed, and to try the request again at a later time.  
---|---  
  
JSON Example: Projected Query Volume Report âPendingâ response

JSON Example: Projected Query Volume Report âPendingâ response ```json {
"errorCode": 410004, "errorMessage": "Report is not ready. Please try again
later." } ```

JSON Example: Projected Query Volume Report return in JSON format

[  
  
{  
  
"year": 2016  
  
"month": "MARCH",  
  
"currentDay": 1,  
  
"rspMtd": 0,  
  
"rspMtd7dAvg": 29,  
  
"rspMtd30dAvg": 35,  
  
"ttlAvg": null,  
  
"rspDaily": 10,  
  
},  
  
{  
  
"year": 2016  
  
"month": "MARCH",  
  
"currentDay": 2,  
  
"rspMtd": 0,  
  
"rspMtd7dAvg": 34,  
  
"rspMtd30dAvg": 25,  
  
"ttlAvg": null,  
  
"rspDaily": 60,  
  
},  
  
{  
  
"year": 2016  
  
"month": "MARCH",  
  
"currentDay": 3,  
  
"rspMtd": 0,  
  
"rspMtd7dAvg": 71,  
  
"rspMtd30dAvg": 11,  
  
"ttlAvg": null,  
  
"rspDaily": 46,  
  
},  
  
{  
  
"year": 2016  
  
"month": "MARCH",  
  
"currentDay": 4,  
  
"rspMtd": 0,  
  
"rspMtd7dAvg": 32,  
  
"rspMtd30dAvg": 93,  
  
"ttlAvg": null,  
  
"rspDaily": 85,  
  
},  
  
{  
  
"year": 2016  
  
"month": "MARCH",  
  
"currentDay": 5,  
  
"rspMtd": 0,  
  
"rspMtd7dAvg": 56,  
  
"rspMtd30dAvg": 47,  
  
"ttlAvg": null,  
  
"rspDaily": 20,  
  
},  
  
{

![](../../Resources/Images/Rest-API_User_Guide/Introduction_62x72.png) |  The Projected Query Volume Report can be returned in a .CSV format, but will require an additional step beyond the default JSON requirements. In the header section, you will need to include the additional field: Accept: text/csv.   
---|---  
  
CSV Example: Projected Query Volume Report return in .CSV format

Month,â Dayâ Ofâ Currentâ Month,â MTDâ Responses,â Projectedâ MTDâ
Resp(7-dayâ avg),â Projectedâ MTDâ Resp(30-dayâ avg),â Averageâ TTL,â
Dailyâ Responses  
MARCH,1,10,29,35,30,10  
MARCH,2,21,28,31,26,11  
MARCH,3,33,27,39,35,12  
MARCH,4,46,26,32,43,13  
MARCH,5,65,36,42,1,84  
MARCH,6,67,32,68,4,13  
MARCH,7,51,17,3,4,24  
MARCH,8,61,97,42,5,87  
MARCH,9,45,7,36,2,37  
MARCH,10,12,87,38,3,23  
MARCH,11,82,4,19,2,59  
MARCH,12,9,84,67,9,84  
MARCH,13,10,31,90,2,81  
MARCH,14,4,49,28,6,63  
MARCH,15,2,31,57,2,72  
MARCH,16,70,21,28,3,73  
MARCH,17,72,59,20,22,41  
MARCH,18,58,94,72,1,62  
MARCH,19,72,16,12,4,43  
MARCH,20,92,30,17,2,33  
MARCH,21,46,80,14,20,81  
MARCH,22,76,93,65,9,1  
MARCH,23,59,13,88,3,58  
MARCH,24,70,85,31,62,2  
MARCH,25,14,87,49,20,70  
MARCH,26,23,26,50,1,66  
MARCH,27,84,60,88,2,31  
MARCH,28,72,58,91,2,26  
MARCH,29,64,52,85,5,45  
MARCH,30,37,23,71,2,12  
MARCH,31,59,65,21,11,84

