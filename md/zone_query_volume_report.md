

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

## Zone Query Volume Report

The purpose of the Zone Query Volume Report is to provide aggregated zone
query volumes for multiple zones on a monthly basis, or for a set period of
time. The maximum time frame between the start and end date cannot exceed 13
months.

### Zone Query Volume Report DTOs

### Requesting Zone Query Volume Report

**Method and URI** :

POST
https://api.ultradns.com/reports/dns_resolution/query_volume/zone?offset={offset}&limit={limit}

**Parameters** : Can include the following:

Zone Query Volume Query Parameters

Parameter |  Description |  Type  
---|---|---  
offset |  This field is optional. If not specified, initial records will always be returned specific to limit and SortOrder. This parameter allows pagination on the reporting records retrieved. The offset will be the integer value that specifies the position of first result to be retrieved. Specify offset as 0 for first results to be retrieved. |  Integer, Optional.  
limit |  This field is optional. If not specified, the total number of records returned in the response will be equal to the default value 1000. This parameter allows pagination on the reporting records retrieved. The limit will be the integer value that specifies the maximum number of results to be retrieved in response. |  Integer, Optional.  
  
**Body** : Must contain Zone Query Volume DTO and Zone Query Volume Sort DTO.

### Zone Query Volume DTO

Zone Query Volume DTO

Field |  Description |  Type  
---|---|---  
zoneName | 

  * The name of the zone to be returned.
  * Wildcard ( * ) is not supported.
  * If zoneName is not supplied, defaults to âAllâ zones in the account.
  * Zone name with and without a DOT(.) at the end are supported.

|  String. Optional.  
accountName |  The name of the account |  String, Optional.  
startDate |  startDate (YYYY-MM-DD) If not supplied, defaults to the first day of the previous calendar month. The maximum number of days between the start and end date cannot exceed 13 months.

  * startDate cannot be a future date.

|  String, Optional  
endDate |  endDate (YYYY-MM-DD) If not supplied, defaults to the last day of the previous calendar month. The maximum number of days between the start and end date cannot exceed 13 months.

  * endDate cannot be a future date.

|  String. Optional  
ultra2 |  Used to return the Zone Query Volume Report details for either zones that are UltraDNS2 enabled or not. This parameter will be applicable for those users that have UltraDNS2 enabled on an account.

  * **true** â will only return zones that are UltraDNS2 enabled.
  * **false** â will only return standard UltraDNS zones.
  * _If ignored, will return all zones for an account._

|  Boolean. Optional.  
  
Zone Query Volume Sort DTO

Field |  Description |  Type  
---|---|---  
**sortFields** |  Contains a map of sortable columns and sort directions. Defaults to sort by zoneName, endDate in ascending order. |  JSON  
  
Zone Query Volume Sortable Columns

Sortable Column |  Sort Direction  
---|---  
zoneName |  ASC (Ascending) or DESC (Descending)  
startDate |  ASC or DESC  
endDate |  ASC or DESC  
rspTotal |  ASC or DESC  
  
JSON Example: Zone Query Volume Report with Sort Columns

{  
"zoneQueryVolume":  
{  
"startDate":"2016-05-10",  
"endDate":"2016-06-25"  
},  
"sortFields":{  
"zoneName":"DESC",  
"startDate":"ASC",  
"endDate":"DESC",  
"rspTotal":"ASC"  
}  
}

**Responses** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error code is returned under the following conditions:

  * Error Code 401 â âUnauthorized. Token not found, expired or invalid.â

### Retrieving Zone Query Volume Reports

**Method and URI** :

GET https://api.ultradns.com/requests/{requestId}

**Parameters** : ReportRequest DTO

**Body** : None

**Responses** : If task completes, Status Code 200 OK is returned with a list
of Zone Query Volume Report Output DTO in the response body. Each value is
comma-separated.

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

### Zone Query Volume Report Output DTO  

![](../../Resources/Images/Rest-API_User_Guide/Introduction_60x69.png) |  Unsigned values of long are allowed from 0 to 263 â 1 (9223372036854775807)  
---|---  
  
Zone Query Volume Report Output DTO

Response Body |  Description |  Type  
---|---|---  
zoneName |  The name of the zone. |  String  
accountName |  The name of the account. |  String  
startDate |  StartDate (YYYY-MM-DD) |  String  
endDate |  EndDate (YYYY-MM-DD) |  String  
rspTotal |  Count of total responses between the StartDate and the EndDate across all record types. |  Long  
tcpTotal |  Count of total TCP responses between the StartDate and the EndDate across all record types. |  Long  
updTotal |  Count of total UDP responses between the StartDate and the EndDate across all record types. |  Long  
ipv4Total |  Count of total IPv4 responses between the StartDate and the EndDate across all record types. |  Long  
ipv6Total |  Count of total IPv6 responses between the StartDate and the EndDate across all record types. |  Long  
ipv4tcpTotal |  Count of total IPv4 TCP responses between the StartDate and the EndDate across all record types. |  Long  
ipv4udpTotal |  Count of total IPv4 UDP responses between the StartDate and the EndDate across all record types. |  Long  
ipv6tcpTotal |  Count of total IPv6 TCP responses between the StartDate and the EndDate across all record types. |  Long  
ipv6udpTotal |  Count of total IPv6 UDP responses between the StartDate and the EndDate across all record types. |  Long  
recordA |  Count of A records. |  Long  
recordA6 |  Count of A6 records. |  Long  
recordAAAA |  Count of AAAA records. |  Long  
recordAny |  Count of ANY records.  |  Long  
recordAxfr |  Count of AXFR records.  |  Long  
recordCert |  Count of CERT records.  |  Long  
recordCname |  Count of CNAME records.  |  Long  
recordDlv |  Count of DLV records.  |  Long  
recordDnskey |  Count of DNSKEY records.  |  Long  
recordHinfo |  Count of HINFO records.  |  Long  
recordIpseckey |  Count of IPSECKEY records.  |  Long  
recordIxfr |  Count of IXFR records.  |  Long  
recordLoc |  Count of LOC records.  |  Long  
recordMf |  Count of MF records.  |  Long  
recordNaptr |  Count of NAPTR records.  |  Long  
recordMx |  Count of MX records.  |  Long  
recordNs |  Count of NS records.  |  Long  
recordNsec |  Count of NSEC records.  |  Long  
recordNsec3 |  Count of NSEC3 records.  |  Long  
recordNsec3Param |  Count of NSEC3PARAM records.  |  Long  
recordRp |  Count of RP records.  |  Long  
recordPtr |  Count of PTR records.  |  Long  
recordRrsig |  Count of RRSIG records.  |  Long  
recordSoa |  Count of SOA records.  |  Long  
recordSpf |  Count of SPF records.  |  Long  
recordSrv |  Count of SRV records.  |  Long  
recordSshfp |  Count of SSHFP records.  |  Long  
recordTa |  Count of TA records.  |  Long  
recordTsig |  Count of TSIG records.  |  Long  
recordTkey |  Count of TKEY records.  |  Long  
recordTxt |  Count of TXT records.  |  Long  
recordHttps |  Count of HTTPS records. |  Long  
recordSvcb |  Count of SVCB records. |  Long  
  
### Response Link Headers

Response Link Headers

Field |  Description  
---|---  
Link |  Relative URL to next page of report if available: POST </v1/reports/dns_resolution/query_volume/zone?offset=8&limit=10>; rel="next"  Relative URL to previous page of report if available: </v1/reports/dns_resolution/query_volume/zone?offset=0&limit=10>; rel="previous" When using the next or previous link header to retrieve report data, you must perform another POST call, and include the original body content (if any) and new query parameters (such as offset and limit).  When continuing to use subsequent Link Headers to retrieve additional results, you must continue to perform the POST call per link header to retrieve the next set of report details.  
Limit |  Specify the maximum number of records in requested response. Cannot be greater than maximum allowed limit. Currently maximum allowed limit is 100k.  
Results |  Total rows in the report response.  
  
JSON Example: Zone Query Volume Report without zoneName

The Zone Query Volume Report return in JSON format when zoneName is not
included in the request (Defaults to all zones in the account) and multiple
zones are returned.

[  
{  
"zoneName": "testzone9.com.",  
"accountName": "account0",  
"startDate": "2016-05-10",  
"endDate": "2016-05-28",  
"rspTotal": 12,  
"tcpTotal": 13,  
"udpTotal": 13,  
"ipv4Total": 15,  
"ipv6Total": 11,  
"ipv4tcpTotal": 8,  
"ipv4udpTotal": 6,  
"ipv6tcpTotal": 3,  
"ipv6udpTotal": 5,  
"recordA": 19,  
"recordA6": 0,  
"recordAAAA": 15,  
"recordAny": 0,  
"recordAxfr": 0,  
"recordCert": 0,  
"recordCname": 0,  
"recordDlv": 0,  
"recordDnskey": 0,  
"recordHinfo": 0,  
"recordIpseckey": 0,  
"recordIxfr": 0,  
"recordLoc": 0,  
"recordMf": 1,  
"recordNaptr": 0,  
"recordMx": 13,  
"recordNs": 19,  
"recordNsec": 0,  
"recordNsec3": 0,  
"recordNsec3Param": 0,  
"recordRp": 0,  
"recordPtr": 15,  
"recordRrsig": 0,  
"recordSoa": 0,  
"recordSpf": 0,  
"recordSrv": 0,  
"recordSshfp": 0,  
"recordTa": 0,  
"recordTsig": 0,  
"recordTkey": 0,  
"recordTxt": 0,

"recordHttps": 7,

"recordSvcb": 0  
},  
{  
"zoneName": "testzone8.com.",  
"accountName": "account0",  
"startDate": "2016-05-10",  
"endDate": "2016-05-28",  
"rspTotal": 13,  
"tcpTotal": 17,  
"udpTotal": 13,  
"ipv4Total": 13,  
"ipv6Total": 16,  
"ipv4tcpTotal": 9,  
"ipv4udpTotal": 6,  
"ipv6tcpTotal": 8,  
"ipv6udpTotal": 8,  
"recordA": 19,  
"recordA6": 0,  
"recordAAAA": 14,  
"recordAny": 0,  
"recordAxfr": 0,  
"recordCert": 0,  
"recordCname": 0,  
"recordDlv": 0,  
"recordDnskey": 0,  
"recordHinfo": 0,  
"recordIpseckey": 0,  
"recordIxfr": 0,  
"recordLoc": 0,  
"recordMf": 1,  
"recordNaptr": 0,  
"recordMx": 13,  
"recordNs": 19,  
"recordNsec": 0,  
"recordNsec3": 0,  
"recordNsec3Param": 0,  
"recordRp": 0,  
"recordPtr": 8,  
"recordRrsig": 0,  
"recordSoa": 0,  
"recordSpf": 0,  
"recordSrv": 0,  
"recordSshfp": 0,  
"recordTa": 0,  
"recordTsig": 0,  
"recordTkey": 0,  
"recordTxt": 0,

"recordHttps": 7,

"recordSvcb": 0  
},  
{  
"zoneName": "testzone7.com.",  
"accountName": "account0",  
"startDate": "2016-05-10",  
"endDate": "2016-05-28",  
"rspTotal": 13,  
"tcpTotal": 14,  
"udpTotal": 14,  
"ipv4Total": 18,  
"ipv6Total": 15,  
"ipv4tcpTotal": 8,  
"ipv4udpTotal": 9,  
"ipv6tcpTotal": 8,  
"ipv6udpTotal": 6,  
"recordA": 19,  
"recordA6": 0,  
"recordAAAA": 11,  
"recordAny": 0,  
"recordAxfr": 0,  
"recordCert": 0,  
"recordCname": 0,  
"recordDlv": 0,  
"recordDnskey": 0,  
"recordHinfo": 0,  
"recordIpseckey": 0,  
"recordIxfr": 0,  
"recordLoc": 0,  
"recordMf": 1,  
"recordNaptr": 0,  
"recordMx": 20,  
"recordNs": 9,  
"recordNsec": 0,  
"recordNsec3": 0,  
"recordNsec3Param": 0,  
"recordRp": 0,  
"recordPtr": 20,  
"recordRrsig": 0,  
"recordSoa": 0,  
"recordSpf": 0,  
"recordSrv": 0,  
"recordSshfp": 0,  
"recordTa": 0,  
"recordTsig": 0,  
"recordTkey": 0,  
"recordTxt": 0,

"recordHttps": 7,

"recordSvcb": 0  
},  
{  
"zoneName": "testzone6.com.",  
"accountName": "account0",  
"startDate": "2016-05-10",  
"endDate": "2016-05-28",  
"rspTotal": 11,  
"tcpTotal": 12,  
"udpTotal": 12,  
"ipv4Total": 12,  
"ipv6Total": 10,  
"ipv4tcpTotal": 9,  
"ipv4udpTotal": 6,  
"ipv6tcpTotal": 1,  
"ipv6udpTotal": 3,  
"recordA": 12,  
"recordA6": 0,  
"recordAAAA": 10,  
"recordAny": 0,  
"recordAxfr": 0,  
"recordCert": 0,  
"recordCname": 0,  
"recordDlv": 0,  
"recordDnskey": 0,  
"recordHinfo": 0,  
"recordIpseckey": 0,  
"recordIxfr": 0,  
"recordLoc": 0,  
"recordMf": 4,  
"recordNaptr": 0,  
"recordMx": 14,  
"recordNs": 11,  
"recordNsec": 0,  
"recordNsec3": 0,  
"recordNsec3Param": 0,  
"recordRp": 0,  
"recordPtr": 14,  
"recordRrsig": 0,  
"recordSoa": 0,  
"recordSpf": 0,  
"recordSrv": 0,  
"recordSshfp": 0,  
"recordTa": 0,  
"recordTsig": 0,  
"recordTkey": 0,  
"recordTxt": 0,

"recordHttps": 7,

"recordSvcb": 0  
},  
{  
"zoneName": "testzone5.com.",  
"accountName": "account0",  
"startDate": "2016-05-10",  
"endDate": "2016-05-28",  
"rspTotal": 13,  
"tcpTotal": 11,  
"udpTotal": 12,  
"ipv4Total": 13,  
"ipv6Total": 12,  
"ipv4tcpTotal": 5,  
"ipv4udpTotal": 7,  
"ipv6tcpTotal": 3,  
"ipv6udpTotal": 6,  
"recordA": 15,  
"recordA6": 0,  
"recordAAAA": 14,  
"recordAny": 0,  
"recordAxfr": 0,  
"recordCert": 0,  
"recordCname": 0,  
"recordDlv": 0,  
"recordDnskey": 0,  
"recordHinfo": 0,  
"recordIpseckey": 0,  
"recordIxfr": 0,  
"recordLoc": 0,  
"recordMf": 2,  
"recordNaptr": 0,

"recordMx": 15,

"recordNs": 13,

"recordNsec": 0,

"recordNsec3": 0,

"recordNsec3Param": 0,

"recordRp": 0,

"recordPtr": 16,

"recordRrsig": 0,

"recordSoa": 0,

"recordSpf": 0,

"recordSrv": 0,

"recordSshfp": 0,

"recordTa": 0,

"recordTsig": 0,

"recordTkey": 0,

"recordTxt": 0,

"recordHttps": 7,

"recordSvcb": 0

}

]

![](../../Resources/Images/Rest-API_User_Guide/Introduction_58x68.png) |  The Zone Query Volume Report can be returned in a .CSV format. In the header section, you will need to include the additional field: **Accept: text/csv**.   
---|---  
  
.CSV Example: Zone Query Volume Report in .CSV format with no zoneName

Zone Query Volume Report return in .CSV format when zoneName is not included
in the request (Defaults to all zones in the account) and multiple zones are
returned.

zoneName, accountName, startDate, endDate, rspTotal, tcpTotal, udpTotal,
ipv4Total, ipv6Total, ipv4tcpTotal, ipv4udpTotal, ipv6tcpTotal, ipv6udpTotal,
recordA, recordA6, recordAAAA, recordAny, recordAxfr, recordCert, recordCname,
recordDlv, recordDnskey, recordHinfo, recordIpseckey, recordIxfr, recordLoc,
recordMf, recordNaptr, recordMx, recordNs, recordNsec, recordNsec3,
recordNsec3Param, recordRp, recordPtr, recordRrsig, recordSoa, recordSpf,
recordSrv, recordSshfp, recordTa, recordTsig, recordTkey, recordTxt,
recordHTTPs, recordSvcb  
testzone9.com.,account0,2016-05-10,2016-05-28,12,13,13,15,11,8,6,3,5,19,0,15,0,0,0,0,0,0,0,0,0,0,1,0,13,19,0,0,0,0,15,0,0,0,0,0,0,0,0,0,7,0  
testzone8.com.,account0,2016-05-10,2016-05-28,13,17,13,13,16,9,6,8,8,19,0,14,0,0,0,0,0,0,0,0,0,0,1,0,13,19,0,0,0,0,8,0,0,0,0,0,0,0,0,0,7,0  
testzone7.com.,account0,2016-05-10,2016-05-28,13,14,14,18,15,8,9,8,6,19,0,11,0,0,0,0,0,0,0,0,0,0,1,0,20,9,0,0,0,0,20,0,0,0,0,0,0,0,0,0,7,0  
testzone6.com.,account0,2016-05-10,2016-05-28,11,12,12,12,10,9,6,1,3,12,0,10,0,0,0,0,0,0,0,0,0,0,4,0,14,11,0,0,0,0,14,0,0,0,0,0,0,0,0,0,7,0  
testzone5.com.,account0,2016-05-10,2016-05-28,13,11,12,13,12,5,7,3,6,15,0,14,0,0,0,0,0,0,0,0,0,0,2,0,15,13,0,0,0,0,16,0,0,0,0,0,0,0,0,0,7,0  
testzone4.com.,account0,2016-05-10,2016-05-28,12,15,16,11,14,4,7,6,6,11,0,15,0,0,0,0,0,0,0,0,0,0,1,0,15,14,0,0,0,0,14,0,0,0,0,0,0,0,0,0,7,0

![](../../Resources/Images/Rest-API_User_Guide/Introduction_72x84.png) |  When attempting to perform a GET for the Link Header details for the next/previous URL, a POST must first be performed to retrieve the next/previous URL of the requestId for the next set of records.  
---|---

