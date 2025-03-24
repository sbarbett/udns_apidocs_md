

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

# SVCB and HTTPS Records

The **Service Binding** (SVCB) record type is used to provides alternative
endpoints that are authoritative for the service, along with parameters
associated with each of the endpoints. Simply put, a SVCB record helps
websites and online services work more efficiently and flexibly to connect to
a device.

By configuring a SVCB record, a client can specify how users should connect to
a service, including which protocols and network endpoints are available or
optimal. Additionally, a SVCB record enables aliasing of Apex domains, which
isn't possible via a CNAME.

_Example Use Case_ : A website that supports both regular HTTP and secure
HTTPS connections configures a SVCB record to help direct the connection to
use HTTPS, ensuring a more secure connection with requiring additional
configurations.

The **HTTPS** resource record is a variation of SVCB designed for use with
HTTP services. These records provide detailed information to the client before
attempting to establish a connection, which can improve the performance and
privacy of web interactions. They allow direct connections to HTTP/3
alternative endpoints and support non-default TCP and UDP ports. Additionally,
they offer benefits like SRV records for HTTP, which have yet to see
widespread adoption.

For more details and configuration options, refer to our blog post about SVCB
and HTTPS records: <https://dns.ultraproducts.support/hc/en-
us/community/posts/25801694057371-Introducing-SVCB-and-HTTPS-Resource-
Records>.

## Create SVCB and HTTPS Records

SVCB and HTTPS records consist of two possible configuration modes, which will
determine which parameters are included in the request, and what values are
supported.

##### Alias Mode

When Alias Mode is configured, the records allow the aliasing at the zone apex
(one domain name to another domain name), where CNAME is not allowed. Unlike a
CNAME, a SVCB record in Alias Mode does not affect the resolution of other
resource record types, and applies only to a specific service, instead of an
entire domain name.

  * If creating a record in Alias Mode, the **priority** value must be set to 0. 

    * The parameters must be left empty.

  * If an SVCB recordâs **target** is â . â (null), the ownerName of the record must be used as the targetName.

  * An HTTPS recordâs **target** should not be the ownerName of the record, otherwise it will create a loop.

##### Service Mode

When Service Mode is configured, the SVCB record provides specific connection
information bound to a service endpoint domain. More simply put, it binds a
service to specific connection attributes that can then be used to offer
different ways to connect or provide additional features.

  * If creating a SVCB record in Service Mode, the **priority** value cannot be set to 0, as this is reserved for alias mode.

  * Creating a record in Service Mode and using â . â (null) as the target requires the targetName to be the ownerName.

**Method and URI:**

POST https://api.ultradns.com/zones/{zoneName}/rrsets/SVCB/{name}

POST https://api.ultradns.com/zones/{zoneName}/rrsets/HTTPS/{name}

  * If creating a record at the apex of the domain, {name} will be {zoneName}.

**Parameters:** None

**Body:** Must include an [ RRSet DTO](Resource Record Sets.htm#RRSet_DTO) and
SVCB and HTTPS DTO.

  * The Rdata DTO details are provided as a string list - SvcPriority TargetName SvcParams

**Response:** If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors:** An error is returned under the following conditions:

  * If {zoneName} is not valid, or a {zoneName} you do not have access to.

  * If you don't have permission to create SVCB or HTTPS Records.

  * If a resource record or {zoneName} of the same type already exists.

  * If SvcPriority is not a valid integer value.

  * If TargetName is not a FQDN.

SVCB and HTTPS DTO

Supported Account Settings

Attribute |  Description |  Type  
---|---|---  
SvcPriority |  Entered as the first value in the body and indicates the priority of the record. Lower values carry greater priority.

  * Valid values between 0-65535.
  * Value of 0 indicates the record will be in Alias mode.

|  Integer  
TargetName |  The domain name of either the alias target (for AliasMode) or the alternative endpoint (for ServiceMode) as a FQDN. Can be either a: 

  * Fully Qualified Domain Name (FQDN)
  * â . â (period) to indicate null

| String  
SvcParams |  A collection of key-value pairs providing specific service parameters.  Key values must be incrementally ordered and can only appear once. ([Service Binding SvcParamKeys](https://www.iana.org/assignments/dns-svcb/dns-svcb.xhtml))  Supported key values:

  * mandatory
  * alpn
  * no-default-alpn
  * port
  * ipv4hint
  * ech
  * ipv6hint
  * dohpath
  * keyNNNN

|  
  
SVCB and HTTPS Additional Parameter Details

Supported Account Settings

Parameter |  Description  
---|---  
alpn |  Lists supported application-layer protocols, crucial for protocol negotiation.  
no-default-alpn |  Indicates the absence of a default ALPN, requiring explicit negotiation.  
ipv4hint and ipv6hint |  Provide IP addresses hints to expedite connection establishment.  
|  
AliasMode (SvcPriority = 0) |  Functions like a CNAME record but can be used at the zone apex.  
ServiceMode (SvcPriority > 0) |  Binds the TargetName to specific service parameters, guiding the client to the optimal service endpoint.  
  
JSON Example: Create Record in Alias Mode

JSON Example: Create Record in Alias Mode ```json { "ttl": 300, "rdata": [ "0
target.example.com." ] } ```

JSON Example: Create HTTPS Record in Service Mode

JSON Example: Create HTTPS Record in Service Mode ```json { "ttl": 300,
"rdata": [ "1 . alpn=h3,h3-29,h2 ipv4hint=104.16.132.229,104.16.33.229
ipv6hint=2606:4700::6810:84e5,2606:4700::6810:85e5" ] } ```

## Get SVCB and HTTPS Records

**Method and URI:**

GET https://api.ultradns.com/zones/{zoneName}/rrsets/SVCB/{name}

GET https://api.ultradns.com/zones/{zoneName}/rrsets/HTTPS/{name}

**Parameters:** None

**Body:** If task completes, Status Code 200 OK is returned with an [ RRSet
DTO](Resource Record Sets.htm#RRSet_DTO)RRSet DTO and SVCB and HTTPS DTO in
the body content.

**Response:** If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors:** An error is returned under the following conditions:

  * If {zoneName} is not valid, or not a {zoneName} you have access to.

  * If you don't have permission to create SVCB or HTTPS records.

The output format of the record is:

Name TTL IN SVCB SvcPriority TargetName SvcParams.

JSON Example: Get SVCB Record

service.example.com. 7200 IN SVCB 1 svc1.example.net.

(

"alpn=h2,h3"

"port=8443"

"ipv4hint=192.0.2.10,192.0.2.11"

"ipv6hint=2001:db8::1,2001:db8::2"

)

##### SVCB Record Output Example and Explanation

Consider a scenario with a domain service.example.com that wants to specify
multiple service endpoints with different parameters.

service.example.com. 7200 IN SVCB 1 svc1.example.net. (

"alpn=h2,h3"

"port=8443"

"ipv4hint=192.0.2.10,192.0.2.11"

"ipv6hint=2001:db8::1,2001:db8::2"

)

In this example:

  * â**7200** â is the TTL (Time To Live) in seconds.

  * â**1** â is the SvcPriority. A non-zero value means it's in ServiceMode.

  * â**svc1.example.net.** â is the TargetName, the domain name of the service endpoint.

  * The â**alpn** â parameter specifies the supported protocols (HTTP/2 and HTTP/3 here).

  * â**port** â specifies the service's port number.

  * â**ipv4hint** â and â**ipv6hint** â provide IP address hints.

##### HTTPS Record Output Example and Explanation

For an HTTPS-specific record, let's consider a domain web.example.com with an
HTTPS service:

web.example.com. 7200 IN HTTPS 1 svc2.example.net. (

"alpn=h3"

"port=443"

"echconfig=..."

)

  * â**HTTPS** â indicates the record type specific to HTTP services.

  * â**svc2.example.net.** â is the TargetName for the HTTPS service.

  * The â**alpn** â parameter specifies HTTP/3 as the supported protocol.

  * â**port** â is the standard HTTPS port (443 in this case).

  * â**echconfig** â provides Encrypted ClientHello configuration, a string representing the encrypted configuration for the initial TLS handshake.

## Update SVCB and HTTPS Records

**Method and URI:**

PUT https://api.ultradns.com/zones/{zoneName}/rrsets/SVCB/{name}

PUT https://api.ultradns.com/zones/{zoneName}/rrsets/HTTPS/{name}

**Parameters:** None

**Body:** Must include either the [ RRSet DTO](Resource Record
Sets.htm#RRSet_DTO)RRSet DTO and/or SVCB and HTTPS DTO in the body content.

**Response:** If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors:** An error is returned under the following conditions:

  * If {zoneName} is not valid, or not a {zoneName} you have access to.

  * If you don't have permission to create SVCB or HTTPS records.

## Delete SVCB and HTTPS Records

**Method and URI:**

DELETE https://api.ultradns.com/zones/{zoneName}/rrsets/SVCB/{name}

DELETE https://api.ultradns.com/zones/{zoneName}/rrsets/HTTPS/{name}

**Parameters:** None

**Body:** None

**Response:** If delete happens immediately, Status Code 204 is returned with
no body content.

  * If delete happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors:** An error is returned under the following conditions:

  * If {zoneName} is not valid, or not a {zoneName} you have access to.

  * If you don't have permission to create SVCB or HTTPS records.

