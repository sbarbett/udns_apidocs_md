

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

# Dangling DNS Report

Dangling DNS Records occur when a domain's DNS record points to a resource
that no longer exists or is incorrectly configured. This can happen when
services (like hosting or email servers) are moved or deleted, but the DNS
records are not updated accordingly. As a result, users or applications trying
to access the domain can encounter errors or downtime because they are
directed to non-existent or outdated resources. This can most commonly occur
when CNAME records are not updated accordingly.

The Dangling DNS Report scans CNAME records and queries external recursive
resolvers to check if they resolve or return an NXDOMAIN response, ensuring
precise identification of security gaps.

For more information and details of the possible security risks, you can refer
to the [Dangling DNS Records](https://dns.ultraproducts.support/hc/en-
us/community/posts/34660838984475-Introducing-UltraDNS-Dangling-CNAME-
Detection) section on our Community platform.

![](../../Resources/Images/Rest-API_User_Guide/Introduction_53x60.png) |  The Dangling DNS Report only supports domains/zones with 20,000 records or less.  
---|---  
  
## Requesting Dangling DNS Report

**Method and URI** :

POST https://api.ultradns.com/v1/zones/<zone_name>/healthchecks/dangling

**Body** : None

**Parameters** : None

**Response** : Status Code 200 OK is returned.

**Errors** : An error is returned under the following conditions:

  * If an unauthorized user tries to call this API.

  * If the zone does not exist.

  * If the zone is a Secondary zone.

  * If the zone has more than 20,000 records.

## Retrieving Dangling DNS Report

**Method and URI** :

GET https://api.ultradns.com/v1/zones/<zone_name>/healthchecks/dangling

**Body** : None

**Parameters** : Can include filters from the DanglingDNS Query Parameter DTO
.

DanglingDNS Query Parameter DTO

Parameter |  Description |  Type  
---|---|---  
host |  **Optional**. Returns the report results based on the hostname. The host parameter only returns results on an exact match; wildcard searches are not supported. |  String  
type |  **Optional**. Returns the report results based on the record type. The type parameter only returns results on an exact record match; wildcard searches are not supported. Values are case-sensitive.  Possible values are:

  * CNAME
  * A
  * AAAA 

|  Enum  
sort |  **Optional**. Allows for the sorting of returned results by the following category type:

  * host (default) 

|  String  
order |  **Optional**. Allows the report results to be displayed in either an ascending or descending order. Values are case-sensitive.  Valid values are: 

  * **ASC**
  * **DESC**

Default value: ASC |  Enum  
offset |  **Optional**. If not specified, initial records will always be returned specified to the limit. This parameter allows pagination on the reporting records retrieved.  The offset will be the integer value that specifies the position of first result to be retrieved. Specify offset as 0 for the first results to be retrieved. |  Integer  
limit |  **Optional**. If not specified, the total number of records returned in the response will equal the default value 100.  This parameter allows pagination on the reporting records retrieved. The maximum number of results retrieved in a single response is 1,000 records. |  Integer  
  
**Response** : If task completes, Status Code 200 OK is returned with a list
of DanglingDNSRecord Report DTO and DanglingDNSRecord DTO.

**Errors** : An error is returned under the following conditions:

  * If an unauthorized user tries to call this API.

  * If the zone does not exist.

  * If the zone is a Secondary zone.

  * If the zone has more than 20,000 records.

DanglingDNSRecord Report DTO

Parameter |  Description |  Type  
---|---|---  
version |  The time the report was run, displayed in GMT. |  Timestamp in the YYYY-MM-DD-HH24:MI:SS.nnnZ format.  
zone |  The target zone name. |  String  
status |  The status of the report. One of the following:

  * IN_PROGRESS
  * COMPLETED
  * FAILED 

|  Enum  
resultInfo/totalCount |  Displays the count of all records matching the specified query. |  Integer  
resultInfo/offset |  Displays the position in the list for the first returned element (0 based). |  Integer  
resultInfo/returnedCount |  Displays the number of records returned. |  Integer  
danglingRecordList |  The list of possible Dangling DNS records identified. |  List of DanglingDNSRecord DTO.  
  
JSON Example: DanglingRecord Report DTO

{

"version": "2025-02-05T14:12:06.882Z",

"zone": "example.com.",

"status": "COMPLETED",

"resultInfo": {

"totalCount": 2,

"offset": 0,

"returnedCount": 1,

"order": "ASC"

},

"danglingRecordsList": [

DanglingDNSRecord DTO

Parameter |  Description |  Type  
---|---|---  
host |  The specific DNS record name that is being flagged as dangling. |  String  
type |  The specific DNS record type.

  * A
  * AAAA
  * CNAME 

|  String  
recordData |  The record details and information. |  String  
ultimateTarget |  The non-existent or expired domain that the record is pointing to.  For example:   
cname.example.com (NOERRROR) â  
cname1.example.com (NOERRROR)â  
**cname2.example.com (NXDOMAIN)** â  
something.example.com  Because an NXDOMAIN was returned while resolving the CNAME chain on **cname2.example.com.** , it becomes the ultimate target.  |  String  
description |  The description of the error/issue with the record, indicating why it was flagged as Dangling DNS. |  String  
message |  Displays a status message if the report has failed to complete or still displays as IN_PROGRESS. |  String  
  
JSON Example: DanglingDNS Record DTO Response Results

"danglingRecordsList": [

{

"host": "cname.example.com",

"type": "CNAME",

"recordData": "cname2.example.com",

"ultimateTarget": "cname3.example.com",

"description": "CNAME target does not resolve or is unreachable."

},

{

"host": "mycname.example.com",

"type": "CNAME",

"recordData": "mycname2.example.com",

"ultimateTarget": "mycname3.example.com",

"description": "CNAME target does not resolve or is unreachable."

}

]

