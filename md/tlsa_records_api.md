

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

# TLSA Records API

The Transport Layer Security Protocol, or TLSA, provides communication
security across the internet, by using channel encryption. The TLSA DNS
resource record is used to associate a TLS server certificate or public key
with the domain name where the record is found, thereby forming a âTLSA
certificate association.â

By using certificates, TLS can bind keys (secret / public) so that they cannot
be duplicated or falsified. By combining a published key with additional
specific information (i.e. name of a service), and then being signed by a
separate key, the TLS records creates in essence, an âanchorâ key. When a
key is used to validate the signature of certificates being received, it will
be validated by the âanchorâ key, thereby preventing untrusted signing
from occurring.

For example:

"Example.com" can only be signed by the key(s) for "com", and the "com" key(s)
can only be signed by the DNS root.

## Create TLSA Records

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/rrsets/TLSA/{zoneName}

**Parameters** : None.

**Body** : Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288) and TLSA DTO .

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid, or if itâs not a {zoneName} you have access to.

  * If you don't have permission to create TLSA Records.

  * If a resource record or {zoneName} of the same type already exists.

JSON Example: Create TLSA Record

{  
"ttl": 300,  
"rdata": ["1 0 0 82003ba34942dc74"]  
}

For a greater detailed explanation of the above JSON example return for
Creating TLSA Records, refer to the following table. Each field and value
combination are separated by a space in the api call.

TLSA DTO

Field |  Description |  Type  
---|---|---  
Certification Usage |  The first integer displayed. Describes the type of Certificate to be used. |  Valid values are:

  * 0 - Specify CA certificate/public key for certificate to certify end server. Certificate might not have the basic Constraints extension present.
  * 1 - Specify CA certificate/public key for certificate to certify end server. Service certificate constraint.
  * 2 - Specify CA certificate/public key for certificate to certify end server. Trust anchor assertion.
  * 3 - Domain-issued certificate (same as 1, with no PKIX validation is tested).

  
Field-Selector |  The second integer displayed. Describes the type of selector to be used. | 

  * 0 â Full certificate of the Certificate Binary structure.
  * 1 â SubjectPublicKeyInfo

  
Matching Type |  The third integer displayed. Describes the type of matching to be used.  | 

  * 0 â Exact match on selected content.
  * 1 â SHA-256 hash of selected content.
  * 2 â SHA-512 hash of selected content.

  
Certificate-Association-Data |  The string of hexadecimal characters that describes certificate associated data. | 

  * The certificate-association-data must be represented as a string of hexadecimal characters. Whitespace is allowed within the string of hexadecimal characters.

  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get TLSA
Records

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/TLSA/{zoneName}

**Parameters** : None.

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
[Resource Record Set (RRSet) DTO](Resource Record Sets.htm#_Ref462834288)and
TLSA DTO  in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid, or not a {zoneName} you have access to.

  * If you don't have permission to create TLSA Records.

JSON Example: Get TLSA Record

{  
"zoneName": "0-a-accounttest.com.",  
"rrSets": [  
{  
"ownerName": "_1._tcp.test1.0-a-accounttest.com.",  
"rrtype": "TLSA (52)",  
"ttl": 20,  
"rdata": [  
"0 0 0 12345678",  
"0 0 0 123ba45679"  
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

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update TLSA
Records

**Method and URI** :

PUT https://api.ultradns.com/zones/{zoneName}/rrsets/TLSA/{zoneName}

**Parameters** : None.

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid, or not a {zoneName} you have access to.

  * If you don't have permission to create TLSA Records.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete TLSA
Records

**Method and URI** :

DELETE https://api.ultradns.com/zones/{zoneName}/rrsets/TLSA/{zoneName}

**Parameters** : None.

**Body** : None.

**Response** : If delete happens immediately, Status Code 204 is returned with
no body content.

  * If delete happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid, or not a {zoneName} you have access to.

  * If you don't have permission to create/delete TLSA Records.

