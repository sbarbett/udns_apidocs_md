

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

# Extended Accounts API

The Extended Accounts API calls allow you to obtain additional information
beyond the initial Accounts API created for the REST API. This new section
includes information on various account-level objects such as: User Creation,
Account Management, Security Group Management (Security Preferences, Security
Questions, System Preferences), and User MetaData (for a current user).

This chapter provides details on the Accounts API calls available for use, as
well as detailed Account DTO (Data Transfer Object) information. Where DTOs
are required in the body of the call, or are returned as a response, cross
reference links are provided to the specific table containing the details of
DTO contents.

## Zone Transfer API Calls

With this method, the zone transfer settings can be configured at the account
level. Zone transfer settings include: Restrict IPs, TSIGs (transaction
signature keys), and Notify Addresses.

When configured at the Account level, zone transfer settings, also referred to
as Transfer ACL (Access Control List), are automatically inherited by every
Primary zone belonging to the account that do not already have these items
configured. They are also automatically applied to any new Primary zones
created for the account.

Zone transfer settings can be changed at the zone level where appropriate,
thereby overriding the account level settings. See [Zone API](../Zone API/Zone
API.htm#_Ref395097719), [Update a Zone](../Zone API/Zone
API.htm#_Ref497481380), and [Partially Update a Zone](../Zone API/Zone
API.htm#_Ref395092542) sections of this guide for setting zone transfer
restrictions at the zone level.

![](../../Resources/Images/Rest-API_User_Guide/Introduction_62x66.png) |  The Account-Level Zone Transfer settings calls have replaced the Add/Remove Restrict IPs for All Zones of Account API calls. If you have previously used those calls, please update your processes to use the new Transfer ACL calls described below.  
---|---  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Create
Zone Transfer Settings â Account Level

Create Zone Transfer Settings is a POST call and is generated as follows:

**Method and URI** :

POST https://api.ultradns.com/accounts/{accountName}/transfer-acl HTTP/1.1

**Parameters** : None

**Body** : Must include a Transfer ACL DTO

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body. Additionally, the timestamp
of all active primary zones in the account will be updated.

**Errors** : An error is returned under the following conditions:

  * You do not have permission to configure transfer settings for the specified {accountName}.

  * If the {accountName} does not exist.

  * If the provided Transfer ACL data is incorrect.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Zone Transfer Settings â Account Level

Updates to account level zone transfer settings (or Transfer ACL) are
automatically inherited by every Primary zone owned by the account. Zone
transfer settings include Restricted IPs, TSIGs (transaction signature keys),
and Notify Addresses.

**IMPORTANT** : Because this is a full update, any Restrict IPs, TSIG, or
Notify Addresses not included will be deleted from the Account level settings,
and the deletions will be subsequently reflected in the zone transfer settings
for all primary zones that inherit the account-level settings.

Update Zone Transfer Settings is a PUT call and is generated as follows:

**Method and URI** :

PUT https://api.ultradns.com/accounts/{accountName}/transfer-acl HTTP/1.1

**Parameters** : None

**Body** : Must include a Transfer ACL DTO

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body. Additionally, the timestamp
of all primary zones in the account that inherits account-level settings (that
are subsequently updated with these changes) will be updated.

**Errors** : An error is returned under the following conditions:

  * You do not have permission to configure transfer settings for the specified {accountName}.
  * If the {accountName} does not exist.
  * If the provided Transfer ACL data is incorrect. This includes restrictIP information where the range included for the update overlaps an existing IP address/range.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update Zone Transfer Settings â Account Level

Updates to account level zone transfer settings (or Transfer ACL) are
automatically inherited by every Primary zone owned by the account. Zone
transfer settings include Restricted IPs, TSIGs (transaction signature keys),
and Notify Addresses.

Because this is a partial update, any Restrict IPs or Notify Addresses
included will be appended to any existing settings, and TSIG will be updated
if provided. These changes will subsequently be reflected to the Zone Transfer
settings for all Primary zones that inherit account-level settings.

The Partial Update Zone Transfer Settings is a PATCH call and is generated as
follows:

**Method and URI** :

PATCH https://api.ultradns.com/accounts/{accountName}/transfer-acl HTTP/1.1

**Parameters** : None

**Body** : Must include a Transfer ACL DTO.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body. Additionally, the timestamp
of all primary zones in the account that inherit account-level settings (that
are subsequently updated with these changes) will be updated.

**Errors** : An error is returned under the following conditions:

  * You do not have permission to configure transfer settings for the specified {accountName}.
  * If the {accountName} does not exist.
  * If the provided Transfer ACL data is incorrect. This includes restrictIP information where the range included for the update overlaps an existing IP address/range.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Remove
Zone Transfer Settings â Account Level

This call removes zone transfer settings from the account level. The removal
of account-level zone transfer information is automatically passed to all
active primary zones of the account that are configured to inherit account
level zone transfer settings.

![](../../Resources/Images/Rest-API_User_Guide/Introduction_68x71.png) |  The Account-Level Zone Transfer settings calls have replaced the Add/Remove Restrict IPs for All Zones of Account API calls. If you have previously used those calls, please update your processes to use the new Transfer ACL calls described here.  
---|---  
  
The removal Zone Transfer Settings is a DELETE call and is generated as
follows:

**Method and URI** :

DELETE https://api.ultradns.com/accounts/{accountName}/transfer-acl HTTP/1.1

**Parameters** : None

**Body** : None

**Response** : If delete completes, Status Code 204 is returned with no
content in the body. Additionally, the timestamp of all active primary zones
in the account will be updated.

**Errors** : An error is returned under the following conditions:

  * You do not have permission to configure transfer settings for the specified {accountName}.
  * If the {accountName} does not exist.

# Allowed IP Ranges

The Allowed IP Ranges (Account Level) API calls provide the ability to limit
access to the UltraDNS Portal or to the REST API, and to one or more
enumerated ranges of IP addresses. If this is not set, then all IP addresses
are valid. If it is set, then only clients within the specified IP ranges will
be allowed to access the UltraDNS Portal or to REST API. The IP restrictions
can be limited to just the UltraDNS Portal, just the API, or can apply to
both.

If you accidentally block yourself from accessing both the UltraDNS Portal and
the REST API, you will need to contact customer support and verify your
identity before you are able to access any UltraDNS services.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get All
Allowed Account-Level IP Range

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/allowedips

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
AccountIPRangeList DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If you do not have permission to specify account-level IP restrictions.

JSON Example: GET All Allowed Account-Level IP Range

{  
"resultInfo": {  
"totalCount": 1,  
"offset": 0,  
"returnedCount": 1  
}  
"accountIPRanges": [  
{  
"guid": 0F0840B06DE2D354",  
"startIP": "1.1.1.1",  
"endIP": "2.2.2.2",  
"applications": [  
"UI"  
]  
}  
]  
}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Add an
Allowed Account-Level IP Range

**Method and URI** :

POST https://api.ultradns.com/accounts/{accountName}/allowedips

**Parameters** : None

**Body** : Must include an AccountIPRange DTO.

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If you do have permission to specify account-level IP restrictions.

JSON Example: Add an Allowed Account-Level IP Range

{  
"startIP": "10.10.10.10",  
"endIP": "20.20.20.20",  
"comments": "This is a comment",  
"applications": [  
"UI"  
]  
}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Allowed Account-Level IP Range

**Method and URI** :

PUT https://api.ultradns.com/accounts/{accountName}/allowedips/{guid}

**Parameters** : None

**Body** : Must include an AccountIPRange DTO.

**Response** : If task completes, Status Code 200 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If you do have permission to specify account-level IP restrictions.

JSON Example: Update an Allowed Account-Level IP Range

JSON Example: Update an Allowed Account-Level IP Range ```json { "startIP":
"11.11.11.11", "endIP": "18.18.18.18", "comments": "This is updated comment",
"applications": [ "UI" ] } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Delete an
Allowed Account-Level IP Range

**Method and URI** :

DELETE https://api.ultradns.com/accounts/{accountName}/allowedips/{guid}

**Parameters** : None

**Body** : None

**Response** : If delete completes, Status Code 204 is returned with no body
content.

**Errors** : An error is returned under the following conditions:

  * If it is not a valid {guid}.

  * If you do not have permission to specify account-level IP restrictions.

## Accounts API

The Accounts API calls allow you to obtain information on various account-
level objects as well as manage the Zone Transfer information for the account.

This chapter provides details on the Accounts API calls available for use, as
well as detailed Account DTO (Data Transfer Object) information. Where DTOs
are required in the body of the call, or are returned as a response, cross
reference links are provided to the specific table containing the details of
DTO contents.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)GET
Accounts of a User

Provides a list of all accounts to which the user is assigned. The âuserâ
is assumed to be the user whose credentials are currently being used for API
call authentication.

**Method and URI** :

GET https://api.ultradns.com/accounts

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
Account List DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If you do not have permission to view accounts

JSON Example: Account List DTO

{

resultInfo: {

totalCount: 1

offset: 0

returnedCount: 1

}

accounts: [

{

"accountName": "WidgetEng",

"accountHolderUserName": "Widget Engineering",

"ownerUserName": "AlphaEngineer",

"numberOfUsers": 15,

"numberOfGroups": 3,

"accountType": "ORGANIZATION"

"features": [

"ADVDIRECTIONAL",

"DNSSEC",

"MAILBACKER",

"RECURSIVE",

"REPORTING",

"RNAME",

"SITEBACKER",

"TRAFFICCNTRL",

"WEBFORWARD"

]

}

]

}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)GET a
Single Account

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
Account List DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If you do not have permission to view the account.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)GET Users
of an Account

This call returns a list of all of the Users assigned to a specified
accountName, which are sorted by user name in ascending order.

Method and URI:

GET https://api.ultradns.com/accounts/{accountName}/users

**Parameters:** None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with User DTO
details in the body content.

**Errors** : An error is returned under the following conditions:

  * If you do not have permission to access the specified {accountName}.

  * If you do not have permission to view users in the {accountName}.

  * If you are not part of the Owner, ADMINISTRATIVE, or SECURITY_ADMINISTRATION groups.

JSON Example: User List DTO

{

"resultInfo": {

"totalCount": 10,

"offset": 0,

"returnedCount": 10

},

"users": [

{

"userName": "JTDoe",

"firstName": "John",

"lastName": "Doe",

"groupName": REPORTING,

"primaryEmail": "jtdoe@example.biz",

"secondaryEmail": "jtdoe@team.example",

"phone": "13333333333",

"fax": "14444444444",

"mobile": "12222222222",

"companyName": "Example",

"apiOnlyUser": false,

"authType": "SHA1",

"isStandAlone": false,

"passwordAge": 0,

"passwordExpiration": 90,

"sessionTimeout": 10,

"userStatus": "ACTIVE",

"apiOnlyUser": false

},

{

"userName": "JPRoe",

"firstName": "Jane",

"lastName": "Roe",

"groupName": ADMINISTRATIVE,

"primaryEmail": "jproe@example.biz",

"secondaryEmail": "jproe@team.example",

"phone": "15555555555",

"fax": "16666666666",

"mobile": "17777777777",

"companyName": "Example",

"apiOnlyUser": true,

"twoFactorAuth": "SMS2FA",

"authType": "SHA1",

"isStandAlone": false,

"passwordAge": 0,

"passwordExpiration": 90,

"sessionTimeout": 10,

"userStatus": "ACTIVE",

"apiOnlyUser": false

}

]

}

![](../../Resources/Images/Rest-API_User_Guide/Introduction_73x85.png) |  Response of this call can be returned in a .CSV format, but will require an additional step beyond the default JSON requirements. In the header section, you will need to include the additional field: _Accept: text/csv_.   
---|---  
  
CSV Example: List of users response in .CSV format

Status 200 OK

[

userName, firstName, lastName, groupName, primaryEmail, secondaryEmail, phone,
fax, mobile, companyName, apiOnlyUser, authType, isStandAlone, passwordAge,
passwordExpiration, sessionTimeout, userStatus, apiOnlyUser

JTDoe,John,Doe,REPORTING,jtdoe@example.biz,jtdoe@team.example,13333333333,14444444444,12222222222,Example,SHA1,false,0,90,10,ACTIVE,false

JPRoe,Jane,Roe,ADMINISTRATIVE,jproe@example.biz,jproe@team.example,15555555555,16666666666,17777777777,Example,SHA1,false,0,90,10,ACTIVE,false

]

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Delete
Access of a User from an Account

This call removes the access of a User that is assigned to a specified
Account. If the designated user is only assigned to one account, this call
will delete the user.

Once a userâs access is deleted, their email address will be automatically
be unsubscribed from https://status.ultradns.com/, which provides notification
emails for UltraDNS system incidents and planned maintenance activity.

Please be aware that with the enhancement of the new Security Groups, the
following exceptions and changes have been added when a user attempts to
perform the Delete Access of a User API call.

  * The user identified as the (Primary) Owner has the authority to delete any user in the account except themselves.

  * Users in the ADMINISTRATIVE group can delete users in the account as long as it isnât themselves, the Owner, or users in the ADMINISTRATIVE group.

  * Users in the SECURITY-ADMINISTRATION group can delete users in the account as long as it isnât themselves, the Owner, or users in the ADMINISTRATIVE and SECURITY-ADMINISTRATION groups.

**Method and URI** :

DELETE https://api.ultradns.com/accounts/{accountName}/users/{userName}

**Parameters:** None

**Body** : None

**Response** : If delete completes, Status Code 204 is returned with no body
content.

**Errors** : An error is returned under the following conditions:

  * Invalid User {username}.

  * Invalid Account {accountName}. 

  * If the target account is not currently in an Active state.

  * If you do not have permission to perform the delete for the account.

  * User is no longer affiliated to the Account.

## Account DTOs

The sections and tables below, provide detailed information about the contents
of the DTOs used for Account API calls. Where a DTO field consists of the
contents of another DTO, a cross reference link to the associated DTO is
provided. When possible, return links to the âparentâ DTO are also
provided, along with links to the API calls that use the DTO.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Account
DTO

This call provides summary information about the Account. This is integrated
into the Account List DTO, which is returned by the Get Accounts of User call.

Account DTO

Field |  Description |  Type |  Editable in PUT/PATCH  
---|---|---|---  
accountName |  Name of the account. |  Name. |  Yes  
accountHolderUserName |  User name for the account holder. |  Name. |  No  
ownerUserName |  User name of the owner (primary user). |  Name. |  Yes  
ownerAddress |  Address of the owner (primary user). |  Address DTO |  Yes  
accountHolderAddress |  Address of the account holder. (This field will be returned and can be updated only for the ORGANIZATION account type) |  Address DTO |  Yes (only for accounts of type ORGANIZATION). If a user tries to update the accountHolderAddress for non-ORGANIZATION account types, a validation error will be returned.   
numberOfUsers |  User(s) count/quantity for account. |  Integer. |  No  
numberOfGroups |  Group count/quantity for account. |  Integer. |  No  
accountType |  Type of the account. |  One from: 

  * INDIVIDUAL
  * ORGANIZATION

|  No  
features |  List of returned features per account, that can include:

  * ADVDIRECTIONAL
  * DNSSEC
  * HOST_ALIAS
  * MAIL_FORWARD
  * MDDI
  * RECURSIVE
  * REPORTING
  * RNAME
  * SIGN_SECONDARY
  * SITEBACKER
  * TRAFFICCNTRL
  * TWO_FACTOR_AUTH
  * ULTRA2
  * WEBFORWARD

|  String. |  No  
accountId |  The short name of the account. (This is found from the ACCT_NBR column from the BILLING_ACCOUNT table). |  Name. |  No  
status |  The status of the account. |  One from:

  * Active
  * Suspended

|  No  
created |  Date the account was created in the ISO 8601 format. |  Date. |  No  
defaultSOAEmail |  The default value used for the SOA email address in newly created zones. If null, not present. |  Email. |  Yes  
restrictAccessIPs |  List of IP restrictions that apply for all users in the account. |  List of RestrictAccessIP DTO.List of RestrictAccesIP DTO. |  Yes  
accountNameServers |  The list of the Account Name Servers, along with the state of the Name Server. |  List of AccountNameServer DTO. |  No  
usageLimit |  The maxiumum number of various record types, queries, and/or pools that are configured for your account. |  List of UsageLimit DTO.  |  No  
  
JSON Example: Account DTO Body

JSON Example: Account DTO Body ```json { "accountName": "sample",
"accountHolderUserName": "sampleUser", "ownerUserName": "sampleUser",
"numberOfUsers": 1, "numberOfGroups": 3, "accountType": "ORGANIZATION",
"accountID": "AG02-200", "status": "ACTIVE", "created": "20150101T12:00Z",
"defaultSOAEmail": "test@ultradns.com", "accountHolderAddress": { "address1":
"address1", "address2": "address2", "country": "USA", "state": "Texas",
"city": "Indore", "zip": "452010" }, "accountNameServers": [ { "nameServer":
"ns1.pdns.com.", "state": "Active" }, { "nameServer": "ns2.pdns.com.",
"state": "Active" } ], "usageLimit": { "sitebackerRecordsLimit": 3000,
"domainsLimit": 900, "recordsLimit": 8900, "queriesLimit": 808090,
"webForwardsLimit": 24354, "trafficControllerRecordsLimit": 7868,
"directionalPoolsLimit": 7979 } } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Account
List DTO

Account List DTO

Field |  Description |  Type  
---|---|---  
accounts/account |  One of the returned accounts. The structure should match the Account DTO. |  Account DTO.  
features |  List of returned features per account, that can include:

  * ADVDIRECTIONAL
  * DNSSEC
  * HOST_ALIAS
  * MAIL_FORWARD
  * MDDI
  * RECURSIVE
  * REPORTING
  * RNAME
  * SIGN_SECONDARY
  * SITEBACKER
  * TRAFFICCNTRL
  * TWO_FACTOR_AUTH
  * ULTRA2
  * WEBFORWARD

|  String.  
queryinfo/q |  The query used to construct the list. |  String.  
queryinfo/sort |  The sort column used to order the list. |  String.  
queryinfo/reverse |  Whether the list is ascending (false) or descending (true). |  Boolean.  
queryinfo/limit |  The maximum number of rows requested. |  Integer.  
resultInfo/totalCount |  Count of all zones in the system for the specified query. |  Integer.  
resultInfo/offset |  The position in the list for the first returned element (0 based). |  Integer.  
resultInfo/returnedCount |  The number of records returned. |  Integer.  
  
JSON Example: Account List DTO Body

{

"accounts": [

{

"accountName": "sample",

"accountHolderUsername": "sampleUser",

"ownerUserName": "sampleUser",

"numberOfUsers": 1,

"numberOfGroups": 1,

"accountType": "ORGANIZATION",

}

]

"queryInfo": {

"q": " ",

"sort": " ",

"reverse": "TRUE",

"limit": 2

}

"resultInfo": {

"totalCount": 2,

"offset": 0,

"returnedCount": 2

}

}

### AccountNameServer DTO

AccountNameServer DTO

Field |  Description |  Type  
---|---|---  
nameServer |  The Account Name Server. |  String.  
ipv4Address |  An IPV4 address. |  String.  
ipv6Address |  An IPV6 address. |  String.  
state |  The Record state (i.e. Active or Pending). |  String.  
  
### UsageLimit DTO

Usage Limit DTO

Field |  Description |  Type  
---|---|---  
sitebackerRecords |  Usage limit of querying sitebacker records. |  Integer  
zones |  Usage limit of queryingZones. |  Integer  
records |  Usage limit of querying resource records. |  Integer  
queries |  Usage limit of querying any DNS-Queries. |  Integer  
webForwards |  Usage limit of querying web forward records. |  Integer  
trafficControllerRecords |  Usage limit of querying traffic controller records. |  Integer  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)User DTO

User DTO

Field |  Description |  Type  
---|---|---  
userName |  User name in UltraDNS system. |  Name  
firstName |  User's given name. |  String  
lastName |  User's family name. |  String  
primaryEmail |  The main email address for the user. **This field cannot be updated manually. A Customer Support ticket must be created to update this field.** |  Email  
secondaryEmail |  The backup email address for the user. Optional. **This field cannot be updated manually. A Customer Support ticket must be created to update this field.** |  Email  
phone |  Phone number. |  String  
fax |  Fax number. Optional. |  String  
mobile |  Cell phone number. Optional. |  String  
companyName |  Name of the company. |  String  
twoFactorNumDeferred |  Indicates how many deferrals the user has left (out of a max of 3) to configure Multi-Factor Authentication on their account. When the value equals 3, the userâs account will be suspended. Value between 0-3 will be returned. Default value of 0.  |  Boolean  
twoFactorEnrollRequired |  Indicates if the account has been enrolled in Mandatory Multi-Factor Authentication (MFA).

  * true = Yes
  * false = No (default) 

|  Boolean  
apiOnlyUser |  Displays if the designated user ONLY has API access (true), or of the user has both UI AND API access (false). |  Boolean  
twoFactorAuth  |  Displays if 2FA is enabled for the userâs account, and the type of 2FA being used (SMS2FA). If the userâs account does not have 2FA enabled, this field will be ignored.  |  String.   
authType |  Displays the User Authentication type. Optional. |  String  
groupName |  Displays the name of the group the user is currently assigned to. It will only be returned when retrieving ALL the users of the account. |  String  
lastLoggedin |  Displays the last logged in time for the user. It will only be returned when retrieving ALL the users of the account. |  String  
passwordExpiration |  Displays the password expiration time (in days) for the user. It will only be returned when retrieving ALL the users of the account.  If this preference is set at the account level, then the account level preference will be returned.  |  Integer  
passwordAge |  Displays how long ago (in days) the user last changed their password. It will only be returned when retrieving ALL the users of the account. |  Integer  
sessionTimeout |  Displays the duration of time (in minutes) a user has before their session will automatically be timed-out. It will only be returned when retrieving ALL the users of the account.  If this preference is set at the account level, the account level preference will be returned.  |  Integer  
  
JSON Example: User DTO Body

JSON Example: User DTO Body ```json { "userName": "JTDoe", "firstName":
"John", "lastName": "Doe", "twoFactorNumDeferred": 1,
"twoFactorEnrollRequired": true, "apiOnlyUser": false } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)User List
DTO

User List DTO

Field |  Description |  Type  
---|---|---  
users/user |  One of the returned users. The structure will match the User DTO. |  List of User DTO.  
queryinfo/q |  The query used to construct the list. |  String.  
queryinfo/sort |  The sort column used to order the list. |  String.  
queryinfo/reverse |  Whether the list is ascending (false) or descending (true).  |  Boolean.  
queryInfo/limit |  The maximum number of rows requested. |  Integer.  
resultInfo/totalCount |  Count of all zones in the system for the specified query. |  Integer.  
resultInfo/offset |  The position in the list for the first returned element (0 based). |  Integer.  
resultInfo/returnedCount |  The number of records returned. |  Integer.  
  
JSON Example: UserList DTO Body

{

"users" : [

{

"userName": "JTDOE",

"firstName": "John",

"lastName": "Doe"

}

],

"queryInfo": {

"q": " ",

"sort": " ",

"reverse": "TRUE",

"limit": 2

},

"resultInfo": {

"totalCount": 2,

"offset": ,

"returnedCount": 2

}

}

### Address DTO

Address DTO

Field |  Description |  Type  
---|---|---  
address1 |  The first line of the address. |  String.  
address2 |  The second line of an address if necessary. Optional. |  String.  
country |  Country the address resides in. |  String. Validated using the ISO-3-661 two letter codes for countries.  
state |  The state or province the address resides in. Optional if outside of the United States or Canada. |  String. Validated using the ISO-3166-2: US standard for US States and territories, and the ISO-3661-2: CA Standard for Canadian provinces and territories.  
city |  The city in which the address resides. |  String.  
zip |  The zip code / postal code for the address. Optional |  String.  
  
## User MetaData

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Transfer
ACL DTO

The Transfer ACL DTO contains zone transfer information to be set at the
account level. This DTO is required in the body of the Create Zone Transfer
Settings â Account Level, Update Zone Transfer Settings â Account Level,
and Partially Update Zone Transfer Settings â Account Level.

Zone transfer settings can also be changed or removed at the zone level where
appropriate. See [Zone API](../Zone API/Zone API.htm#_Ref395097719), and
[Partially Update a Zone](../Zone API/Zone API.htm#_Ref395092542) sections of
this guide for information on configuring zone transfer settings at the zone
level.

Transfer ACL DTO

Field |  Description |  Type  
---|---|---  
restrictIPList |  The list of IP ranges that are allowed to use AXFR to transfer primary zones out. |  List of [Zone API](../Zone API/Zone API.htm#_Ref395099778)s.  
tsig |  The TSIG information for the primary zone. |  [Zone API](../Zone API/Zone API.htm#_Ref395099815).  
notifyAddresses |  The addresses that are notified when updates are made to the primary zone. |  List of [Zone API](../Zone API/Zone API.htm#_Ref395099840)s.  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)AccountIPRange
DTO

AccountIPRange DTO

Field |  Description |  Type  
---|---|---  
guid |  The internal ID for range. If specified during creation, it is ignored. It is returned when getting the list of all allowed IP ranges. |  String.  
startIP |  The first allowed IP address in the range, inclusive. |  Valid ipv4 address.  
endIP |  The last allowed IP address in the range, inclusive. |  Valid ipv4 address.  
comments |  Optional comments. |  String.  
applications |  The list of applications that this range applies to. There must be at least one value specified. Valid values are: 

  * **UI** â When included in the list, the allowed IP range applies to the UltraDNS Portal.
  * **API** â When included in the list, the allowed IP range applies to the REST API. 

|  List of one or more valid values.  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)AccountIPRangeList
DTO

AccountIPRangeList DTO

Field |  Description  |  Type  
---|---|---  
accountIPRanges |  A list of AccountIPRange DTO. |  List of AccountIPRange DTO.  
resultInfo/totalCount |  The number of accountIPRanges. |  Integer.  
resultInfo/offset |  The starting point for the list. This is currently always 0 for AccountIPRangeList, as pagination is not currently supported. |  Integer.  
resultInfo/returnedCount |  The number of accountIPRange DTOs returned. This is currently equal to the total count, as pagination is not supported. |  Integer.  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get
Address Info for a Current User

**Method and URI** :

GET https://api.ultradns.com/address

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
Address DTO in the body content.

**Errors** : None

JSON Example: Get Address Info of Current User Response

JSON Example: Get Address Info of Current User Response ```json { "address1":
"asis", "address2": "add222", "country": "UGA", "state": "Va", "city": "fsff",
"zip": "20147" } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Address Info for a Current User

**Method and URI** :

PUT https://api.ultradns.com/address

**Parameters** : None

**Body** : Must contain an Address DTO

**Response** : If task completes, Status Code 200 is returned with an
appropriate status message in the response body.

**Errors** : An error code is returned under the following conditions:

  * If invalid data was submitted in the body.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get
Details of Current User

**Method and URI** :

GET https://api.ultradns.com/user

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 is returned with User DTO in
response body.

**Errors** : None

JSON Example: Get details of Current User Response

JSON Example: Get details of Current User Response ```json { "userName":
"JTDoe", "firstName": "John", "lastName": "Doe", "primaryEmail":
"test1@ultradns.com", "secondaryEmail": "test2@ultradns.com ", "phone":
"123456789", "fax": "123456789", "mobile": "123456789", "companyName":
"Example" } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Details of Current User

When a user updates their email, the specified email address will be auto-
subscribed to https://status.ultradns.com/, which provides notification emails
for UltraDNS system incidents and planned maintenance activity.

**To enhance account security and integrity, we have integrated Single-Sign On
(SSO) between the UltraDNS Managed Services Portal and our Zendesk powered
Support and Knowledgebase, which will prevent users from directly editing the
primary or secondary email addresses for their UltraDNS accounts. Users
needing to update their email addresses should contact our support team for
assistance.**

**Method and URI** :

PUT https://api.ultradns.com/user

**Parameters** : None

**Body** : Must include the User DTO.

**Response** : If task completes, Status Code 200 is returned with User DTO in
response body.

**Errors** : An error is returned under the following conditions:

  * If there is an attempt to update the Username.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Details of Other Users

Similar to the Update Details of Current User API call, this call allows users
with the necessary permissions to update the details of other users in the
account. The following user details can be updated when performing this API
call.

**To enhance account security and integrity, we have integrated Single-Sign On
(SSO) between the UltraDNS Managed Services Portal and our Zendesk powered
Support and Knowledgebase, which will prevent users from directly editing the
primary or secondary email addresses for their UltraDNS accounts. Users
needing to update their email addresses should contact our support team for
assistance.**

  * firstName

  * lastName

  * phone

  * companyName

  * fax

  * mobile

  * apiOnlyUser

Please note that only those users belonging to the following Groups can
perform updates associated to this call, with some restrictions.

  * The user identified as the (Primary) Owner has the authority to update the details of any user in the account, except themselves.

  * Users in the ADMINISTRATIVE group can update the details of users in the account as long as it isnât themselves, the Owner, or users in the ADMINISTRATIVE group.

  * Users in the SECURITY-ADMINISTRATION group can update the details of users in the account as long as it isnât themselves, the Owner, or others users in the ADMINISTRATIVE and SECURITY-ADMINISTRATION groups.

  * Anytime an update is made to a userâs details by this API call, a system generated email notification will be sent to the userâs email address informing them of the change.

  * The isApiOnlyUser parameter must be sent in every PUT request. If not provided, then the false value will be taken by default.

**Method and URI:**

PUT https://api.ultradns.com/users/{userName}

**Parameters:** None

**Body:** Must include the User DTO.

**Response:** If task completes, Status Code 200 is returned with Successful
message in response body.

**Errors:** An error is returned under the following conditions:

  * If there is an attempt to update the Username.

  * If the requesting user does not have permission to perform the update.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Forced
Password Reset for User

This API call is used to force a user in the account to reset their password.
Please note that only those users belonging to the following groups can
perform updates associated to this call, with some restrictions.

  * The user defined as the (Primary) Owner can force the password reset for any user in the account, except themselves.

  * Users in the ADMINISTRATIVE group can force the password reset of any user in the account as long as it isnât themselves, the Owner, or users in the ADMINISTRATIVE group.

  * Users in the SECURITY-ADMINISTRATION group can force the password reset of any user in the account as long as it isnât themselves, the Owner, or other users in the ADMINISTRATIVE and SECURITY-ADMINISTRATION groups.

Once the API call is performed, an Email notification will be sent to the
impacted user with a link to reset their password. Please be aware that the
impacted user will not be able to generate a new token if they are forced to
reset the password.

Method and URI:

PUT https://api.ultradns.com/users/{userName}/password

**Parameters:** forceReset=true

**Body:** NONE

**Response:** If task completes, Status Code 200 is returned with Successful
message in response body.

**Errors:** An error is returned under the following conditions:

  * If the requesting user does not have permission to force reset the password.

  * If the user does not belong to the account.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Change
Password for a User in the Account

This API call is used to manually change the password for a user in the
account. The user performing this API call will select a new password the
indicated user.

Please note that only those users belonging to the following Groups can
perform updates associated to this call, with some restrictions.

  * The user identified as the (Primary) Owner has the authority to change the password of any user in the account, except themselves.

  * Users in the ADMINISTRATIVE group can change the password of any user in the account as long as it isnât themselves, the Owner, or users in the ADMINISTRATIVE group.

  * Users in the SECURITY-ADMINISTRATION group can change the password of any user in the account as long as it isnât themselves, the Owner, or other users in the ADMINISTRATIVE and SECURITY-ADMINISTRATION groups.

Once the API call is performed, an Email notification will be sent to the
impacted user informing them that their password has been changed by someone
else. Please be aware that the impacted user will not be able to generate a
new token with their old password.

**Method and URI:**

PUT https://api.ultradns.com/users/{userName}/password

**Parameters:** NONE

**Body:** Must include the following parameter.

Field |  Description |  Type  
---|---|---  
password |  A valid password that adheres to the following rules:

  * Password must be 8-32 characters long and include at least 3 of the following:
    * an uppercase letter,
    * a lowercase letter,
    * a numeral, or a non-alphabetical character (such as !, $, #, %).
  * Spaces are not allowed.

| String  
  
**Response:** If task completes, Status Code 200 is returned with Successful
message in response body.

**Errors:** An error is returned under the following conditions:

  * If the requesting user does not have permission to change the password.

## User Creation

This API call allows you to add a new user to the REST API, or to re-invite a
user that did not receive the initial user creation invitation. You will need
to know the security group name before you can create the invitation for the
user.

Once a new user becomes Active (logs in with their username and password),
their email address will be auto-subscribed to https://status.ultradns.com/,
which provides notification emails for UltraDNS system incidents and planned
maintenance activity.

![](../../Resources/Images/Rest-API_User_Guide/Introduction_62x66.png) |  Please note, that if the Account Owner, or the inviting user does not have a completed profile (First Name, Last Name, Email Address), a new user cannot be invited.  
---|---  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Invite New
User

**Method and URI** :

POST https://api.ultradns.com/accounts/{accountName}/users

**Parameters** : None

**Body** : Must contain the UserInvite DTO.

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If you have permission to list users in the account, but do not have permission to invite new users.

  * If you do not have permission to access the account.

  * If the account is not currently in an Active state.

  * If invalid data was submitted in the UserInvite DTO (invalid/missing email address, invalid/missing security group).

JSON Example: Add Non-API User to Standalone Group

JSON Example: Add Non-API User to Standalone Group ```json { "email":
"email@email.com", "isApiOnlyUser": false, "isStandalone": true } ```

JSON Example: Add Non-API User to Group

JSON Example: Add Non-API User to Group ```json { "email": "email@email.com",
"isApiOnlyUser": false, "isStandalone": false, "group": "TECHNICAL" } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Re-Invite
User

**Method and URI** :

PUT https://api.ultradns.com/accounts/{accountName}/users

**Parameters** : None

**Body** : Must contain the UserInvite DTO.

**Response** : If task completes, Status Code 200 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If you have permission to list users in the account, but do not have permission to invite new users.

  * If you do not have permission to access the account.

  * If invalid data was submitted in the UserInvite DTO (invalid/missing email address, invalid/missing security group).

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get
Pending Invitations

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/users/invitation

**Parameters** : None

**Body** : Must contain the UserInviteList DTO.

**Response** : If task completes, Status Code 200 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If you do not have permission to access the account.

JSON Example: Get Pending User Invite Invitations

JSON Example: Get Pending User Invite Invitations ```json { "resultInfo": {
"totalCount": 1, "offset": 0, "returnedCount": 1 }, "invitations": [ {
"group": "Technical", "isStandalone": false, "isApiOnlyUser": false, "email":
"email@yahoo.com" } ] } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Delete
Pending Invitations

This API is only accessible for the users in the OWNER, ADMINISTRATIVE, and/or
SECURITY-ADMINISTRATION group in the account.

**Method and URI** :

DELETE
https://api.ultradns.com/accounts/{accountName}/users/invitation/{emailAddress}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 204 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * If you do not have permission to access the account.

  * If emailAddress does not exist as a user invitation.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)UserInvite
DTO

UserInvite DTO

Attribute |  Description |  Type  
---|---|---  
group |  Name of the security group for the user. |  String. Valid security group for account. Required for Invite User when isStandalone is âFalse.â  Ignored for Re-Invite User and when isStandalone is âtrue.â   
isStandalone |  Whether or not the user is a standalone user.  
If set to **true** , user will not belong to any group.  
If set to **false** , user will be assigned to the group specified in the group attribute. |  Boolean. Required. Defaults to false.  Ignored for Re-Invite User.  
isApiOnlyUser |  Whether or not the user has api only access. If set to **true** , user will only be able to access the API services. If set to **false** , user will be able to access both the API services and UltraDNS Managed Services Portal. |  Boolean. Defaults to false.  Ignored for Re-Invite User.  
email  |  Email address for the new user. |  Email. Required.  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)UserInviteList
DTO

UserInviteList DTO

Attribute |  Description |  Type  
---|---|---  
resultInfo/totalCount |  The total count of all pending user invitations. |  Integer.  
resultInfo/offset |  The position in the list for the first returned element. (0 based) |  Integer. Always 0.  
resultInfo/returnedCount |  The number of records returned. |  Integer.  
invitations |  List of UserInvite DTO. |  UserInvite DTO  
  
## Account Management

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get
Account Info

**Method and URI** :

GET https://api.ultradns.com/accounts/(accountName)

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
Account DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If you do not have permission to access the account.

JSON Example: Get Account Info Response for INDIVIDUAL Account type

JSON Example: Get Account Info Response for INDIVIDUAL Account type ```json {
"accountName": "team", "accountHolderUserName": "teamtest", "ownerUserName":
"teamtest", "ownerAddress": { "address1": "asis", "address2": "add222",
"country": "UGA", "state": "Va", "city": "fsff", "zip": "20147" },
"numberOfUsers": 2, "numberOfGroups": 16, "accountType": "INDIVIDUAL",
"accountId": "ABC-1234", "status": "ACTIVE", "created": "2017-06-09T13:40Z",
"features": [ "ADVDIRECTIONAL", "DNSSEC", "LAB_ENABLED", "MDDI", "RECURSIVE",
"REPORTING", "SITEBACKER", "TRAFFICCNTRL", "WEBFORWARD", "ZBR" ] } ```

JSON Example: Get Account Info Response for ORGANIZATION Account type

JSON Example: Get Account Info Response for ORGANIZATION Account type ```json
{ "accountName": "team", "accountHolderUserName": "teamtest", "ownerUserName":
"teamtest", "ownerAddress": { "address1": "asis", "address2": "add222",
"country": "UGA", "state": "Va", "city": "fsff", "zip": "20147" },
"accountHolderAddress": { "address1": "address1", "address2": "add222",
"country": "UGA", "state": "Va", "city": "fsff", "zip": "20147" },
"numberOfUsers": 2, "numberOfGroups": 16, "accountType": "ORGANIZATION",
"accountId": "ABC-1234", "status": "ACTIVE", "created": "2017-06-09T13:40Z",
"features": [ "ADVDIRECTIONAL", "DNSSEC", "LAB_ENABLED", "MDDI", "RECURSIVE",
"REPORTING", "SITEBACKER", "TRAFFICCNTRL", "WEBFORWARD", "ZBR" ] } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Account Info

![](../../Resources/Images/Rest-API_User_Guide/Introduction_72x84.png) |  This method allows a user to change the primary user of an account, change the primary userâs address information, change the account name, or change the SOA email address.  
---|---  
  
**Method and URI** :

PUT https://api.ultradns.com/accounts/(accountName)

**Parameters** : None

**Body** : Must incude an Account DTO.

_Since this is a PUT method, all fields that can be edited by the user must be
specified. The read-only fields in the Account DTO are optional and do not
need to be specified. Any non-specified optional fields will be assumed to
have an empty value, which will replace any already assigned values._

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * Invalid data was submitted in the body.

  * If you have permission to get the account info, but do not have permission to edit the account info. 

  * If you are not allowed to edit some of the fields that are specified in your input, a 403 error code will be returned, and none of the edits will take effect.

  * If you do not have permission to access the account.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update Account Info

![](../../Resources/Images/Rest-API_User_Guide/Introduction_72x84.png) |  This method allows a user to change the primary user of an account, change the primary userâs address information, change the account name, or change the SOA email address.  
---|---  
  
**Method and URI** :

PATCH https://api.ultradns.com/accounts/{accountName}

**Parameters** : None

**Body** : Must include an Account DTO.

_Since this is a PATCH method, only the fields being modified need to be
specified. Any fields that are not specified will retain their already
assigned value(s)_.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * Invalid data was submitted in the body.

  * If you have permission to get the account info, but do not have permission to edit the account info. 

  * If you are not allowed to edit some of the fields that are specified in your input, a 403 error code will be returned, and none of the edits will take effect.

  * If you do not have permission to access the account.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)TTL DTO

TTL DTO

Attribute |  Description |  Type  
---|---|---  
type |  The type of record whose TTL is being set. |  One of the following resource record types:

  * A
  * AAAA
  * CNAME
  * MX
  * TXT
  * SRV
  * NS
  * PTR
  * RP
  * HINFO
  * NAPTR
  * SOA
  * SPF

Also supported are these special cases:

  * ANY (All resource records)
  * SBTC (Sitebacker and Traffic Controller pools)
  * SOA_REFRESH (Refresh field in SOA)
  * SOA_RETRY (Retry field in SOA)
  * SOA_EXPIRE (Expire field in SOA)
  * SOA_MIN_CACHE (Min Cache field in SOA)

  
defaultValue |  The default value for the TTL. |  Integer. Between 0 and 2147483647  
min |  The minimum value for the TTL. |  Integer. Between 0 and 2147483647  
max |  The maximum value for the TTL. |  Integer. Between 0 and 2147483647  
  
JSON Example: TTL DTO

JSON Example: TTL DTO ```json { "type": "A", "defaultValue": 123, "min": 12,
"max": 512 } ```

### TTL List DTO

ttllist DTO

Attribute |  Description |  Type  
---|---|---  
**ttls** |  The specified TTLs for the account. |  List of TTL DTO.  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get
Account TTLs

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/ttls

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
ttllist DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If you have permission to get the account info, but do not have permission to edit the account info.

  * If you do not have permission to access this account.

JSON Example: Get Account TTLs Response

JSON Example: Get Account TTLs Response ```json { "ttls": [ { "type": "MX",
"max": 1111 }, { "type": "NAPTR", "defaultValue": 9010 }, { "type": "TXT",
"defaultValue": 100, "min": 30, "max": 1000 }, { "type": "TLSA",
"defaultValue": 222 }, { "type": "A", "defaultValue": 500 } ] } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Account TTLs

**Method and URI** :

PUT https://api.ultradns.com/accounts/{accountName}/ttls

**Parameters** : None

**Body** : Must include a TTL DTO.

_Since this is a PUT function, all TTLs and all the fields in the TTL DTOs
must be specified, otherwise the values will be reset to the default (empty)
value_.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * Invalid data was submitted in the body.

  * If you have permission to get the account info, but do not have permission to edit the account info.

  * If you do not have permission to access this account.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update Account TTLs

**Method and URI** :

PATCH https://api.ultradns.com/accounts/{accountName}/ttls

**Parameters** : None

**Body** : Must include a TTL DTO.

_Since this is a PATCH function, only the TTLs being updated need to be
included in the list. All TTLs and fields in the TTL DTOs not included in the
list will retain their current state_.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * Invalid data was submitted in the body.

  * If you have permission to get the account info, but do not have permission to edit the account info.

  * If you do not have permission to access this account.

## Security Group Management

An UltraDNS account has the following default system-generated Security Groups
present in the account. These Security Groups cannot be deleted, nor can their
default permissions be changed.

  * **OWNER** âThis group is reserved for the (Primary) Owner for the account, and therefore, only one user can be present in this group. This user will have full administrative privileges for the entire account.

  * **ADMINISTRATIVE** \- The users belonging to this group will have full administrative privileges for the account and can perform API calls that update or impact any users in the account, except for the Owner.

  * **REPORTING** \- The users belonging to this group will have the basic READ permission, preventing them from performing any operation that would modify the state of an object in the account.

  * **TECHNICAL** \- The users belonging to this group will be able to perform all the operations at the DNS level but are restricted from performing any operation associated to Account Management.

  * **SECURITY-ADMINISTRATION** \- The users belonging to this Security Group will be able to perform all the operations at the DNS and account level These users are restricted to only retrieving details at the group level, (they cannot perform any additional operations at the group level).

  * **DNS-ADMINISTRATION** â The users belonging to this Security Group can perform any operation at the DNS and group level. These users are restricted from performing any operation at the user or account level.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Security
Group DTO

Security Group DTO

Attribute |  Description |  Type  
---|---|---  
name |  The name of the security group.  Returned on a GET call. Ignored on a POST/PUT/PATCH call. |  String.  
entries  |  The security group entries for this security group. |  List of Extended Accounts API.  
exceptions |  A list of security exceptions. |  Security Exception List DTO  
usersCount |  The total number of users in the group(s) being returned. Returned on a GET call.  For Standalone groups, the usersCount will be reflected in the returned totalCount value, as only one user can be assigned to a Standalone group.  |  Integer.  
  
JSON Example: Security Group DTO

JSON Example: Security Group DTO ```json { "name": "1441307959243group2",
"entries": [ { "type": "ACCOUNT", "permission": "READ" } ] } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Security
Group Entry DTO

SecurityGroupEntry DTO

Attribute |  Description |  Type  
---|---|---  
type |  The name of the Object or Page being configured.  The specific Permission must to be set to a record type if the Permission is being set at the pool level. The Permission and Type attributes work as a Top-Down attribute. For example: If the DELETE permission is set for a SiteBacker Pool (that contains an A Record), then the DELETE permission must also be set for the A Record as well to allow changes to be made at the record level. |  String. Required to have one of the following values: 

  * ACCOUNT
  * APEXALIAS
  * DOMAIN_SERVICES
  * ZONE
  * RESOURCE_RECORDS
  * A
  * AAAA
  * CAA
  * CNAME
  * DIR_POOL
  * HINFO
  * MX
  * NAPTR
  * NS
  * PTR
  * RP
  * RD_POOL
  * SB_POOL
  * SRV
  * SSHFP
  * TC_POOL
  * TLSA
  * TXT
  * WEB_FORWARD
  * REPORTS
  * ACCOUNTS_PERMISSIONS
  * ACCOUNT_PREFERENCES
  * BILLING
  * SERVICE_PACKAGE

The following types are available if the group is SECURITY-ADMINISTRATION.

  * SECURITY_SERVICES
  * SECURITY_PREFERENCES
  * USER_MANAGEMENT
  * SAML_SSO

The following types are available if the group is DNS-ADMINISTRATION.

  * DNS_SERVICES
  * GROUP_MANAGEMENT

  
permission |  The permission being applied to the type. Permissions are cumulative:

  * If you have Write, you also have Read, 
  * If you have Create, you also have Write and Read, etc.

|  String. Required to have one of the following values:

  * NONE
  * INHERIT
  * READ
  * WRITE
  * CREATE
  * DELETE
  * GRANT

GRANT is only legal when type is set to ACCOUNT.  
It is returned for the account owner, but cannot be given to another security
group. SERVICE_PACKAGE is only allowed to have NONE, READ or INHERIT.
ACCOUNTS_PERMISSIONS, ACCOUNT_PREFERENCES, and BILLING  
are only allowed to have NONE, READ, WRITE, or INHERIT. ACCOUNT is not allowed
to have NONE or INHERIT.  
inheritedValue |  Shows the calculated value for this security group entry if the permission is set to INHERIT. Returned on GET, ignored on POST/PUT/PATCH. |  String. Only returned if permission is set to INHERIT. Must have one of the following values:

  * NONE
  * READ
  * WRITE
  * CREATE
  * DELETE

  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Security
Group List DTO

SecurityGroupList DTO

Attribute |  Description |  Type  
---|---|---  
groups |  A list of security groups. |  List of SecurityGroup DTO objects.  
resultInfo/totalCount |  Count of all the exceptions returned. |  Integer.  
resultInfo/offset |  The position in the list for the first returned element (0 based). |  Integer. Always 0, since the pagination is not currently supported.  
resultinfo/returnedCount |  The number of records returned. |  Integer.  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Security
Exception DTO

SecurityException DTO

Attribute |  Description |  Type  
---|---|---  
groupName |  The name of the group. This is only populated when getting the list of all exceptions for an object. For STANDLAONE groups, the groupName will be returned as the username, as opposed to a FirstName Lastname result. |  String.  
type |  The type of the entity with the exception. |  String. Required to have one of the following:

  * ZONE
  * A
  * AAAA
  * APEXALIAS
  * CAA
  * CNAME
  * DIR_POOL
  * HNFO
  * MX
  * NAPTR
  * NS
  * PTR
  * RP
  * RD_POOL
  * SB_POOL
  * SRV
  * SSHFP
  * TC_POOL
  * TLSA
  * TXT
  * WEB_FORWARD

  
name |  The name of the entity.  |  String. Required:

  * For a web forward, will be a GUID.
  * For a mail forward, will be an email address.
  * For a zone, it will be the zone name (with or without the trailing dot).
  * For a resource record set or pool, it will be the fully qualified domain name for the rrset or pool (with or without the trailing dot).

  
permission |  The permission being applied to the type. Permissions are cumulative. For Example:

  * If you have Write, you also have Read.
  * If you have Create, you also have Write and Read, etcâ¦

|  String. Required (for pools) to have one of the following:

  * NONE
  * READ
  * WRITE
  * CREATE
  * DELETE

  
rdata |  The Rdata of the Resource Record on which the exception should be set. |  List <string>. Optional  
rrtype |  The Resource Record type of the member record of the pools. It is mandatory for pools, but will be ignored for the following: Web Forward, Zone and Resource Records. |  String. Required (for pools) to have one of the following:

  * A
  * AAAA
  * CNAME
  * HINFO
  * MX
  * NAPTR
  * NS
  * PTR
  * RP
  * SRV
  * TXT

  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Security
Exception List DTO

SecurityExceptionList DTO

Attribute |  Description |  Type  
---|---|---  
exceptions |  A list of security exceptions. |  List of Security Exception DTO objects.  
resultInfo/totalCount |  The count of all exceptions returned. |  Integer.  
resultInfo/offset |  The position in the list for the first returned element. (0 based) |  Integer. Always 0.  
resultInfo/returnedCount |  The number of records returned. |  Integer.  
  
![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Create
Security Group

**Method and URI** :

POST https://api.ultradns.com/accounts/{accountName}/groups/{groupName}

**Parameters** : None

**Body** : Must include a Security Group DTO.

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error code is returned under the following conditions:

  * Invalid data was submitted in the body, or the group name is already in use.

  * If you have permission to get the account info, but do not have permission to create security groups.

  * If you do not have permission to access this account.

JSON Example: Create Security Group without Exceptions

{

"entries": [

{

"type": "ACCOUNT",

"permission": "CREATE"

},

{

"type": "RESOURCE_RECORDS",

"permission": "DELETE"

},

{

"type": "DOMAIN_SERVICES",

"permission": "READ"

},

{

"type": "ZONE",

"permission": "READ"

},

{

"type": "REPORTS",

"permission": "READ"

},

{

"type": "ACCOUNTS_PERMISSIONS",

"permission": "READ"

},

{

"type": "ACCOUNT_PREFERENCES",

"permission": "READ"

},

{

"type": "BILLING",

"permission": "READ"

},

{

"type": "SERVICE_PACKAGE",

"permission": "READ"

}

]

}

JSON Example: Create Security Group with Exceptions

{

"entries": [

{

"type": "ACCOUNT",

"permission": "DELETE"

}

],

"exceptions":

{

"exceptions":

[

{

"type": "ZONE",

"permission": "CREATE",

"name": "zoneName"

},

{

"type": "DIR_POOL",

"permission": "WRITE",

"name": "DRR.AAAA-test.com",

"rrtype": "A",

"rdata": ["{1.1.1.1}"]

},

{

"type": "RD_POOL",

"permission": "CREATE",

"name": "rd.aaaa-test.com.",

"rrtype": "A"

}

]

}

}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get a
Security Group

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/groups/{groupName}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
Security Group DTO in the body content.

**Errors** : An error code is returned under the following conditions:

  * If you have permission to access the account, but do not have permission to view the security groups.

  * If the Group does not exist, the Account does not exist, or if you do not have permission to access this account.

  * If you are not part of the Owner, ADMINISTRATIVE, or SECURITY_ADMINISTRATION groups.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get
Security Groups

This API will return all the groups of account which are not standalone. There
is a separate API for getting standalone groups.

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/groups

**Parameters** : You can include:

Attribute |  Description |  Type  
---|---|---  
**namesOnly** |  If set to true, it will only populate the name field in the security groups. Default is set to false. |  Boolean  
  
  
**Body** : None

**Response** : If the task completes, Status Code 200 OK is returned with a
Security Group List DTO in the body content.

**Errors** : An error code is returned under the following conditions:

  * If you have permission to get the account info, but do not have permission to view the security groups.â

  * If the Account does not exist, or you do not have permission to access this account.

  * If you are not part of the Owner, ADMINISTRATIVE, SECURITY_ADMINISTRATION, or DNS_ADMINISTRATION groups.

JSON Example: Get Security Groups Response

{

"groups": [

{

"name": "Guinea-pig-group",

"entries": [

"exceptions":

{

"type": "MX",

"permission": "READ"

},

{

"type": "ZONE",

"permission": "READ"

},

{

"type": "A",

"permission": "READ"

},

{

"type": "ACCOUNT_PREFERENCES",

"permission": "READ"

},

{

"type": "HINFO",

"permission": "READ"

},

{

"type": "REPORTS",

"permission": "READ"

}

]

"usersCount": 5

}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get Users
in a Security Group

This call returns a list of all of the Users assigned to a specified
groupName, which are sorted by user name in ascending order.

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/groups/{groupName}/users

**Parameters** :

Attribute |  Description |  Type  
---|---|---  
**namesOnly** |  If set to true, it will only populate the name field in the User DTO. Default is set to false. |  Boolean  
  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a User
List DTO in the body content.

**Errors** : An error code is returned under the following conditions:

  * If you have permission to access the account, but do not have permission to view security groups.

  * If the Group does not exist, the Account does not exist, or if you do not have permission to access this account.

  * If you are not part of the Owner, ADMINISTRATIVE, SECURITY_ADMINISTRATION, or DNS_ADMINISTRATION groups.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get
Standalone Security Groups

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/standalone

**Parameters** :

Attribute |  Description |  Type  
---|---|---  
**namesOnly** |  If set to true, it will only populate the name field in the security group DTOs. Default is set to false. |  Boolean  
  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
Security Group List DTO in the body content.

**Errors** : An error code is returned under the following conditions:

  * If you have permission to access the account, but do not have permission to view security groups.

  * If the User does not exist, if the {accountName} does not exist, or if you do not have permission to access this account.

  * If you are not part of the Owner, ADMINISTRATIVE, SECURITY_ADMINISTRATION, or DNS_ADMINISTRATION groups.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get
Settings for a Standalone Security Groups

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/standalone/{userName}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
Security Group DTO in the body content.

**Errors** : An error code is returned under the following conditions:

  * If you have permission to access the account, but do not have permission to view security groups.

  * If the User does not exist, if the {accountName} does not exist, or if you do not have permission to access this account.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get All
Exceptions for an Object

This function returns the exceptions for a specified object across all
Security Groups. To make changes, you will need to edit the settings for the
security group.

**Method and URI** :

GET
https://api.ultradns.com/accounts/{accountName}/exceptions/{type}/{objectName}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
Security Exception List DTO in the body content.

**Errors** : An error code is returned under the following conditions:

  * If you have access to the account, but you do not have permission to view security groups.

  * If the user does not exist, if {accountName} does not exist, or if you do not have permission to access the account.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update a
Security Group

**Method and URI** :

PUT https://api.ultradns.com/accounts/{accountName}/groups/{groupName}

**Parameters** : None

**Body** : Must include a Security Group DTO.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error code is returned under the following conditions:

  * If you have permission to access the account, but do not have permission to modify security groups.

  * If the group does not exist, the {accountName} does not exist, or if you do not have permission to access this account.

JSON Example: Update Security Group without Exceptions

{

"entries": [

{

"type": "RESOURCE_RECORDS",

"permission": "DELETE"

}

]

}

JSON Example: Update Security Group with Exceptions

{

"entries": [

{

"type": "ACCOUNT",

"permission": "DELETE"

}

],

"exceptions":

{

"exceptions":

[

{

"type": "ZONE",

"permission": "CREATE",

"name": "zoneName"

}

]

}

}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update a Security Group

**Method and URI** :

PATCH https://api.ultradns.com/accounts/{accountName}/groups/{groupName}

**Parameters** : None

**Body** : Must include a Security Group DTO.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error code is returned under the following conditions:

  * If you have permission to access the account, but do not have permission to modify security groups.

  * If the group does not exist, if the {accountName} does not exist, or if you do not have permission to access this account.

JSON Example: Partial Update Security Group without Exceptions

{

"entries": [

{

"type": "ACCOUNT",

"permission": "CREATE"

},

{

"type": "RESOURCE_RECORDS",

"permission": "DELETE"

},

{

"type": "DOMAIN_SERVICES",

"permission": "READ"

},

{

"type": "ZONE",

"permission": "READ"

},

{

"type": "REPORTS",

"permission": "READ"

}

]

}

JSON Example: Partial Update Security Group with Exceptions

{

"entries": [

{

"type": "ACCOUNT",

"permission": "DELETE"

}

],

"exceptions":

{

"exceptions":

[

{

"type": "ZONE",

"permission": "CREATE",

"name": "zoneName"

}

]

}

}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Settings for a Standalone Security Group

**Method and URI** :

PUT https://api.ultradns.com/accounts/{accountName}/standalone/{userName}

**Parameters** : None

**Body** : Must include a Security Group DTO.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error code is returned under the following conditions:

  * If you have permission to access the account, but do not have permission to modify security groups.

  * If the User does not exist, if the {accountName} does not exist, or if you do not have permission to access this account.

JSON Example: Update Settings for Standalone Security Group without Exceptions

{

"entries": [

{

"type": "ACCOUNT",

"permission": "CREATE"

},

{

"type": "RESOURCE_RECORDS",

"permission": "DELETE"

}

]

}

JSON Example: Update Settings for Standalone Security Groups with Exceptions

{

"entries": [

{

"type": "ACCOUNT",

"permission": "DELETE"

},

{

"type": "RESOURCE_RECORDS",

"permission": "CREATE"

}

],

"exceptions":

{

"exceptions":

[

{

"type": "ZONE",

"permission": "CREATE",

"name": "zoneName"

}

]

}

}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update Settings for a Standalone Security Group

**Method and URI** :

PATCH https://api.ultradns.com/accounts/{accountName}/standalone/{userName}

**Parameters** : None

**Body** : Must include a Security Group DTO.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error code is returned under the following conditions:

  * If you have permission to access the account, but do not have permission to modify security groups.

  * If the User does not exist, if the {accountName} does not exist, or if you do not have permission to access this account.

JSON Example: Partial Update Settings for Standalone Security Group without
Exceptions

{

"entries" : [

{

"type": "RESOURCE_RECORDS",

"permission": "DELETE"

}

]

}

JSON Example: Partial Update Settings for Standalone Security Group with
Exceptions

{

"entries": [

{

"type": "ACCOUNT",

"permission": "DELETE"

}

],

"exceptions":

{

"exceptions":

[

{

"type": "ZONE",

"permission": "CREATE",

"name": "zoneName"

}

]

}

}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Assign
User to a Security Group

![](../../Resources/Images/Rest-API_User_Guide/Introduction.png) |  This call will perform the two following operations:  

  * **Move a Uuser to different group of the same account** : If the specified user already existis in another security group (of the specified account already mentioned in request URL), this call will remove the user from their existing security group and move them to the specified security group (mentioned in the URL). If the user is a standalone user, the standalone group will be deleted.

  * **Add User to the group of another account** : If the specified user does not exists in any security group (of the specified account mentioned in the request URL), this call will add the user in the specified security group of the specified account (mentioned in the URL). This will not remove the user from their existing security group.
    * Once the (new) user has been added, their email address will be auto-subscribed to https://status.ultradns.com/ to receive notifications related to UltraDNS system incidents and maintenance activity.

  
---|---  
  
**Method and URI** :

POST
https://api.ultradns.com/accounts/{accountName}/groups/{groupName}/users/{userName}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error code is returned under the following conditions:

  * If you have permission to access the account, but do not have permission to modify security groups.

  * If the User does not exist, if the Account does not exist, or if you do not have permission to access this account.

  * If the account is not in an Active status.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Move User
to Standalone Security Group

![](../../Resources/Images/Rest-API_User_Guide/Introduction_68x79.png) |  This call will move the user from their current security group. If the user is already a standalone user, then no action will be taken for the user.  
---|---  
  
**Method and URI** :

POST https://api.ultradns.com/accounts/{accountName}/standalone/{userName}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error code is returned under the following conditions:

  * If you have permission to access the account, but do not have permission to modify security groups.

  * If the User does not exist, if the Account does not exist, or if you do not have permission to access this account.

  * If the account is not in an Active status.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Delete
Security Group

**Method and URI** :

DELETE https://api.ultradns.com/accounts/{accountName}/groups/{groupName}

**Parameters** : None

**Body** : None

**Response** : If delete completes, Status Code 204 is returned with no body
content..

**Errors** : An error code is returned under the following conditions:

  * If you have permission to get the account info, but do not have permission to delete security groups.

  * If you do not have permission to access the account.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Delete
Access of a User from a Security Group

Once a user is deleted, their email address will be automatically unsubscribed
from https://status.ultradns.com/, which provides notification emails for
UltraDNS system incidents and planned maintenance activity.

**Method and URI** :

DELETE
https://api.ultradns.com/accounts/{accountName}/groups/{groupName}/users/{userName}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 204 is returned with no body
content.

**Errors** : An error code is returned under the following conditions:

  * If you have permission to access the account, but do not have permission to modify security groups.

  * If the User does not exist, if the Account does not exist, or if you do not have permission to access this account.

## DNSSEC Settings

The Account Level DNSSEC settings enables administrative users to set default
global DNSSEC values that will be used for every signing, rollover, and
resigning action, for every zone in the account.

Users in the following Groups will have the necessary permissions to configure
the DNSSEC Settings. Users not in the mentioned groups will have read only
access to the DNSSEC Settings information.

  * OWNER

  * ADMINISTRATIVE

  * DNS-ADMINISTRATION

  * SECURITY-ADMINISTRATION

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Create the
Global DNSSEC Settings

**Method and URI:**

POST https://api.ultradns.com/accounts/{accountName}/settings/DNSSEC_SETTINGS

**Parameters:** None

**Body:** Must include the DNSSEC Settings DTO.

**Response:** If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

  * If update happens in the background, Status Code 202 is returned along with an X-Task-ID header and a status message of Pending in the body content.

**Errors:** An error is returned under the following conditions:

  * If you do not have permission to change security on {accountName}.

  * If {accountName} does not exist.

  * If invalid body details, or details already exist.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get the
Global DNSSEC Settings

This call returns the current configured global DNSSEC settings for the
account.

**Method and URI:**

GET https://api.ultradns.com/accounts/{accountName}/settings/DNSSEC_SETTINGS

**Parameters:** None

**Body:** None

**Response:** If task completes, Status Code 200 is returned with DNSSEC
Settings DTO in the response body.

  * If update happens in the background, Status Code 202 is returned along with an X-Task-ID header and a status message of Pending in the body content.

**Errors:** An error is returned under the following conditions:

  * If you do not have permission to change security on {accountName}.

  * If {accountName} does not exist.

  * If invalid body details, or details already exist.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Global DNSSEC Settings

Performing this operation as a **PUT** call will replace all previously
provided dnssecSettings that were initially configured.

Performing this operation as a **PATCH** call will only update the fields
provided in the body details.

**Method and URI:**

PUT/PATCH
https://api.ultradns.com/accounts/{accountName}/settings/DNSSEC_SETTINGS

**Parameters:** None

**Body:** Must include DNSSEC Settings DTO.

**Response:** If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If update happens in the background, Status Code 202 is returned along with an X-Task-ID header and a status message of Pending in the body content.

**Errors:** An error is returned under the following conditions:

  * If you do not have permission to change security on {accountName}.

  * If {accountName} does not exist.

  * If invalid body details, or details already exist.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Reset
Global DNSSEC Settings to Default

Performing this call will reset any previously configured values in the
**dnssecSettings** to the default values.

**Method and URI:**

DELETE
https://api.ultradns.com/accounts/{accountName}/settings/DNSSEC_SETTINGS

**Parameters:** None

**Body:** None

**Response:** If delete happens immediately, Status Code 204 is returned with
no body content.

  * If delete happens in the background, a Status Code 202 is returned with a status response message of Pending along with an X-Task-Id header in body content.

**Errors:** An error is returned under the following conditions:

  * If you do not have permission to change security on {accountName}.

  * If {accountName} does not exist.

  * If invalid body details, or details already exist.

DNSSEC Settings DTO

Attribute |  Description |  Type  
---|---|---  
dnssecSettings /dnskeyTtl |  The Time to Live (TTL) value, in seconds, that is used for the DNSKEY Resource Record Set (RRSET).  Valid values are between 300 - 172800. Default value is 86400.  |  Integer  
dnssecSettings/rrsigValidity |  The Resource Reset Set Signature (RRSIG) value used to set the interval period (in days) when signing the responses for a zone.  Valid values are between 5 â 30. Default value is 14.  |  Integer  
dnssecSettings/zskRolloverFrequency |  The Zone Signing Key (ZSK) signs the data within a zone and needs to be rolled over more often due to the sheer volume of data being signed. The ZSK Rollover Frequency indicates, in days, how often the ZSK keys are rolled over.  Valid values are between 30-120 days. Default value is 30.  |  Integer  
dnssecSettings/kskRolloverFrequency |  The Key Signing Key (KSK) signs the keys within the zone, and because they sign less data than ZSKs, they do not need to be rolled over as often.  Valid values are between 365-1826 days. Default value is 365.  |  Integer  
  
JSON Example: Configure Account Level DNSSEC Settings

JSON Example: Configure Account Level DNSSEC Settings ```json {
"dnssecSettings": { "dnskeyTtl": 172800, "rrsigValidity": 30,
"zskRolloverFrequency": 30, "kskRolloverFrequency": 365 } } ```

## Security Preferences

Please note, that your account will be locked out if you are unsuccessful
logging in with your username and password after multiple attempts. If this
occurs, please wait for the indicated period of time before logging in again,
or contact our Customer Support team for further assistance.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)SecurityPreferences
DTO

SecurityPreferences DTO

Attribute |  Description |  Type  
---|---|---  
oldPassword |  The old password for the user. Mandatory only if the password parameter is provided in the input. Only used for setting, never returned from the server. |  String.  
password |  The password for the user. Only used for setting, never returned from the server. |  String. Password must be between 8-36 characters in length, and include at least 3 of the following: an Uppercase letter, a Lowercase letter, a Numerical digit, or a Special Character (such as: +, $, !, %).  Spaces are not allowed. Additional Special Characters now supported include: @ , . / ` ~ < ? ; ' : \\\ \" [ ] { } | ! # $ % ^ & * ( ) - = _ +  
passwordExpiration |  Maximum number of days until the password expires. |  Number. You can set the value to zero so that a password change will never be required.  
securityQuestion1 |  The ID for the security question to use. |  String. (Currently a number from 1-12)  
securityAnswer1 |  The answer to securityQuestion1. |  String. securityAnswer1 length must not be greater than 36 characters.  
securityQuestion2 |  The ID for the security question to use. |  String. (Currently a number from 1-12)  
securityAnswer2 |  The answer to securityQuestion2. |  String. securityAnswer2 length must not be greater than 36 characters.  
securityQuestion3 |  The ID for the security question to use. |  String. (Currently a number from 1-12)  
securityAnswer3 |  The answer to securityQuestion3 |  String. securityAnswer3 length must not be greater than 36 characters.  
restricAccessIPs |  IP addresses and ranges that are allowed to connect to the ingestion applications as the user. |  List of RestrictAccessIP DTO.  
inactivityTimeout |  Maximum inactive duration (in minutes) after which the Java UI session will expire. |  Integer.  
requireMFA |  Indicates if user is enrolled in Mandatory Multi-Factor Authentication.  Returned on a GET.  |  Boolean.  
  
JSON Example: Security Preferences DTO

{

"oldPassword": "oldpassword",

"password": "password",

"passwordExpiration": "90",

"securityQuestion1": "1",

"securityAnswer1": "white",

"securityQuestion2": "3"

"securityAnswer2": "tiger",

"securityQuestion3": "8",

"securityAnswer3": "2008",

"restrictAccessIPs": [

{

"startIP": "1.1.1.1",

"endIP": "2.2.2.2",

"comment": "Unit Test"

}

]

"inactivityTimeout": 15

}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Security
Question DTO

SecurityQuestion DTO

Attribute |  Description |  Type  
---|---|---  
id |  The id for the security question. |  String. (Currently set as a number from 1-12)  
question |  The text for the security question. |  String.  
  
JSON Example: SecurityQuestion DTO

JSON Example: SecurityQuestion DTO ```json { "id": "1", "question":
"question1" } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Security
Question List DTO

SecurityQuestList DTO

Attribute |  Description |  Type  
---|---|---  
**questions** |  The list of the security questions. |  List of Security Question DTOobjects.  
  
JSON Example: SecurityQuestionLIst DTO

JSON Example: SecurityQuestionLIst DTO ```json { "questions": [ { "id": "1",
"question": "question1" } ] } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)RestrictIP
DTO

This is for restricting the IPs that are allowed to outbound transfer primary
zones.

![](../../Resources/Images/Rest-API_User_Guide/Introduction_73x85.png) |  Users will not be able to replace overlapping restrict IPs via PATCH, whereas non-overlapping restrict IPs can be added. If a user wants to add overlapping restrict IP range, then PUT (full update) should be used.  
---|---  
  
RestrictIP DTO

Attribute |  Description |  Type  
---|---|---  
startIP |  The starting IP address for the range. Inclusive |  IPv4 Address.  
endIP |  The ending IP address for the range. Inclusive |  IPv4 Address.  
cidr |  The IP range represented using CIDR. This can be used to specify a new or updated Restrict IP, but responses will always be sent as startIP/endIP pairs. |  IPv4 CIDR range.  
singleIP |  A single IP address. This can be used to specify a new or updated Restrict IP, but responses will always be sent as startIP/endIP pairs. |  IPv4 Address.  
comment |  A description of the range. Optional. |  String.  
  
JSON Example: RestrictIP

{

"startIP": "1.2.3.4",

"endIP": "1.2.3.4",

}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)RestrictAccessIP
DTO

This is used to control which IP addresses are allowed to connect to the
ingestion applications ( REST API or Java UI). It can be specified per-account
or per-user. The per-account settings allow for application-specific
restrictions.

RestrictAccesIP DTO

Attribute |  Description |  Type  
---|---|---  
startIP |  The starting IP address for the range. Inclusive |  IPv4 Address.  
endIP |  The ending IP address for the range. Inclusive |  IPv4 Address.  
cidr |  The IP range represented using CIDR. This can be used to specify a new or updated Restrict IP, but responses will always be sent as startIP/endIP pairs. |  IPv4 CIDR range.  
singleIP |  A single IP address. This can be used to specify a new or updated Restrict IP, but responses will always be sent as startIP/endIP pairs. |  IPv4 Address.  
comment |  A description of the range. Optional. |  String  
application |  Indicates whether this restriction should apply to ingestion applications, the UltraDNS Portal (UI), or the REST API application (API).  Optional.  If not specified, defaults to meaning all applications.  |  Valid values are: 

  * UI
  * API

  
  
JSON Example: Restrict Access of IP

JSON Example: Restrict Access of IP ```json { "restrictAccessIPs": [ {
"startIP": "1.1.1.1", "endIP": "255.255.255.255", "comment": "Restrict IP.",
"application": "UI" } ] } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get
Security Questions

**Method and URI** :

GET https://api.ultradns.com/securityQuestions

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with Security
Question List DTO and Security Question List DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * None

JSON Example: Get Security Questions Response

JSON Example: Get Security Questions Response ```json { "questions": [ { "id":
"1", "question": "What color was your first vehicle?" }, { "id": "2",
"question": "What year was your mother born?" }, { "id": "3", "question":
"What was the name of your first pet?" }, { "id": "4", "question": "Where did
you go on your honeymoon?" }, { "id": "5", "question": "What is your high
school mascot?" } ] } ```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get
Security Preferences for a Current User

**Method and URI** :

GET https://api.ultradns.com/security

**Parameters** : None

**Body** : None

**Response** : If task completes , Status Code 200 OK is returned with
Security Question List DTO and Security Question List DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * None

JSON Example: Get Security Preferences for a User Response

JSON Example: Get Security Preferences for a User Response ```json {
"passwordExpiration": 90, "securityQuestion1": "1", "securityAnswer1":
"Answer1", "securityQuestion2": "3", "securityAnswer2": "tiger",
"securityQuestion3": "8", "securityAnswer3": "2008", "inactivityTimeout": 15 }
```

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Security Preferences for a Current User

**Method and URI** :

PUT https://api.ultradns.com/security

**Parameters** : None

**Body** : Must include a SecurityPreferences DTO.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error code is returned under the following conditions:

  * Invalid data was submitted in the body.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update Security Preferences for a Current user

**Method and URI** :

PATCH https://api.ultradns.com/security

**Parameters** : None

**Body** : Must include a SecurityPreferences DTO.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error code is returned under the following conditions:

  * Invalid data was submitted in the body.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)System
Preferences DTO

System Preferences DTO

Attribute |  Description |  Type  
---|---|---  
**autoCreatePTR** |  true if PTR records should be auto-created when A records are created, false otherwise. |  Boolean.  
  
JSON Example: System Preferences DTO

{

"autoCreatePTR": True

}

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Get System
Preferences for a Current User

**Method and URI** :

GET https://api.ultradns.com/prefs

**Parameters:** None

**Body:** None

**Response** : If task completes, Status Code 200 OK is returned with System
Preferences DTO in the body content.

"restrictAccessIPs": [

{

"startIP": "1.1.1.1",

"endIP": "255.255.255.255",

"comment": "Restrict IP.",

"application": "UI"

}

]

}

**Errors** : An error is returned under the following conditions:

  * None

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Update
System Preferences for a Current User

**Method and URI** :

PUT https://api.ultradns.com/prefs

**Parameters** : None

**Body** : Must include a System Preferences DTO.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * Invalid data was submitted in the body.

![Closed](../../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update System Preferences for a Current User

**Method and URI** :

PATCH https://api.ultradns.com/prefs

**Parameters** : None

**Body** : Must include a System Preferences DTO.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * Invalid data was submitted in the body.

