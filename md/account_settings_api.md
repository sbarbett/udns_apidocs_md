

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

# Account Settings API

Using the Account Setting API, users can obtain and manage information for
various account level settings. The following details contain the account
level settings that can be managed using the available Account Setting APIs.

Supported Account Settings Parameters

Supported Account Settings

Setting Name |  Description |  DTO  
---|---|---  
ZONE_TRANSFER_NOTIFICATION |  When there are Zone Transfer updates or failures, this setting allows you to customize the recipient(s) that should be notified, how they should be notified, and the threshold limit at which the notifications should be sent. |  NotificationSetting DTO  
SERVICE_NOTIFICATION  |  The Service Notification configuration allows you to configure email addresses that will receive system generated emails for incidents that impact the UltraDNS service. **Note: Service Notifications are not applicable for Parent Sub Accounts or Sub Accounts in the Multi-Level Account Management hierarchy.** |  NotificationSetting DTO  
USAGE_NOTIFICATION |  The Usage Notification configuration allows you to set a threshold value (percentage) and configure email addresses that will receive system generated emails when the DNS query volume for an account exceeds the threshold value. |  NotificationSetting DTO  
ZONE_USAGE_NOTIFICATION |  The Zone Volume Notifications function allows you to monitor the Query Volume changes of up to five (5) zones (domains) within your account, and receive automated system generated email notifications if the Query Volume exceeds a configured percentage of change. The Query Volume for a configured zone is taken over the course of a seven-day average. |  Zone Usage Notification DTO  
PUSH_NOTIFICATIONS |  The Push Notifications configuration allows you configure a webhook URL to receive real-time notifications for a series of configured events as they occur within your account. |  RealtimePushNotification Create DTO  
SECURITY_PREFERENCES |  The Security Preferences configuration allows you to specify and configure security preferences at the account level, which will impact users in the account as well.  |  Security Preferences DTO  
  
## Realtime Push Notifications

The Realtime Push Notifications feature allows _Owners and/or Users in the
Administrative group_ to configure a webhook to directly receive system
notifications related to Domain and/or Record changes for an account.

Configuring the Realtime Push Notifications is a multi-step account, that
requires a test validation before configuring the various changes and events
you wish to be notified about. Please perform the following API calls in the
specified order to test and configure your Realtime Push Notification.

Please note that a maximum of three Realtime Push Notification configurations
can exist for an account.

  1. Run the Realtime Push Notifications - Test Endpoint call to verify that the URL Endpoint you have provided can be reached.

  2. Copy the **telemetryEventId** value that is returned.

  3. Run the Realtime Push Notifications - Verify Endpoint call, using the **telemetryEventId** value from step 2 to verify the connection response.

  4. Optionally, you can run the GET Realtime Push Notifications - Available Channels to return a list of possible channels and events that can be configured for your account.

  5. Run the Create Realtime Push Notification call to setup your configuration.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Realtime Push
Notifications - Test Endpoint

Use this API call to test your Endpoint URL connection prior to configuring
your Realtime Push Notifications setup.

**Method and URI:**

POST accounts/{accountName}/telemetryWebhook/test

**Parameters:** None

**Body:** Must contain the RealtimePushNotification Test Connection DTO.

**Response:** If task completes, Status Code 200 OK is returned with a
RealtimePushNotification Test Response DTO.

**Errors:** An error is returned under the following conditions:

  * You are not the Owner or Administrative User for the specified account.

  * The Endpoint URL could not be reached.

JSON Example: Realtime Push Notification - Test Endpoint Response

{

"telemetryEventId": "3e58c9a7-5e7b-405f-8bf6-b8bad72a32e8",

"telemetryEventType": "TEST_TELEMETRY_WEBHOOK",

"telemetryEventTime": "2023-06-22 12:13:33.441",

"environment": "test",

"accountName": "{accountName}"

}

RealtimePushNotification Test Connection DTO

Supported Account Settings

Attribute |  Description |  Type  
---|---|---  
url  |  The Endpoint URL you will be sending notifications to. |  String.  
type |  Always **TEST_TELEMETRY_WEBHOOK**. |  String.  
  
RealtimePushNotification Test Response DTO

Supported Account Settings

Attribute |  Description |  Type  
---|---|---  
telemtryEventID |  The unique ID assigned to the Push Notification event details. Used to verify the endpoint.  |  String.  
telemetryEventType |  Identifies the type of event(s) that triggered the real-time notification to be sent. |  String.  
telemetryEventTime |  The time at which the event triggered the notification (in UTC). |  String.  
environment  |  The environment where the event occurred.  |  String.   
accountName |  The name of the account that the Endpoint URL has been configured for. |  String.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Realtime Push
Notifications - Verify Endpoint

Use this API call to verify that your Endpoint URL can be reached and returns
a Success message.

**Method and URI:**

POST accounts/{accountName}/telemetryWebhook/test

**Parameters:** Requires the **telemetryEventId** from the
RealtimePushNotification Test Response DTO.

**Body:** None

**Response:** If task completes, Status Code 200 OK is returned.

**Errors:** An error is returned under the following conditions:

  * You are not the Owner or Administrative User for the specified account.

  * The Endpoint URL could not be reached.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)GET Master
Catalog for all Account Level Settings

Using this API, you can retrieve a list of all supported account level
settings that are in the system.

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/settings/

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with an
AccountSettingsCatalogItem List DTO in the response body.

**Errors** : An error is returned under the following conditions:

  * You do not have permission to read account settings for the specified {accountName}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)GET Realtime
Push Notifications - Available Channels

Use this API call to return the list of possible channels and events that can
be configured when creating your Realtime Push Notification. The list of
possible channels can also be found in the RealtimePushNotification Create
DTO.

**Method and URI:**

GET /accounts/{accountName}/settings/PUSH_NOTIFICATIONS/availableChannels

**Parameters:** None

**Body:** None

**Response:** If task completes, Status Code 200 OK is returned.

**Errors:** An error is returned under the following conditions:

  * You are not the Owner or Administrative User for the specified account.

JSON Example: Realtime Push Notifications - Available Channels Response

{

"availableChannels": [

{

"id": "DOMAIN_CHANGES",

"name": "Domain Changes",

"parentId": "ALL_CHANGES",

"displayOrder": 1,

"testEventPayload": "{\n \"objectType\": \"ZONE\", \n \"changeType\":
\"DELETE\", \n \"object\": \"udns-telemetry-test.invalid.\",\n \"user\":
\"test-user\", \n \"ipAddress\": \"64.6.64.6\",\n \"changeTime\": \"2021-10-07
06:45:21.467\",\n \"account\": \"accountName\", \n \"changeComment\": \"Test
telemetry event\", \n \"detail\": {\n \"changes\": [ { \n \"value\":
\"name\",\n \"from\": \"udns-telemetry-test.invalid.\",\n \"to\": \"\"\n }
],\n \"extraInfo\": {\n \"number_of_records\": \"2\",\n \"type\":
\"Primary\",\n \"isTestEvent\": \"true\"\n} } }"

},

{

"id": "AUTHENTICATION_EVENTS",

"name": "Authentication Events",

"parentId": "ALL_EVENTS",

"displayOrder": 3

},

{

"id": "XFR_EVENTS",

"name": "Zone Transfer Events",

"parentId": "ALL_EVENTS",

"displayOrder": 2

},

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create
Account Setting for an account

**Method and URI** :

POST https://api.ultradns.com/accounts/{accountName}/settings/{settingName}

**Parameters** : settingName can be one of from Supported Account Settings
Parameters

**Body** : NotificationSetting DTOas per path param specified in the endpoint
URL.

Since this is a POST function, all account settings and all the fields in the
DTOs must be specified, otherwise the user will get validations error.

For the **SERVICE_NOTIFICATION** setting, only one email address is permitted
as part of the request payload.

For the **USAGE_NOTIFICATION** setting, a maximum of five email addresses can
be configured as part of the request payload.

**Response** : If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * Invalid data was submitted in the body around any validation error.

  * Given {settingName} already exists in the system.

  * You do not have permission to configure account settings for the specified {accountName}.

  * You are not the Owner or Administrative user for the specified {accountName}.

  * Invalid email address or invalid email address count provided.

JSON Example: Create Service Notification setting

JSON Example: Create Service Notification setting ```json {
"emailNotification": { "emails": [ "test1@test.com" ] } } ```

JSON Example: Create Usage Notification Setting

JSON Example: Create Usage Notification Setting ```json { "threshold": 100,
"emailNotification": { "enable": true, "emails": [ "john.smith@test.com",
"jane.smith@test.com", "ted.name@test.com", "dnsqueryalert@test.com",
"engineering@test.com" ] } } ```

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create
Account Level Security Preferences

Users belonging to either the Owner and/or ADMINISTRATIVE groups can create
security preferences at the account level.

**Method and URI:**

POST https://api.ultradns.com/accounts/{accountName}/settings/{settingName}

**Parameters:** Must include the **securityPreferences** parameter.

**Body:** Security Preferences DTO.

JSON Example: Create Account-Level Security Preference Setting

JSON Example: Create Account-Level Security Preference Setting ```json {
"securityPreferences": { "inactivityTimeout": 40, "passwordExpiration": 50,
"inactivityUserLockThreshold": 0 } } ```

Security Preferences DTO

Supported Account Settings

Attribute |  Description |  Type  
---|---|---  
requireMFA |  Indicates if the Mandatory Multi-Factor Authentication account-level setting is enabled for the account, requiring users to configure MFA for their account.

  * true = Enabled
  * false = No (Default) 

|  Boolean.  
inactivityTimeout |  Determines the length of time (in minutes) at which point the session for a user will be timed out, The value of this field will either be 0 or ( >= 10 minutes and <= 120 minutes).  |  The value 0 means this preference is not set at the account level and will instead be applied from the user level.  
passwordExpiration  |  Determines the length of time (in days) at which point all usersâ passwords in the account should be marked as expired. The value of this field will either be 0 or ( >= 14 days and <= 365 days). |  The value 0 means this preference is not set at the account level and will instead be applied from the user level.  
inactivityUserLockThreshold  |  Determines the time (in days) at which point users should be marked as suspended due to inactivity. The value of this field will either be 0 or (>= 60 days and <= 365 days). |  The value 0 means this preference is not set at the account level and will instead be applied from the user level.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create
Realtime Push Notification

**Method and URI:**

POST /accounts/{accountName}/settings/PUSH_NOTIFICATIONS

**Parameters:** None

**Body:** Must include the RealtimePushNotification Create DTO.

**Response:** If task completes, Status Code 200 OK is returned.

**Errors:** An error is returned under the following conditions:

  * You are not the Owner or Administrative User for the specified account.

RealtimePushNotification Create DTO

Supported Account Settings

Attribute |  Description |  Type  
---|---|---  
enable |  Determines if the webhook url should be active and receiving real-time push notifications for the configured events, or if it should be disabled. |  Boolean.  
url |  The Webhook URL Endpoint. |  String.  
include |  The list of channels and events that you wish to receive notifications for. Valid values are: 

  * ALL_CHANGES
  * DOMAIN_CHANGES
  * RECORD_CHANGES
  * USER_GROUP_CHANGES
  * ALL_EVENTS
  * ZONE_EVENTS
  * FAILOVER_EVENT
  * DNSSEC_EVENT
  * XFR_EVENTS
  * ZONE_TRANSFER_SUCCESS
  * ZONE_TRANSFER_FAILURE
  * AUTHENTICATION_EVENTS
  * LOGIN_SUCCESS
  * LOGIN_FAILURE

|  String.  
  
JSON Example: Create Realtime Push Notification Configuration

JSON Example: Create Realtime Push Notification Configuration ```json {
"webhooks": [ { "enable": true, "url": "https://example.com/webhookOne",
"include": { "ALL_CHANGES": true } }, { "enable": true, "url":
"https://example.com/webhookTwo", "include": { "RECORD_CHANGES": true,
"DOMAIN_CHANGES": true } }, { "enable": true, "url":
"https://example.com/webhookThree", "include": { "AUTHENTICATION_EVENTS": true
} } ] } ```

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Account Setting for an account

**Method and URI** :

PUT https://api.ultradns.com/accounts/{accountName}/settings/{settingName}

**Parameters** : settingName can be one of from Supported Account Settings
Parameters.

**Body** : NotificationSetting DTO

For the **SERVICE_NOTIFICATION** setting, only one email can be
added/updated/deleted at a time. For adding an email, the existing emails
along with the new email should be present in the request payload. Similarly,
for updating an existing email, the updated email should be present in the
request payload along with the existing ones. For deleting an email, all the
emails except the one to be deleted should be present in the request payload.

For the **USAGE_NOTIFICATION** setting, a maximum of five email addresses can
be added/updated/deleted.

For the **PUSH_NOTIFICATION** setting, a maximum of three Webhook URLs can be
configured.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * Invalid data was submitted in the body around any validation error.

  * Given {settingName} does not exists in the system.

  * You do not have permission to configure account settings for the specified {accountName}.

  * You are not the Owner or Administrative user for the specified {accountName}.

  * Invalid email address or invalid email address count provided.

  * Invalid threshold value setting.

JSON Example: Add email while updating (Service) Notification setting

JSON Example: Add email while updating (Service) Notification setting ```json
{ "emailNotification": { "emails": [ "test1@test.com", "test2@test.com" ] } }
```

JSON Example: Update email while updating (Service) Notification setting

JSON Example: Update email while updating (Service) Notification setting
```json { "emailNotification": { "emails": [ "test1@test.com",
"test2updated@test.com" ] } } ```

JSON Example: Remove email while updating (Service) Notification setting

JSON Example: Remove email while updating (Service) Notification setting
```json { "emailNotification": { "emails": [ "test1@test.com" ] } } ```

JSON Example: Update Push Notification Webhook URL Settings

JSON Example: Update Push Notification Webhook URL Settings ```json {
"webhooks": [ { "enable": true, "url": "https://httpbin.org/status/202",
"include": { "DOMAIN_CHANGES": true } }, { "enable": false, "url":
"https://4rn82guh47.execute-api.us-east-1.amazonaws.com/demo/recordChanges",
"include": { "RECORD_CHANGES": true } }, { "enable": false, "url":
"https://httpbin.org/status/202", "include": { "ALL_TELEMETRY": true } } ] }
```

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update
Account Level Security Preferences

Users belonging to either the Owner and/or ADMINISTRATIVE groups can update
the security preferences at the account level.

**Method and URI:**

PUT https://api.ultradns.com/accounts/{accountName}/settings/{settingName}

**Parameters:** Must include the **securityPreferences** parameter.

**Body:** Security Preferences DTO.

JSON Example: Update Account Level Security Preferences

JSON Example: Update Account Level Security Preferences ```json {
"securityPreferences": { "inactivityTimeout": 40, "passwordExpiration": 50,
"inactivityUserLockThreshold": 0 } } ```

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update Account Setting for an account

**Method and URI** :

PATCH https://api.ultradns.com/accounts/{accountName}/settings/{settingName}

**Parameters** : **settingName** can be one of from Supported Account Settings
Parameters.

**Body** : Since this is a PATCH function, only the specified
NotificationSetting DTO being updated need to be included in the list. All
settings in the NotificationSetting DTO not included in the list will retain
their current state.

This endpoint is not supported for the **SERVICE_NOTIFICATION** setting.

**Response** : If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

**Errors** : An error is returned under the following conditions:

  * Invalid data was submitted in the body around any validation error.

  * Given {settingName} does not exists in the system.

  * You do not have permission to configure account settings for the specified {accountName}.

  * You are not the Owner or Administrative user for the specified {accountName}.

  * If the request was submitted for the **SERVICE_NOTIFICATION** setting.

  * Invalid email address or invalid email address count.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Partially
Update Account Level Security Preferences

Users belonging to either the Owner and/or ADMINISTRATIVE groups can partially
update the security preferences at the account level.

**Method and URI:**

PATCH https://api.ultradns.com/accounts/{accountName}/settings/{settingName}

**Parameters:** Must include the **securityPreferences** parameter.

**Body:** Security Preferences DTO.

JSON Example: Partial Update Account Level Security Preferences

JSON Example: Partial Update Account Level Security Preferences ```json {
"securityPreferences": { "inactivityTimeout": 40, "passwordExpiration": 50,
"inactivityUserLockThreshold": 0 } } ```

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)GET Account
Setting for an account

**Method and URI** :

GET https://api.ultradns.com/accounts/{accountName}/settings/{settingName}

**Parameters** : **settingName** can be one of Supported Account Settings
Parameters.

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
NotificationSetting DTO in the response body.

**Errors** : An error is returned under the following conditions:

  * Given {settingName} does not exists in the system.

  * You do not have permission to read account settings for the specified {accountName}.

  * You are not the Owner or Administrative user for the specified {accountName}.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get Account
Level Security Preferences

Users belonging to either the Owner and/or ADMINISTRATIVE groups can retrieve
the security preferences at the account level.

**Method and URI:**

GET https://api.ultradns.com/accounts/{accountName}/settings/{settingName}

**Parameters:** Must include the **securityPreferences** parameter.

**Body:** None

JSON Example: Retrieve Account Level Security Preferences Response

JSON Example: Retrieve Account Level Security Preferences Response ```json {
"securityPreferences": { "requireMFA": true, "inactivityTimeout": 40,
"passwordExpiration": 50, "inactivityUserLockThreshold": 0 } } ```

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete
Account Setting for an account

**Method and URI** :

DELETE https://api.ultradns.com/accounts/{accountName}/settings/{settingName}

**Parameters** : The settingName can be one of the available attributes from
the Account Settings API.

**Body** : None.

This endpoint is not supported for the **SERVICE_NOTIFICATION** setting.

**Response** : If delete completes, Status Code 204 is returned with no
content in the response body.

**Errors** : An error is returned under the following conditions:

  * You do not have permission to delete account settings for the specified {accountName}.

  * Given {settingName} does not exists in the system.

  * If the request was submitted for the **SERVICE_NOTIFICATION** setting.

  * You are not the Owner or Administrative user for the specified {accountName}.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete
Account Level Security Preferences

Account-Level Security Preferences cannot be deleted at this time. To disable
the Account-Level Security Preferences, set all the configured Security
Preferences DTO values to 0.

## _Account Settings DTOs_

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Account
Settings Catalog Item DTO

AccountSettingsCatalogItem DTO

Attribute |  Description |  Type  
---|---|---  
displayName |  The display name of account level setting |  One of the following account level setting as mentioned in Supported Account Settings table String type  
uri |  The uri for performing the operation of account level setting |  String type  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Account
Settings Catalog Item List DTO

AccountSettingsCatalogItem List DTO

Attribute |  Description |  Type  
---|---|---  
**accountSettingsCatalogItems** |  The specified account settings for the account |  List ofAccountSettingsCatalogItem DTO.  
  
JSON Example: AccountSettingList DTO

"accountSettingsCatalogItems" : [  
{  
"displayName" : "Zone Transfer Notifications"  
"uri" : "/acccount/{accountName}/settings/ZONE_TRANSFER_NOTIFICATION"  
}  
]

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Notification
Setting DTO

NotificationSetting DTO

Attribute |  Description |  Type  
---|---|---  
threshold |  The specified threshold value that when met (or exceeded) , will trigger system generated emails to be sent to the configured email addresses. This property is not applicable for the SERVICE_NOTIFICATION setting. If specified then it will be ignored. |  Integer type.  
emailNotification |  The specified account settings for email notification. |  EmailNotification DTO type.   
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif) Email
Notification DTO

EmailNotification DTO

Attribute |  Description |  Type  
---|---|---  
enable |  Account setting for enabling/disabling Email pool level notification. The property is not applicable for the **SERVICE_NOTIFICATION** setting. |  Boolean type  
emails |  The specified account settings for configuring email Ids for receiving Email notification.

  * Max of five email addresses for the **USAGE_NOTIFICATION** setting.

|  List of String  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Zone Usage
Notification DTO

Attribute |  Description |  Type  
---|---|---  
zone |  The Zone Name to configure the Query Usage Notification for. |  String  
threshold  |  The percentage value that will be used when comparing the last seven-daysâ worth of queries for the zone. If the query volume exceeds the threshold value, a notification will be sent to the list of configured emails.  Valid values are: **5, 10, 20, 25, 50, 75, 100**.  |  Integer  
enable |  Account setting for enabling/disabling Email pool level notification. This property is not applicable for the **SERVICE_NOTIFICATION** setting. |  Boolean type  
emails |  The specified account settings for configuring email Ids for receiving Email notification.

  * Max of five email addresses can be configured per zone.

|  List of String  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)JSON Examples

JSON Example: NotificationSetting DTO  

The below example is applicable for the ZONE_TRANSFER_NOTIFICATION setting:

{  
"threshold": 200,  
"emailNotification": {  
"enable": true,  
"emails": [  
"test@test.com"  
]  
}  
}

The following example is applicable for the SERVICE_NOTIFICATION setting:

JSON Example: NotificationSetting DTO ```json { "emailNotification": {
"emails": [ "test@test.com" ] } } ```

The following example is applicable for the USAGE_NOTIFICATION setting:

{  
"threshold": 200,  
"emailNotification": {  
"enable": true,  
"emails": [  
"test@test.com"  
]  
}  
}

The following example is applicable for the ZONE_USAGE_NOTIFICATION setting:

"uri" : "/acccount/{accountName}/settings/ZONE_USAGE_NOTIFICATION"

{

"zone" : zonetest.com,

"threshold": 25,

"emailNotification": {

"enable": true,

"emails": [

"user@example.com",

"user2@example.com",

"distrolist@example.com"

]

}

}

