

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

## Host Query Volume Report

The purpose of the Host Query Volume Report is to provide aggregated host
query volumes for one or all hosts within a zone. It is intended to be a
âdrill downâ report, designed to get more granular information on a host
basis from the Zone Query Volume Report.

The output columns are the same as the Zone Query Volume with the addition of
the **Host Name**.

### Host Query Volume Report DTOs

### Requesting Host Query Volume Report

**Method and URI** :

POST
https://api.ultradns.com/reports/dns_resolution/query_volume/host?offset={offset}&limit={limit}

**Parameters** : Can include the following:

Host Query Volume Report Query Parameters

Parameter |  Description |  Type  
---|---|---  
offset |  This field is optional. If not specified, initial records will always be returned specific to limit and SortOrder. This parameter allows pagination on the report records retrieved.  The offset will be the integer value that specifies the position of the first result to be retrieved. Specify offset as 0 for the first results to be retrieved. |  Integer, Optional.  
limit |  This field is optional. If not specified, the total number of records returned in the response will be equal to the default value 1000. This parameter allows pagination on the report records retrieved.  The maximum number of results to be retrieved in a single response is 100,000 records. |  Integer, Optional.  
  
**Body** : Must contain a Host Query Volume DTO.

### Host Query Volume DTO

Host Query Volume DTO

Field |  Description |  Type  
---|---|---  
zoneName | 

  * The name of the zone to be returned.
  * Zone names with and without a DOT(.) at the end are supported.

|  String. Required.  
hostName | 

  * The name of the host to be returned.
  * If not supplied, defaults to âAllâ hosts in the zone.
  * The HostName is a FQDN. 

|  String. Optional.  
accountName |  Name of the account. |  String, Optional  
startDate |  StartDate (YYYY-MM-DD) If not supplied, defaults to the first day of the previous calendar month. The maximum number of days between the startDate and endDate cannot exceed 7 days. This is inclusive of startDate and endDate.

  * The startDate must be before or equal to the endDate.
  * startDate cannot be older than 90 days from the present date.
  * startDate cannot be a future date.

|  String, Optional  
endDate |  EndDate (YYYY-MM-DD) If not supplied, defaults to the 7th day of the previous calendar month. The maximum number of days between the startDate and endDate cannot exceed 7 days. This is inclusive of startDate and endDate.

  * endDate cannot be a future date.

|  String. Optional  
  
Host Query Volume Sort DTO

Field |  Description |  Type  
---|---|---  
**sortFields** |  Contains a map of sortable columns and sort directions. Defaults to sort by hostName, endDate in ascending order. |  JSON  
  
Host Query Volume Sortable Columns

Sortable Column |  Sort Direction  
---|---  
hostName |  ASC (Ascending) or DESC (Descending)  
startDate |  ASC or DESC  
endDate |  ASC or DESC  
rspTotal |  ASC or DESC  
  
**Responses** : If task completes, Status Code 201 is returned with a Host
Query Volume DTOin the response body.

**Errors** : An error code is returned under the following conditions:

  * Error Code 401 â âUnauthorized. Token not found, expired or invalid.â

  * Error Code 400 â If report endDate is before startDate.

  * Error Code 400 â If date provided is not in valid format i.e. âYYYY-MM-DD.â

  * Error Code 400 â When zone name is not provided.

  * Error Code 400 â When any one of startDate and endDate is not provided.

  * Error Code 400 â If startDate/endDate is a future date.

  * Error Code 400 â If offset is a negative value.

  * Error Code 400 â When startDate is older than 90 days.

JSON Example: Host Query Volume Report with Sort Columns

JSON Example: Host Query Volume Report with Sort Columns ```json {
"hostQueryVolume": { "zoneName": "abc.com.", "startDate": "2016-07-12",
"endDate": "2016-07-18" }, "sortFields": { "hostName": "ASC", "rspTotal":
"DESC", "startDate": "ASC", "endDate": "ASC" } } ```

### Retrieving Host Query Volume Reports

**Method and URI** :

GET https://api.ultradns.com/requests/{requestId}

  
**Parameters** : Must contain a ReportRequest DTO

**Responses** : If task completes, Status Code 200 OK is returned with a list
of Host Query Volume Report DTO Output in the response body. Each value is
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

### Host Query Volume Report Output DTO

Host Query Volume Report DTO Output

Response Body |  Description |  Type  
---|---|---  
zoneName |  The name of the zone. |  Sting  
hostName |  The name of the host. |  Sting  
accountName |  The name of the account. |  String  
startDate |  The startDate (YYYY-MM-DD) time. |  String  
endDate |  The endDate (YYYY-MM-DD) time. |  String  
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
recordAny |  Count of ANY records. |  Long  
recordAxfr |  Count of AXFR records. |  Long  
recordCert |  Count of CERT records. |  Long  
recordCname |  Count of CNAME records. |  Long  
recordDlv |  Count of DLV records. |  Long  
recordDnskey |  Count of DNSKEY records. |  Long  
recordHinfo |  Count of HINFO records. |  Long  
recordIpseckey |  Count of IPSECKEY records. |  Long  
recordIxfr |  Count of IXFR records. |  Long  
recordLoc |  Count of LOC records. |  Long  
recordMf |  Count of MF records. |  Long  
recordNaptr |  Count of NAPTR records. |  Long  
recordMx |  Count of MX records. |  Long  
recordNs |  Count of NS records. |  Long  
recordNsec |  Count of NSEC records. |  Long  
recordNsec3 |  Count of NSEC3 records. |  Long  
recordNsec3Param |  Count of NSEC3PARAM records. |  Long  
recordRp |  Count of RP records. |  Long  
recordPtr |  Count of PTR records. |  Long  
recordRrsig |  Count of RRSIG records. |  Long  
recordSoa |  Count of SOA records. |  Long  
recordSpf |  Count of SPF records. |  Long  
recordSrv |  Count of SRV records. |  Long  
recordSshfp |  Count of SSHFP records. |  Long  
recordTa |  Count of TA records. |  Long  
recordTsig |  Count of TSIG records. |  Long  
recordTkey |  Count of TKEY records. |  Long  
recordTxt |  Count of TXT records. |  Long  
recordHttps |  Count of HTTPS records. |  Long  
recordSvcb |  Count of SVCB records. |  Long  
  
![](../../Resources/Images/Rest-API_User_Guide/Introduction_67x78.png) |  Long is an unsigned 64-bit number and its value can be anything between 0 to 263 â 1 (9223372036854775807).  
---|---  
  
### Response Link Headers

Response Link Headers

Field |  Description  
---|---  
Link |  **Relative URL to next page of report if available** : </v1/reports/dns_resolution/query_volume/host?offset=8&limit=4>; rel="next"  **Relative URL to previous page of report if available** : </v1/reports/dns_resolution/query_volume/host?offset=0&limit=4>; rel="previous" When using the next or previous link header to retrieve report data, you must perform another POST call, and include the original body content (if any) and new query parameters (such as offset and limit).  When continuing to use subsequent Link Headers to retrieve additional results, you must continue to perform the POST call per link header to retrieve the next set of report details.  
Limit |  Specify the maximum number of records in requested response. Cannot be greater than maximum allowed limit. Currently maximum allowed limit is 100k  
Results |  Total rows in the report response.  
  
JSON Example: Host Query Volume Report return in JSON format when no hostName
is included, and multiple hosts are returned.

JSON Example: Host Query Volume Report return in JSON format when no hostName
is included, and multiple hosts are returned. ```json [ { "zoneName":
"abc.com.", "hostName": "http.", "accountName": "account0", "startDate":
"2016-07-15", "endDate": "2016-07-15", "rspTotal": 2, "tcpTotal": 0,
"udpTotal": 2, "ipv4Total": 2, "ipv6Total": 0, "ipv4tcpTotal": 0,
"ipv4udpTotal": 2, "ipv6tcpTotal": 0, "ipv6udpTotal": 0, "recordA": 2,
"recordA6": 0, "recordAAAA": 0, "recordAny": 0, "recordAxfr": 0, "recordCert":
0, "recordCname": 0, "recordDlv": 0, "recordDnskey": 0, "recordHinfo": 0,
"recordIpseckey": 0, "recordIxfr": 0, "recordLoc": 0, "recordMf": 0,
"recordNaptr": 0, "recordMx": 0, "recordNs": 0, "recordNsec": 0,
"recordNsec3": 0, "recordNsec3Param": 0, "recordRp": 0, "recordPtr": 0,
"recordRrsig": 0, "recordSoa": 0, "recordSpf": 0, "recordSrv": 0,
"recordSshfp": 0, "recordTa": 0, "recordTsig": 0, "recordTkey": 0,
"recordTxt": 0, "recordHttps": 7, "recordSvcb": 0 }, { "zoneName": "abc.com.",
"hostName": "ftp.", "accountName": "account0", "startDate": "2016-07-16",
"endDate": "2016-07-16", "rspTotal": 1, "tcpTotal": 0, "udpTotal": 1,
"ipv4Total": 1, "ipv6Total": 0, "ipv4tcpTotal": 0, "ipv4udpTotal": 1,
"ipv6tcpTotal": 0, "ipv6udpTotal": 0, "recordA": 0, "recordA6": 0,
"recordAAAA": 1, "recordAny": 0, "recordAxfr": 0, "recordCert": 0,
"recordCname": 0, "recordDlv": 0, "recordDnskey": 0, "recordHinfo": 0,
"recordIpseckey": 0, "recordIxfr": 0, "recordLoc": 0, "recordMf": 0,
"recordNaptr": 0, "recordMx": 0, "recordNs": 0, "recordNsec": 0,
"recordNsec3": 0, "recordNsec3Param": 0, "recordRp": 0, "recordPtr": 0,
"recordRrsig": 0, "recordSoa": 0, "recordSpf": 0, "recordSrv": 0,
"recordSshfp": 0, "recordTa": 0, "recordTsig": 0, "recordTkey": 0,
"recordTxt": 0, "recordHttps": 7, "recordSvcb": 0 }, { "zoneName": "abc.com.",
"hostName": "voip.", "accountName": "account0", "startDate": "2016-07-16",
"endDate": "2016-07-16", "rspTotal": 1, "tcpTotal": 0, "udpTotal": 1,
"ipv4Total": 1, "ipv6Total": 0, "ipv4tcpTotal": 0, "ipv4udpTotal": 1,
"ipv6tcpTotal": 0, "ipv6udpTotal": 0, "recordA": 0, "recordA6": 0,
"recordAAAA": 1, "recordAny": 0, "recordAxfr": 0, "recordCert": 0,
"recordCname": 0, "recordDlv": 0, "recordDnskey": 0, "recordHinfo": 0,
"recordIpseckey": 0, "recordIxfr": 0, "recordLoc": 0, "recordMf": 0,
"recordNaptr": 0, "recordMx": 0, "recordNs": 0, "recordNsec": 0,
"recordNsec3": 0, "recordNsec3Param": 0, "recordRp": 0, "recordPtr": 0,
"recordRrsig": 0, "recordSoa": 0, "recordSpf": 0, "recordSrv": 0,
"recordSshfp": 0, "recordTa": 0, "recordTsig": 0, "recordTkey": 0,
"recordTxt": 0, "recordHttps": 7, "recordSvcb": 0 } ] ```

![](../../Resources/Images/Rest-API_User_Guide/Introduction_57x66.png) |  The Host Query Volume Report can be returned in a .CSV format, but will require an additional step beyond the default JSON requirements. In the header section, you will need to include the additional field: **Accept: text/plain**.   
---|---  
  
.CSV Example: Host Query Volume Report return in .CSV format when no hostName
is included and multiple hosts are returned.

zoneName, hostName, accountName, startDate, endDate, rspTotal, tcpTotal,
udpTotal, ipv4Total, ipv6Total, ipv4tcpTotal, ipv4udpTotal, ipv6tcpTotal,
ipv6udpTotal, recordA, recordA6, recordAAAA, recordAny, recordAxfr,
recordCert, recordCname, recordDlv, recordDnskey, recordHinfo, recordIpseckey,
recordIxfr, recordLoc, recordMf, recordNaptr, recordMx, recordNs, recordNsec,
recordNsec3, recordNsec3Param, recordRp, recordPtr, recordRrsig, recordSoa,
recordSpf, recordSrv, recordSshfp, recordTa, recordTsig, recordTkey,
recordTxt, recordHTTPs, recordSvcb

abc.com.,http.,account0,2016-07-15,2016-07-15,2,0,2,2,0,0,2,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0

abc.com.,ftp.,account0,2016-07-16,2016-07-16,1,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0

abc.com.,voip.,account0,2016-07-16,2016-07-16,1,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0

![](../../Resources/Images/Rest-API_User_Guide/Introduction_64x75.png) |  When attempting to perform a GET for the Link Header details for the next/previous URL, a POST must first be performed to retrieve the next/previous URL of the requestId for the next set of records.  
---|---

