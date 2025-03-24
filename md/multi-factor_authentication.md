

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

# Multi-Factor Authentication

UltraDNS provides Multi-Factor Authentication (MFA) security for the UltraDNS
Portal. This is an optional tool that you can choose to enable on your
account(s) at no extra expense. Upon logging into the UltraDNS Portal with the
Multi-Factor Authentication feature enabled, you will receive either the
6-digit Verification Code from your Mobile Authentication App, if you enrolled
in the QR Code Based MFA feature, or the Verification Code sent to your mobile
phone number, if you enabled the SMS Based MFA option. Once the Verification
Code has been provided and verified, you will have full access to the UltraDNS
Portal.

Presently, Multi-Factor Mobile Authentication is not supported by the REST
API. If any attempt is made to utilize the REST API from an account that has
Multi-Factor Authentication currently enabled, the following error message
will be returned:

"Two Factor Mobile Authentication security is enabled for this Login. Logging
in from <user_name> is restricted to the UltraDNS Managed Services Portal."

In order to utilize the REST API, the Multi-Factor Authentication feature will
need to be disabled from the UltraDNS Portal.

