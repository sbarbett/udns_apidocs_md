

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

## Synchronous Zone Query Volume Report

The purpose of the Synchronous Zone Query Volume Report is to provide
aggregated zone query volumes for multiple zones on a monthly basis, or for a
set period of time.

**Key differences from the Zone Query Volume Report**

  * The maximum time frame between the start and end date cannot exceed 7 days.

  * Synchronous in nature, so Report ID will be returned as results will be returned immediately.

  * Significantly more details returned for each zone.

  * No DTO required in the Body as this is a GET call.

### Synchronous Zone Query Volume Report DTOs

**Method and URI:**

GET https://api.ultradns.com/reports/dns_resolution/query_volume/zone

Synchronous Zone Query Volume Report Response DTO

Response Body |  Description |  Type  
---|---|---  
zoneName |  The name of the zone. |  String  
accountName |  The name of the account. |  String  
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
  
**Parameters** : Can include the following:

Parameter |  Description |  Type  
---|---|---  
sort |  The sort column used to order the list. The valid values are:

  * zoneName
  * nxdomainCount
  * servfailCount
  * rspTotal

Example: /reports/dns_resolution/query_volume/zone?sort=zoneName:ASC  
At a time, sorting is allowed only on single field. By default results will be sorted on zoneName in ascending order. |  String.  
offset |  This field is optional. If not specified, initial records will always be returned specific to limit and SortOrder. This parameter allows pagination on the reporting records retrieved. The offset will be the integer value that specifies the position of first result to be retrieved. Specify offset as 0 for first results to be retrieved. |  Integer. Optional.  
limit |  This field is optional. If not specified, the total number of records returned in the response will be equal to the default value 1000. This parameter allows pagination on the reporting records retrieved. The limit will be the integer value that specifies the maximum number of results to be retrieved in response. |  Integer.  
Optional.  
filter |  The query used to construct the list. Query operators are: 

  1. zoneName â Name of the zone
  2. accountName â Name of account
  3. startDate â Start Date from which the results needs to be fetched. By default it will be 1st of the previous month. It cannot be older than 13 months.
  4. endDate â End Date till which the results needs to be fetched. By default it will be 7th day of previous month. It cannot be older than 13 months. 

|  Integer.  
Optional.  
  
**Body** : None

### Response Link Headers

Response Link Headers

Field |  Description  
---|---  
Link |  Relative URL to next page of report if available: POST </v1/reports/dns_resolution/query_volume/zone?offset=8&limit=10>; rel="next"  Relative URL to previous page of report if available: </v1/reports/dns_resolution/query_volume/zone?offset=0&limit=10>; rel="previous" When using the next or previous link header to retrieve report data, you must perform another POST call, and include the original body content (if any) and new query parameters (such as offset and limit).  When continuing to use subsequent Link Headers to retrieve additional results, you must continue to perform the POST call per link header to retrieve the next set of report details.  
Limit |  Specify the maximum number of records in requested response. Cannot be greater than maximum allowed limit. Currently maximum allowed limit is 100k.  
Results |  Total rows in the report response.  
  
JSON Example: Synchronous Zone Query Volume Report Response Details

JSON Example: Synchronous Zone Query Volume Report Response Details ```json [
{ "zoneName": "testzone1.com.", "accountName": "account1", "rspTotal": 535,
"tcpTotal": 0, "udpTotal": 535, "ipv4Total": 344, "ipv6Total": 191,
"ipv4tcpTotal": 0, "ipv4udpTotal": 344, "ipv6tcpTotal": 0, "ipv6udpTotal":
191, "recordA": 10, "recordA6": 0, "recordAAAA": 0, "recordAny": 0,
"recordAxfr": 0, "recordCert": 0, "recordCname": 0, "recordDlv": 0,
"recordDnskey": 0, "recordHinfo": 0, "recordIpseckey": 0, "recordIxfr": 0,
"recordLoc": 0, "recordMf": 0, "recordNaptr": 0, "recordMx": 0, "recordNs":
33, "recordNsec": 0, "recordNsec3": 0, "recordNsec3Param": 0, "recordRp": 0,
"recordPtr": 492, "recordRrsig": 0, "recordSoa": 0, "recordSpf": 0,
"recordSrv": 0, "recordSshfp": 0, "recordTa": 0, "recordTsig": 0,
"recordTkey": 0, "recordTxt": 0, "recordHttps": 7, "recordSvcb": 0,
"refusedCount": 0, "notimpCount": 0, "nxdomainCount": 527, "servfailCount": 0,
"formerrCount": 0, "noerrorCount": 8 }, { "zoneName": "testzone2.com.",
"accountName": "account1", "rspTotal": 493, "tcpTotal": 0, "udpTotal": 493,
"ipv4Total": 303, "ipv6Total": 190, "ipv4tcpTotal": 0, "ipv4udpTotal": 303,
"ipv6tcpTotal": 0, "ipv6udpTotal": 190, "recordA": 12, "recordA6": 0,
"recordAAAA": 0, "recordAny": 0, "recordAxfr": 0, "recordCert": 0,
"recordCname": 0, "recordDlv": 0, "recordDnskey": 0, "recordHinfo": 0,
"recordIpseckey": 0, "recordIxfr": 0, "recordLoc": 0, "recordMf": 0,
"recordNaptr": 0, "recordMx": 0, "recordNs": 88, "recordNsec": 0,
"recordNsec3": 0, "recordNsec3Param": 0, "recordRp": 0, "recordPtr": 391,
"recordRrsig": 0, "recordSoa": 0, "recordSpf": 0, "recordSrv": 0,
"recordSshfp": 0, "recordTa": 0, "recordTsig": 0, "recordTkey": 0,
"recordTxt": 0, "recordHttps": 7, "recordSvcb": 0, "refusedCount": 0,
"notimpCount": 0, "nxdomainCount": 459, "servfailCount": 0, "formerrCount": 0,
"noerrorCount": 34 }, { "zoneName": "testzone3.com.", "accountName":
"account1", "rspTotal": 431, "tcpTotal": 0, "udpTotal": 431, "ipv4Total": 173,
"ipv6Total": 258, "ipv4tcpTotal": 0, "ipv4udpTotal": 173, "ipv6tcpTotal": 0,
"ipv6udpTotal": 258, "recordA": 5, "recordA6": 0, "recordAAAA": 0,
"recordAny": 0, "recordAxfr": 0, "recordCert": 0, "recordCname": 0,
"recordDlv": 0, "recordDnskey": 0, "recordHinfo": 0, "recordIpseckey": 0,
"recordIxfr": 0, "recordLoc": 0, "recordMf": 0, "recordNaptr": 0, "recordMx":
0, "recordNs": 24, "recordNsec": 0, "recordNsec3": 0, "recordNsec3Param": 0,
"recordRp": 0, "recordPtr": 400, "recordRrsig": 0, "recordSoa": 0,
"recordSpf": 0, "recordSrv": 0, "recordSshfp": 0, "recordTa": 0, "recordTsig":
0, "recordTkey": 0, "recordTxt": 0, "recordHttps": 7, "recordSvcb": 0,
"refusedCount": 0, "notimpCount": 0, "nxdomainCount": 423, "servfailCount": 0,
"formerrCount": 0, "noerrorCount": 8 }, { "zoneName": "testzone4.com.",
"accountName": "account1", "rspTotal": 524, "tcpTotal": 0, "udpTotal": 524,
"ipv4Total": 322, "ipv6Total": 202, "ipv4tcpTotal": 0, "ipv4udpTotal": 322,
"ipv6tcpTotal": 0, "ipv6udpTotal": 202, "recordA": 11, "recordA6": 0,
"recordAAAA": 0, "recordAny": 0, "recordAxfr": 0, "recordCert": 0,
"recordCname": 0, "recordDlv": 0, "recordDnskey": 0, "recordHinfo": 0,
"recordIpseckey": 0, "recordIxfr": 0, "recordLoc": 0, "recordMf": 0,
"recordNaptr": 0, "recordMx": 0, "recordNs": 18, "recordNsec": 0,
"recordNsec3": 0, "recordNsec3Param": 0, "recordRp": 0, "recordPtr": 494,
"recordRrsig": 0, "recordSoa": 0, "recordSpf": 0, "recordSrv": 0,
"recordSshfp": 0, "recordTa": 0, "recordTsig": 0, "recordTkey": 0,
"recordTxt": 0, "recordHttps": 7, "recordSvcb": 0, "refusedCount": 0,
"notimpCount": 0, "nxdomainCount": 520, "servfailCount": 0, "formerrCount": 0,
"noerrorCount": 4 }, { "zoneName": "testzone5.com.", "accountName":
"account1", "rspTotal": 215, "tcpTotal": 0, "udpTotal": 215, "ipv4Total": 133,
"ipv6Total": 82, "ipv4tcpTotal": 0, "ipv4udpTotal": 133, "ipv6tcpTotal": 0,
"ipv6udpTotal": 82, "recordA": 0, "recordA6": 0, "recordAAAA": 0, "recordAny":
0, "recordAxfr": 0, "recordCert": 0, "recordCname": 0, "recordDlv": 0,
"recordDnskey": 0, "recordHinfo": 0, "recordIpseckey": 0, "recordIxfr": 0,
"recordLoc": 0, "recordMf": 0, "recordNaptr": 0, "recordMx": 0, "recordNs": 1,
"recordNsec": 0, "recordNsec3": 0, "recordNsec3Param": 0, "recordRp": 0,
"recordPtr": 213, "recordRrsig": 0, "recordSoa": 0, "recordSpf": 0,
"recordSrv": 0, "recordSshfp": 0, "recordTa": 0, "recordTsig": 0,
"recordTkey": 0, "recordTxt": 0, "recordHttps": 7, "recordSvcb": 0,
"refusedCount": 0, "notimpCount": 0, "nxdomainCount": 213, "servfailCount": 0,
"formerrCount": 0, "noerrorCount": 2 }, { "zoneName": "testzone6.com.",
"accountName": "account1", "rspTotal": 294, "tcpTotal": 0, "udpTotal": 294,
"ipv4Total": 107, "ipv6Total": 187, "ipv4tcpTotal": 0, "ipv4udpTotal": 107,
"ipv6tcpTotal": 0, "ipv6udpTotal": 187, "recordA": 11, "recordA6": 0,
"recordAAAA": 0, "recordAny": 0, "recordAxfr": 0, "recordCert": 0,
"recordCname": 0, "recordDlv": 0, "recordDnskey": 0, "recordHinfo": 0,
"recordIpseckey": 0, "recordIxfr": 0, "recordLoc": 0, "recordMf": 0,
"recordNaptr": 0, "recordMx": 0, "recordNs": 30, "recordNsec": 0,
"recordNsec3": 0, "recordNsec3Param": 0, "recordRp": 0, "recordPtr": 251,
"recordRrsig": 0, "recordSoa": 0, "recordSpf": 0, "recordSrv": 0,
"recordSshfp": 0, "recordTa": 0, "recordTsig": 0, "recordTkey": 0,
"recordTxt": 0, "recordHttps": 7, "recordSvcb": 0, "refusedCount": 0,
"notimpCount": 0, "nxdomainCount": 286, "servfailCount": 0, "formerrCount": 0,
"noerrorCount": 8 }, { "zoneName": "testzone7.com.", "accountName":
"account1", "rspTotal": 659, "tcpTotal": 0, "udpTotal": 659, "ipv4Total": 375,
"ipv6Total": 284, "ipv4tcpTotal": 0, "ipv4udpTotal": 375, "ipv6tcpTotal": 0,
"ipv6udpTotal": 284, "recordA": 75, "recordA6": 0, "recordAAAA": 0,
"recordAny": 0, "recordAxfr": 0, "recordCert": 0, "recordCname": 0,
"recordDlv": 0, "recordDnskey": 0, "recordHinfo": 0, "recordIpseckey": 0,
"recordIxfr": 0, "recordLoc": 0, "recordMf": 0, "recordNaptr": 0, "recordMx":
0, "recordNs": 25, "recordNsec": 0, "recordNsec3": 0, "recordNsec3Param": 0,
"recordRp": 0, "recordPtr": 556, "recordRrsig": 0, "recordSoa": 0,
"recordSpf": 0, "recordSrv": 0, "recordSshfp": 0, "recordTa": 0, "recordTsig":
0, "recordTkey": 0, "recordTxt": 0, "recordHttps": 7, "recordSvcb": 0,
"refusedCount": 0, "notimpCount": 0, "nxdomainCount": 651, "servfailCount": 0,
"formerrCount": 0, "noerrorCount": 8 }, { "zoneName": "testzone8.com.",
"accountName": "account1", "rspTotal": 96263, "tcpTotal": 0, "udpTotal":
96263, "ipv4Total": 69678, "ipv6Total": 26585, "ipv4tcpTotal": 0,
"ipv4udpTotal": 69678, "ipv6tcpTotal": 0, "ipv6udpTotal": 26585, "recordA":
4490, "recordA6": 0, "recordAAAA": 98, "recordAny": 20, "recordAxfr": 0,
"recordCert": 0, "recordCname": 197, "recordDlv": 0, "recordDnskey": 0,
"recordHinfo": 0, "recordIpseckey": 0, "recordIxfr": 0, "recordLoc": 0,
"recordMf": 0, "recordNaptr": 0, "recordMx": 0, "recordNs": 7522,
"recordNsec": 0, "recordNsec3": 0, "recordNsec3Param": 0, "recordRp": 0,
"recordPtr": 83494, "recordRrsig": 0, "recordSoa": 1, "recordSpf": 0,
"recordSrv": 0, "recordSshfp": 0, "recordTa": 0, "recordTsig": 0,
"recordTkey": 0, "recordTxt": 0, "recordHttps": 7, "recordSvcb": 0,
"refusedCount": 0, "notimpCount": 0, "nxdomainCount": 4340, "servfailCount":
0, "formerrCount": 0, "noerrorCount": 91923 }, { "zoneName": "testzone9.com.",
"accountName": "account1", "rspTotal": 24247, "tcpTotal": 0, "udpTotal":
24247, "ipv4Total": 17972, "ipv6Total": 6275, "ipv4tcpTotal": 0,
"ipv4udpTotal": 17972, "ipv6tcpTotal": 0, "ipv6udpTotal": 6275, "recordA":
1539, "recordA6": 0, "recordAAAA": 84, "recordAny": 0, "recordAxfr": 0,
"recordCert": 0, "recordCname": 45, "recordDlv": 0, "recordDnskey": 0,
"recordHinfo": 0, "recordIpseckey": 0, "recordIxfr": 0, "recordLoc": 0,
"recordMf": 0, "recordNaptr": 0, "recordMx": 0, "recordNs": 2536,
"recordNsec": 0, "recordNsec3": 0, "recordNsec3Param": 0, "recordRp": 0,
"recordPtr": 19924, "recordRrsig": 0, "recordSoa": 8, "recordSpf": 0,
"recordSrv": 0, "recordSshfp": 0, "recordTa": 0, "recordTsig": 0,
"recordTkey": 0, "recordTxt": 0, "recordHttps": 7, "recordSvcb": 0,
"refusedCount": 0, "notimpCount": 0, "nxdomainCount": 1839, "servfailCount":
0, "formerrCount": 0, "noerrorCount": 22408 }, { "zoneName":
"testzone10.com.", "accountName": "account1", "rspTotal": 21235, "tcpTotal":
0, "udpTotal": 21235, "ipv4Total": 15830, "ipv6Total": 5405, "ipv4tcpTotal":
0, "ipv4udpTotal": 15830, "ipv6tcpTotal": 0, "ipv6udpTotal": 5405, "recordA":
557, "recordA6": 0, "recordAAAA": 18, "recordAny": 0, "recordAxfr": 0,
"recordCert": 0, "recordCname": 53, "recordDlv": 0, "recordDnskey": 0,
"recordHinfo": 0, "recordIpseckey": 0, "recordIxfr": 0, "recordLoc": 0,
"recordMf": 0, "recordNaptr": 0, "recordMx": 0, "recordNs": 2440,
"recordNsec": 0, "recordNsec3": 0, "recordNsec3Param": 0, "recordRp": 0,
"recordPtr": 18053, "recordRrsig": 0, "recordSoa": 3, "recordSpf": 0,
"recordSrv": 0, "recordSshfp": 0, "recordTa": 0, "recordTsig": 0,
"recordTkey": 0, "recordTxt": 0, "recordHttps": 7, "recordSvcb": 0,
"refusedCount": 0, "notimpCount": 0, "nxdomainCount": 1788, "servfailCount":
0, "formerrCount": 0, "noerrorCount": 19447 } ] ```

