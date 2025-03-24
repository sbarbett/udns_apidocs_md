

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

# CAA Records API

The Certification Authority Authorization, or CAA record, allows for a domain
name holder to authorize one or more certification authorities to issue
certificates for a domain. Additionally, the records allow for the
implementation of additional controls by a Public Certification Authority
which can prevent certificate issues. (Certificates are generally valid for at
least one year)

The CAA records specify an authorization control to be performed by a
certificate issuer before the issuance of a certificate.

A CAA resource record consists of a flags byte and a tag-value pair referred
to as a property. Domain names may have multiple CAA RRs (Resource Record that
includes the owner name, class, type, time to live, and data) associated with
it, so a given property may be specified more than once.  
  

CAA DTO Record Tags/Types

**Field (Tags)** |  **Description** |  **Type**  
---|---|---  
**issue** |  Authorizes the domain name holder to issue certificates for the domain. |  Value Types:

  * â0â â Default
  * â1â (Issuer Critical) - Indicates that the corresponding tag MUST be understood if the record is to be properly interpreted by an issuer.

SeeCAA REcord - Additional Tag Values for acceptable tag formats.  
**issuewild** |  Authorizes the domain name holder to issue wildcard certificates for the domain. |  Adheres to the same syntax as issue, however, will take precedence over issue properties if specified.   
**issuemail** |  Authorizes the domain name owner to restrict the issuance of certificates that certify email addresses. |  Adheres to the same syntax as **issue**.  
**issuevmc** |  Authorizes the domain name holder to issue mark certificates for the domain. |  Adheres to the same syntax as **issue**.  
**iodef** |  Specifies a URL to which an issuer âmayâ report certificate issue requests that may be inconsistent with the issuerâs policies or practices. |  HTTP or HTTPS.  
  
The canonical presentation format of the CAA record is:

CAA <flags> <tag> <value>

Where:

  * **Flags** : Is an unsigned integer between 0 and 255.

  * **Tag** : Is a non-zero sequence of US-ASCII letters and numbers in lower case.

  * **Value** : Is the <character-string> encoding of the value field

The following example depicts a situation in which certificates are not to be
issued, except by the holder of the domain name, or an authorized agent.

{  
$ORIGIN example.com  
CAA 0 issue "ca.example.net"  
}

For circumstances in which one more iodef properties are specified, a
certificate issuer may report invalid certificate requests to a specific
address.

{  
$ORIGIN example.com  
CAA 0 issue "ca.example.net"  
CAA 0 iodef "mailto:security@example.com"  
CAA 0 iodef "http://iodef.example.com"  
}

Certificate issuers may specify additional parameters that allow customers to
specify additional parameters in return which can govern the certificate
issuance. This could include a Certificate policy number for example to be
used or referenced. The following example demonstrates a situation in which
domain holder for âca.example.netâ has requested its customers
(example.com) to specify an account number in each CAA record.

{  
$ORIGIN example.com  
CAA 0 issue "ca.example.net; account=xxxxxx"  
}

CAA REcord - Additional Tag Values

Tag Type |  Value  
---|---  
issuevalue |  = [domain] [â ; â *(space parameter)]  
domain |  = label *(â.â label)  
label |  = (ALPHA / DIGIT) *( *(â-â) (ALPHA / DIGIT))  
space |  = *(SP / HTAB)  
parameter |  = tag â=â value  
tag |  = 1*(ALPHA / DIGIT)  
value |  = *VCHAR  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create CAA
Records

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/rrsets/CAA/{zoneName}

**Parameters** : None.

**Body** : Must include an [Resource Record Set (RRSet) DTO](Resource Record
Sets.htm#_Ref462834288) and CAA Records API.

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid, or a {zoneName} you do not have access to.

  * If you don't have permission to create CAA Records.

  * If a resource record or {zoneName} of the same type already exists.

JSON Example: Create a CAA Record

{  
"zoneName": "0-a-accounttest.com.",  
"ownerName": "caarec",  
"rrtype": "CAA",  
"ttl": null,  
"rdata": [  
"3 issue \"a\""  
]  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get CAA
Records

**Method and URI** :

GET https://api.ultradns.com/zones/{zoneName}/rrsets/CAA/{zoneName}

**Parameters** : None.

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
[Resource Record Set (RRSet) DTO](Resource Record Sets.htm#_Ref462834288)and
CAA Records API in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid, or not a {zoneName} you have access to.

  * If you don't have permission to create CAA records.

JSON Example: Get a CAA Record

{  
"zoneName": "0-a-accounttest.com.",  
"rrSets": [  
{  
"ownerName": "caarec.0-a-accounttest.com.",  
"rrtype": "CAA (257)",  
"ttl": 86400,  
"rdata": [  
"1 issue \"a a\"",  
"3 issue \"a\""  
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

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update CAA
Records

**Method and URI** :

PUT https://api.ultradns.com/zones/{zoneName}/rrsets/CAA/{zoneName}

**Parameters** : None.

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid, or not a {zoneName} you have access to.

  * If you don't have permission to create CAA records.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete CAA
Records

**Method and URI** :

DELETE https://api.ultradns.com/zones/{zoneName}/rrsets/CAA/{zoneName}

**Parameters** : None.

**Body** : None.

**Response** : If delete happens immediately, Status Code 204 is returned with
no body content.

  * If delete happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid, or not a {zoneName} you have access to.

  * If you don't have permission to delete CAA records.

