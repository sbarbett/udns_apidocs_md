

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

# Email Notifications

You are able to update the notification email address that is on file via the
RESTful interface, and using the [Making Updates via JSON PATCH Format](Making
Updates via JSON PATCH.htm).

Email notifications commonly are sent for Zone Transfer Notification issues
(failures or threshold settings being exceeded), DDOS Notifications,
SiteBacker and Traffic Controller Probe Events, Record Events, and Scheduled
Events.

## Update Notification Email Address

  
**Method and URI** :

PATCH https://api.ultradns.com/zones/{secondaryZoneName}

JSON Example: Update Notification Email Address

{  
"secondaryCreateInfo":  
{  
"notificationEmailAddress":"<updated email address>"  
}  
}

