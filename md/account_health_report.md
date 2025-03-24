

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

# Account Health Report

The Account Health Report returns a list of health status checks for the
accounts that the user has access to, which pertain to best practices and
optional enabled features.

**Method and URI** :

GET https://api.ultradns.com/accounts/healthchecks

**Body** : None

**Parameters** : None

**Response** : Status Code 200 OK is returned with the AccountHealthReport
DTO.

**Errors** : An error is returned under the following conditions:

  * If an unauthorized user tries to call this API.

## AccountHealthReport DTO

Field |  Description |  Type  
---|---|---  
**status** |  The consolidated status of all checks for all accounts of the logged-in user. The value can be one of the followings:

  * **OK**
  * **WARNING**

|  Enum  
**accountHealths** |  The list of AccountHealthRecord. |  The list of AccountHealthReport DTOs.  
  
## AccountHealthRecord DTO

Field |  Description |  Type  
---|---|---  
**accountName** |  Name of the account. |  String  
**status** |  The status of the individual account. The value can be:

  * **OK**
  * **WARNING**

|  Enum  
**results** |  The list of AccountHealthCheckResult. |  The list of AccountHealthCheckResult DTO  
  
## AccountHealthCheckResult DTO

Field |  Description |  Type  
---|---|---  
**name** |  The name of the health check. |  String.  
**status** |  The status of the health check. The value can be:

  * **OK**
  * **WARNING**

|  Enum.  
**description** |  The description of/for the health check. |  String.  
**hint** |  The hint to assist in fixing any issue reported in the health check results. |  String.  
**messages** |  The list of Messages. |  The list of Message DTO  
  
## Message DTO

Field |  Description |  Type  
---|---|---  
**status** |  The status associated with the message. It can contain one of the following values:

  * **OK**
  * **WARNING**

|  Enum  
**message** |  The message string. |  String.  
  
JSON Example: Account Health Report Response

JSON Example: Account Health Report Response ```json { "status": "WARNING",
"accountHealths": [ { "accountName": "example1", "status": "WARNING",
"results": [ { "name": "Is 'two factor authentication(2FA)' enabled on the
account ?", "status": "OK", "description": "'Two factor authentication(2FA)'
avoids security threats due to compromised credentials.", "messages": [ {
"status": "OK", "message": "The 'two factor authentication(2FA)' is enabled on
the account." } ] }, { "name": "Are all the users in the account have 'two
factor authentication(2FA)' configured ?", "status": "WARNING", "description":
"'Two factor authentication(2FA)' avoids security threats due to compromised
credentials.", "hint": "You need to enable 'two factor authentication(2FA)'
for the users '[ultraflash]'.", "messages": [ { "status": "WARNING",
"message": "The 'two factor authentication(2FA)' is not enabled on all the
users of the account." } ] }, { "name": "Is DNSSEC feature enabled on the
account?", "status": "WARNING", "description": "DNSSEC allows your domain to
be secured against spoofing & recursive cache poisoning.", "hint": "Please
contact UltraDNS customer support to enable DNSSEC on your account.",
"messages": [ { "status": "WARNING", "message": "DNSSEC feature is not enabled
on your account." } ] } ] }, { "accountName": "SawanPatidar", "status":
"WARNING", "results": [ { "name": "Is 'two factor authentication(2FA)' enabled
on the account ?", "status": "OK", "description": "'Two factor
authentication(2FA)' avoids security threats due to compromised credentials.",
"messages": [ { "status": "OK", "message": "The 'two factor
authentication(2FA)' is enabled on the account." } ] }, { "name": "Are all the
users in the account have 'two factor authentication(2FA)' configured ?",
"status": "WARNING", "description": "'Two factor authentication(2FA)' avoids
security threats due to compromised credentials.", "hint": "You need to enable
'two factor authentication(2FA)' for the users '[harshazz, spati123, qwertyu,
javauie2e]'.", "messages": [ { "status": "WARNING", "message": "The 'two
factor authentication(2FA)' is not enabled on all the users of the account." }
] }, { "name": "Is DNSSEC feature enabled on the account?", "status": "OK",
"description": "DNSSEC allows your domain to be secured against spoofing &
recursive cache poisoning.", "messages": [ { "status": "OK", "message":
"DNSSEC feature is enabled on your account." } ] } ] } ] } ```

