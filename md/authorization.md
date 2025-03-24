

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

# Authorization

The UltraDNS REST API uses a sub-set of OAuth 2 for authentication. This means
you must know your username and password to proceed. Our form data example
below assumes a username of restapi and password RestAPI1.

Your account will be locked out if you are unsuccessful logging in with your
username and password after multiple attempts. If this occurs, please wait for
the indicated period of time before logging in again, or contact our Customer
Support team for further assistance.

![](../Resources/Images/Rest-API_User_Guide/Introduction_57x65.png) |  If you are a new user and are not able to log into the UltraDNS Portal with your username and password, check with your account owner to verify if your account has been set to **API only Access**. This is a feature that only allows your username and password to give you access to the REST API.  
---|---  
  
For more information about OAuth2, see:
[http://apiux.com/2013/07/10/oauth-2-trumps-basic-
authentication/](http://apiux.com/2013/07/10/oauth-2-trumps-basic-
authentication/ "link to API UX webpage regarding OAuth2 authentication")

**Method and URI:**

[POST
https://api.ultradns.com/authorization/token](https://restapi.ultradns.com/v2/authorization/token)

**Body:** Provide the following form/field details.

Parameter |  Description |  Type  
---|---|---  
grant_type |  The method a client application uses to get an access token. For REST API, grant_type = password |  Value =   
password  
username |  The username for your account. |  String  
password |  The password for your account. |  String  
  
In the following example, we'll be using the following:

  * username = restapi
  * password = RestAPI1

You will receive two tokens in the response:

  * The **accessToken** , which is used to provide your identity on subsequent REST API calls.
  * The **refreshToken** , which is used to obtain a new access token after the previous one expires. The refresh token allows you to get a new access token without sending your username and password.

The response also contains an _expires_in_ value, which tells you the number
of seconds until the accessToken expires.

The screenshot below shows the URL, the completed form data, the call type
(POST), and the response body containing the tokens and the expiration.

![](../Resources/Images/Rest-API_User_Guide/Authorization.png)

![](../Resources/Images/Rest-API_User_Guide/Introduction_53x58.png) |  We use the Postman REST Client to provide example screenshots in this document. Postman is a freely-available REST client that allows you to save and organize frequently-used queries for later use. It can be obtained at [http://www.getpostman.com/.](http://www.getpostman.com/)  
---|---  
  
  
Once you have an accessToken, use it in the request headers to provide
authorization for subsequent requests:

Authorization: Bearer <token>

The screenshot below shows a request header with the accessToken being used
for authorization.

![](../Resources/Images/Authorization-Request.png)

## Refresh Token

When your access token expires, use the refresh token to acquire a new access
token. Alternatively, you can use your login credentials to generate a new
access token and new refresh token, if needed (see previous page for
instructions).

![](../Resources/Images/Rest-API_User_Guide/Introduction_53x58.png) |  You can now set the **expire_in** value to configure the expiration time, in seconds, for your Refresh Token.  
---|---  
  
  

To generate the refresh token:

**Method and URI:**

[POST
https://api.ultradns.comauthorization/token](https://restapi.ultradns.com)

**Body:** Include the following form/field data.

Parameter |  Description |  Type  
---|---|---  
grant_type |  The method a client application uses to get. For REST API, grant_type = refresh_token |  Value =   
refresh_token  
refresh_token |  The Refresh Value token taken from the Authorization API call. |  String  
expire_in |  Set the duration, in seconds, in which the Refresh Token will expire. This is an optional field with. Default value = 604800 (7 days) Allowed Value = 1 - 604800 |  Integer  
  
![](../Resources/Images/Rest-API_User_Guide/Introduction_63x72.png) |  A Note About Refresh Tokens:

  * The refresh token expires after 7 days by default, unless **expire_in** value is configured.
  * Only one refresh token is valid at a time.
  * If you use your username and password to acquire a new access token and refresh token, the old refresh token will automatically become expired.

  
---|---  
  
  
The figure below shows a completed request header that uses the refreshToken
to obtain a new accessToken.

![](../Resources/Images/Authorization-Request-Full.png)

