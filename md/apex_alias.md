

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

# Apex Alias

Apex Alias (APEXALIAS) provides a way for domain administrators to provide DNS
CNAME functionality at the apex (or root) of a domain. Traditionally, the use
of CNAMES at the apex of a domain have been discouraged and eventually
forbidden by the protocol specification. However, modern usage of CDNs and
outsourced cloud environments have driven the need for the ability to point
the apex of a domain to resources outside of the domain. The Apex Alias
addresses this need, by introducing a custom record for domain owners to
maintain this linkage.

At query and resolution, the UltraDNS resolvers will chase the Apex Alias, in
the same way that a recursing resolver would, and return the results of the
chase in the answer to the query. Apex Alias functionality supports both IPv4
and IPv6 address resolution, returning A and AAAA records as appropriate.
UltraDNS has also built in support for the edns0-client-subnet (ECS)
specification, meaning that caching resolvers that pass in the client subnet
will be able to take advantage of ECS functionality when querying for the zone
apex.

## Creating the Apex Alias

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/rrsets/APEXALIAS/{zoneName}

**Parameters** : None

**Body** : Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288).

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If you try to sign a zone with apex alias.
  * When the record type can only be created at the apex of the domain.
  * HostName and pointsTo cannot be same.
  * pointsTo must be a fully qualified domain name.
  * This record type cannot be created on a signed zone.
  * Only one APEX Alias record can be configured per zone.
  * This record type cannot be created when both A and AAAA records exist at zone apex.
  * A/AAAA cannot be added so that there are apex alias and both A and AAAA at apex.

## Reading the Apex Alias

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/APEXALIAS/{zoneName}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * Data is not found.
  * Insufficient permissions: User cannot access object.
  * Zone does not exist in the system.

JSON Example: Reading the Apex Alias

{  
"zoneName": "ultratest.biz"  
"rrsets": [  
{  
"ownerName": "ultratest.biz"  
"rrtype": "APEXALIAS (65282)"  
"ttl": 300,  
"rdata": [  
"mywebfront.mysecretcdn.com"  
]  
}  
]  
"queryInfo": (  
"sort": "OWNER",  
"reverse": false,  
"limit": 100  
}  
"resultInfo": {  
"totalCount": 1,  
"offset": 0,  
"returnedCount": 1  
}  
}

