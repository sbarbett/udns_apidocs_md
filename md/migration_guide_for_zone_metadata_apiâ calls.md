

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

## Migration Guide for Zone Metadata API Calls

The following content outlines the Migration Steps for List Metadata for Zones
â Cursor Based Pagination for customers that are still trying to use the
deprecated version of these API calls, to the [List Metadata for Zones v3 -
Cursor Based](Zone API/Zone API.htm#List) call. Please note, that this only
applies to the API call utilizing /v1 or /v2 AND offset in the method.

  1. Remove the version in your URL as shown below.

    1. **Your existing URL format** :  
  
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

GET https://api.ultradns.com/zones/

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

  

## Steps to Migrate from GET Zones of an Account to List Metadata for Zones
â v3

![](../Resources/Images/Rest-API_User_Guide/Introduction_62x66.png) |  **The GET Zones of an Account API call has been deprecated as of 2022-09-30**. As an alternative to this API call, users should use the [List Metadata for Zones v3 - Cursor Based](Zone API/Zone API.htm#List) API call.  
---|---  
  
As we continue to make improvements to our RestAPI performance and remove
redundancy, we are requesting that users no longer use the _GET Zones of an
Account (Deprecated)_ API call. The updated [List Metadata for Zones v3 -
Cursor Based](Zone API/Zone API.htm#List) API call will provide the same
response details as the Get Zones of an Account API call did, as well as
providing an updated pagination method.

Please use the following steps below to migrate your existing Get Zones of an
Account API to the **List Metadata for Zones â v3** call.

  1. Change the URL to the List Metadata for Zone -v3 URL as shown below.

    1. **Your existing URL format** \- 

https://api.ultradns.com/accounts/{accountName}/zones

    2. **Your new URL format** \- 

https://api.ultradns.com/v3/zones?q=account_name:{accountName}

  2. The following content emphasizes the changes in how you will retrieve the first page of results.

    1. There are no changes required in retrieving the first page of result details. Performing the above URL change will be sufficient.

    2. There is a difference in the pagination behavior when using the new /v3 call. The new version does not return the previously used resultInfo section, instead, it returns a new section called cursorInfo. This section provides the cursor-based information used to navigate to the different pages of results that can be returned. The cursorInfo section contains four values â **first** , **next** , **previous** , and **last**.

      1. If there are additional pages of details that can be navigated to, the cursorInfo section will contain the **previous** and **first** values.

      2. If there are no additional pages to navigate to, the cursorInfo section will be empty. 

The following API example shows a cursorInfo section with **next** and
**last** values available.

**Method and URI** :

GET https://api.ultradns.com/v3/zones?q=account_name:TestAccount

JSON Example: List Metadata for Zones v3 Response

JSON Example: List Metadata for Zones v3 Response ```json { "queryInfo": {
"q": "account_name:TestAccount", "sort": "name", "reverse": false, "limit": 2
}, "cursorInfo": { "next": "em9uZTIuY29tLjpORVhU", "last": "fjpMQVNU" },
"zones": [ { "properties": { "name": "zone1.com.", "accountName":
"TestAccount", "type": "PRIMARY", "dnssecStatus": "SIGNED", "status":
"SUSPENDED", "owner": "test", "resourceRecordCount": 40,
"lastModifiedDateTime": "2022-01-11T15:42Z" } }, { "properties": { "name":
"zone2.com.", "accountName": "TestAccount", "type": "PRIMARY", "dnssecStatus":
"UNSIGNED", "status": "ACTIVE", "owner": "test", "resourceRecordCount": 40,
"lastModifiedDateTime": "2022-01-12T12:41Z" } } ] } ```

3\. Retrieving other pages of result details.

a. You need to add a new parameter called **cursor** in order to navigate to
the other pages, when viewing details from the current page.

b. When retrieving the next page, select the value of the next attribute from
the **cusorInfo** section (from the response) and add it to the cursor
parameter in request URL.

**Method and URI** :

GET
https://api.ultradns.com/v3/zones?q=account_name:TestAccount&cursor=em9uZTIuY29tLjpORVhU

JSON Example: List of Zone Metadata v3 - cursor Included

JSON Example: List of Zone Metadata v3 - cursor Included ```json {
"queryInfo": { "q": "account_name:TestAccount", "sort": "name", "reverse":
false, "limit": 2 }, "cursorInfo": { "previous":
"em9uZTMuY29tLjpQUkVWSU9VUw==", "first": "OkZJUlNU" }, "zones": [ {
"properties": { "name": "zone3.com.", "accountName": "TestAccount", "type":
"PRIMARY", "dnssecStatus": "SIGNED", "status": "SUSPENDED", "owner": "test",
"resourceRecordCount": 40, "lastModifiedDateTime": "2022-01-11T15:42Z" } } ] }
```

4\. Similarly, select the values of the first, last, or previous attribute
from the cusorInfo section (from the response) in order to navigate to the
desired page.

