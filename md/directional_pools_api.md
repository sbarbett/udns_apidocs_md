

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

# Directional Pools API

The valid RRType values for directional pools are:

  * A
  * AAAA
  * PTR
  * HINFO
  * MX
  * TXT
  * RP
  * SRV
  * NAPTR
  * SPF

Directional pools can inter-mix CNAME records with either A or AAAA pool
types. You cannot specify a directional pool of type CNAME.

Multiple directional pools with the same owner name and type are not allowed.

With the addition of new parameters added to Directional Pools that include
GeoIP, Force Overlap, and the TTL v2 update, please review the Profile Fields
DTO below carefully to ensure you are using the proper fields in your API
calls.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Directional
Pools Profile

All pools are implemented as additional information added to [Resource Record
Sets](Resource Record Sets.htm#_Ref442345895) (RRSets). This additional
information is specified in a section within the label profile. Every profile
contains an entry with the label @context. The value of @context is a URI that
uniquely identifies the type of the pool.

The URI for a Directional pool is
http://schemas.ultradns.com/DirPool.jsonschema.

The other fields in the profile for a Directional Pool are:

Directional Pool Profile Fields

Field |  Description |  Type  
---|---|---  
description |  An optional description of the Directional pool. |  String, less than 255 characters. If it is not specified, the owner name for the RRSet will be used.  
ignoreECS |  Whether to ignore the EDNSO (which is an extended label type allowing for greater DNS message size) Client Subnet data when available in the DNS request. false = EDNSO data will be used for IP directional routing. true = EDNSO data will not be used and IP directional routing decisions will always use the IP address of the recursive server. Please refer to [RFC6891](https://tools.ietf.org/html/rfc6891), and [RFC7871](https://tools.ietf.org/html/rfc7871). |  Optional. Boolean. Default value is false. Note: Regardless of the value of ignoreECS, conveying the EDNS0 Client Subnet data is not feasible for mixed pools (pools that have both Geo and Source IP selectors). Note: EDNSO data is not used in a directional pool that contains GeoIP and/or Source IP routing.  
conflictResolve |  When there is a conflict between a matching GeoIP group and a matching SourceIP group, this will determine which should take precedence.  
This only applies to a mixed pool (contains both GeoIP and SourceIP data). |  GEO (GeoIP) or IP (SourceIP).  If not specified, defaults to GEO.  
rdataInfo |  One entry for each entry in rdata. The order of the rdata entries matches with the order of the rdataInfo entries. |  Array of maps of rdataInfo structures.  
rdataInfo/allNonConfigured |  Indicates whether or not the associated rdata is used for all non-configured geographical territories and SourceIP ranges. At most, one entry in rdataInfo can have this set to true. If this is set to true, then geoInfo and ipInfo are ignored. |  Boolean â true or false. If not specified, defaults to false.  
rdataInfo/geoInfo |  The GeoIP group associated with the rdata. |  Map of geoInfo structure. Optional.  
rdataInfo/geoInfo/name |  The name of the GeoIP group. |  String. Required.  
rdataInfo/geoInfo/isExistingGroupFromPool |  Determines if the provided code(s) are already defined in an existing GeoIP group, or if they are a new entry. If True, codes are ignored. |  Optional. Default is False. Boolean.  
rdataInfo/geoInfo/forceOverlap |  Determines the behavior if there is an overlap of GeoIP codes between different records of the same pool.  
  
If true, the overlapping codes will be removed from conflicting pool level GeoIP groups that have forceOverlap as false. |  Optional. Default is false.  
Ignored if isExistingGroupFromPool is True.  
rdataInfo/geoInfo/isAccountLevel |  true if this GeoIP group is referring to an account-level GeoIP group, otherwise false.   
If this is true, codes are ignored. |  Boolean. If not specified, defaults to false.  
rdataInfo/geoInfo/codes |  The codes for the geographical territories that make up this group. |  Array of string. See Valid GeoIP Codes for Directional Pools for the valid strings.  
rdataInfo/ipInfo |  The SourceIP group associated with the rdata. |  Map of ipInfo structure. Optional.  
rdataInfo/ipInfo/isExistingGroupFromPool |  Determines if the provided IPs are already defined in an existing SourceIP group, or if they are a new entry. If true, IPs are ignored. |  Optional. Default is false. Boolean.  
rdataInfo/ipInfo/name |  The name of the SourceIP group. |  String. Required.  
rdataInfo/ipInfo/isAccountLevel |  **true** if this SourceIP group is referring to an account-level SourceIP group, otherwise **false**. If this is true, rdataInfo/geoInfo/ codes are ignored. |  Boolean. If not specified, defaults to false.  
rdataInfo/ipInfo/ips |  The list of IP addresses and IP ranges this SourceIP group contains. |  Array of IP addresses. Required if this is not an account-level group.  
rdataInfo/ipInfo/ips/start |  The starting IP address (v4 or v6) for a SourceIP range. If start is present, end must be present as well. CIDR and address must NOT be present. |  IPv4 or IPv6 Address.  
rdataInfo/ipInfo/ips/end |  The ending IP address (v4 or v6) for a SourceIP range. If end is present, start must be present as well. CIDR and address must NOT be present. |  IPv4 or IPv6 Address.  
rdataInfo/ipInfo/ips/cidr |  The CIDR format (IPv4 or IPv6) for an IP address range. If CIDR is present, the start, end, and address must NOT be present. |  IPv4 or IPv6 CIDR format Address.  
rdataInfo/ipInfo/ips/address |  A single IPv4 address. If address is present, the start, end, and CIDR must NOT be present. |  IPv4 or IPv6 Address.  
rdatainfo/ttl |  The Time To Live (in seconds) for the corresponding record in rdata. Must be a value between 0 and 2147483647, inclusive. |  Integer.  
rdatainfo/type |  Returned only on a GET. Indicates the Pool type if the pool type is a subpool. Possible values include: **RD** , **SLB** , **SF** , **SB** , and **TC**. If the Pool type is not a subpool, then the type of pool record will be returned instead. |  String.  
noResponse |  Allows a user to specify certain geographical territories and IP addresses that will get no response if they try to access the directional pool. |  Map of rdataInfo. Optional.  
noResponse/allNonConfigured |  Indicates whether or not âno responseâ is returned for all non-configured geographical territories and IP ranges. This can only be set to true if there is no entry in rdataInfo with allNonConfigured set to true. If this is set to true, then geoInfo and ipInfo are ignored. |  Boolean. Optional.  Defaults to false.  
noResponse/geoInfo |  The GeoIP group associated with the âno responseâ group. |  Map of geoInfo structure. Optional.  
noResponse/geoInfo/name |  The name for the âno responseâ GeoIP group. |  String. Required.  
noResponse/geoInfo/isAccountLevel |  true if the âno responseâ GeoIP group is referring to an account-level GeoIP group, otherwise false.   
If this is true, codes are ignored. |  Boolean. If not specified, defaults to false.  
noResponse/geoInfo/codes |  The codes for the geographical territories that make up the âno responseâ group. |  An array of string.  See  GeoIP Codes for Directional Pools for the valid strings.  
noResponse/ipInfo |  The SourceIP group associated with the âno responseâ group. |  Map of IpInfo. Optional.  
noResponse/ipInfo/name |  The name of the âno responseâ SourceIP group. |  String required.  
noResponse/ipInfo/isAccountLevel |  true if the âno responseâ SourceIP group is referring to an account-level SourceIP group, otherwise false.   
If this is true, IP addresses are ignored. |  Boolean. If not specified, defaults to false.  
noResponse/ipInfo/ips |  The list of IP addresses and IP ranges for the âno responseâ SourceIP group. |  Array of IP structures. Required if this is not an account-level group.  
noResponse/ipInfo/ips/start |  The starting IP address (IPv4 or IPv6) for an IP range. If start is present, end must be present as well. CIDR and address must NOT be present. |  IPv4 or IPv6 Address.  
noResponse/ipInfo/ips/end |  The ending IP address (IPv4 or IPv6) for an IP address range. If end is present, start must be present as well. CIDR and address must NOT be present. |  IPv4 or IPv6 Address.  
noResponse/ipInfo/ips/cidr |  The CIDR format (IPv4 or IPv6) for an IP address range. If CIDR is present, start, end, and address must NOT be present. |  IPv4 or IPv6 CIDR format Address.  
noResponse/ipInfo/ips/address |  A single IPv4 or IPv6 address. If an IP address is present, start, end, and CIDR must NOT be present. |  IPv4 or IPv6 Address.   
  
JSON Example: Directional Pool RRSet with Profile

{  
"zoneName": "domain.name.",  
"ownerName": "pool.domain.name.",  
"rrtype": "A",  
"ttl": 300,  
"type":  
"rdata": [  
"1.2.3.4",  
"a.domain.name.",  
"9.8.7.6",  
"30.40.50.60"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"description": "Description of pool",  
"conflictResolve": "GEO",  
"ignoreECS": true,  
"rdataInfo": [  
{  
"allNonConfigured": true  
},  
{  
"geoInfo": {  
"name": "North America",  
"codes": [ "US", "CA", "MX"]  
}  
},  
{  
"ipInfo": {  
"name": "some Ips",  
"ips": [  
{  
"start": "200.20.0.1",  
"end": "200.20.0.10"  
},  
{  
"cidr": "20.20.20.0/24"  
},  
{  
"address": "50.60.70.80"  
}  
]  
}  
},  
{  
"geoInfo": {  
"name": "accountGeoGroup",  
"isAccountLevel": true  
},  
"ipInfo": {  
"name": "accountIPGroup",  
"isAccountLevel": true  
}  
}  
],  
"noResponse": {  
"geoInfo": {  
"name": "nrGeo",  
"codes": ["Z4"]  
},  
"ipInfo": {  
"name": "nrIP",  
"ips": [  
{  
"address": "197.231.41.3"  
}  
]  
}  
}  
}

JSON Example: Add Existing Global Group to a Directional Pool

The following JSON example outlines how a Global Directional Group can be
added to a Directional Pool for more than one record. To do this, the local
group name must be provided in the group name, and the **isAccountLevel** and
**isExistingGroupFromPool** parameters must be set to true. In the following
example, first record is the allNonConfigured record, the second record is
assigned to global group "groupName,â and the third record is being assigned
the same global group again in the pool.

JSON Example: Add Existing Global Group to a Directional Pool ```json {
"ownerName": "pool-zone.com.", "rrtype": "SRV (33)", "rdata": [ "1 11 12
target1.com", "2 2 2 target2.com", "3 2 2 target3.com" ], "profile": {
"@context": "http://schemas.ultradns.com/DirPool.jsonschema", "description":
"srv", "rdataInfo": [ { "allNonConfigured": true, "ttl": 86400, "type": "SRV"
}, { "geoInfo": { "name": "groupName", "isAccountLevel": true }, "ttl": 86400,
"type": "SRV" }, { "geoInfo": { "name": "groupName", "isAccountLevel": true,
"isExistingGroupFromPool": true }, "ttl": 86400, "type": "SRV" } ] } } ```

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Configuring
GeoIP and Source IP Together

Depending on your needs to configure your directional pool records, you may
opt to combine a Source IP group and a GeoIP group together into one
directional record. When you do so, the record gets selected only when BOTH
the Source IP and GeoIP restrictions are satisfied. For example:

POST  
{  
"ownerName": "and.000geoiptest.net.",  
"rrtype": "A (1)",  
"rdata": [  
"1.1.1.1",  
"2.2.2.2"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"rdataInfo": [  
{  
"allNonConfigured": true  
},  
{  
"geoInfo": {  
"name": "br",  
"codes": [  
"BR"  
]  
},  
"ipInfo": {  
"name": "some Ips",  
"ips": [  
{  
"start": "200.20.0.1",  
"end": "200.20.0.10"  
}  
]  
}  
}  
]  
}  
}

The directional record 2.2.2.2 above will be selected only if you are in
Brazil, AND your Source IP is within the range [200.20.0.1 â 200.20.0.10].
However, if you were coming from Brazil, but your Source IP was 200.20.0.55
(outside of the range), the All Non-Configured resolution of 1.1.1.1 would be
chosen.

Similarly, if using the above example, the Source IP range of 200.20.0.1 â
200.20.0.10 no longer resided in Brazil, and the userâs IP Address was
coming from 200.20.0.1, the resolution would once again choose the All Non-
Configured record of 1.1.1.1 because you did not satisfy both the GeoIP and
Source IP restrictions.

If you continue to receive the All Non-Configured response when combining
GeoIP and Source IP, verify you satisfy both of the restrictions.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)TTL Update

The Time to Live (TTL) for Directional Pools can optionally be set at the
record level via PUT, POST and PATCH calls. The GET call will return record
level TTL values for Directional Pools.  
  

![](../Resources/Images/Rest-API_User_Guide/Introduction_55x63.png) |  Sub Pool TTLs cannot be updated using the TTL optional field.  
---|---  
  
The priority of the TTL display will act as follows for POST, PUT and PATCH
calls:

  * If provided, the Record level TTL will take priority over the Pool TTL. 

  * If no record TTL is provided, the Pool level TTL will be used for both Record and Pool TTLs.

  
**NOTE** : The RESTAPI does not validate the compatibility of a pool or a pool
recordâs TTL versus that of a sub-pool or a sub-poolâs record TTL. A sub-
poolâs TTL value will take precedence over the controlling (parent) poolâs
TTL value.

For example, if you were to create a Directional pool named dir.example.com
that contained a record named sb.example.com which points to a SiteBacker
pool, then the TTL for the Sitebacker pool records will take precedence and be
used upon resolution of the dir.example.com pool. The TTL(s) of the
Directional pool records will be ignored upon resolution, but still accessible
and able to be updated by the REST API.

Below are various JSON examples depicting the hierarchy of TTLs per record
type / pool type.

JSON Example: Determining the TTL of a pool record

**Step 1** : Create (POST) a SiteBacker Pool with TTL of 180

{  
"ownerName": "sb.000geoiptest.net.",  
"rrtype": "A (1)",  
"ttl": 180,  
"rdata": [  
"1.1.1.1"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/SBPool.jsonschema",  
"description": "sb.000geoiptest.net.",  
"runProbes": true,  
"actOnProbes": true,  
"order": "ROUND_ROBIN",  
"maxActive": 1,  
"maxServed": 0,  
"rdataInfo": [  
{  
"state": "NORMAL",  
"runProbes": true,  
"priority": 1,  
"failoverDelay": 0,  
"threshold": 1  
}  
]  
}

**Step 2** : Create (POST) a Directional Pool with the previous SiteBacker
Pool as a Subpool, and the Directional Pool has a TTL of 1500.

{  
"ownerName": "dir.000geoiptest.net.",  
"rrtype": "A (1)",  
"rdata": [  
"sb.000geoiptest.net."  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"description": "dir.000geoiptest.net.",  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "na",  
"codes": [  
"NAM"  
]  
},  
"ttl": 1500  
}  
]  
}  
}  

The âdir.000geoiptest.netâ resolves to 1.1.1.1 and with a TTL of 180.  
  
**Step 3** : Perform a GET of the SiteBacker Pool shows the TTL of 180.

{  
"zoneName": "000geoiptest.net",  
"rrSets": [  
{  
"ownerName": "sb.000geoiptest.net.",  
"rrtype": "A (1)",  
"ttl": 180,  
"rdata": [  
"1.1.1.1"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/SBPool.jsonschema",  
"description": "sb.000geoiptest.net.",  
"runProbes": true,  
"actOnProbes": true,  
"order": "ROUND_ROBIN",  
"maxActive": 1,  
"maxServed": 0,  
"rdataInfo": [  
{  
"state": "NORMAL",  
"runProbes": true,  
"priority": 1,  
"failoverDelay": 0,  
"threshold": 1,  
"availableToServe": true,  
}  
]  
}  
}  
]

**Step 4** : Perform a GET of the Directional Pool shows the TTL of 1500.

{  
"zoneName": "000geoiptest.net",  
"rrSets": [  
{  
"ownerName": "dir.000geoiptest.net.",  
"rrtype": "A (1)",  
"rdata": [  
"sb.000geoiptest.net."  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"description": "dir.000geoiptest.net.",  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "na",  
"codes": [  
"NAM"  
]  
},  
"ttl": 1500,  
"type": "SB"  
}  
]  
}  
}  
],

**Step 5** : Update (PUT) the TTL of the Directional Pool to 1600.

{  
"ownerName": "dir.000geoiptest.net.",  
"rrtype": "A (1)",  
"rdata": [  
"sb.000geoiptest.net."  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"rdataInfo": [  
{  
"ttl": 1600  
}  
]  
}  
}

**Step 6** : Update (PUT) the TTL of the SiteBacker Pool to 200.

{  
"ownerName": "sb.000geoiptest.net.",  
"rrtype": "A (1)",  
"ttl": 200,  
"profile": {  
"@context": "http://schemas.ultradns.com/SBPool.jsonschema"  
}  
}

The âsb.000geoiptest.netâ resolves with a TTL of 200.  
Then the âdir.000geoiptest.netâ resolves with a TTL of 200.

  
**Step 7** : Perform a GET of the SiteBacker Pool shows a TTL of 200.

{  
  
"zoneName": "000geoiptest.net",  
  
"rrSets": [  
  
{  
  
"ownerName": "sb.000geoiptest.net.",  
  
"rrtype": "A (1)",  
  
"ttl": 200,  
  
"type": SB,  
  
"rdata": [  
  
"1.1.1.1"  
  
],  
  
"profile": {  
  
"@context": "http://schemas.ultradns.com/SBPool.jsonschema",  
  
"description": "sb.000geoiptest.net.",  
  
"runProbes": true,  
  
"actOnProbes": true,  
  
"order": "ROUND_ROBIN",  
  
"maxActive": 1,  
  
"maxServed": 0,  
  
"rdataInfo": [  
  
{  
  
"state": "NORMAL",  
  
"runProbes": true,  
  
"priority": 1,  
  
"failoverDelay": 0,  
  
"threshold": 1,  
  
"availableToServe": true  
  
}  
  
]  
  
}  
  
}  
  
],

**Step 8** : Perform a GET of the Directional Pool shows a TTL of 1800.

{  
"zoneName": "000geoiptest.net",  
"rrSets": [  
{  
"ownerName": "dir.000geoiptest.net.",  
"rrtype": "A (1)",  
"rdata": [  
"sb.000geoiptest.net."  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"description": "dir.000geoiptest.net.",  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "na",  
"codes": [  
"NAM"  
]  
},  
"ttl": 1600,  
"type": "SB"  
}  
]  
}  
}  
],

![](../Resources/Images/Rest-API_User_Guide/Introduction_56x65.png) |  The above steps are used as an example to depict the differences in how a TTL will be displayed / applied to a pool, which take into consideration whether the pool is a subpool, and in what order the records are resolved.  
---|---  
  
The following examples demonstrate the difference between the /v1/ and the
current version usages in the REST API.

JSON Example: REST API /v1/ TTL Response only at the Pool Level

"zoneName": "restapi.test.com",  
"rrSets": [  
{  
"ownerName": "ttl.test.biz",  
"rrtype": "A (1)",  
"ttl": 1000,  
"type":  
"rdata": [  
"212.82.0.6"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"description": "ttl.test.biz",  
"conflictResolve": "GEO",  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "g42",  
"codes": [  
"AR",  
"BO",  
"BR",  
"CL",  
"CO",  
"EC",  
"FK",  
"GF",  
"GS",  
"GY",  
"PE",  
"PY",  
"SR",  
"U4",  
"UY",  
"VE"  
]  
},  
"type": "A"  
}  
]  
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

JSON Example: REST API Current version TTL Response at Record Level

"zoneName": "restapi.test.com",  
"rrSets": [  
{  
"ownerName": "ttl.test.biz",  
"rrtype": "A (1)",  
"rdata": [  
"212.82.0.6"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"description": "ttl.test.biz",  
"conflictResolve": "GEO",  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "g42",  
"codes": [  
"SAM"  
]  
},  
"ttl": 1000,  
"type": "A"  
}  
]  
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

## Force Overlap

Force Overlap is a parameter that is only applicable for GeoIP data. This
parameter determines the behavior if there is an overlap of GeoIP codes
between different records of the same pool. If the value is True, the
overlapping codes will be removed from conflicting pool level GeoIP groups
that have forceOverlap set to False.  
  
For example, if pool record A is existing and set up for âAsiaâ and
âNorth America,â and record B is added to the same pool with âNorth
Americaâ and âAfricaâ with forceOverlap set to True, the resulting pool
will display âAsiaâ for record A, and âNorth Americaâ and âAfricaâ
for record B.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create a
Directional Pool

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/rrsets/{rrType}/{ownerName}

**Parameters** : None

**Body** : Must contain Directional Pools API.

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If {ownerName} does not exist.

JSON Example: Create Directional Pool with GeoIP location data

{  
"ownerName": "Myaccount",  
"rdata": [  
"txt1","txt2"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "gr1", "codes": ["ASI", "AFR"]  
}  
},  
{  
"geoInfo": {  
"name":"gr1",  
"isExistingGroupFromPool": true,  
"codes":["ANT"]  
}  
}  
]  
}  
}

JSON Example: Create Directional Pool with ignoreECS flag enabled

{  
"ownerName": "dir-ignoreECS",  
"rdata": [  
"txt1","txt2"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"ignoreECS": true,  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "gr1", "codes": ["ASI", "AFR"]  
}  
},  
{  
"geoInfo": {  
"name":"gr1",  
"isExistingGroupFromPool": true,  
"codes":["ANT"]  
}  
}  
]  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get a
Directional Pool

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/TXT/{ownerName}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with
Directional Pools Profile DTO details in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If {ownerName} does not exist.

JSON Example: Get a Directional Pool with Force Overlap enabled

{  
"zoneName": "ForceOverlap.biz",  
"rrSets": [  
{  
"ownerName": "MyAccount",  
"rrtype": "TXT (16)",  
"type:"  
"rdata": [  
"\"txt1\"",  
"\"txt2\""  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"description": "MyAccount",  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "gr1",  
"codes": [  
"AFR",  
"ASI"  
]  
},  
"ttl": 86400,  
"type": "TXT"  
},  
{  
"geoInfo": {  
"name": "gr1",  
"codes": [  
"AFR",  
"ASI"  
]  
},

JSON Example: Get a Directional Pool with ignoreECS flag enabled

{  
"zoneName": "NewDirPool.biz",  
"rrSets": [  
{  
"ownerName": "dir-ignoreECS",  
"rrtype": "TXT (16)",  
"type:"  
"rdata": [  
"txt1",  
"txt2"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"description": "dir-ignoreECS.NewDirPool.biz",  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "gr1",  
"codes": [  
"AFR",  
"ASI"  
]  
},  
"ttl": 3900,  
"type": "TXT"  
},  
{  
"geoInfo": {  
"name": "gr2",  
"codes": [  
"ANT",  
"EUR"  
]  
},  
"ttl": 3900,  
"type": "TXT"  
}  
]  
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

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get All
Directional Pools

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/?q=kind:DIR_POOLS

**Parameters** : None

**Body** : None.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If {ownerName} does not exist.

![](../Resources/Images/Rest-API_User_Guide/Introduction_57x66.png) |  Users should provide a maximum limit of 1000 when requesting to get all Directional pools. If the limit is greater than 1000, the following error message will be returned:  
---|---  
  
{  
errorCode: 22000  
errorMessage: "Invalid Page Limit, the maximum number of records that can be
retrieved are restricted to 1000."  
}

![](../Resources/Images/Rest-API_User_Guide/Introduction_58x67.png) |  In order to acquire more than 1,000 records (if necessary), you can change the offset and limit parameters to satisfy the record range you are seeking. For example, to get records 2,001 through 3,000 change offset=2000&limit=1000.  
---|---  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update a Directional Pool

**Method and URI** :

PATCH https://api.ultradns.com/zones/{zoneName}/rrsets/{rrType}/{ownerName}

Parameters: None

**Body** : Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288) with a Directional pool profile info, or a [JSON PATCH
DTO](Making Updates via JSON PATCH.htm#JSON_PATCH_DTO).

Patchable Objects for DIR Pool:

  * biz.example.ultra.rest.dto.DirectionalPoolProfile

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If {ownerName} does not exist.

  * If you donât have permission to partial update DIR Pools.

  * If patch operation is not allowed for the given json pointer value.

JSON Example: Partial Update a Directional Pool with GeoIP location enabled

{  
"ownerName": "ForceOverlap.biz",  
"rdata": [  
"txt2"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"rdataInfo": [  
{  
"geoInfo": {  
"name":"gr2", "codes":["ANT", "EUR", "ASI"],  
"forceOverlap": true  
}  
}  
]  
}  
}

JSON Example: Partial Update a Directional Pool with ignoreECS flag enabled

{  
"ownerName": "dir-ignoreECS",  
"rdata": [  
"txt2"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"ignoreECS": false,  
"rdataInfo": [  
{  
"geoInfo": {  
"name":"gr2", "codes":["ANT", "EUR", "ASI"],  
"forceOverlap": true  
}  
}  
]  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Directional Pools

**Method and URI** :

PUT https://api.ultradns.com/zones/{zoneName}/rrsets/{rrType}/{ownerName}

**Parameters** : None

**Body** : Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288) with a Directional pool profile info, or a [JSON PATCH
DTO](Making Updates via JSON PATCH.htm#JSON_PATCH_DTO).

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If {ownerName} does not exist.

  * If you donât have permission to partial update DIR Pools.

  * If a CNAME already exists for the owernName.

![](../Resources/Images/Rest-API_User_Guide/Introduction_64x75.png) |  The âUpdate Directional Poolsâ API call can be used to convert a Directional Pool to a Resource Record, as long as a CNAME does not already exist for the ownerName.  
---|---  
  
![](../Resources/Images/Rest-API_User_Guide/Introduction_64x75.png) |  Users can delete a specific record from a DIR pool by sending a PUT request without providing that record in the input.  
---|---  
  
JSON Example: Update Directional Pool with GeoIP location

{  
"ownerName": ForceOverlap.biz",  
"rdata": [  
"txt1","txt2"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "gr1", "codes": ["ASI", "AFR"]  
}  
},  
{  
"geoInfo": {  
"name":"gr2", "codes":["ANT", "EUR"]  
}  
}  
]  
}  
}

JSON Example: Update Directional Pool with ignoreECS flag

{  
"ownerName": "dir-ignoreECS",  
"rdata": [  
"txt1","txt2"  
],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"ignoreECS": true,  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "gr1", "codes": ["ASI", "AFR"]  
}  
},  
{  
"geoInfo": {  
"name":"gr2", "codes":["ANT", "EUR"]  
}  
}  
]  
}  
}

## **Converting to a Resource Record**

**Existing DIR Pool to Resource Record**

To convert an existing owner of a DIR Pool to a Resource Record, perform a
full update (PUT) and _do not_ include the profile information.

  * If a CNAME already exists for the ownerName, an error will occur.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Valid GeoIP
Codes for Directional Pools

The REST API follows the ISO-3661-1 standard to specify the names of
countries. REST API is using the Alpha-2 (two letter) code format. The
ISO-3166-2:US standard is used to represent US states and territories, and the
ISO-3166-2:CA standard is used to represent Canadian provinces and
territories.

Any geographic location can be included in any directional pool record. The
pool record with the most specific geographic location will take precedence
when matching the IP address to the location. The State / Province takes
precedence over country, which takes precedence over continent. For example,
an IP address originating in Virginia, USA, and North America would select the
âVirginiaâ record over the USA or North America location. If there is no
âVirginiaâ record defined, the next most specific match would then be USA.

For a comprehensive list of sub-country codes recognized by the REST API,
please refer to the [Geo-IP ISO Code
Guide](file:///C:\\Users\\backerma\\AppData\\Local\\Microsoft\\Windows\\Portal-
Static\\static\\docs\\Geo_IP_ISO_Codes.xlsx)(which can also be found on the
Support page of the Ultradns Portal), or use the GET GeoIP
Territories(geoip/territories) end point. In most instances, the sub country
codes recognized by the REST API for a given country (XX) will be a full set,
or a sub set of the ISO-3166-2:XX standard for that country.

![](../Resources/Images/Rest-API_User_Guide/Introduction_66x77.png) |  REST API will utilize localized spelling for State/Province names. For example, the state of Tuscany in Italy will be identified as âToscana.â  
---|---  
  
In addition, other non-standard codes have been defined to represent other
geographical areas, as well as DNS records that don't fall into geographical
territories:

GeoIP Codes for Directional Pools

Code |  Meaning |  Equivalent ISO codes  
---|---|---  
A1 |  Anonymous Proxy |  None  
A2 |  Satellite Provider |  None  
A3 |  Unknown / Uncategorized IPs |  None  
NAM |  North America (including Central America and the Caribbean) |  AG,AI,AN,AW,BB,BL,BM,BQ,BS,BZ,CA,CR,CU,CW,DM,DO,GD,GL,GP,GT,HN,HT,JM,KN,KY,LC,MF,MQ,MS,MX,NI,PA,PM, PR,SV,SX,TC,TT,U3,US,VC,VG,VI  
SAM |  South America |  AR,BO,BR,CL,CO,EC,FK,GF,GS,GY,PE,PY,SR,U4,UY,VE  
EUR |  Europe |  AD,AL,AM,AT,AX,AZ,BA,BE,BG,BY,CH,CZ,DE,DK,EE,ES,FI,FO,FR,GB,GE,GG,GI,GR,HR,HU,IE,IM,IS,IT,JE,LI,LT,LU,LV,MC, MD,ME,MK,MT,NL,NO,PL,PT,RO,RS,SE,SI,SJ,SK,SM,U5,UA, VA  
AFR |  Africa |  AO,BF,BI,BJ,BW,CD,CF,CG,CI,CM,CV,DJ,DZ,EG,EH,ER,ET,GA,GH,GM,GN,GQ,GW,KE,KM,LR,LS,LY,MA,MG,ML,MR,MU,MW, MZ,NA,NE,NG,RE,RW,SC,SD,SH,SL,SN,SO,SS,ST,SZ,TD,TG,TN,TZ,U7,UG,YT,ZA,ZM,ZW  
ASI |  Asia (including Middle East and the Russian Federation) |  AE,AF,BD,BH,BN,BT,CN,CY,HK,ID,IL,IN,IO,IQ,IR,JO,JP,KG,KH,KP,KR,KW,KZ,LA,LB,LK,MM,MN,MO,MV,MY,NP,OM,PH,PK,PS, QA,RU,SA,SG,SY,TH,TJ,TL,TM,TR,TW,U6,U8,UZ,VN,YE  
OCN |  Australia / Oceania |  AS,AU,CC,CK,CX,FJ,FM,GU,HM,KI,MH,MP,NC,NF,NR,NU,NZ,PF,PG,PN,PW,SB,TK,TO,TV,U9,UM,VU,WF,WS  
ANT |  Antarctica |  AQ, TF, BV  
Legacy Codes (To be deprecated in the future)  
US-U1 |  Undefined United States |   
CA-U2 |  Undefined Canada |   
U3 |  Undefined Central America |   
U4 |  Undefined South America |   
U5 |  Undefined Europe |   
U6 |  Undefined Middle East |   
U7 |  Undefined Africa |   
U8 |  Undefined Asia |   
U9 |  Undefined Australia / Oceania |   
Z1 |  The Caribbean |  AI, AG, AW, BS, BB, BM, VG, KY, CU, DM, DO, GD, GP, HT, JM, MQ, MS, AN, PR, BL, MF, VC, KN, LC, TT, TC, VI  
Z2 |  Central America |  BZ, CR, SV, GT, HN, NI, PA, U3  
Z3 |  South America |  AR, BO, BR, CL, CO, EC, FK, GF, GY, PY, PE, GS, SR, U4, UY, VE  
Z4 |  Europe |  AX, AL, AD, AM, AT, AZ, BY, BE, BA, BG, HR, CZ, DK, EE, FO, FI, FR, GE, DE, GI, GR, GG, HU, IS, IE, IM, IT, JE, LV, LI, LT, LU, MK, MT, MD, MC, ME, NL, NO, PL, PT, RO, SM, RS, SK, SI, ES, SJ, SE, CH, UA, U5, GB, VA  
Z5 |  Middle East |  AF, BH, CY, IR, IQ, IL, JO, KW, LB, OM, PS, QA, SA, SY, TR, U6, AE, YE  
Z6 |  Africa |  DZ, AO, BJ, BW, BF, BI, CM, CV, CF, TD, KM, CG, CI, CD, DJ, EG, GQ, ER, ET, GA, GM, GH, GN, GW, KE, LS, LR, LY, MG, MW, ML, MR, MU, YT, MA, MZ, NA, NE, NG, RE, RW, ST, SN, SC, SL, SO, ZA, SH, SD, SZ, TZ, TG, TN, UG, U7, EH, ZM, ZW  
Z7 |  Asia (Excluding Middle East and the Russian Federation) |  BD, BT, IO, BN, KH, CN, HK, IN, ID, JP, KZ, KP, KR, KG, LA, MO, MY, MV, MN, MM, NP, PK, PH, SG, LK, TW, TJ, TH, TL, TM, U8, UZ, VN  
Z8 |  Australia / Oceania |  AS, AU, CX, CC, CK, FJ, PF, GU, HM, KI, MH, FM, NR, NC, NZ, NU, NF, MP, PW, PG, PN, WS, SB, TK, TO, TV, U9, VU, WF  
Z9 |  Antarctica |  AQ, TF, BV  
  
![](../Resources/Images/Rest-API_User_Guide/Introduction_57x66.png) |  Using the ISO code US is equivalent to all the codes in ISO-3166-2:US, except for the outlying territories which include American Samoa, Guam, Northern Mariana Islands, Puerto Rico, and the Virgin Islands, plus US-U1.In addition to the ISO-3166-2:US codes, there are 3 Armed Forces Designations included: US-AA, US-AE, and US-AP. Similarly, the ISO code CA is equivalent to ISO-3166-2:CA plus CA-U2.  
---|---  
  
  
To ensure the backward compatibility of existing customer verification
scripts, GeoIP Codes returned by a GET /v1 endpoint will match the behavior of
the REST API before the August 2016 update. Customers using the /v1/ GeoIP
Codes are encouraged to switch to the new code format.

Deprecated ISO Codes below contains GeoIP Codes for which the past behavior of
the REST API is preserved in the /v1 versions of the corresponding GET
endpoints. For example, if you create a directional record for South America,
the result returned by the corresponding /v1 GET endpoint would list all of
the eight country codes associated with South America, as opposed to a single
GeoIP code âSAMâ that corresponds to the continent of South America as a
whole.

Deprecated ISO Codes

ISO Code |  Description  
---|---  
US |  United States  
CA |  Canada  
Z3 / SAM |  South America  
Z4 / EUR |  Europe  
Z6 / AFR |  Africa  
Z8 / OCN |  Australia  
Z9 / ANT |  Antarctica  
GL |  Greenland  
PM |  Saint Pierre and Miquelon  
  
JSON Example: /v1/ ISO Code Example

"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"description": "restapi.test.com",  
"conflictResolve": "GEO",  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "g42",  
"codes": [  
"AR",  
"BO",  
"BR",  
"CL",  
"CO",  
"EC",  
"FK",  
"GF",  
"GS",  
"GY",  
"PE",  
"PY",  
"SR",  
"U4",  
"UY",  
"VE"  
]  
}  
}  
]  
}

JSON Example: Current version ISO Code Example

"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"description": "restapi.test.com",  
"conflictResolve": "GEO",  
"rdataInfo": [  
{  
"geoInfo": {  
"name": "g42",  
"codes": [  
"SAM"  
]  
},  
}  
]  
}  
]

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Parent /
Child Territories Overlap

With the rollout of the Global State Level GeoIP feature, any geographic
location can be included in any directional pool record. The pool record with
the most specific geographic location will take precedence when matching the
IP address to the correlating location.

Previously, it would not have been possible to have the state of Virginia (US-
VA) in one record, and the country of United States (US) in another record in
the same pool. The system would have forced the exclusion of the state of
Virginia from the second record, effectively replacing the United States (US)
with the list of remaining states (all excluding Virginia).

JSON Example: Parent / Child Territory Overlap

POST /zones/{zoneName}/rrsets/A/{poolName}  
{  
"rdata": ["1.1.1.1","1.1.1.2","1.1.1.3"],  
"profile": {  
"@context": "http://schemas.ultradns.com/DirPool.jsonschema",  
"rdataInfo": [  
{"geoInfo": {"name": "g1", "codes":["MX-MEX"]}},  
{"geoInfo": {"name": "g2", "codes":["MX"]}},  
{"geoInfo": {"name": "g3", "codes":["NAM"]}}  
]  
}  
}

The above JSON Example demonstrates that if the source IP is in the
âStateâ of Mexico, the resolution is 1.1.1.1. If the source IP is in any
other part of the country of Mexico, the resolution is 1.1.1.2. If the source
IP is in any other part in North America, the resolution is 1.1.1.3. In this
example, there is no overlap.

The new GeoIP model will allow for various Parent/Child overlaps. You can now
have a record with the state of Virginia, another record for the U.S., and
still another record for all of North America.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)GET GeoIP
Territories

GET https://api.ultradns.com/geoip/territories

Parameters:

Parameter |  Description |  Type  
---|---|---  
  
**codes** |  Comma-separated list of one or more territories. You can pass an empty string for a top level return (continents only returned). You can pass a three-letter continent code (refer to the spreadsheet for a complete list of GeoIP ISO codes) for a continent. You can drill down further by passing a continent code dash separated (-) ISO-3166 country code for a country (NAM-MX). |  String.  
  
### Territory DTO

GeoIP Territory DTO

Field |  Description |  Type  
---|---|---  
name |  Name of the territory. |  String  
code |  GeoIP Code assigned to the territory. (Reference Excel Spreadsheet) |  String  
type |  One of the following: Territory (Continent), Country, State. |  String  
id |  Integer used for internal numeric id to represent the territory. |  Integer  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a list
of Territory DTO elements for each comma-separated code from the input
parameter in the body content.

**Errors** : An error will be returned under the following conditions:

  * A duplicate Continent/Country code was provided.

  * The return contains more than 100 records.

  * The ISO code provided is a non-existent ISO code.

JSON Example: GeoIP Current version Territory Empty String Return

GET https://api.ultradns.com/geoip/territories?codes=  
{  
"name": "Anonymous Proxy",  
"code": "A1",  
"type": "Country",  
"id": 315  
},  
{  
"name": "Satellite Provider",  
"code": "A2",  
"type": "Country",  
"id": 316  
},  
{  
"name": "Unknown / Uncategorized IPs",  
"code": "A3",  
"type": "Country",  
"id": 331  
},  
{  
"name": "North America",  
"code": "NAM",  
"type": "Region",  
"id": 338  
},  
{  
"name": "South America",  
"code": "SAM",  
"type": "Region",  
"id": 337  
},  
{  
"name": "Europe",  
"code": "EUR",  
"type": "Region",  
"id": 336  
},  
{  
"name": "Africa",  
"code": "AFR",  
"type": "Region",  
"id": 332  
},  
{  
"name": "Asia",  
"code": "ASI",  
"type": "Region",  
"id": 334  
},  
{  
"name": "Australia / Oceania",  
"code": "OCN",  
"type": "Region",  
"id": 335  
},  
{  
"name": "Antarctica",  
"code": "ANT",  
"type": "Region",  
"id": 333  
}  
]  
]

JSON Example: GeoIP Current version with 2 Territories comma-separated

GET https://api.ultradns.com/geoip/territories?codes=ANT,EUR-AD  
[  
[  
{  
"name": "Antarctica",  
"code": "AQ",  
"type": "Country",  
"id": 330  
},  
{  
"name": "Bouvet Island",  
"code": "BV",  
"type": "Country",  
"id": 297  
},  
{  
"name": "French Southern Territories",  
"code": "TF",  
"type": "Country",  
"id": 298  
}  
],  
[  
{  
"name": "Andorra La Vella",  
"code": "07",  
"type": "State",  
"id": 351  
},  
{  
"name": "Canillo",  
"code": "02",  
"type": "State",  
"id": 346  
},  
{  
"name": "Encamp",  
"code": "03",  
"type": "State",  
"id": 347  
},  
{  
"name": "Escaldes-Engordany",  
"code": "08",  
"type": "State",  
"id": 352  
},  
{  
"name": "La Massana",  
"code": "04",  
"type": "State",  
"id": 348  
},  
{  
"name": "Ordino",  
"code": "05",  
"type": "State",  
"id": 349  
},  
{  
"name": "Sant Julia De Loria",  
"code": "06",  
"type": "State",  
"id": 350  
}  
]  
]

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get All
Account-level GeoIP Groups

Retrieve a list of all configured account-level GeoIP directional groups for a
specified GeoIP code, for a particular account.

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/dirgroups/geo

**Parameters** :

GeoIP AccountList Parameters

Parameter |  Description |  Type  
---|---|---  
q |  The query used to construct the list. Query operators are name, which is a substring match for any GeoIP group name. |  String  
offset |  The position in the list for the first returned element (0 based). The default value is â0â. |  Integer  
limit |  The maximum number of rows requested. The default value is 100. |  Integer  
sort |  The sort column used to order the list. Valid values are NAME. |  String  
reverse |  Whether the list is ascending (false) or descending (true). The default value is false. |  Boolean  
  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
Account-Level GeoIP Directional Group List DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If {accountName} is not valid, or not an {accountName} you have access to.

  * If you don't have permission to read account-level groups.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get All
Account-level SourceIP Groups

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/dirgroups/ip

**Parameters** :

IP AccountList Parameters

Parameter |  Description |  Type  
---|---|---  
q |  The query used to construct the list. Query operators are name, which is a substring match for any IP group name. |  String  
offset |  The position in the list for the first returned element (0 based). The default value is â0â. |  Integer  
limit |  The maximum number of rows requested. The default value is â100â. |  Integer  
sort |  The sort column used to order the list. Valid values are âNAMEâ. |  String  
reverse |  Whether the list is ascending (false) or descending (true). The default value is false. |  Boolean  
  
**Body** : None

**Response** : If task completes, Status Code 200 is returned with an Account-
Level IP Directional Group List DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If {accountName} is not valid, or not an {accountName} you have access to.

  * If you don't have permission to read account-level groups.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get an
Account-level GeoIP Group

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/dirgroups/geo/{name}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
Account-Level GeoIP Directional Group DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If {accountName} is not valid, or not an {accountName} you have access to.

  * If you don't have permission to read account-level directional groups.

  * If {name} is not the name of an account-level GeoIP directional group.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get an
Account-level SourceIP Group

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/dirgroups/ip/{name}

**Parameters** : None.

**Body** : None.

**Response** : If task completes, Status Code 200 is returned with an Account-
Level SourceIP Directional Group DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If {accountName} is not valid, or not an {accountName} you have access to.

  * If you don't have permission to read account-level directional groups.

  * If {name} is not the name of an account-level IP directional group.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create an
Account-level GeoIP Group

**Method and URI** :

POST https://api.ultradns.com/accounts/{accountName}/dirgroups/geo/{name}

**Parameters** : None

**Body** : Must include an Account-Level GeoIP Directional Group DTO.

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If {accountName} is not valid, or not an {accountName} you have access to.

  * If you don't have permission to create account-level geo group.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create an
Account-level SourceIP Group

**Method and URI** :

POST https://api.ultradns.com/accounts/{accountName}/dirgroups/ip/{name}

**Parameters** : None.

**Body** : Must contain an Account-Level SourceIP Directional Group DTO.

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If {accountName} is not valid, or not an {accountName} you have access to.

  * If you don't have permission to create account-level IP group.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update an
Account-level GeoIP Group

**Method and URI** :

PUT https://api.ultradns.com/accounts/{accountName}/dirgroups/geo/{name}

**Parameters** : None

**Body** : Must include an Account-Level GeoIP Directional Group DTOin the
body content.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {accountName} is not valid, or not an {accountName} you have access to.

  * If you don't have permission to edit account-level directional groups.

  * If {name} is not the name of an account-level Geo directional group.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update an
Account-level SourceIP Group

**Method and URI** :

PUT https://api.ultradns.com/accounts/{accountName}/dirgroups/ip/{name}

**Parameters** : None.

**Body** : Must contain an Account-Level SourceIP Directional Group DTO.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {accountName} is not valid, or not an {accountName} you have access to.

  * If you don't have permission to edit account-level directional groups.

  * If {name} is not the name of an account-level IP directional group.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update an Account-level GeoIP Group

**Method and URI** :

PATCH https://api.ultradns.com/accounts/{accountName}/dirgroups/geo/{name}

**Parameters** : None

**Body** : Must include an Account-Level GeoIP Directional Group DTOin the
body content.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {accountName} is not valid, or not an {accountName} you have access to.

  * If you don't have permission to edit account-level directional groups.

  * If {name} is not the name of an account-level Geo directional group.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update an Account-level SourceIP Group

**Method and URI** :

PATCH https://api.ultradns.com/accounts/{accountName}/dirgroups/ip/{name}

**Parameters** : None.

**Body** : Must contain an Account-Level SourceIP Directional Group DTO or a
[JSON PATCH DTO](Making Updates via JSON PATCH.htm#_Ref399929538).

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {accountName} is not valid, or not an {accountName} you have access to.

  * If you don't have permission to edit account-level directional groups.

  * If {name} is not the name of an account-level IP directional group.

JSON Example: Partially Updating an Account-Level SourceIP Group with JSON
PATCH

[  
{  
"body": [  
{  
"op": "remove",  
"path": "/ips/4.4.4.4%2F32"  
}  
],  
"method": "PATCH",  
"uri": "/accounts/testdir/dirgroups/ip/foo1"  
},  
{  
"body": [  
{  
"op": "remove",  
"path": "/ips/2.2.2.2%2F32"  
}  
],  
"method": "PATCH",  
"uri": "/accounts/testdir/dirgroups/ip/foo2"  
},  
{  
"body": [  
{  
"op": "add",  
"path": "/ips/2.2.2.2%2F32"  
}  
],  
"method": "PATCH",  
"uri": "/accounts/testdir/dirgroups/ip/foo1"  
}  
,  
{  
"body": [  
{  
"op": "add",  
"path": "/ips/4.4.4.4%2F32"  
}  
],  
"method": "PATCH",  
"uri": "/accounts/testdir/dirgroups/ip/foo2"  
}  
]

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete an
Account-level GeoIP Group

**Method and URI** :

DELETE https://api.ultradns.com/accounts/{accountName}/dirgroups/geo/{name}

**Parameters** : None.

**Body** : None.

**Response** : If delete happens immediately, Status Code 204 is returned with
no body content.

  * If delete happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {accountName} is not valid, or not an {accountName} you have access to.

  * If you don't have permission to delete account-level directional groups.

  * If {name} is already in use by another account-level directional group (either IP or Geo).

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete an
Account-level SourceIP Group

**Method and URI** :

DELETE https://api.ultradns.com/accounts/{accountName}/dirgroups/ip/{name}

**Parameters** : None.

**Body** : None.

**Response** : If delete happens immediately, Status Code 204 is returned with
no body content.

  * If delete happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {accountName} is not valid, or not an {accountName} you have access to.

  * If you don't have permission to delete account-level directional groups.

  * If {name} is already in use by another account-level directional group (either IP or Geo).

### Account-Level GeoIP Directional Group DTO

Account-Level GeoIP Group DTO Structure

Field |  Description |  Type  
---|---|---  
name |  The name of the group. |  String. _Required in GET response_ ,   
Ignored in POST/PATCH/PUT, since it's specified in the URI.  
description |  The description for the group. |  String. Optional  
  
JSON Example: Account-Level GeoIP Group (in context)

{  
"name": "accountGeoGroup",  
"description": "A sample group",  
"codes": ["Z6", "RU"]  
}

### Account-Level SourceIP Directional Group DTO

Account-Level SourceIP Group DTO Structure

Field |  Description |  Type  
---|---|---  
name |  The name of the group. |  String. _Required for GET_.   
Ignored in POST/PATCH/PUT.  
description |  The description for the group. |  String. Optional.  
ips |  The list of IP addresses this group contains. |  Array of IP structures.  
ips/start |  The starting IP address (v4) for an IP range. If start is present, end must be present as well. CIDR and address must NOT be present |  IPv4  
ips/end |  The ending IP address (v4) for an IP range. If end is present, start must be present as well. CIDR and address must NOT be present. |  IPv4  
ips/cidr |  The CIDR format (v4) for an IP address range. If CIDR is present, start, end, and address must NOT be present. |  IPv4 CIDR format.  
ips/address |  A single IPv4 address. If address is present, start, end, and CIDR must NOT be present. |  IPv4  
  
JSON Example: Account-Level SourceIP Group (in context)

{  
"name": "accountIPGroup",  
"description": "Another sample",  
"ips": [  
{  
"start": "1.1.1.1",  
"end": "2.2.2.2"  
},  
{  
"address": "4.3.2.1"  
}  
]  
}

### Account-Level GeoIP Directional Group List DTO

This is returned when retrieving multiple Account-Level GeoIP Groups from the
server. It is not used for creating or updating Account-Level GeoIP Groups.

Account-Level GeoIP Group List DTO Structure

Field |  Description |  Type  
---|---|---  
accountName |  The account name for the groups. |  String.  
geoGroups |  The list of all Account-Level GeoIP Groups that matched the query for the offset and limit. |  List of Account-Level GeoIP Directional Group DTO.  
queryInfo/q |  The query used to construct the list. |  String  
queryInfo/sort |  The sort column used to order the list. |  String  
queryInfo/reverse |  Whether the list is ascending (false) or descending (true). |  Boolean  
queryInfo/limit |  The maximum number of rows requested. |  Integer  
resultInfo/totalCount |  Count of all events in the system for the specified query. |  Integer  
resultInfo/offset |  The position in the list for the first returned element (0 based). |  Integer  
resultInfo/returnedCount |  The number of records returned. |  Integer  
  
JSON Example: Account-Level GeoIP Group List

{  
"accountName" : "myAccount",  
"geoGroups" : [  
{  
"name": "accountGeoGroup",  
"description": "geo sample",  
"codes": [ "FR", "GB", "RU" ]  
},  
{  
"name": "accountGeoGroup2",  
"codes": [ "US-NY" ]  
}  
],  
"queryInfo": {  
"q": "",  
"sort": "name",  
"reverse": false,  
"limit": 100  
},  
"resultInfo": {  
"totalCount": 2,  
"offset": 0,  
"returnedCount": 2  
}  
}

### Account-Level IP Directional Group List DTO

This is returned when retrieving multiple Account-Level IP Groups from the
server. It is not used for creating or updating Account-Level IP Groups.

Account-Level SourceIP Group List DTO Structure

Field |  Description |  Type  
---|---|---  
accountName |  The account name for the groups. |  String  
ipGroups |  The list of all Account-Level SourceIP Groups that matched the query for the offset and limit. |  List of Account-Level SourceIP Directional Group DTO.  
queryInfo/q |  The query used to construct the list. |  String  
queryInfo/sort |  The sort column used to order the list. |  String  
queryInfo/reverse |  Whether the list is ascending (false) or descending (S). |  Boolean  
queryInfo/limit |  The maximum number of rows requested. |  Integer  
resultInfo/totalCount |  Count of all events in the system for the specified query. |  Integer  
resultInfo/offset |  The position in the list for the first returned element (0 based). |  Integer  
resultInfo/returnedCount |  The number of records returned. |  Integer  
  
JSON Example: Account-Level SourceIP Group List

{  
"accountName": "myAccount",  
"ipGroups": [  
{  
"name": "accountIPGroup",  
"description": "Another sample",  
"ips": [  
{  
"start": "1.1.1.1",  
"end": "2.2.2.2"  
},  
{  
"address": "4.3.2.1"  
}  
]  
},  
{  
"name": "accountIPGroup2",  
"ips": [  
{  
"cidr": "10.10.10.10/30",  
}  
]  
}  
],  
"queryInfo" : {  
"q": "",  
"sort": "name",  
"reverse": false,  
"limit": 100  
},  
"resultInfo": {  
"totalCount": 2,  
"offset": 0,  
"returnedCount": 2  
}  
}

