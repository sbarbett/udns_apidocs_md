

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

## Raw Query Sample Report

The Advanced Raw Queries report includes copious data for both queries and
responses. This report can provide details for query and response
troubleshooting. For more details about reports, review the **Report Center
User Guide**.

### Requesting Raw Query Sample Report

**Method and URI** :

POST https://api.ultradns.com/reports/dns_resolution/sample/raw_queryHTTP/1.1

OR

POST
https://api.ultradns.com/reports/dns_resolution/sample/raw_query?offset={offset}&limit={limit}

  
**Parameters** : May contain the following:

### Raw Query Sample Parameters

Raw Query Parameters DTO

Parameter |  Description |  Type  
---|---|---  
offset |  This field is optional.  If not specified, initial records will always be returned specified to limit. This parameter allows pagination on the reporting records retrieved. The offset will be the integer value that specifies the position of first result to be retrieved. Specify offset as 0 for first results to be retrieved. |  Integer. Optional.  
limit |  This field is optional.  If not specified, the total number of records returned in the response will be equal to the default value 1000. This parameter allows pagination on the reporting records retrieved. The maximum number of results to be retrieved in a single response is 10,000 records. |  Integer. Optional.  
  
**Body** : Must contain a Raw Query Sort DTO.

### Raw Query Report DTO

Raw Query Sort DTO

Field |  Description |  Type  
---|---|---  
accountName |  The name of the account. |  String. Required.  
zoneName |  The results of the one zone being returned.

  * When not specified, all zones under the account will be queried for reporting.
  * Wildcards in the zone name are currently not supported.
  * Zone names with and without a DOT(.) at the end are supported.

|  String. Optional  
packetStartDateTime |  The packetStartDateTime must be supplied in the ISO 8601 UTC format (yyyy-MM-ddâTâHH:mm:ss.SSSZ).

  * If not supplied, will default to 00:00:00 of yesterdayâs date.
  * The maximum number of days between the packetStartDateTime and packetEndDateTime cannot exceed 90 days. 
  * The packetStartDateTime must be before or the same as the packetEndDateTime.
  * The packetStartDateTime cannot be more than 90 days prior to the current date.
  * The packetStartDateTime cannot be a future date.

|  Date-Time. Optional  
packetEndDateTime |  The packetEndDateTime must be supplied in the ISO 8601 UTC format (yyyy-MM-ddâTâHH:mm:ss.SSSZ).

  * If not supplied, will default to 23:59:59 of âYesterdayâsâ date.
  * The maxiumum number of days between the packetStartDateTime and packetEndDateTime cannot exceed 90 days. 

|  Date-Time. Optional.  
  
  
**Responses** : If task completes, Status Code 201 is returned with a
requestId in the response body.

**Errors** : An error code is returned under the following conditions:

  * Error Code 401 â âUnauthorized. Token not found, expired or invalid.â

  * Error Code 400 â âpacketEndDateTime is before packetStartDateTime.â

  * Error Code 400 â âDate provided is not in a valid format.â

  * Error Code 400 â âAccount name not provided.â

  * Error Code 400 â âpacketStartDateTime/packetEndDateTime is a future date.â

  * Error Code 400 â âOffset value is a negative value.â

  * Error Code 400 â âpacketStartDateTime is older than 90 days.â

JSON Example: Raw Query Sample Request

JSON Example: Raw Query Sample Request ```json { "rawQuerySample": {
"accountName": "teamrest", "packetStartDateTime": " 2017-08-09T10:25:00Z",
"packetEndDateTime": " 2017-08-11T10:10:00Z", "zoneName":
"apexcnamedemo1.com." } } ```

### Retrieving Raw Query Sample Report

**Method and URI** :

GET https://ai.ultradns.com/requests/{requestID}

  
**Parameters** : Must contain a ReportRequest DTO

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a Raw
Query Sample Report Output DTO in the response body. Each value is comma-
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

Raw Query Sample Report Output DTO

Response Body |  Description |  Type  
---|---|---  
accountName |  The name of the Account being queried. |  String.  
udpTcpIndicator |  Will return either UDP or TCP. |  String.  
tldSldIndicator |  Will return Top Level Domain or Server Level Domain value of either TLD or SLD server. |  String.  
queryResponseIndicator |  The Query response indicator. Will return either Query or Response. |  String.  
responseMicroSet |  Will return either the response in micro seconds or a NULL value if a response is not matched to a query. |  Integer.  
ucapPacketErr |  Packet parsing error in ucap. Will return:  
  
0 = No Error  
  
1 = IP Header error  
  
2 = DNS Header error  
  
3 = Record Count error  
  
4 = Query error  
  
5 = Answer error  
  
6 = Auth error  
  
7 = Additional error |  Integer.  
resolverPort |  The Resolver port. |  Integer.  
resolverIP |  The Resolver IP in binary.  
  
4 bytes for IPv4,  
  
16 bytes for IPv6. |  Integer. IP address.  
truncatedIndicator |  The Truncation indicator:   
  
1 = Message truncated  
  
0 = Not truncated |  Integer.  
recursionDesired |  The Recursion desired indicator. 1=True  
  
2=False |  Integer.  
recursionAvailable |  The Recursive available indicator. 1=True  
  
2=False |  Integer.  
rcode |  The Response Code:   
  
0 = NOERROR  
  
1 = FORMERR  
  
2 = SERVFAIL  
  
3 = NXDOMAIN  
  
4 = NOTIMP  
  
5 = REFUSED |  Integer.  
qdcount |  The query count. |  Integer.  
packetId |  Packet identifier. This unique identifier is produced in the capture application from a timestamp, node, and sequence number. |  Integer.  
packetDatetime |  Packet date/time. A timestamp when the packet was received by the capture process. |  Date-Time.  
opcode |  The query code:   
  
0 = QUERY  
  
1 = IQUERY  
  
2 = STATUS |  Integer.  
dnsMsgLength |  Length of the DNS message. Excludes ether/IP/UDP/TCP headers. |  Integer.  
dnsId |  The DNS Identifier. An ID generated by the client and returned by the resolver. |  Integer.  
clientPort |  The client port. |  Integer.  
clientIp |  Client IP in either binary.  
  
4 bytes for IPv4  
  
16 bytes for IPv6 |  Integer. IP address  
checkingDisabled |  Checking disabled indicator:   
  
1 = True  
  
2 = False |  Integer.  
authenticDataIndicator |  Authentic data indicator:   
  
1 = True  
  
2 = False |  Integer.  
authenticAnswerIndicator |  Authoritative answer indicator:   
  
1 = Authoritative  
  
0 = Non-Authoritative |  Integer.  
arcount |  The Additional Record count.  |  Integer.  
ancount |  The Answer Record count. |  Integer.  
nscount |  The Authority record count. |  Integer.  
qname |  The query name. |  String.  
qtype |  The Query type.  
  
1 = A  
  
5 = CNAME  
  
6 = SOA  
  
28 = AAAA etc. |  Integer.  
zoneName |  The Zone Name being queried.  |  String.  
ipVersion |  The IP version being used by the zone.   
  
IPv4 = 4  
  
IPv6 = 6 |  Integer.   
  
JSON Example: Retrieving Raw Query Sample Report

{

"accountName": "teamrest",

"udpTcpIndicator": "UDP",

"tldSldIndicator": "SLD",

"queryResponseIndicator": "Query",

"responseMicroSec": null,

"ucapPacketErr": 0,

"resolverPort": 53,

"resolverIp": "10.31.147.7",

"truncatedIndicator": 0,

"recursionDesired": 1,

"recursionAvailable": 0,

"rcode": 0,

"qdcount": 1,

"packetId": "6267557462119846686",

"packetDateTime": 2016-03-29T19:21:22.769Z,

"opcode": 0,

"dnsMessageLength": 47,

"dnsId": "64586",

"clientPort": 53194,

"clientIp": "10.33.162.158",

"checkingDisabled": 0,

"authenticDataIndicator": 1,

"authenticAnswerIndicator": 0,

"arcount": 1,

"ancount": 0,

"nscount": 0,

"qname": "apexcnamedemo1.com.",

"qtype": "A",

"zoneName": "apexcnamedemo1.com.",

"ipVersion": "4"

}

The Raw Query Sample Report can be returned in the .CSV format. See the
[Calling the APIs](../Introduction.htm#_Ref490648854)section for further
details.

.CSV Example: Raw Query Sample Report

Account Name,UDP / TCP,TLD / SLD,Query / Response,Response Time (in Î¼s),Ucap
Packet Error,Resolver Port,Response IP,Truncated Indicator,Recursion
Desired,Recursion Available,Response code,Question Record count,Packet
Id,Packet Date Time,Opcode,DNS Message Length,DNS Id,Client Port,Client
IP,Checking Disabled,Authentic Data Indicator,Authentic Answer
Indicator,Additional Record Count,Answer Record Count,Namespace Record
Count,QName,QType,Zone Name,IP Version

GTV8,UDP,SLD,Query,,0,53,204.74.108.1,0,1,0,0,1,6524704301611519106,2018-02-20T18:25:02.298Z,0,32,60455,39787,107.21.211.150,0,0,0,0,0,0,gmon-n.invalid.,SOA,gmon-n.invalid.,4

GTV8,UDP,SLD,Response,163,0,53,204.74.108.1,0,1,0,0,1,6524704301611519269,2018-02-20T18:25:02.298Z,0,143,60455,39787,107.21.211.150,0,0,1,0,1,1,gmon-n.invalid.,SOA,gmon-n.invalid.,4

GTV8,UDP,SLD,Query,,0,53,204.74.108.1,0,1,0,0,1,6524704305906574096,2018-02-20T18:25:03.385Z,0,32,37375,46677,107.21.211.150,0,0,0,0,0,0,gmon-n.invalid.,SOA,gmon-n.invalid.,4

