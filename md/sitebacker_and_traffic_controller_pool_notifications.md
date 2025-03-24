

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

# SiteBacker and Traffic Controller Pool Notifications

Notifications are used to specify who is alerted when an event is triggered
for a particular pool record. Since events can only be created for pool
records, notifications in turn can only be created for pool records, not for
sub pools however.

Notifications can only be created for Primary Records. You cannot create
notifications for All Fail Records. If the request contains an All Fail
Record, then an error is returned with the following message - **Notifications
cannot be configured for All Fail Records.**

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get
Notifications for a Pool

**Method and URI** :

GET
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/notifications

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
NotificationList DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create a
Notification for Specified Pool Records

**Method and URI** :

POST
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/notifications/{emailAddress}

**Parameters** : None

**Body** : Must include a Notification DTO.

**Response** : If task completes, Status Code 201 is returned with a Location
Header containing the URI of the notification.

  * If the task happens in the background, Status Code 202 is returned along with an X-Task-ID header and a status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

  * If {emailAddress} is already associated with any pool records in this pool.

  * If the pool contains both A and AAAA record types.

JSON Example: Create a Pool Notification

{  
"email": "email@notification.com",  
"poolRecords": [  
{  
"poolRecord": "1.2.3.4",  
"notification": {  
"probe": true,  
"record": false,  
"scheduled": true  
}  
},  
{  
"poolRecord": "a.domain.name.",  
"notification": {  
"probe": true,  
"record": true,  
"scheduled": false  
}  
}  
]  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get a
Notification for a Pool

**Method and URI** :

GET
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/notifications/{emailAddress}

**Parameters** : None

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
NotificationList DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

  * If this {emailAddress} has not been defined for notifications for this pool.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update a
Notification

This will update the Notification Information for only the Pool Record
specified in the Notification DTO. If the notify flag (probe, scheduled,
record) is not specified in the Notification DTO, then it is set to false.

The following sample JSON will turn off Notifications for a Pool Record:

{  
"email": "test@test1.com",  
"poolRecords": [  
{  
"poolRecord": "1.2.3.4",  
"notification": {  
}  
}  
]  
}

**Method and URI** :

Provide the current email address in the {emailAddress} of the PUT URL, and
then add the new email address in the body of the call.

PUT
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/notifications/{emailAddress}

**Parameters** : None

**Body** : Must include a Notification DTO. Because this is a full update, if
the notification flag is not specified in the DTO, the notification will be
set to false (turned off). See the JSON example above.

  * Include the new email address in the body of the call.

**Response** : If update completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If update happens in the background, Status Code 202 is returned along with an X-Task-ID header and a status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

  * If you don't have permissions to access the pool.

  * If {emailAddress} is not associated with any pool records in this pool.

  * If the pool contains both A and AAAA record types.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete a
Notification

**Method and URI** :

DELETE
https://api.ultradns.com/zones/{zoneName}/rrsets/A/{ownerName}/notifications/{emailAddress}

**Parameters** : None

**Body** : None

**Response** : If delete completes immediately, Status Code 204 is returned
with no content in the body.

  * If delete happens in the background, Status Code Status Code 202 is returned along with an X-Task-ID header and status message of âPendingâ in the body content.

**Errors** : An error is returned under the following conditions:

  * If {zoneName} is not valid.

  * If you don't have permission to read this zone.

  * If pool does not exist or is not a SiteBacker/Traffic Controller pool.

## _Pool Notification DTOs_

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)NotificationInfo
DTO

The NotificationInfo DTO describes the conditions in which a notification is
sent.

NotificationInfo DTO

Field |  Description |  Type  
---|---|---  
**probe** |  Indicates whether to notify on probe events. |  Boolean.  
**record** |  Indicates whether to notify on record events. |  Boolean.  
**scheduled** |  Indicates whether to notify on scheduled events. |  Boolean.  
  
JSON Example: Notification

{  
"probe": true,  
"record": true,  
"scheduled": false  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Notification
DTO

The Notification DTO associates an email address with a list of pool records.
Each pool record is in turn associated with a NotificationInfo configuration.

Notification DTO

Field |  Description |  Type  
---|---|---  
**email** |  The email address being notified. This field is returned on GET, but ignored on POST, PUT, and PATCH. |  String. Valid email address.  
**notifications/poolRecords** |  The list of pool record settings for this email address. |  Array.  
**notifications/poolRecords/poolRecord** |  The pool record. |  String. Either an IP address or a valid owner name.  
**notifications/poolRecords/notification** |  The NotificationInfo DTO describing the notifications for this pool record/email address combination. |  NotificationInfo DTO  
  
JSON Example: Notification Info

{  
"email": "a@b.com",  
"poolRecords": [  
{  
"poolRecord": "1.2.3.4",  
"notification": {  
"probe": true,  
"record": false,  
"scheduled": true  
}  
},  
{  
"poolRecord": "2.4.5.6",  
"notification": {  
"probe": true,  
"record": true,  
"scheduledâ: false  
}  
}  
]  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)NotificationList
DTO

The NotificationList indicates the configured notifications.

NotificationList DTO

Field |  Description |  Type  
---|---|---  
**notifications** |  The list of notifications. |  Array of the Notification DTO.  
  
JSON Example: Notification Info List

{  
"notifications": [  
{  
"email": "a@b.com",  
"poolRecords": [  
{  
"poolRecord": "1.2.3.4",  
"notification": {  
"probe": true,  
"record": false,  
"scheduled": true  
}  
},  
{  
"poolRecord": "2.4.5.6",  
"notification": {  
"probe": true,  
"record": true,  
"scheduled": false  
}  
}  
]  
},  
{  
"email": "c@d.com",  
"poolRecords": [  
{  
"poolRecord": "1.2.3.4",  
"notification": {  
"probe": false,  
"record": true,  
"scheduled": false  
}  
}  
]  
}  
]  
}

