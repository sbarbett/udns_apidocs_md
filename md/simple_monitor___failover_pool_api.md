

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

# Simple Monitor / Failover Pool API

Simple Failover (SF) Pools are used to define a single address (the live
record), a simple HTTP monitor, and a backup address. If the monitor detects
that the live record is unreachable from too many global regions, the backup
(Failover) record is shown. The user can also force the backup record to be
live, or unforce it.

Simple Monitoring is a feature that is a subset of Simple Failover and Simple
Load Balancing (SLB). You can run all the Simple Failover calls as a Simple
Monitor call instead by ensuring that your Failover record information is
removed from the body of the call. Examples will be provided for each call.

Simple Monitoring (SM) is designed to provide single resource record sites
with a very basic website availability monitor. This monitor tracks if a
website is available or unreachable, and alerts the customer to unavailability
via email notification. This feature does not provide fail over assistance to
an alternative record (i.e. All fail), nor does it provide any measurement
statistics on the health of the website (beyond whether the site is available
or down).

The most common example of a Simple Monitor would be a customer having only
one IP Address, and needs a monitor to notify them when the address has an
outage, instead of needing to failover to another address.

Simple Monitor/ Failover pools support the usage of IPv6 addresses by using
the âAAAAâ record type. You will need to alter the API calls to match the
AAAA record type when trying to use an IPv6 instead of an IPv4 address that
uses the A record type.

IPv6 Address Format |  Example  
---|---  
**Ipv6 Full Notation** |  â2001:0db8:0a0b:12f0:0000:0000:0000:0001â  
**Compressed** |  â2001:db8:a0b:12f0::1â OR "2610:a1:1059:0:0:0:0:35"  
  
## Modifications of Existing DTOs and Parameters

Pools are implemented as additional information added to RRSets. A SF Pool DTO
has an optional section called "Profile". The Profile contains information
that is outside the bounds of the various DNS specifications.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Profile
Information for Simple Monitor / Failover Pools

A profile is simply a JSON Map. All profiles must contain a key called
@context. This is a JSON-LD reference to a schema (http://json-ld.org/). The
schema describes the custom data that is used in the profile fields

The schema name for Simple Monitor / Failover pools is :
http://schemas.ultradns.com/SFPool.jsonschema.

The other fields in the profile for a Simple Monitor / Failover pool are:

Simple Failover Pool Profile Fields

Field |  Description |  Type  
---|---|---  
poolDescription |  An optional description of the Simple Failover field. |  String. Less than 255 characters. Optional.  
liveRecordDescription |  An optional description of the live record. |  String. Less than 255 characters. Optional.  
liveRecordState |  Whether or not the live record is currently active. This field is optional for create or update, but is not returned for a list of RRSETS. |  One of either: FORCED_INACTIVE or NOT_FORCED.

  * FORCED_INACTIVE â the backup record should always be returned by a DNS query.
  * NOT_FORCED â the monitor should determine if the live record or the backup record is returned by a DNS query.

  
backupRecord |  Information for the backup record. |  A backupRecord (All Fail) DTO. Required for Simple Failover pools. Ignored for Simple Monitor pools.  
backupRecord/rdata |  BIND data for the backup record. |  IPv4 address or IPv6 address. Required for Simple Failover pools. Ignored for Simple Monitor pools.  
backupRecord/description |  An optional description for the backup record. |  String. Less than 255 characters. Optional for Simple Failover pools. Ignored for Simple Monitor pools.  
monitor |  Information for the monitor. |  A monitor DTO. Required.  
monitor/method |  HTTP method used to connect to the monitored URL. |  One of either GET or POST. Required.  
monitor/url |  Monitored URL. |  A full URL including: protocol, host, and URI. Required.   
Valid protocols are http and https.  
monitor/transmittedData |  If a monitor is sending a POST, the data that is sent as the body of the request. |  String. Less than 255 characters. Optional.  
monitor/searchString |  If supplied, a string that is checked against the returned data from the request. The monitor fails if the searchString is not present. |  String. Less than 255 characters. Optional.  
  
regionFailureSensitivity |  Specifies the sensitivity to the number of regions that need to fail for the backup record to be made active. |  Required. One either LOW or HIGH:

  * LOW â All 4 regions have to fail.
  * HIGH â 2 or more regions have to fail.

  
status |  Ignored if sent on create or update. Returned when list of RRSets is returned. |  One of: OK, CRITICAL, MANUAL

  * OK â Live record is being served.
  * CRITICAL â The backup record is being served due to the monitor detecting a failure.
  * MANUAL â The backup record is being served due to user forcing the live record to be inactive.

  
  
JSON Example: Simple Monitor / Failover Pool Profile

{  
"zoneName": "domain.name.",  
"ownername": "a.domain.name.",  
"rrtype": "A",  
"ttl": 300,  
"rdata": [  
"1.2.3.4",  
],  
"profile": {  
"@context": "http://schema.ultradns.com/SFPool.jsonschema",  
"pooldescription": "Pool description",  
"liveRecordDescription": "Live Record Description",  
"liveRecordState": "FORCED_INACTIVE",  
"backupRecord": {  
"rdata": "5.6.7.8.",  
"description": "backup record description",  
},  
"monitor": {  
"method": "POST",  
"url": "http://www.cnn.com/",  
"transmittedData": "foo=10&bar=20",  
"searchString": "testing",  
}  
"regionFailureSensitivity": "LOW",  
"status": "OK",  
}  
}

  * Simple Monitor / Failover Pools can only be defined for RRSets of type A. 

  * The DNS value of an A record is displayed as a value of 1. For the complete list of DNS values, they can be found here: <https://en.wikipedia.org/wiki/List_of_DNS_record_types>. It is an error to define a Simple Failover Pool for other RRSet types.

  * It is an error to define a Simple Monitor / Failover Pool with any number of records other than one.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create Simple
Monitor / Failover Pools

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/rrsets/{type}/{newPoolName}

**Parameters** : None

**Body** : Must include Simple Failover Pool Profile Fields.

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

JSON Example: Create Simple Monitor / Failover Pool

{  
"zoneName": "domain.name.",  
"ownerName": "a.domain.name.",  
"rrtype": "A",  
"ttl": 300,  
"rdata": [  
"1.2.3.4"  
]  
"profile": {  
"@context": "http://schema.ultradns.com/SFPool.jsonschema",  
"poolDescription": "Pool description",  
"liveRecordDescription": "Live Record description",  
"liveRecordState": "FORCED_INACTIVE",  
"backupRecord": {  
"rdata": "5.6.7.8",  
"description": backup record description"  
},  
"monitor": {  
"method": "POST",  
"url": "http://www.cnn.com/",  
"transmittedData": "foo=10&bar=20",  
"searchString": "testing"  
},  
"regionFailureSensitivity": "LOW"  
}  
}

![](../Resources/Images/Rest-API_User_Guide/Introduction.png) |  Simple Monitor and Simple Failover pools use the same API calls, but you will see a slight difference in the _liverecordstate_. A Simple Monitor pool will display the following: "liveRecordState": "NOT_FORCED" or "NULL".  
---|---  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)List Simple
Monitor / Failover Pools

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/{type}

OR  
  

GET https://api.ultradns.com/zones/{zoneName}/rrsets/?q=kind:SF_POOLS

**Parameters** : Include one of the following:

List Configuration Fields

Value |  Meaning  
---|---  
ALL |  All pools and records (same as RECORDS, POOLS)  
RECORDS |  Only resource records.  
POOLS |  All pools.  
RD_POOLS |  Only RD pools.  
DIR_POOLS |  Only Directional pools.  
SF_POOLS |  Only Simple Monitor / Failover pools.  
SLB_POOLS |  Only Simple Load Balancing Pools  
  
The **q** parameter recognizes an attribute, **kind**. These values must
adhere to the following:

  * These values can be comma-separated.

  * If kind is not specified, it defaults to the value ALL.

**Body** : None.

**Response** : If task completes, Status Code 200 OK is returned with Simple
Failover Pool Profile Fields in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

JSON Example: List Simple Monitor / Failover Pools Sample Response

{  
"zoneName": "primary-example.",  
"rrsets": [  
{  
"ownerName": "sf.primary-exmaple.com",  
"rrtype": "A(1)",  
"ttl": 300  
"rdata": [  
"1.2.3.4"  
]  
"profile": {  
"@context": "http://schema.ultradns.com/SFPool.jsonschema",  
"poolDescription": "Pool description",  
"liveRecordDescription": "Live Record description",  
"backupRecord": {  
"description": "backup record description",  
"rdata": "5.6.7.8"  
},  
"monitor": {  
"method": "POST",  
"url": "http://www.cnn.com/",  
"transmittedData": "foo=10&bar=20",  
"searchString": "testing"  
},  
"regionFailureSensitivity": "LOW"  
"status": "MANUAL",  
}  
}  
]  
"queryInfo": {  
"sort": "OWNER",  
"reverse": false,  
"limit": " 100  
}  
"resultInfo": {  
"totalCount": 1,  
"offset": 0,  
"returnedCount": 1  
}  
}

![](../Resources/Images/Rest-API_User_Guide/Introduction_73x85.png) |  Simple Monitor and Simple Failover pools use the same API calls, but you will see a slight difference in the _liverecordstate_. A Simple Monitor pool will display the following: "liveRecordState": "NOT_FORCED" or "NULL".  
---|---  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update Simple
Monitor / Failover Pools

For full updates (PUT), the Simple Monitor / Failover Pool profile must be
fully specified.

**Method and URI** :

PUT https://api.ultradns.com/zones/{zoneName}/rrsets/{type}/{newPoolName}

**Parameters** : None

**Body** : Must include Simple Failover Pool Profile Fields.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

JSON Example: Update for Simple Monitor / Failover Pools

{  
"zoneName": "domain.name",  
"rrSets": [  
{  
"ownername": "a.domain.name",  
"rrtype": "A (1)",  
"ttl": 300,  
"rdata": [  
"4.3.2.1"  
]  
"profile": {  
"@context": "http://schema.ultradns.com/SFPool.jsonschema",  
"poolDescription": "Pool description",  
"liveRecordDescription": "Live Record description",  
"backupRecord": {  
"description": "backup record description",  
"rdata": "8.7.6.5",  
}  
"monitor": {  
"method": "POST",  
"url": "http://www.cnn.com",  
"transmittedData": "foo=10&bar=20",  
"searchString": "testing"  
}  
"regionFailureSensitivity": "LOW"  
"status": "MANUAL"  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update Simple Monitor / Failover Pools

For partial updates (PATCH) that do not affect the sorting order or pool /
live record, the profile section is not required.

**Method and URI** :

PATCH https://api.ultradns.com/zones/{zoneName}/rrsets/{type}/{newPoolName}

**Parameters** : None

**Body** : Must include Simple Failover Pool Profile Fields.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

JSON Example: Partial Update Simple Monitor / Failover Pools Sample Request
Body

{  
"rdata": [  
"1.1.1.1"  
]  
"profile": {  
"backupRecord": {  
"rdata": "2.2.2.2"  
"description": "backup record description",  
}  
}  
}

### Conversions for Traffic Service Pools

Conversions to and from Simple Monitor / Failover pools are allowed only via
the PUT operation. Conversions via PATCH API are not currently supported for
these pool types.

### Converting existing A records to Simple Monitor / Failover Pools

To convert an existing owner of a single A record to a Simple Monitor /
Failover pool, perform a full update (PUT) and include the profile information
for a Simple Monitor / Failover Pool.

### Converting a Simple Monitor / Failover Pool to an A record

To convert a Simple Monitor / Failover Pool to an owner of a single A record,
perform a full update (PUT) and do not include the profile information. There
can only be a single rdata record specified.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete Simple
Monitor / Failover Pools

**Method and URI** :

DELETE
https://api.ultradns.com/zones/{zoneName}/rrsets/{type}/{ExistingPoolName}

**Parameters** : None.

**Body** : None.

**Response** : If delete happens immediately, Status Code 204 is returned with
no body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid, or you do not have access to it.

  * If you don't have permission to delete the {zoneName}.

  * The {ExistingPoolName} can be either a Fully Qualified Domain Name, or a Relative Domain Name.

