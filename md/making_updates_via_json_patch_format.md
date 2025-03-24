

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

# Making Updates via JSON PATCH Format

UltraDNS APIs can create, modify, and return responses in both XML and JSON
formats using a DTO that contains the data fields for an entity. However,
there are limitations to making updates via this approach. Using PUT requires
you to specify all attributes even if you are only changing one attribute.
Using the current PATCH method allows you to update only the fields you need,
but does not allow you to modify a value in an array, or remove an attribute
or array entry.

In order to work around these limitations, the UltraDNS REST API supports the
use of the JSON PATCH standardized format (defined in [RFC
6902](http://tools.ietf.org/html/rfc6902)) for specifying entity updates.

JSON PATCH calls allow you to specify multiple types of updates to a single
entity in the system. For example, you can use a single call to update a
NotifyAddress for a zone, add a new address to the list, and remove one you no
longer need.

Currently, the UltraDNS REST API allows for JSON PATCH formatted calls to:

  * [Partially Update a Zone](Zone API/Zone API.htm#_Ref395092542)\- that includes Primary, Secondary and Alias zones.
  * [Partially Update Web Forwards](Web Forwards.htm#_Ref399843533)
  * [Partially Update an RRSet](Resource Record Sets.htm#_Ref399843565) â for standard RRSets, Resource Distribution (RD) pools, SiteBacker/Traffic Controller pools, and Directional pools.
  * [Partially Update a Probe](SiteBacker and Traffic Controller Pool Probes.htm#_Ref409181324)â for all pool probe types.
  * [Directional Pools API](Directional Pools API.htm#_Ref503427934) \- various calls for Directional Pools will allow for the usage of the JSON PATCH (each call will identify if you can use JSON PATCH).

The above links will take you to the section of this guide that contains
partial update call information for each of the objects listed.

JSON PATCH requests are sent to the same endpoint as PUT or PATCH updates.
However, to indicate that you are sending the request in JSON PATCH format,
you must:

  * Use the PATCH HTTP method.
  * Supply application/json-patch+json for the value in the "Content-Type" HTTP header.
  * Include a JSON array in the body of the request that contains one or more JSON PATCH DTOs (defined below).

  
![](../Resources/Images/Rest-API_User_Guide/Introduction_64x75.png) |  **A Note About JSON PATCH:** There is difference between PATCH and JSON PATCH. This difference is communicated to REST API by providing header Content-Type: application/json-patch+json for JSON PATCH versus Content-Type: application/json for regular formats like PATCH, PUT, POST, DELETE, and GET.   
  
As a consequence, the whole batch should contain only JSON PATCH bodies, or
only regular bodies.  
---|---  
  
## JSON PATCH DTO

When using the JSON PATCH format you must provide a JSON PATCH DTO. The JSON
PATCH DTO identifies the type of update you want to make, which attribute you
want to modify, and the new value for that attribute. As with all JSON PATCH
targets, the first item is numbered 0, the second is numbered 1 and so on. The
JSON PATCH is constructed as shown in the below table.

JSON PATCH DTO

Field |  Description |  Type  
---|---|---  
op |  Patch operation type you want to perform. Valid values are:

  * add
  * replace
  * remove
  * move

|  String  
path |  A JSON pointer that identifies the target (JSON target) on which you want to perform the provided operation. The path should be [RFC-6901 compliant.](http://tools.ietf.org/html/rfc6901 "Link to IETF.org site page listing RFC6901 standards") |  String  
value |  The value you want to apply to the JSON target provided. The value is ignored when the op is set to "remove." |  Object  
from |  The existing value or path that needs to be changed or moved. This field is used when the âmoveâ operation type is used. |  String  
  
## JSON PATCH Examples

The following example shows an array of JSONPATCH DTOs for updating a Primary
zone. Notice that the zone is being updated using multiple operations for the
different values for the zone.

JSON PATCH Example: Update Primary Zone information

[  
{  
"op": "replace",  
"path": "/restrictIpList/0/endIP",  
"value": "7.7.7.7"  
},  
{  
"op": "add",  
"path": "/restrictIpList/1",  
"value": {"startIP": "1.1.1.1", "endIP": "2.2.2.2"}  
},  
{  
"op": "remove",  
"path": "/restrictIpList/3"  
}  
]

In the above example, the JSON PATCH performs the following changes to the
Primary zone (identified in the PATCH call URI):

  * The endIP address for the first-listed restrictIP is replaced by 7.7.7.7
  * The restrictIP list has a new entry, an IP range 1.1.1.1 to 2.2.2.2. This new IP range will be shown second in a list of restrictIPs for this zone.
  * The fourth-listed restrictIP entry is removed from the zone.

![](../Resources/Images/Rest-API_User_Guide/Making Updates via JSON PATCH_60x69.png) |  When updating Primary Zone Information by performing a POST (create) or a PUT/PATCH (update/partial update) call, the ârestrictIPListâ call is case sensitive (specificially the âIPâ aspect). For these instances, the âIPâ needs to be uppercase. When performing a GET call, or when using JSON-PATCH to PATCH a zone, the âIpâ section of restrictIpList needs to remain as lower case (âIpâ).  
---|---  
  
This next example displays the JSON PATCH operation for âmove.â This
operation allows a recordâs position to be moved from one position to
another within a pool. Currently, this operation is only valid for Resource
Distribution (RD) pools, Simple Load Balancing (SLB) pools, and SiteBacker /
Traffic Controller (SB/TC) pools, as these are the pools that contain multiple
rdata values.  

In regards to the SiteBacker and Traffic Controller pools with priority
settings, once a record is moved to another position in the pool, the priority
setting will be updated accordingly for the change.

JSON PATCH Example: Move operation

[  
{  
"op": "move",  
"path": "/rdata/2",  
"from": "/rdata/1"  
}  
]

In the above example, the rdata is moving from position 1 to position 2 within
the pool.

The example below shows a JSON PATCH DTO for updating a Secondary Zone.

JSON PATCH Example: Update Secondary Zone information

[  
{  
"op": "add",  
"path": "/primaryNameServers/nameServerIpList/nameServerIp1/ip",  
"value": "2.2.20.8"  
}  
]

In this example, the IP address for the first Primary Name Server for the
secondary zone has been set to 2.2.20.8. In the [Zone API](Zone API/Zone
API.htm#_Ref395097899) for this zone, this is the value that will now appear
for the _nameServerIp1_ attribute.

JSON PATCH format for partial updates is also supported for RRSets. However,
resource record types that have multiple values within an rdata entry (such as
MX, NS, or SOA) present a challenge to the standard JSON Pointer format. The
standard provides no way to refer to a particular value within a single rdata
entry.

To accommodate this limitation, the UltraDNS REST API provides a special case
for rdata entries, allowing both the record **and** the value for that record
to be optionally indexed like a list. The first target number in the path
identifies the particular record in the set you want to update; the second
target number in the path identifies the value for the record you want to
update. If you do not list this second target number, it is assumed that you
are updating all values in the specified target record.

The following example shows a JSON PATCH call to update multiple MX records in
a set, demonstrating the ability to index into an rdata record.

JSON PATCH Example: Update MX records in a set

[  
{  
"op": "replace",  
"path": "/rdata/0/1",  
"value": "new.mail.server.biz."  
},  
{  
"op": "replace",  
"path": "/rdata/1",  
"value": "30 new3.mail.server.biz."  
}  
]

In the above example, the first portion of the call updates only the mail
server name for the first MX record in the set. The second portion of the call
replaces all values (both the priority and the mail server) in the second MX
record.

Performing a GET call for a resource provides the JSON structure on which the
JSON-PATCH operates. The fields in the returned resource are the fields that
will be specified in the path of the JSON-PATCH.

The GET calls for JSON PATCH supported items can be found in the following
sections:

  * [Get Zone Metadata](Zone API/Zone API.htm#_Ref395100959)
  * [List all RRSets of a Type for an Owner](Resource Record Sets.htm#_Ref399844854) (both Owner and Type are required for the partial update RRSet call). 
  * [Get a Probe](SiteBacker and Traffic Controller Pool Probes.htm#_Ref409181639)
  * [Get Web Forwards](Web Forwards.htm#_Ref474401801)

