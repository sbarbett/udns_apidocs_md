

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

# DS Records

The Delegation Signer (DS) record refers to a DNSKEY resource record, and is
used in the DNSKEY authentication process. The DS resource record is inserted
at a zone cut (i.e., a delegation point) to indicate that the delegated zone
is digitally signed and that the delegated zone recognizes the indicated key
as a valid zone key for the delegated zone. By authenticating the DS record, a
resolver can then authenticate the DNSKEY resource record, to which the DS
record points to.

The RDATA for a DS record consists of a two-octet Key Tag field, a one-octet
Algorithm field, a one-octet Digest Type field, and a Digest field.

For example, the DS resource record for "example.com" is stored in the "com"
zone (the parent zone), rather than in the "example.com" zone (the child
zone). The corresponding DNSKEY resource record is stored in the "example.com"
zone (the child zone). This simplifies DNS zone management and zone signing.
For additional information, please refer to
[RFC-3658](https://www.ietf.org/rfc/rfc3658.txt).

## Create DS Record

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/rrsets/DS/{zoneName}

**Parameters** : None

**Body** : Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288), and the following Delegation Signer DTO:

Field |  Description |  Type  
---|---|---  
Key Tag |  The Key Tag field contains the key tag value of the DNSKEY RR that validates this signature, in network byte order.  |  Integer.  
  
Algorithm |  The Algorithm type used to hash the public key. For the full list of Algorithm types, please refer to  |  8 â RSA/SHA -256 13 â ECDSA Curve P-256 with SHA-256.  
Digest Type |  The digest refers to the DNSKEY resource record. The Digest Type Identifies the algorithm used to construct the digest. |  1 - SHA-1 2 - SHA-256  
  
Digest |  The digest is calculated by concatenating the canonical form of the fully qualified owner name of the DNSKEY RR with the DNSKEY RDATA, and then applying the digest algorithm. |  Hexadecimal string â 40 characters in length.  Not returned on GET call.  
  
  
**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid, or if itâs not a {zoneName} you have access to.

  * If an invalid Input is provided.

  * If you don't have permission to create DS Records.

  * If a resource record or {zoneName} of the same type already exists

JSON Example: Create DS Record

{  
"ttl":500,  
"rdata":["1000 8 1 A94A8FE5CCB19BA61C4C0873D391E987982FBBD3"]  
}

## Get DS Record

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/DS

OR

GET https://api.ultradns.com/zones/{zoneName}/rrsets/DS/{ownerName}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * Data is not found.

  * Insufficient permissions: User cannot access object.

  * Zone does not exist in the system.

JSON Example: Get DS Records

{  
"zoneName": "ultratest.bizâ  
"rrsets": [  
{  
"ownerName": " www.ultradstest.com.ultratest.biz"  
"rrtype": "DS (43)",  
"ttl": 800,  
"rdata": [  
"1000 8 1 A94A8FE5CCB19BA61C4C0873D391E987982FBBD3"  
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

## Delete DS Record

**Method and URI** :

DELETE https://api.ultradns.com/zones/{zoneName}/rrsets/DSs/{zoneName}

**Parameters** : None

**Body** : None

**Response** : If delete happens immediately, Status Code 204 is returned with
no body content.

**Errors** : An error is returned under the following conditions:

  * Data is not found.

  * Insufficient permissions: User cannot access object.

  * Zone does not exist in the system.

