

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

## Zone Daily Query Report

The purpose of the Zone Daily Query Report is to provide Zone Query Daily
Volume usage in an aggregate sum for up to 60 days. This information provides
detailed data that may be used to support aggregate monthly totals used for
billing, or for the generation of a GUI with daily data. The data provided via
the REST API is similar to the following table (not the graphic) provided by
the UltraDNS Advanced Reporting, Response Comparisons report in the GUI
interface with the addition of query counts by DNS record type, protocol (UDP,
TCP) and IP version. The path to the current GUI in Advanced Reporting is:

### Zone Daily Query Volume Report DTOs

### Requesting Zone Daily Query Volume Report

**Method and URI** :

POST https://api.ultradns.com/reports/dns_resolution/query_volume/zone/daily

**Parameters** : None

**Body** : Must contain Zone Daily Query Volume DTO.

### Zone Daily Query Volume DTO

Zone Daily Query Volume DTO

Field |  Description |  Type  
---|---|---  
zoneName |  The name of the one zone to be returned. Wildcards in the zone name are not supported at this time. Zone name(s) with and without a DOT (.) at the end are also supported. |  String.  
accountName |  The name of the account |  String, Optional.  
startDate |  startDate (YYYY-MM-DD) If not supplied, defaults to the first day of the previous calendar month. The maximum number of days between the start and end date cannot exceed 60 days. startDate cannot be older than 13 months. startDate cannot be a future date. |  String, Optional.  
endDate |  endDate (YYYY-MM-DD) If not supplied, defaults to the last day of the previous calendar month. The maximum number of days between the start and end date cannot exceed 60 days. endDate cannot be a future date. |  String. Optional.  
  
Zone Daily Query Volume Sort DTO

Field |  Description |  Type  
---|---|---  
**sortFields** |  Contains a map of sortable columns and sort directions. Defaults to sort by date in ascending order. |  JSON  
  
Zone Daily Query Volume Sortable Columns

Sortable Column |  Sort Direction  
---|---  
date |  ASC or DESC  
rspTotal |  ASC or DESC  
  
![](../../Resources/Images/Rest-API_User_Guide/Introduction_56x65.png) |  For a list of field definitions, please refer to Zone Daily Query Volume DTO  
---|---  
  
**Responses** : If task completes, Status Code 201 is returned with Zone Daily
Query Volume DTOin the response body.

**Errors** : An error code is returned under the following conditions:

  * Error Code 401 â âUnauthorized. Token not found, expired or invalid.â

JSON Example: Zone Daily Query Volume Report with Sort Columns

JSON Example: Zone Daily Query Volume Report with Sort Columns ```json {
"zoneDailyQueryVolume": { "zoneName": "testzone1.com.", "startDate":
"2016-04-01", "endDate": "2016-05-01" }, "sortFields": { "date": "DESC",
"rspTotal": "ASC" } } ```

### Retrieving Zone Daily Query Volume Report

**Method and URI** :

GET https://api.ultradns.com/requests/{requestId}

**Parameters** : Must contain a ReportRequest DTO

**Body** : None

**Responses** : If task completes, Status Code 200 OK is returned with a Zone
Daily Query Volume Report Output DTOin the response body.Each value is comma
separated.

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

### Zone Daily Query Volume Report Output DTO  

![](../../Resources/Images/Rest-API_User_Guide/Introduction_56x65.png) |  Unsigned values of long are allowed from 0 to 263 â 1 (9223372036854775807)  
---|---  
  
Zone Daily Query Volume Report Output DTO

Response Body |  Description |  Type  
---|---|---  
zoneName |  The name of the zone. |  String  
accountName |  The name of the account. |  String  
date |  Date (YYYY-MM-DD) |  String  
rspTotal |  Count of total responses between the StartDate and the EndDate across all record types. |  Long  
tcpTotal |  Count of total TCP responses between the StartDate and the EndDate across all record types. |  Long  
udpTotal |  Count of total UDP responses between the StartDate and the EndDate across all record types. |  Long  
ipv4Total |  Count of total IPv4 responses between the StartDate and the EndDate across all record types. |  Long  
ipv6Total |  Count of total IPv6 responses between the StartDate and the EndDate across all record types. |  Long  
ipv4tcpTotal |  Count of total IPv4 TCP responses between the StartDate and the EndDate across all record types. |  Long  
ipv4udpTotal |  Count of total IPv4 UDP responses between the StartDate and the EndDate across all record types. |  Long  
ipv6tcpTotal |  Count of total IPv6 TCP responses between the StartDate and the EndDate across all record types. |  Long  
ipv6udpTotal |  Count of total IPv6 UDP responses between the StartDate and the EndDate across all record types. |  Long  
recordA |  Count of A records.  |  Long  
recordA6 |  Count of A6 records.  |  Long  
recordAAAA |  Count of AAAA records.  |  Long  
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
  
JSON Example: Zone Daily Query Volume Report with one zoneName

Zone Daily Query Volume Report return in JSON format when one zoneName is
included in the request.

[

{

"zoneName": "testzone1.com.",

"accountName": "account0",

"date": "2016-05-01",

"rspTotal": 0,

"tcpTotal": 0,

"udpTotal": 0,

"ipv4Total": 1,

"ipv6Total": 1,

"ipv4tcpTotal": 0,

"ipv4udpTotal": 0,

"ipv6tcpTotal": 0,

"ipv6udpTotal": 0,

"recordA": 1,

"recordA6": 0,

"recordAAAA": 0,

"recordAny": 0,

"recordAxfr": 0,

"recordCert": 0,

"recordCname": 0,

"recordDlv": 0,

"recordDnskey": 0,

"recordHinfo": 0,"recordIpseckey": 0,

"recordIxfr": 0,

"recordLoc": 0,

"recordMf": 0,

"recordNaptr": 0,

"recordMx": 0,

"recordNs": 0,

"recordNsec": 0,

"recordNsec3": 0,

"recordNsec3Param": 0,

"recordRp": 0,

"recordPtr": 0,

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

"zoneName": "testzone1.com.",

"accountName": "account0",

"date": "2016-04-28",

"rspTotal": 0,

"tcpTotal": 0,

"udpTotal": 0,

"ipv4Total": 1,

"ipv6Total": 1,

"ipv4tcpTotal": 0,

"ipv4udpTotal": 0,

"ipv6tcpTotal": 0,

"ipv6udpTotal": 0,

"recordA": 0,

"recordA6": 0,

"recordAAAA": 0,

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

"recordMf": 0,

"recordNaptr": 0,

"recordMx": 1,

"recordNs": 0,

"recordNsec": 0,

"recordNsec3": 0,

"recordNsec3Param": 0,

"recordRp": 0,

"recordPtr": 1,

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

"zoneName": "testzone1.com.",

"accountName": "account0",

"date": "2016-04-27",

"rspTotal": 0,

"tcpTotal": 1,

"udpTotal": 0,

"ipv4Total": 0,

"ipv6Total": 1,

"ipv4tcpTotal": 0,

"ipv4udpTotal": 0,

"ipv6tcpTotal": 1,

"ipv6udpTotal": 0,

"recordA": 0,

"recordA6": 0,

"recordAAAA": 1,

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

"recordMf": 0,

"recordNaptr": 0,

"recordMx": 0,

"recordNs": 1,

"recordNsec": 0,

"recordNsec3": 0,

"recordNsec3Param": 0,

"recordRp": 0,

"recordPtr": 1,

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

"zoneName": "testzone1.com.",

"accountName": "account0",

"date": "2016-04-26",

"rspTotal": 1,

"tcpTotal": 0,

"udpTotal": 0,

"ipv4Total": 0,

"ipv6Total": 1,

"ipv4tcpTotal": 0,

"ipv4udpTotal": 0,

"ipv6tcpTotal": 0,

"ipv6udpTotal": 0,

"recordA": 1,

"recordA6": 0,

"recordAAAA": 1,

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

"recordMf": 0,

"recordNaptr": 0,

"recordMx": 0,

"recordNs": 0,

"recordNsec": 0,

"recordNsec3": 0,

"recordNsec3Param": 0,

"recordRp": 0,

"recordPtr": 0,

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

"zoneName": "testzone1.com.",

"accountName": "account0",

"date": "2016-04-25",

"rspTotal": 0,

"tcpTotal": 0,

"udpTotal": 1,

"ipv4Total": 0,

"ipv6Total": 0,

"ipv4tcpTotal": 0,

"ipv4udpTotal": 0,

"ipv6tcpTotal": 0,

"ipv6udpTotal": 0,

"recordA": 1,

"recordA6": 0,

"recordAAAA": 0,

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

"recordMf": 0,

"recordNaptr": 0,

"recordMx": 1,

"recordNs": 1,

"recordNsec": 0,

"recordNsec3": 0,

"recordNsec3Param": 0,

"recordRp": 0,

"recordPtr": 0,

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

![](../../Resources/Images/Rest-API_User_Guide/Introduction_66x76.png) |  The Zone Daily Query Volume Report can be returned in a .CSV format, but will require an additional step beyond the default JSON requirements. In the header section, you will need to include the additional field: Accept: text/csv.   
---|---  
  
.CSV Example: Zone Daily Query Volume Report with one zoneName

Zone Daily Query Volume Report return in .CSV format when a single zoneName is
included in the request.

zoneName, accountName, date, rspTotal, tcpTotal, udpTotal, ipv4Total,
ipv6Total, ipv4tcpTotal, ipv4udpTotal, ipv6tcpTotal, ipv6udpTotal, recordA,
recordA6, recordAAAA, recordAny, recordAxfr, recordCert, recordCname,
recordDlv, recordDnskey, recordHinfo, recordIpseckey, recordIxfr, recordLoc,
recordMf, recordNaptr, recordMx, recordNs, recordNsec, recordNsec3,
recordNsec3Param, recordRp, recordPtr, recordRrsig, recordSoa, recordSpf,
recordSrv, recordSshfp, recordTa, recordTsig, recordTkey, recordTxt,
recordHTTPs, recordSvcb

testzone1.com.,account0,2016-05-01,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0

testzone1.com.,account0,2016-04-28,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,7,0

testzone1.com.,account0,2016-04-27,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,7,0

testzone1.com.,account0,2016-04-26,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0

testzone1.com.,account0,2016-04-25,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0

testzone1.com.,account0,2016-04-24,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0

testzone1.com.,account0,2016-04-23,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0

