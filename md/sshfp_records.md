

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

# SSHFP Records

A Secure Shell Fingerprint (SSFHP) record is a resource record that identifies
the SSH keys (which provide secure remote log and network services over an
insecure network) that are associated with a host or domain name. The SSHFP
record can be used when a public key is not recognized, and if accepted, will
be saved locally and used for verification for subsequent connections.

Per [RFC-4255](https://tools.ietf.org/html/rfc4255), âUpon connection to an
SSH server, the SSH client MAY look up the SSHFP resource record(s) for the
host it is connecting to. If the algorithm and fingerprint of the key received
from the SSH server match the algorithm and fingerprint of one of the SSHFP
resource record(s) returned from DNS, the client MAY accept the identity of
the server.â

The SSHFP record consists of an alrogirthm number, a fingerprint type, and the
fingerprint of the public host key.

## Create SSHFP Record

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/rrsets/SSHFP/{zoneName}

**Parameters** : None

**Body** : Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288), and the following SSHFP DTO:

Field |  Description |  Type  
---|---|---  
algorithm |  The first integer displayed. Describes the type of Algorithm to be used. |  Valid values are: 1 - RSA;  
2 - DSS;  
3 - ECDSA;  
4 - Ed25519  
type |  The Algorithm type used to hash the public key. |  1 - SHA-1;  
2 - SHA-256  
fingerprint |  The hexadecimal representation of the hash result, as text. |  Valid hexadecimal string.  
  
**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid, or if itâs not a {zoneName} you have access to.

  * If an invalid Input is provided.

  * If you don't have permission to create SSHFP Records.

  * If a resource record or {zoneName} of the same type already exists

JSON Example: Create SSHFP Records

{  
"rdata": [  
"1 1 6E657573746172"  
]  
}

## Get SSHFP Record

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/SSHFP

OR

GET https://api.ultradns.com/zones/{zoneName}/rrsets/SSHFP/{ownerName}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * Data is not found.

  * Insufficient permissions: User cannot access object.

  * Zone does not exist in the system.

JSON Example: Get SSHFP Records

{  
"zoneName": "ultratest.biz"  
"rrsets": [  
{  
"ownerName": "www.sshfp.com.ultratest.biz"  
"rrtype": "SSHFP (44)",  
"ttl": 100,  
"rdata": [  
"1 2 6E657573746172"  
]  
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

## Delete SSHFP Record

**Method and URI** :

DELETE https://api.ultradns.com/zones/{zoneName}/rrsets/SSHFP/{zoneName}

**Parameters** : None

**Body** : None

**Response** : If delete happens immediately, Status Code 204 is returned with
no body content.

**Errors** : An error is returned under the following conditions:

  * Data is not found.

  * Insufficient permissions: User cannot access object.

  * Zone does not exist in the system.

