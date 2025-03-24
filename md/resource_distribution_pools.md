

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

# Resource Distribution Pools

Resource Distribution (RD) Pools are used to define rules for returning
multiple A or AAAA records for a given owner name. There are three different
ordering rules possible:

  * Fixed (records appear in the same order all the time).

  * Random (order of the records is random on each request).

  * Round robin (the order of the records changes on each request, in order).

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Profile

All pools are implemented as information added to [Resource Record
Sets](Resource Record Sets.htm) (RRSETS). This additional information is
specified in a section within the label profile. Every profile contains an
entry with the label @context. The value of @context is a URI that uniquely
identifies the type of the pool.

The URI for an RD pool is http://schemas.ultradns.com/RDPool.jsonschema.

The other fields in the profile for an RD pool are:

RD Pool Profile Fields

Field |  Description |  Type  
---|---|---  
order |  The order the records will be returned in. |  From one of: FIXED, RANDOM, ROUND_ROBIN  
description |  An optional description of the RD pool. |  String, less than 255 characters.  If not specified, the owner name for the RRSet will be used.  
  
JSON Example: Resource Distribution Pool

{  
"zoneName": "andria.com",  
"rrsets": [  
{  
"ownerName": "redredrobin.andria.com.",  
"rrtype": "A (1)",  
"ttl": 86400,  
"rdata": [  
"198.16.1.22",  
"192.168.2.56"  
]  
}  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/RDPool.jsonschema",  
"order": "ROUND_ROBIN",  
"description": "T. migratorius"  
},  
"queryInfo": {  
"q": "kind:POOLS",  
"sort": "OWNER",  
"reverse": false,  
"limit": 100  
},  
"resultInfo": {  
"totalCount": 1,  
"offset": 0,  
"returnedCount": 1  
}  
}

RD Pools can only be defined for RRSets of type A (1) or AAAA (28). It is an
error to define an RD Pool for other RRSet types.

Multiple A or AAAA records for a single owner can only be defined if the owner
is a pool. It is an error to define multiple RData for an owner of type A or
AAAA if the owner is not a pool.

It is legal to define an RD Pool with zero or one Rdata records.

The order of the records in the pool is determined by the order in which they
are listed in the rdata array Listing RD Pools. See .

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Listing RD
Pools

RD Pools are listed just like standard resource record sets. As described in
[List RRsets in Zone](Resource Record Sets.htm#_Ref268782776), use the query
operation **kind** for the **q** query parameter to control which resource
record set types are returned.

RD Pool: Kind values

Value |  Meaning  
---|---  
ALL |  All pools and records (same as RECORDS,POOLS)  
RECORDS |  Only resource Records.  
POOLS |  All Pools.  
RD_POOLS |  Only RD Pools.  
  
  * These values can be comma-separated if you wish to specify more than one.

  * If kind is not specified, it defaults to the value ALL.

URL Example: Return all RD Pools in zone andria.com.

https://api.ultradns.com/zones/andria.com/rrsets?q=kind:RD_POOLS

This will return all RD Pools in the zone andria.com.

![](../Resources/Images/Rest-API_User_Guide/Listing_RD_Pools.png)

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Displaying RD
Pools

When an owner that represents an RD Pools is returned, the profile information
must be included.

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/{rrType}/{ownerName}

**Parameters** : None

**Body** : None.

**Response** : If task completes, Status Code 200 OK is returned with  RD Pool
Profile Fields in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If {ownerName} does not exist.

JSON Example: GET RD Pool

{  
"zoneName": "primary-example.com.",  
"rrSets": [  
{  
"ownerName": "rdpool.primarytest.com.primary-example.com.",  
"rrtype": "A (1)",  
"ttl": 300,  
"rdata": [  
"1.2.3.4",  
"2.4.6.8",  
"9.8.7.6"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/RDPool.jsonschema",  
"order": "RANDOM",  
"description": "This is a great RD Pool"  
}  
}  
],  
"queryInfo": {  
"sort": "OWNER",  
"reverse": false,  
"limit": 100  
},  
"resultInfo": {  
"totalCount": 1,  
"offset": 0,  
"returnedCount": 1  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create RD
Pools

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/rrsets/{rrType}/{ownerName}

**Parameters** : None

**Body** : Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288) with RD pool profile info, or a [JSON PATCH
DTO](Making Updates via JSON PATCH.htm#JSON_PATCH_DTO).

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If {ownerName} does not exist.

{  
"ttl": 300,  
"rdata":  
[  
"1.2.3.4",  
"2.4.6.8",  
"9.8.7.6"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/RDPool.jsonschema",  
"order": "RANDOM",  
"description": "This is a great RD Pool"  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update RD
Pools

For partial updates (PATCH) that do not affect the order or description, the
profile section is not required.

For full updates, (PUT) the RD Pool profile must be fully specified.

To change the order of records in the RD Pool, or to remove a record from the
RD Pool, a full update (PUT) must be performed.

To add a record to an existing RD Pool, a partial update (PATCH) can be
performed.

**Method and URI** :

PUT https://api.ultradns.com/zones/{zoneName}/rrsets/{rrType}/{ownerName}

**Parameters** : None

**Body** : Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288) with RD pool profile info, or a [JSON PATCH
DTO](Making Updates via JSON PATCH.htm#JSON_PATCH_DTO).

**Response** : If the task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If the task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If {ownerName} does not exist.

JSON Example: Update RD Pool

{  
  
"ttl": 86400,  
  
"rdata": [  
  
"206.204.52.32",  
  
"216.12.145.20",  
  
"1.2.3.6",  
  
"1.2.3.5"  
  
],  
  
"profile": {  
  
"@context": "http://schemas.ultradns.com/RDPool.jsonschema",  
  
"order": "ROUND_ROBIN",  
  
"description": "www"  
  
}  
  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update RD Pools

**Method and URI** :

PATCH https://api.ultradns.com/zones/{zoneName}/rrsets/{rrType}/{ownerName}

**Parameters** : None

Body: Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288) with RD pool profile info, or a [JSON PATCH
DTO](Making Updates via JSON PATCH.htm#JSON_PATCH_DTO).

**Patchable Objects for RD Pools** :

  * biz.example.ultra.rest.dto.RDPoolProfile

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If {ownerName} does not exist.

  * If you donât have permission to perform a Partial Update of RD Pools.

JSON Example: Partial Update an RD Pool

{  
"ttl": 86400,  
"rdata": [  
"10.10.10.1"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/RDPool.jsonschema",  
"order": "ROUND_ROBIN",  
"description": "www"  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete an RD
Pool

**Method and URI** :

DELETE https://api.ultradns.com/zones/{zoneName}/rrsets/{rrType}/{ownerName}

**Parameters** : None

**Body** : None

**Response** : If delete happens immediately, Status Code 204 is returned with
no body content.

  * If delete happens in the background, a Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.  

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to delete records.

  * If the {rrType} is invalid.

  * If {ownerName} does not exist.

## _Converting To and From RD Pools_  

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Existing A or
AAAA Records to RD Pools

To convert an existing owner of a single A or AAAA record to an RD pool,
perform an update (PUT or PATCH) and include the profile information for an RD
Pool.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Existing RD
Pool to an A or AAAA Record

To convert an RD Pool to an owner of a single A or AAAA record, perform a full
update (PUT) and do not include the profile information. There can only be a
single rdata record specified.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Pool to Pool
Conversions

RD Pools of type A (not AAAA) can be converted to and from SiteBacker (SB) and
Traffic Controller (TC) pools. To convert between pool types, perform an
update (PUT or PATCH) and include the profile information for the appropriate
pool type.

RD Pools cannot be converted to or from Directional pools.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)TTL Records
Consistency in RD Pool Records

Per [RFC 2181](https://tools.ietf.org/html/rfc2181#section-5.2), the Time to
Live (TTL) of all Resource Records in an RRSet must be the same value.
Whenever any existing RD Pool record TTL is modified using a partial update
request, all other existing RD Pool records will also be updated with the
modified TTL value. There will be an audit event for each RD Pool record
modification.

Note: Prior to August 15, 2017 it was possible to modify the TTL of any
existing RD Pool record using partial update request.

Below is an example scenario of the new TTL function for RD pools.

If there is an existing RD pool with two records:

  * Record 1 â Points to 1.1.1.1 with a TTL value of 400

  * Record 2 â Points to 1.2.3.4 with a TTL value of 86400

If the TTL value for Record 1 (1.1.1.1) is updated using the partial update
request to change the value from 400 to 500, then the additional records will
be updated as well. In this scenario, Record 2 (1.2.3.4) will be altered from
a TTL value of 86400 to 500.

JSON Example: Update RD pool TTL value

{  
"ttl": 500,  
"rdata": [  
"1.1.1.1"  
]  
}

