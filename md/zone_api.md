

Skip To Main Content

Account

Settings

* * *

Logout

[](../News and Updates.htm)

  * placeholder

Account

Settings

* * *

Logout

Filter:

  * All Files

Submit Search

# Zone API

A DNS Zone is a portion of a DNS Domain separated for administrative control.
You can think of it as a container for individual DNS Resource Records. Zones
(domains) are the basic building blocks of DNS. UltraDNS defines three classes
of zone types: Primary, Secondary, and Alias.

  * A Primary Zone is the master copy of the zone data. UltraDNS manages Primary zones. They may include advanced features like pools.
  * A Secondary Zone is a copy of the primary zone, and is owned and controlled by a nameserver outside the UltraDNS system. UltraDNS retrieves a copy via zone transfer of the zone from the remote nameserver. Secondary zones are read-only (except for requests for transfer) and cannot contain advanced UltraDNS features.
  * An Alias Zone is a virtual copy of a Primary zone; itâs basically the primary zone under a different zone name. They are read-only, but contain all of the advanced features of the primary zones they alias.

This section displays the details on the Zone API calls available for use, as
well as detailed Zone DTO (Data Transfer Object) information.

When DTOs are required in the body of the call, or are returned as a response,
cross reference links are provided to the specific table containing the
details of DTO contents.

![](../../Resources/Images/MSP_User_Guide/Two Factor Mobile Authentication_68x68.png) |  To escape forward slashes in zone names (for example, a reverse zone with the name 0/24.50.156.193.in-addr.arpa), use %2F. In our example URIs, to specify the reverse zone noted above, follow this example -  https://api.ultradns.com/zones/0%2F24.50.156.193.in-addr.arpa.  
---|---  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Create a
Zone

The Create Zone API allows you to create a Primary, Secondary, or Alias Zone,
and furthermore, allows you to create a Zone âfrom scratchâ by copying
another zone via an uploaded file or by Zone transfer. The JSON examples
provided below give a sample of each type of zone create call.

Create a Zone is a POST call and is generated as follows:

**Method and URI:**

POST https://api.ultradns.com/zones

**Parameters** : None

**Body** : Must include [Zone Create DTO](Zone API DTOs.htm#Zone_Create_DTO)
parameters.

The Zone Create DTO requires the inclusion of a **Zone Properties DTO**.
Depending on the type of Zone you are creating, you will also require a
**Primary Zone DTO** , a **Secondary Zone DTO** or an **Alias Zone DTO**.

**Response** : If task completes, Status Code 201 is returned with an
appropriate message in the response body.

  * If creation happens in the background, a Status Code 202 is returned with a status response message of âPendingâ along with an X-Task-Id header in body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} already exists.
  * If {zoneName} is not valid.
  * If you don't have permission to create zones.
  * If creating a Primary Zone via copy, if creating an Alias, or if the original zone is not a Primary zone.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Delete a
Zone

The Delete Zone API allows you to delete any zone you have the proper
authority to delete. You cannot delete a primary zone if it has an Alias zone.

Delete Zone call is generated as follows:

**Method and URI:**

DELETE https://api.ultradns.com/zones/{zoneName}

**Parameters:** None

**Body:** None

**Response** : If delete happens immediately, Status Code 204 returned with no
body content.

  * If delete happens in the background, a Status Code 202 is returned with a status response message of Pending, along with an X-Task-Id header in body content.

**Errors:** An error is returned under the following conditions:

  * If you do not have permission to delete {zoneName}.
  * If {zoneName} does not exist.

JSON Example: Delete Zone with Change Comment

JSON Example: Delete Zone with Change Comment ```json { "changeComment":
"Deleting Zone as agreed" } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get Zone
Metadata

The Get Zone Metadata call returns Zone information for the specified
{zoneName} in the form of a [Zone DTO](Zone API DTOs.htm#Zone_DTO). This DTO
can in turn be used for other calls as needed.

Method and URI:

GET https://api.ultradns.com/zones/{zoneName}

**Parameters:** None

**Body:** None

**Response:** If task completes, Status Code 200 OK is returned with a [Zone
DTO](Zone API DTOs.htm#Zone_DTO) in the body content. Example responses for
different zone types are shown below.

**Errors:** An error is returned under the following conditions:

  * If {zoneName} does not exist.
  * If you do not have permission to read {zoneName}.

JSON Example: Responses to Primary Zone â Get Metadata

{  
"properties": {  
"name": "primary-example.com.",  
"accountName": "example",  
"owner": "example",  
"type": "PRIMARY",  
"recordCount": 3,  
"dnssecStatus": "UNSIGNED",  
"lastModifiedDateTime": "2014-07-01T22:13Z"  
},  
"registrarInfo": {  
"registrar": "Generic Domain Name Registrar",  
"whoisExpiration": "2015-01-01 00:00:00",  
"nameServers": {  
"ok": ["PDNS1.ULTRADNS.NET", "PDNS2.ULTRADNS.NET"],  
}  
},  
"restrictIpList": [  
{  
"startIP": "10.20.30.40",  
"endIP": "20.20.20.20",  
"comment": "Comment"  
}  
],  
"tsig": {  
"tsigKeyName":"Key",  
"tsigKeyValue": "This would be a hash if it was real",  
"description": "TSIG for primary-example.com",  
"tsigAlgorithm": "hmac-sha256"  
},  
"notifyAddresses": [  
{  
"notifyAddress": "2.4.5.6",  
"description": "East Coast Server"  
},  
{  
"notifyAddress": "5.6.7.8",  
"description": "West Coast Server"  
}  
]  
}  

JSON Example: Secondary Zone â Get Metadata

{  
"properties": {  
"name": "secondary-example.com.",  
"accountName": "example",  
"owner": "example",  
"type": "SECONDARY",  
"recordCount": 3,  
"dnssecStatus": "UNSIGNED",  
"lastModifiedDateTime": "2014-07-01T22:13Z"  
},  
"primaryNameServers": {  
"nameServerIpList": {  
"nameServerIp1": {  
"ip": "1.2.3.4",  
"tsigKey": "key1",  
"tsigKeyValue": "value1"  
},  
"nameServerIp2": {  
"ip": "2.4.5.6",  
"tsigKey": "key2",  
"tsigKeyValue": "value2"  
},  
"nameServerIp3": {  
"ip": "3.4.5.6",  
"tsigKey": "key3",  
"tsigKeyValue": "value3"  
}  
}  
}  
"transferStatusDetails": {  
"lastRefresh": "06/13/18 06:07:45 AM GMT",  
"nextRefresh": "06/13/18 07:07:45 AM GMT",  
"lastRefreshStatus": "FAILED",  
"lastRefreshStatusMessage": "Failed to transfer zone 'secondary-  
example.com.' from host: 54.209.41.82; reason:  
java.net.SocketTimeoutException"  
}  
}  
}

JSON Example: Alias Zone â Get Metadata

{  
"properties": {  
"name": "alias-example.com.",  
"accountName": "example",  
"owner": "example",  
"type": "ALIAS",  
"recordCount": 3,  
"dnssecStatus": "UNSIGNED",  
"lastModifiedDateTime": "2014-07-01T22:13Z"  
},  
"originalZoneName": "example.com."  
}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Migration
Steps for List Metadata for Zones â v3

Please follow the steps below to migrate from the previous method of using
/v1, /v2, or no versioning in the API call, to our new API format for
Migration Steps for List Metadata for Zones â v3.

  1. Add the /v3 version in your URL as shown below.

    1. **Your existing URL format** :  
  
https://api.ultradns.com/zones  
https://api.ultradns.com/v1/zones  
https://api.ultradns.com/v2/zones

    2. **Your new URL format** :  
  
https://api.ultradns.com/v3/zones

  2. The following content emphasizes the changes in how you will retrieve the first page of results.

    1. There are no changes required in retrieving the first page of result details. Performing the above URL change will be sufficient.

    2. There is a difference in the pagination behavior when using the new /v3 call. The new version does not return the previously used resultInfo section, instead, it returns a new section called cursorInfo. This section provides the cursor-based information used to navigate to the different pages of results that can be returned. The cursorInfo section contains four values â **first** , **next** , **previous** , and **last**.

      1. If there are additional pages of details that can be navigated to, the cursorInfo section will contain the **previous** and **first** values.

      2. If there are no additional pages to navigate to, the cursorInfo section will be empty.

The following API example shows a cursorInfo section with **next** and
**last** values available.

**Method and URI** :

GET https://api.ultradns.com/v3/zones/

JSON Example: List Metadata for Zones v3

JSON Example: List Metadata for Zones v3 ```json { "queryInfo": { "q": "",
"sort": "name", "reverse": false, "limit": 2 }, "cursorInfo": { "next":
"em9uZTIuY29tLjpORVhU", "last": "fjpMQVNU" }, "zones": [ { "properties": {
"name": "zone1.com.", "accountName": "TestAccount", "type": "PRIMARY",
"dnssecStatus": "SIGNED", "status": "SUSPENDED", "owner": "test",
"resourceRecordCount": 40, "lastModifiedDateTime": "2022-01-11T15:42Z" } }, {
"properties": { "name": "zone2.com.", "accountName": "TestAccount", "type":
"PRIMARY", "dnssecStatus": "UNSIGNED", "status": "ACTIVE", "owner": "test",
"resourceRecordCount": 40, "lastModifiedDateTime": "2022-01-12T12:41Z" } } ] }
```

  3. The following emphasizes the changes in how you will retrieve additional pages of results, besides the first.

    1. The new parameter **cursor** is required to navigate to other pages in the URI.

    2. For example, if you are attempting to retrieve the next page of results, select (copy) the value of the **next** attribute from the cusorInfo section (from the response) and add it to the cursor parameter in the request URL. 

**Method and URI** :

GET https://api.ultradns.com/v3/zones?cursor=em9uZTIuY29tLjpORVhU

JSON Example: List Metadata for Zones - cursorInfo Provided

JSON Example: List Metadata for Zones - cursorInfo Provided ```json {
"queryInfo": { "q": "em9uZTIuY29tLjpORVhU", "sort": "name", "reverse": false,
"limit": 2 }, "cursorInfo": { "previous": "em9uZTMuY29tLjpQUkVWSU9VUw==",
"first": "OkZJUlNU" }, "zones": [ { "properties": { "name": "zone3.com.",
"accountName": "TestAccount", "type": "PRIMARY", "dnssecStatus": "SIGNED",
"status": "SUSPENDED", "owner": "test", "resourceRecordCount": 40,
"lastModifiedDateTime": "2022-01-11T15:42Z" } } ] } ```

Similarly, select the values from the **first** , **last** , or **previous**
attribute from the cusorInfo section in the response to navigate to that
desired page.  

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)List
Metadata for Zones v3 - Cursor Based

The List Metadata for Zones v3 call differs from the Get Zone Metadata call in
that it provides a summary list of all zones (or all zones of a specified
type), rather than metadata for a particular zone.

Using the newest /v3 version, the List Metadata for Zones API is now utilizing
cursor-based pagination to return specified items in a dataset. The response
will contain the cursorInfo parameter with the **next** , **previous** ,
**first** and **last** values displayed.

Additionally, using the /v3 version of this API call, will now return the full
list of requested zones, and alleviate some customers that previously had to
use both versions to get the full list.

  * Add either the **next** or **previous** value in the request parameter of a subsequent GET call to view the details of the next set of zones (the number of responses per page are determined by the **limit** parameter).

  * The **first** and **last** values can be added in the request parameter of a subsequent GET call to view the first and the last page of details.

The List Metadata for Zones call is a GET call and is generated as follows:

**Method and URI** :

GET https://api.ultradns.com/v3/zones

**Parameters** : The following table lists the supported parameters for
customized search results:

Parameters for List Metadata for Zones - v3

Parameter |  Description |  Type  
---|---|---  
q |  The query used to construct the list. Query operators are:

  * _name_ â Name of the zone (allowing for partial string matches).

  * _zone_type_ â Returns zones of an identified type. If not specified, all zone types are returned. Valid values are:
    * ALIAS
    * PRIMARY 
    * SECONDARY

  * _zone_status_ â Returns zones with the identified status. Active zones are returned if not specified. Valid values are:
    * ACTIVE
    * SUSPENDED
    * ALL.

  * _account_name_ â Returns the zones based upon the account. If not specified, zones of all of the accounts that the user has access to will be returned. 
    * If the account name has space characters in it, the space characters need to be replaced with â%20.â For example, account âtest accountâ will need to be âtest%20account.â
  * **network** â Only applicable for those accounts with the UltraDNS2 feature enabled. Returns zones that are either on the UltraDNS (standard) network or are part of the UltraDNS2 service network. Valid values are:
  * **ultra1** (standard UltraDNS)
  * **ultra2**

|  String  
cursor |  Can be provided after the initial List Metadata for Zones request. Use with the cursorInfo details for fetching the next, previous, first or last page(s) of details. |  String. Optional.  
limit |  The maximum number of rows requested. Default number of requests returned is 100, but the maximum value supported is 1,000. |  Integer. Optional.  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a Zone
List v3 DTO in the body content.

**Errors** : An error is returned in following cases:

  * If you do not have permission to read zones.

JSON Example: List Metadata for Zones Response

JSON Example: List Metadata for Zones Response ```json { "queryInfo": { "q":
"", "limit": 2, "cursor": "MC0teC5uZXQu" }, "cursorInfo": { "next":
"Y3Vyc29yT3BlcmF0aW9uPU5FWFQmY3Vyc29yPWFiYy5jb20u", "last": "fjpMQVNU" },
"zones": [ { "properties": { "name":
"0-0-0-0-0-0-0-0-0-0-0-0-0-45-0-0-0-0-0-0-0-0-0-0-0-0-0.info.", "accountName":
"javauie2e", "type": "SECONDARY", "dnssecStatus": "UNSIGNED", "status":
"ACTIVE", "owner": "", "resourceRecordCount": 15, "lastModifiedDateTime":
"2019-11-20T14:20Z" } }, { "properties": { "name": "0-0-club.club.",
"accountName": "javauie2e", "type": "SECONDARY", "dnssecStatus": "UNSIGNED",
"status": "ACTIVE", "owner": "", "resourceRecordCount": 12,
"lastModifiedDateTime": "2019-11-20T14:22Z" } } ] } ```

JSON Example: List Metadata of Zones Response with cursorInfo Provided

{

"zones": [

{

"properties": {

"name": "100maruolo.online.",

"accountName": "javauie2e",

"type": "SECONDARY",

"dnssecStatus": "UNSIGNED",

"status": "ACTIVE",

"owner": "",

"resourceRecordCount": 11,

"lastModifiedDateTime": "2019-11-20T14:32Z"

}

},

{

"properties": {

"name": "100maruolo.press.",

"accountName": "javauie2e",

"type": "SECONDARY",

"dnssecStatus": "UNSIGNED",

"status": "ACTIVE",

"owner": "",

"resourceRecordCount": 11,

"lastModifiedDateTime": "2019-11-20T14:32Z"

}

}

],

}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)List
Metadata for Zones (Deprecated)

![](../../Resources/Images/MSP_User_Guide/Two Factor Mobile Authentication_68x68.png) |  **This call has been officially deprecated as of 2022-09-30.** We highly recommend that users begin to utilize the Migration Steps for List Metadata for Zones â v3 call as soon as possible to prevent any errors or confusion.  
---|---  
  
**As we continue to make improvements to our RestAPI performance, we are
requesting that users no longer use the List Metadata for Zones API call that
references either the /v1 or /v2 versioning, or no versioning at all.**

![](../../Resources/Images/MSP_User_Guide/Two Factor Mobile Authentication_68x68.png) |  Please note that for users continuing to use /v1, /v2, or no version specification in the List Metadata for Zones API call now that these calls are deprecated, we will no longer provide support resolution for **offset-based pagination**.  
---|---  
  
  * GET https://api.ultradns.com/v1/zones

  * GET https://api.ultradns.com/v2/zones

  * GET https://api.ultradns.com/zones

Instead, we highly recommend that all users begin to adopt the updated method
to using this API as soon as possible; Zone API. Please refer to the following
section for steps on how to migrate to the new API call - Migration Steps for
List Metadata for Zones â v3.

Moving forward, our goal is that our customers will not need to specify a
version, such as /v1 or v2, in any of our API calls on an ongoing basis. The
version-less API URL automatically routes to the latest official version.

The List Metadata for Zones call differs from the Get Zone Metadata call in
that it provides a summary list of all zones (or all zones of a specified
type), rather than metadata for a particular zone. The List Metadata for zones
call is a GET call and is generated as follows:

**Method and URI** :

GET https://api.ultradns.com/zones/

**Parameters** : Parameters are listed in the following table:

Parameters for List Metadata for Zones

Parameter |  Description |  Type  
---|---|---  
q |  The query used to construct the list. Query operators are:

  * **name** â Name of the zone (allowing for partial string matches).

  * **zone_type** â Returns zones of an identified type. If not specified, all zone types are returned. Valid values are ALIAS, PRIMARY, or SECONDARY.

  * **zone_status** â Returns zones with the identified status. Active zones are returned if not specified. Valid values are ACTIVE, SUSPENDED, or ALL. 

  * **dnssec_status** â Returns zones based upon the dnssec status. Valid values are SIGNED or UNSIGNED. If not specified, both types of zones will be returned.

  * **account_name** â Returns the zones based upon the account. If not specified, zones of all of the accounts that the user has access to will be returned. 
    * If the account name has space characters in it, the space characters need to be replaced with â%20.â For example, account âtest accountâ will need to be âtest%20account.â

|  String  
offset |  The position in the list for the first returned element (0 based). Default is â0.â |  Integer  
limit |  The maximum number of rows requested. Default is 100. |  Integer  
sort |  The sort column used to order the list. The valid values are:

  * NAME (default sort column)
  * ACCOUNT_NAME
  * ZONE_TYPE

|  String  
reverse |  List is sorted in Ascending order by default, with the parameter value being _false_. Enter _true_ to sort the list in Descending order by the sort column specified (or by Name if no sort value is entered). |  Boolean  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a [Zone
List DTO](Zone API DTOs.htm#Zone_List_DTO) in the body content.

**Errors** : An error is returned under the following conditions:

  * If you do not have permission to read zones.

JSON Example: Zone List

{  
"queryInfo": {  
"q": "",  
"sort": "NAME",  
"reverse": false,  
"limit": 100  
},  
"resultInfo": {  
"totalCount": 3,  
"offset": 0,  
"returnedCount": 3  
}  
"zones": [  
{  
"properties": {  
"name": "alias-example.com.",  
"accountName": "example",  
"owner": "example",  
"type": "ALIAS",  
"recordCount": 3,  
"dnssecStatus": "UNSIGNED",  
"lastModifiedDateTime": "2014-07-01T22:13Z"  
},  
"originalZoneNameâ: "example.com."  
},  
{  
"properties": {  
"name": "primary-example.com.",  
"accountName": "example",  
"owner": "example",  
"type": "PRIMARY",  
"recordCount": 3,  
"dnssecStatus": "UNSIGNED",  
"lastModifiedDateTime": "2014-07-01T22:13Z"  
},  
"registrarInfo": {  
"registrar": "Generic Domain Name Registrar",  
"whoisExpiration": "2015-01-01 00:00:00",  
"nameServers": {  
"ok": ["PDNS1.ULTRADNS.NET", "PDNS2.ULTRADNS.NET"],  
}  
},  
"restrictIpList": [  
{  
"startIP": "10.20.30.40",  
"endIP": "20.20.20.20",  
"comment": "Comment"  
}  
],  
"tsig": {  
"tsigKeyName":"Key",  
"tsigKeyValue": "This would be a hash if it was real,  
"description": "TSIG for primary-example.com",  
"tsigAlgorithm": "hmac-sha256"  
},  
"notifyAddresses": [  
{  
"notifyAddress": "2.4.5.6",  
"description": "East Coast Server"  
},  
{  
"notifyAddress": "5.6.7.8",  
"description": "West Coast Server"  
}  
]  
},  
{  
"properties": {  
"name": "secondary-example.com.",  
"accountName": "example",  
"owner": "example",  
"type": "SECONDARY",  
"recordCount": 3,  
"dnssecStatus": "UNSIGNED",  
"lastModifiedDateTime": "2014-07-01T22:13Z"  
},  
"primaryNameServers": {  
"nameServerIpList": {  
"nameServerIp1": {  
"ip": "1.2.3.4",  
"tsigKey": "key1",  
"tsigKeyValue": "value1"  
},  
"nameServerIp2": {  
"ip": "2.4.5.6",  
"tsigKey": "key2",  
"tsigKeyValue": "value2"  
},  
"nameServerIp3": {  
"ip": "3.4.5.6",  
"tsigKey": "key3",  
"tsigKeyValue": "value3"  
}  
}  
}  
}  
],  
}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Convert a
Zone

The Convert Zone call converts a Secondary Zone into a Primary Zone. The
Convert Zone call is a POST call and is generated as follows:

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/convert

**Parameters** : None

**Body** : Optionally, can include the [Zone DTOs](Zone API DTOs.htm) and the
use of the changeComment field. If providing DTO fields, the "Content-Type:
application/json" header is required.

**Response** : If conversion completes, Status Code 201 is returned with an
appropriate status message in the response body.

  * If conversion happens in the background, a Status Code 202 is returned along with an X-Task-ID header and a status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} does not exist.
  * If you do not have write permission for {zoneName}.
  * If {zoneName} is not a secondary zone.

JSON Example: Convert Zone with Change Comment

JSON Example: Convert Zone with Change Comment ```json { "changeComment":
"Converting zone 12/05/2020" } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Unalias a
Zone

Unaliasing a zone is the process of converting an Alias Zone into a Primary
Zone. When you unalias a zone, the following changes happen:

  * All of the data and zone configuration information is copied from the Primary to the Alias.
  * The Alias is converted into a Primary zone.
  * Any correlation between the original Primary and new Primary (formerly the Alias) is removed; the two are now wholly separate Primary zones.

The Unalias call is a POST call and is generated as follows:

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/unalias

**Parameters:** None

**Body:** Can include the following optional field. The "Content-Type:
application/json" header is required.

Field |  Description |  Type  
---|---|---  
changeComment |  An optional field allowing users to create a comment for a zone operation using up to 512 characters of free text, which can be viewed and searched for via the Audit Log Report. Not applicable for Batch or JSON Patch calls.  |  String.  
  
**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and a status message of Pending in the body content.

**Errors:** An error is returned under the following conditions:

  * If {zoneName} does not exist.
  * If you do not have permission to unalias {zoneName}.
  * If {zoneName} is a not an alias zone.

JSON Example: Unalias Zone with Change Comment

JSON Example: Unalias Zone with Change Comment ```json { "changeComment":
"Unalias this zone. No longer required." } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Suspend a
Zone

Suspending a zone allows you to temporarily stop serving data for a zone
without deleting that zone. When you suspend a zone, the following changes
happen:

  * The zone cannot be updated via a PUT or PATCH
  * Performing a GET will still return zone data

The Suspend call is a POST call and is generated as follows:

**Method and URI** :

POST https://api.ultradns.com/zones/{zoneName}/suspend

**Parameters** : None

**Body** : Can include the following optional field. The "Content-Type:
application/json" header is required.

Field |  Description |  Type  
---|---|---  
changeComment |  An optional field allowing users to create a comment for a zone operation using up to 512 characters of free text, which can be viewed and searched for via the Audit Log Report. Not applicable for Batch or JSON Patch calls.  |  String.  
  
**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and a status message of Pending in the body content.

**Errors:** An error is returned under the following conditions:

  * If {zoneName} does not exist.
  * If you do not have permission to unalias {zoneName}.
  * If {zoneName} is a not an alias zone.

JSON Example: Suspend a Zone with Change Comment

JSON Example: Suspend a Zone with Change Comment ```json { "changeComment":
"Suspend this zone. No longer active." } ```

# UnSuspend a Zone

For users that need to perform the UnSuspend a Zone API call, please reach out
to our Customer Support team for further assistance.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update a
Zone

The Update Zone call allows you to update certain aspects of either a Primary
or a Secondary Zone. You _cannot_ use this call to:

  * Update an Alias Zone.
  * Specify Primary Name Servers for a Primary zone.
  * Specify restrict IPs, TSIG, or Notify addresses for a Secondary Zone.

As this is a FULL update (replacing data) for Primary Zone updates, you must
include any necessary restrict IPs, Notify addresses, or Primary Name Servers
that apply. Any data not included with the update **will be deleted** from the
Primary Zone. See also Partially Update a Zone.

Update Zone is a PUT call and is generated as follows:

**Method and URI:**

PUT https://api.ultradns.com/zones/{zoneName}

**Parameters** : None

**Body** : Must include a [Zone Create DTO](Zone API
DTOs.htm#Zone_Create_DTO), specifically containing information as follows:

  * To update a Primary Zone, include only the createPrimaryInfo section. This section consists of a [Primary Zone DTO](Zone API DTOs.htm#Primary_Zone_DTO), of which you only need to provide the **restrictIPList** , **tsig** , and/or **notifyAddresses** sections.
  * **IMPORTANT:** Because this is a full update, any restrictIPs, tsig, or notifyAddresses not included will be deleted from the Primary Zone (unless the zone inherits the setting from the account).
  * To update a Secondary Zone, include only the _createSecondaryInfo_ section. This section consists of a [Secondary Zone DTO](Zone API DTOs.htm#Secondary_Zone_DTO), of which you only need to provide the _primaryNameServers_ section.
  * **IMPORTANT:** Because this is a full update, any primaryNameServers not included will be deleted from the Secondary Zone.

Examples of the information to be provided are shown below. If additional
sections are sent, they will be ignored.

For DTO reference, see the following tables:

  * [Zone Create DTO](Zone API DTOs.htm#Zone_Create_DTO)
  * [Primary Zone DTO](Zone API DTOs.htm#Primary_Zone_DTO)
  * [Secondary Zone DTO](Zone API DTOs.htm#Secondary_Zone_DTO)

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and a status message of âPendingâ in the body content.

**Errors:** An error is returned under the following conditions:

  * If {zoneName} does not exist.
  * If you do not have write permission for {zoneName}.
  * If zone is an Alias Zone (cannot update Alias zones).
  * If the wrong kind of data is submitted for a zone (see above for information required).

JSON Example: Update Restrict IP information for Primary Zone

{  
"primaryCreateInfo": {  
"restrictIPList": [  
{  
"startIP": "10.20.30.40",  
"endIP": "20.20.20.20",  
"comment": "Comment"  
}  
]  
},

"changeComment":"Updating zone"  
}

JSON Example: Update TSIG and Notify information for Primary Zone

{  
"primaryCreateInfo": {  
"tsig": {  
"tsigKeyName": "Key",  
"tsigKeyValue": "This would be a hash if it was real",  
"description": "TSIG for primary-example.com",  
"tsigAlgorithm": "hmac-sha256"  
},  
"notifyAddresses" : [  
{  
"notifyAddress": "2.4.5.6",  
"description": "East Coast Server"  
},  
{  
"notifyAddress": "5.6.7.8",  
"description": "West Coast Server"  
}  
]  
}  
}

JSON Example: Update Primary Name Server information for Secondary Zone

{  
"secondaryCreateInfo": {  
"primaryNameServers": {  
"nameServerIpList": {  
"nameServerIp1": {  
"ip": "1.2.3.4",  
"tsigKey": "key1",  
"tsigKeyValue": "value1"  
},  
"nameServerIp2": {  
"ip": "2.4.5.6",  
"tsigKey": "key2",  
"tsigKeyValue": "value2"  
},  
"nameServerIp3": {  
"ip": "3.4.5.6",  
"tsigKey": "key3",  
"tsigKeyValue": "value3"  
}  
}  
}  
}  
}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update a Zone

The Partial Update a Zone call is used to:

  * Update the restrictIPs, TSIG key, and/or Notify Address information for a Primary zone without having to explicitly list all of them. Any Restrict IPs, TSIGs or Notify Addresses not included in the call are retained on the server.
  * Update the Primary Name Servers for a Secondary zone without having to explicitly list all of them. Any Primary Name Servers not included in the call are retained on the server.

Alias zones cannot be updated.

Partially Update a Zone is a PATCH or a JSON PATCH call and is generated as
follows:

**Method and URI:**

PATCH https://api.ultradns.com/zones/[zoneName}

**Parameters** : None

**Body** : For standard XML or JSON formatted calls, the body must include a
[Zone Create DTO](Zone API DTOs.htm#Zone_Create_DTO), specifically containing
information as follows:

  * To update a Primary Zone, include only the createPrimaryInfo section. This section consists of a [Primary Zone DTO](Zone API DTOs.htm#Primary_Zone_DTO), of which you only need to provide the restrictIpList, tsig, and/or notifyAddresses sections.
  * Because this is a partial update, any restrictIps, tsig, or notifyAddresses not included in the call will be retained on the Primary zone.
  * To update a Secondary Zone, include only the createSecondaryInfo section. This section consists of a [Secondary Zone DTO](Zone API DTOs.htm#Secondary_Zone_DTO), of which you only need to provide the primaryNameServers section, or the notificationEmailAddress.
  * Because this is a partial update, any primaryNameServers not included will be retained on the Secondary Zone. If additional sections are sent, they will be ignored.

For [JSON PATCH formatted updates](../Making Updates via JSON
PATCH.htm#_Making_Updates_via "link to JSON PATCH section of this document"),
the body must include a [JSON PATCH DTO](../Making Updates via JSON
PATCH.htm#JSON_PATCH_DTO).

For DTO reference, see the following tables:

  * [JSON PATCH DTO](../Making Updates via JSON PATCH.htm#JSON_PATCH_DTO)
  * [Zone Create DTO](Zone API DTOs.htm#Zone_Create_DTO)
  * [Primary Zone DTO](Zone API DTOs.htm#Primary_Zone_DTO)
  * [Secondary Zone DTO](Zone API DTOs.htm#Secondary_Zone_DTO)

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors:** An error is returned under the following conditions:

  * If {zoneName} does not exist.
  * If you do not have write permission for {zoneName}.
  * If zone is an Alias Zone (Alias Zones cannot be updated).
  * If the wrong kind of data is submitted for a zone (see above for information required).

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Request
Zone Transfer

The Request Zone Transfer call sends an AXFR request through a Secondary Zone,
to the primary name server in order to update the Secondary Zone with
information from the Primary Zone.

The {zoneName} identified in the call should be the name of the Secondary Zone
to be updated.

The Request Zone Transfer call is a POST call and is generated as follows:

**Method and URI:**

POST https://api.ultradns.com/zones/{zoneName}/transfer

**Parameters:** None

**Body:** None

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If task happens in the background, Status Code 202 is returned along with an X-Task-ID header and status message of Pending in the body content.

**Errors:** An error is returned under the following conditions:

  * If {zoneName} does not exist.
  * If you do not have permission to update {zoneName}.
  * If {zoneName} does not refer to a Secondary Zone.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Export a
Zone

Exporting a Zone will create a task to export the zone details into a BIND
file. Once the task has been completed the BIND file can be downloaded.

**Method and URI:**

POST https://api.ultradns.com/zones/export

**Parameters:** None

**Body:** The body must include the zonename that is being exported.

Parameter |  Description |  Type  
---|---|---  
zoneNames |  The name or names of the zones that are being exported, with or without the trailing dot. Multiple zone names must be comma separated.  |  String. Must be a valid zone name.  
  
**Response** : If task completes, Status Code 202 Accepted is returned along
with an X-Task-ID header and status message of Pending in the body content. To
check the status of the export, use the Get the Status of a Task call.

**Errors:** An error is returned under the following conditions:

  * If {zoneName} does not exist.

  * If you do not have permission to export {zoneName}.

  * If zoneNames contains more than 250 zone names for export.

JSON Example: Export a Zone Body example

JSON Example: Export a Zone Body example ```json { "zoneNames": [ "name.com",
"name2.com." ] } ```

JSON Example: Export Zone BIND File Details

  
;File created: 12/01/2020 16:13  
;Record count: 6  
$ORIGIN 00-ben-doc-ns.com.  
@ 86400 IN SOA udns1.ultradns.net. rajender\\.aindla.example.biz. (  
2018062747 ;Serial  
10800 ;Refresh  
3600 ;Retry  
2592000 ;Expire  
10800 ;Minimum  
)  
@ 86400 IN NS udns1.ultradns.net.  
@ 86400 IN NS udns2.ultradns.net.  
www.momandpopgas.com 600 IN A 1.1.1.1  
;record belongs to the pool HealthProbeTest.com.00-ben-doc-ns.com.  
HealthProbeTest.com 120 IN A 6.5.4.3  
mydeadpool.com 60 IN A 2.2.2.2

### Get the Status of a Task

**Method and URI** :

GET https://api.ultradns.com/tasks/{taskId}

**Parameters** : Must include the specific Task ID.

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a Task
DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If {taskId} does not exist.

  * If you do not have permission to read {taskId}.

### Get the Results of a Task

**Method and URI** :

GET https://api.ultradns.com/tasks/{taskId}/result

**Parameters** : Must include a Task ID.

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a Task
DTO in the body content.

The content will be returned as a downloadable file. The name of the file will
be the {taskId} that was submitted with the request. The file extension and
content type are set by the background task and will be appropriate to the
data returned.

**Errors** : An error is returned under the following conditions:

  * If {taskId} does not exist.

  * If you do not have permission for the task associated with the supplied {taskId}.

  * If task is not yet completed.

### Task DTO

The Task DTO is used to describes the current state of a task.

Task DTO

Field |  Description |  Type  
---|---|---  
taskId |  Id for the task. |  UUID  
code |  Current state of the task. |  Use one from: 

  * PENDING 
  * IN_PROCESS
  * COMPLET
  * ERROR 

  
message |  Current message for the task. |  String  
resultUri |  If task is COMPLETE, the URI from where the resulting data can be downloaded. |  URI  
  
JSON Example: Task Status

{  
"taskId": "0b40c7dd-748d-4c49-8506-26f0c7d2ea9c",  
"Code": "COMPLETE",  
"message": "Processing complete",  
"resultUri": "/tasks/0b40c7dd-748d-4c49-8506-26f0c7d2ea9c/result"  
}

