

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

# Zone DTOs

The sections and tables below provide detailed information about the contents
of the DTOs used for Zone API calls. When a DTO field consists of the contents
of another DTO, a cross reference link to the associated DTO is provided. When
possible, return links to the âparentâ DTO are provided, along with links
to the API calls that use the DTO.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Zone
Properties DTO

The Zone Properties DTO holds the common metadata across all types of zones.
This must be included in the Zone Create DTO which is used for the Zone DTOs
call, unless it is present on an update, in which case it can be ignored.

Zone Properties DTO

Field |  Description |  Type  
---|---|---  
name |  Name of the zone, with trailing periods (â¦.) |  Must be a valid domain name.  _Required for zone creation._ Ignored if present on update.  
accountName |  Name of the account.  |  String. _Required for zone creation._ Ignored if present on update.  
type |  Type of zone. Valid values are PRIMARY, SECONDARY or ALIAS. |  _Required for zone creation._ Ignored if present on update.  
owner |  Name of the user that created the zone. |  String. Returned in GET responses for zone information. Ignored if present on create or update.  
recordCount |  Number of records in the zone |  Integer. Returned in GET responses for zone information. Ignored if present on create or update.  
dnssecStatus |  Whether or not the zone is signed with DNSSEC. Valid values are SIGNED or UNSIGNED. |  Returned in GET responses for zone information.  Ignored if present on create or update.  
lastModifiedDateTime |  The last date and time the zone was modified, represented in ISO8601 format. |  Returned in GET responses for zone information. Ignored if present on create or update.  
ultra2 |  _Only applicable to accounts that have enabled the UltraDNS2 service._ Indicates if the zone has UltraDNS2 enabled or not.  Valid values are **false** and **true**.  |  Boolean. Returned in GET responses for zone information.   
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Zone
Create DTO

The Zone Create DTO is the data structure used for the Zone DTOs, and Zone
DTOs API calls.

Zone Create DTO

Field |  Description |  Type  
---|---|---  
properties |  The name, account name, and type of zone being created. |  Zone Properties DTO. _Required for zone creation_. Ignored if present on update.  
primaryCreateInfo |  Metadata for a primary zone. |  Primary Zone DTO. _Required to create or update a primary zone_ , ignored in all other cases.  
secondaryCreateInfo |  Metadata for a secondary zone. |  Secondary Zone DTO. _Required to create or update a secondary zone_ , ignored in all other cases.  
aliasCreateInfo |  Metadata for an alias zone. |  Alias Zone DTO. _Required to create an alias zone_ , ignored in all other cases.  
changeComment |  An optional field allowing users to create a comment for a zone operation using up to 512 characters of free text. Applicable for all Zone api calls. Not applicable for Batch or JSON Patch calls. Additionally, the use of a colon (:) is prohibited.  |  String.  
  
JSON Example: New Primary Zone

{  
"properties": {  
"name": "primary-example.com.",  
"accountName": "example",  
"type": "PRIMARY"  
},  
"primaryCreateInfo": {  
"forceImport": true,  
"createType": "NEW"  
},

"changeComment": "Created as agreed"  
}

JSON Example: New Primary Zone Copied from Another Zone

{  
  
"properties": {  
  
"name": "copy-example.com.",  
  
"accountName": "example",  
  
"type": "PRIMARY"  
  
},  
  
"primaryCreateInfo": {  
  
"forceImport": true,  
  
"createType": "COPY",  
  
"originalZoneName": "example.cm."  
  
}  
  
}

JSON Example: New Primary Uploaded from a File

{  
"properties": {  
"name": "example.com.",  
"accountName": "example",  
"type": "PRIMARY"  
},  
"primaryCreateInfo": {  
"forceImport": true,  
"createType": "UPLOAD"  
}  
}

## Bind Upload â TTL Behavior during Zone Creation

### First Scenario

When creating a Zone via bind upload, any records with the same owner and
type, but have different TTLs (in the bind file), will be created with the
lowest TTL value amongst all the records of the same owner and type (in the
bind file).  
  
For example, the following three records for the owner âtxtrecordâ and the
type TXT, along with rdata and TTLs in one bind file:

  1. txtrecorddata1 with TTL 30
  2. txtrecorddata2 with TTL 500
  3. txtrecorddata3 with TTL 400

In this scenario, all three of the above records would be created with the TTL
value 300.

### Second Scenario

Similarly to the previous example, if you have records with the same owner and
type in a bind file, but only some of the TTLs are provided for the records in
the rrset, then all of the records of the rrset will inherit the lowest TTL
value (provided in the bind file).

  1. txtrecorddata1 with no TTL
  2. txtrecorddata2 with TTL 500
  3. txtrecorddata3 with TTL 400

All of the above records in the example will be given the TTL value of 400. If
none of the provided records have TTL values, then the TTL value for each
record will be given the default TTL value of 86400.

JSON Example: New Primary Zone via Transfer

{  
"properties": {  
"name": "copy-example.com.",  
"accountName": "example",  
"type": "PRIMARY"  
},  
"primaryCreateInfo": {  
"forceImport": true,  
"createType": "TRANSFER",  
"nameServer": {  
"ip": "1.2.3.4",  
"tsigKey": "key",  
"tsigKeyValue":"value"  
}  
}  
}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Primary
Zone DTO

The Primary Zone DTO contains the metadata used to create or update a Primary
Zone. The Zone DTOs, and Zone DTOs API calls use the Zone Create DTO, which in
turn references this DTO.

Primary Zone DTO

Field |  Description |  Type  
---|---|---  
forceImport |  Whether or not to move existing records from zones into this new zone. Values include: 

  * true = move
  * false = leave in existing zone (default)

|  Boolean.  _Only used for primary zone creation_. If not present, defaults
to âfalseâ.  Ignored if present for update.  
createType |  Indicates the method for creating the primary zone. Values include: 

  * NEW
  * COPY
  * TRANSFER
  * UPLOAD

|  _Required for primary zone creation_. Ignored if present for update.  
nameServer/ip |  IP address of the primary zone's name server (where the primary zone is being transferred from). |  IPv4 or IPv6 address. _Required if createType is âTRANSFER._ â  Ignored if present for update.  
nameServer/tsigKey |  If TSIG is enabled for this name server, the name of the TSIG key. |  String.   
Used only if createType is âTRANSFER.â  Required if TSIG is enabled for
this name server. Ignored if present for update.  
nameserver/tsigKeyValue |  If TSIG is enabled for this name server, the TSIG key's value. |  String.   
Used only if createType is âTRANSFER.â  Required if TSIG is enabled for
this name server. Ignored if present for update.  
nameserver/ tsigAlgorithm |  The hash algorithm used to generate the TSIG key.  Valid values are:

  * hmac-md5
  * hmac-sha1
  * hmac-sha224
  * hmac-sha256
  * hmac-sha384
  * hmac-sha512

|  String.  
_Used only if createType is âTRANSFER.â_ Default is hmac-md5. _Required if
TSIG is enabled for this name server._ Ignored if present for update.  
originalZoneName |  The name of the zone being copied. The existing zone must be owned by the same account as the new zone. |  String. Must be a valid domain name.  _Required if createType is âCOPY.â_ Ignored if present for update.  
restrictIPList |  The list of IP ranges that are allowed to transfer primary zones out using zone transfer protocol (AXFR/IXFR). |  List of Restrict IP DTOs.  Optional for both creation and update.  
tsig |  The TSIG information for the primary zone. |  TSIG DTO.  Optional for both creation and update.  
notifyAddresses |  The addresses that are notified when updates are made to the primary zone. |  List of Notify Address DTOs.  Optional for both creation and update.  
inherit |  Defines whether this zone should inherit the zone transfer values from the Account, and also specifies which values to inherit. Defaults to "ALL" if zone transfer settings on the account have been set. |  Optional for both creation and update. Valid values include:

  * ALL
  * NONE
  * Any combination of -  

    * IP_RANGE
    * NOTIFY_IP
    * TSIG

Separate multiple values with a comma, i.e., IP_RANGE, NOTIFY_IP  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Restrict
IP DTO

Each Restrict IP DTO holds the IP addresses that are allowed to transfer
Primary Zones out using the Zone Transfer protocol (AXFR/IXFR). The Restrict
IP DTO contains information used in the Primary Zone DTO.

The IP address information can be specified in three different formats:

  1. IP Range (startIP and endIP)

  2. CIDR (cidr)

  3. Single IP (singleIP)

Only one format should be specified in the DTO at a time (range, CIDR or
single IP).

Restrict IP DTO

Field |  Description |  Type  
---|---|---  
**startIP** |  The start of the IP range that is allowed to transfer this primary zone out using zone transfer protocol.  |  IPv4 or IPv6 address.  
**endIP** |  The end of the IP range that is allowed to transfer this primary zone out using zone transfer protocol. |  IPv4 or IPv6 address/  
**cidr** |  The IP ranges specified in CIDR |  CIDR (e.g. 1.1.1.1/30, ::10/126)  
**singleIP** |  The IP that is allowed to transfer this primary zone out using zone transfer protocol. |  IPv4 or IPv6 address.  
**comment** |  A description of this range of IP addresses. |  String. Optional.  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)TSIG DTO

The TSIG DTO holds TSIG information for the Primary Zone. The TSIG DTO
contains information used in the Primary Zone DTO.

Tsig DTO

Field |  Description |  Type  
---|---|---  
**tsigKeyName** |  The name of the TSIG key for the zone.  |  String. REQUIRED.  
**tsigKeyValue** |  The value of the TSIG key for the zone. |  String. REQUIRED.  
**description** |  A description of this key. |  String. Optional.  
**tsigAlgorithm** |  The hash algorithm used to generate the TSIG key.  Valid values are:

  * hmac-md5
  * hmac-sha1
  * hmac-sha224
  * hmac-sha256
  * hmac-sha384
  * hmac-sha512

|  String. REQUIRED.  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Notify
Address DTO

Each Notify Address DTO defines an address that gets notified when there are
updates to a Primary Zone. The Notify Address DTO contains information used in
the Primary Zone DTO.

Notify Address Detail DTO

Field |  Description |  Type  
---|---|---  
notifyAddress |  The IP address that is notified when the primary zone is updated. |  IPv4 address. REQUIRED.  
description |  A description of this address. |  String. Optional.  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Secondary
Zone DTO

The Secondary Zone DTO holds the metadata used to create or update a Secondary
Zone. The Zone DTOs, and Zone DTOs API calls use the Zone Create DTO, which in
turn references this DTO.

This DTO is also used to return the Primary Name Servers for a Secondary Zone
when the Zone DTOs call is used.

Secondary Zone DTO

Field |  Description |  Type  
---|---|---  
primaryNameServers |  The primary name servers of the source zone for the secondary zone. |  Name Server IP List DTO. _Required for creating or updating a secondary zone_. Ignored in all other cases.  
notificationEmailAddress |  The Notification Email for a secondary zone. |  String. Optional.  
  
JSON Example: New Secondary Zone

{  
"properties": {  
"name": "secondary-example.com.",  
"accountName": "example",  
"type": "SECONDARY"  
},  
"secondaryCreateInfo": {  
"primaryNameServers": {  
"nameServerIpList": {  
"nameServerIp1": {  
"ip": "1.2.3.4",  
"tsigKey": "key1",  
"tsigKeyValue": "value1"  
}  
}  
},  
"notificationEmailAddress": "<email_address>"  
}  
}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Alias Zone
DTO

The Alias Zone DTO holds the metadata used for creating an Alias Zone. The
Zone DTOs API call uses the Zone Create DTO which in turn references this DTO.

Alias Zone DTO

Field |  Description |  Type  
---|---|---  
**originalZoneName** |  The name of the zone being aliased. The existing zone must be owned by the same account as the new zone. |  Must be a valid domain name. _Required for alias during creation._  
  
JSON Example: New Alias Zone

{  
"properties": {  
"name": "alias-example.com.",  
"accountName": "example",  
"type": "ALIAS"  
},  
"aliasCreateInfo": {  
"originalZoneName": "example.com."  
},

"changeComment":"Create an alias zone"  
}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Name
Server IP List DTO

The Name Server IP List DTO lists the Primary Name Servers for a Secondary
Zone. It is referenced by the Secondary Zone DTO which is used for the Zone
DTOs, Zone DTOs, and Zone DTOs API calls.

Name Server IP List DTO

Field |  Description |  Type  
---|---|---  
nameServerIpList  
/nameServerIP1/ip |  The IP address of the primary name server for the source zone. |  IPv4 or IPv6 address.  _Required for creation or update of a secondary zone._  
nameServerIpList  
/nameServerIP1/tsigKey |  If TSIG is enabled for this name server, the name of the TSIG key. |  String. _Required for creation or update of a secondary zone if TSIG is enabled for this name server._  
nameServerIpList  
/nameServerIP1 /tsigKeyValue |  If TSIG is enabled for this name server, the TSIG key's value. |  String. _Required for creation or update of a secondary zone if TSIG is enabled for this name server._  
nameServerIpList  
/nameServerIP1 /tsigAlgorithm |  The hash algorithm used to generate the TSIG key.  Valid values are:

  * hmac-md5
  * hmac-sha1
  * hmac-sha224
  * hmac-sha256
  * hmac-sha384
  * hmac-sha512

|  String. Default is hmac-md5. _Required for creation or update of a
secondary zone if TSIG is enabled for this name server._  
nameServerIpList/  
nameServerIP2/ip |  The IP address of the first backup name server for the source zone. |  IPv4 or IPv6 address. Optional for creation or update of a secondary zone.  
nameServerIpList/  
nameServerIP2/tsigKey |  If TSIG is enabled for this name server, the name of the TSIG key. |  String. Required for creation or update of a secondary zone if TSIG is enabled for this name server.   
nameServerIpList/  
nameServerIP2  
/tsigKeyValue |  If TSIG is enabled for this name server, the TSIG key's value. |  String. _Required for creation or update of a secondary zone if TSIG is enabled for this name server._  
nameServerIpList/  
nameServerIP2  
/tsigAlgorithm |  The hash algorithm used to generate the TSIG key.  Valid values are:

  * hmac-md5
  * hmac-sha1
  * hmac-sha224
  * hmac-sha256
  * hmac-sha384
  * hmac-sha512

|  String. Default is hmac-md5 _Required for creation or update of a secondary
zone if TSIG is enabled for this name server._  
nameServerIpList  
/nameServerIP3/ip |  The IP address of the second backup name server for the source zone. |  IPv4 or IPv6 address. Optional for creation or update of a secondary zone.  
nameServerIpList  
/nameServerIP3/tsigKey |  If TSIG is enabled for this name server, the name of the TSIG key. |  String. _Required for creation or update of a secondary zone if TSIG is enabled for this name server._  
nameServerIpList  
/nameServerIP3  
/tsigKeyValue |  If TSIG is enabled for this name server, the TSIG key's value. |  String. _Required for creation or update of a secondary zone if TSIG is enabled for this name server._  
nameServerIpList  
/nameServerIP3  
/tsigAlgorithm |  The hash algorithm used to generate the TSIG key.  Valid values are:

  * hmac-md5
  * hmac-sha1
  * hmac-sha224
  * hmac-sha256
  * hmac-sha384
  * hmac-sha512

|  String. Default is hmac-md5. _Required for creation or update of a
secondary zone if TSIG is enabled for this name server._  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Transfer
Status Details DTO

The Transfer Status Details contains the Zone Transfer Status Details.

Transfer Status Details DTO

Field |  Description |  Type  
---|---|---  
lastRefresh |  Displays when the last transfer attempt or refresh was. |  String. Date/Time formatted in ISO 8601 format, UTC offset based on customer-specified time zone  
nextRefresh |  Displays when the next transfer attempt or refresh is. |  String. Date/Time formatted in ISO 8601 format, UTC offset based on customer-specified time zone  
lastRefreshStatus |  Displays the status of the last transfer that was attempted. Valid values are:

  * IN_PROGRESS
  * FAILED
  * SUCCESSFUL

|  String. Date/Time formatted in ISO 8601 format, UTC offset based on
customer-specified time zone  
lastRefreshStatusMessage |  Displays the last transferâs status message. This is currently shown as failure reason. |  String.  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Zone DTO

The Zone DTO is the data structure returned for the Zone DTOs call.

Zone DTO

Field |  Description |  Type  
---|---|---  
properties |  The basic metadata for any zone. |  Zone Properties DTO.  
restrictIpList |  The list of IP ranges that are allowed to use AXFR to transfer primary zones out. |  List of Restrict IP DTOs. Only present if this is a primary zone.  
primaryNameServers |  The primary name servers that are the source of a secondary zone. |  Name Server IP List DTO. Only present if this is a secondary zone.  
originalZoneName |  The name of the zone that is the source of an alias zone. |  Domain name. Only present if this is an alias zone.  
registrarInfo |  Information about the name server configuration for this zone. |  Registrar Info DTO. Only present if this is a primary zone.  
tsig |  The TSIG information for the primary zone. |  TSIG DTO. Only present if this is a primary zone.  
notifyAddresses |  The addresses that are notified when updates are made to the primary zone. |  List of Notify Address DTOs. Only present if this is a primary zone.  
transferStatusDetails |  The zone transfer status details. |  Transfer Status Details DTO  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Registrar
Info DTO

The Registrar Info DTO holds the domain name registry information for a
Primary Zone.

Registrar Info DTO

Field |  Description |  Type  
---|---|---  
registrar |  The name of the domain registrar. |  String  
whoisExpiration |  The date when the domain name registration expires. |  Date when the domain registration expires.  
nameServers/ok |  List of UltraDNS name servers that are configured for this domain. |  List of domain names.  
nameServers/unknown |  List of name servers that are configured for this domain, but are not UltraDNS-managed name servers. |  List of domain names.  
nameServers/missing |  List of UltraDNS name servers that should be configured for this domain, but are not. |  List of domain names.  
nameServers/incorrect |  List of any obsolete UltraDNS name servers that are still configured for this zone. |  List of domain names.  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Zone List
DTO

The Zone List DTO wraps the zones returned for a [Zone API](Zone
API.htm#List_Metadata_for_Zones-v3) call, and the metadata for the request.

Zone List DTO Structure

Field |  Description |  Type  
---|---|---  
zones |  List of the returned zones. Each item in the list matches the zone DTO described above. |  List of Zone DTOs.  
queryInfo/q |  The query used to construct the list. |  String  
queryInfo/sort |  The sort column used to order the list. |  String  
queryInfo/reverse |  Whether the list is ascending (false) or descending (true). |  Boolean  
queryInfo/limit |  The maximum number of rows requested. |  Integer  
resultInfo/totalCount |  Count of all zones in the system for the specified query. |  Integer  
resultInfo/offset |  The position in the list for the first returned element (0 based). |  Integer  
resultInfo/returnedCount |  The number of zones returned. |  Integer

