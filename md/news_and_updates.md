

Skip To Main Content

Account

Settings

* * *

Logout

  * placeholder

Account

Settings

* * *

Logout

Filter:

  * All Files

Submit Search

# News and Updates

The News and Updates section provides a list of recent enhancements made to
the REST API User Guide documentation that we want to make customers aware of.
These updates may range from small clarification updates to new features
becoming available via the REST API.

All of the updates found below will coincide with the Release Notes section,
which can be found on the Home page of the Support portal.

Date |  Description |  Section  
---|---|---  
03/12/2025 | 

  * The [Dangling DNS Report](Reports/Dangling DNS Report.htm) is now available. This report is designed to scan for and identify hidden security gaps caused by a Dangling DNS (CNAME) record, which occurs when a CNAME points to a resource that is no longer active or claimed.

|  [Reporting APIs](Reports/Reporting APIs.htm)  
12/11/2024 | 

  * The [DNSSEC Settings](Extended Accounts API/Extended Accounts API.htm#DNSSEC_SETTINGS) section has been updated to include 2 new Account Level DNSSEC configurable settings: **zskrolloverfrequency** and **kskrolloverfrequency**. When configured, these 2 settings will be applied at the account level for all future DNSSEC signing API calls.
  * The [Sign a Zone â Override Account Level Settings](Zone DNSSEC APIs.htm#Sign2) API call allows a zone to be signed without using the preconfigured account-level settings, but instead use custom values when signing the zone. This can be done by using the new dnssecPolicy parameter.
  * The [Custom HTTP Probe Headers](SiteBacker and Traffic Controller Pool Probes.htm#Custom) feature has been added for both SiteBacker and Traffic Controller pools. Configuring HTTP Probe Headers allows you to tailor monitoring to your specific needs and allows you to test server configurations for accurate results and mimic real user traffic to improve monitoring accuracy. 

|  [Extended Accounts API](Extended Accounts API/Extended Accounts API.htm)  
[Zone DNSSEC APIs](Zone DNSSEC APIs.htm) [SiteBacker and Traffic Controller
Pool Probes](SiteBacker and Traffic Controller Pool Probes.htm)  
11/15/2024 | 

  * The [CAA DTO Record Tags/Types](CAA Records API.htm#CAA_DTO_Record_Tags/Types) now includes two additional âissueâ fields:
    * **issuevmc** \- Authorizes the domain name holder to issue mark certificates for the domain.
    * **issuemail** \- Authorizes the domain name owner to restrict the issuance of certificates that certify email addresses.
  * SiteBacker and Traffic Controller Pools now contain **the restorationDelay** field, which allows you to specify the time SiteBacker/Traffic Controller waits after detecting that the failed record--that was failed-over from--is no longer in a failure state and will now failback to. A value of 0 minutes indicates immediate failback. [ SiteBacker Pool Fields](SiteBacker and Traffic Controller Pools API.htm#SiteBacker_Pool_Fields) & [ RDataInfo Fields](SiteBacker and Traffic Controller Pools API.htm#RDataInfo_Fields).
  * Multiple MX records are now supported at the domain/host level. However, a Null MX cannot be added to a domain/host that contains non-null MX records. The [ RRSet DTO](Resource Record Sets.htm#RRSet_DTO) â**rdata** â section has been updated to include these changes.

|  [CAA Records API](CAA Records API.htm) [SiteBacker and Traffic Controller
Pools API](SiteBacker and Traffic Controller Pools API.htm)  
[Resource Record Sets](Resource Record Sets.htm)  
10/24/2024 | 

  * The [Key DTO](Zone DNSSEC APIs.htm#Key) description for the **dnsKeyRecord** has been updated. Additionally, both primary and secondary signed zones will return the âdnsKeyRecordâ field.
  * The [AXFR Failure Reporting Audit Log](Reports/Audit Log Report.htm#AXFR_Failure_Reporting_Audit_Log) API details are now available. This API scheme allows you to generate detailed reports for Zone Transfer Failures (AXFR) across your authoritative DNS zones. Designed to help DNS administrators and operators who utilize DNS redundancy or manage multiple zones, by providing visibility into transfer failures that could impact zone propagation and redundancy.

|  [Zone DNSSEC APIs](Zone DNSSEC APIs.htm) [Audit Log Report](Reports/Audit
Log Report.htm)  
10/02/2024 | 

  * The [Refresh Token](Authorization.htm#Refresh_Token) has been updated to allow users to customize the timeout value of the **expire_in** field for the Refresh Token. If a value is not provided, the Refresh Token will timeout after 7 days.

|  [Authorization](Authorization.htm)  
09/19/2024 | 

  * The DNSSEC [KSK Key Rollover](Zone DNSSEC APIs.htm#KSK_Key_Rollover) call is now available. This call allows you to manually trigger a KSK Key Rollover.

  * The [DNSSEC Multi-Signer (RFC-8901)](Zone DNSSEC APIs.htm#DNSSEC) External Key DTO API call now treats the **ksk** field as optional.

  * The [Security Preferences DTO](Account Settings API.htm#Security_Preferences_DTO) returns the **requireMFA** field, which indicates if the account has been configured for Mandatory Multi-Factor Authentication.
  * The [GET a Single Account ](Extended Accounts API/Extended Accounts API.htm#GET2) API call now returns two new fields in the [User DTO](Extended Accounts API/Extended Accounts API.htm#User): **twoFactorNumDeferred** and **twoFactorEnrollRequired**. These fields indicate if the account is enrolled in Mandatory Multi-Factor Authentication, and if the account has an MFA configured. 

|  [Zone DNSSEC APIs](Zone DNSSEC APIs.htm) [Account Settings API](Account
Settings API.htm) [Extended Accounts API](Extended Accounts API/Extended
Accounts API.htm)  
08/13/2024 | 

  * The management of [SVCB and HTTPS Records](SVCB and HTTPS Records.htm) are now supported.
  * An update was made to the failoverDelay field description for SB and TC pools to indicate the following:
    * Specifies the time, from 0â30 minutes, that SiteBacker will wait after detecting that the pool record has failed before activating secondary records. **This same failover delay value (in minutes) will act as failback delay time. In other words, if failover delay value is x mins, then record will be fail-overed and fail-backed after x mins.**

|  [SVCB and HTTPS Records](SVCB and HTTPS Records.htm) [SiteBacker and
Traffic Controller Pools API](SiteBacker and Traffic Controller Pools API.htm)  
06/26/2024 | 

  * The **Zone Usage Notification** feature is a new Account Setting parameter that allows customers to monitor the Query Volume changes of up to five (5) zones (domains) within their account, and receive automated system generated email notifications if the Query Volume exceeds a configured percentage of change. The Query Volume for a configured zone is taken over the course of a seven-day average.

|  [Account Settings API](Account Settings API.htm)  
06/17/2024 | 

  * The following REST API Reports now return the HTTPS and SVCB record types.
    * [Zone Query Volume Report](Reports/Zone Query Volume Report.htm)
    * [Synchronous Zone Query Volume Report](Reports/Synchronous Zone Query Volume Report.htm)
    * [Zone Daily Query Report](Reports/Zone Daily Query Volume Report.htm)
    * [Host Query Volume Report](Reports/Host Query Volume Report.htm)

|  [Reporting APIs](Reports/Reporting APIs.htm)  
04/15/2024 | 

  * UltraDNS now supports [DNSSEC Multi-Signer (RFC-8901)](Zone DNSSEC APIs.htm#DNSSEC) for zones, which now makes it possible for multiple independent DNS operators to sign a single domain simultaneously.

  * Users can also set the global [DNSSEC Settings](Extended Accounts API/Extended Accounts API.htm#DNSSEC_SETTINGS) now for an account, which will apply the configured values to all zones being signed in the account. 

|  [Zone DNSSEC APIs](Zone DNSSEC APIs.htm) [Extended Accounts API](Extended
Accounts API/Extended Accounts API.htm)  
04/01/2024 | 

  * With the implementation of Zendesk SSO, users (regardless of permissions) can no longer update their Primary or Secondary email address. Please open a ticket at the Support center to request an email address update.
  * Due to the Zendesk SSO changes, the following API calls will no longer allow the Primary or Secondary Email Address for a user to be updated. As such, the corresponding DTO fields have been updated as well.
    * [Update Details of Current User](Extended Accounts API/Extended Accounts API.htm#Update2)
    * [Update Details of Other Users](Extended Accounts API/Extended Accounts API.htm#Update)
  * [Directional Pool Profile Fields](Directional Pools API.htm#Directional_Pool_Profile_Fields-Table) \- the **rdatainfo/type** field has been updated to correctly include RD as a possible pool type.
  * The [Batch Query Request DTO](Batch Query API.htm#_Ref507404150) section has been updated to clarify that the rdata field must be submitted in the **body** field of the request.
  * The Zone Query Volume Report does not support the use of Wildcards, and the documentation has been updated to reflect this.
  * The Traffic Controller [Update a Notification](SiteBacker and Traffic Controller Pool Notifications.htm#Update) API content has been updated to more clearly indicate that the current email address needs to be provided in the method URL, and the new email address needs to be provided in the body of the call.

|  [Extended Accounts API](Extended Accounts API/Extended Accounts API.htm)  
  
[Directional Pools API](Directional Pools API.htm) [Batch Query API](Batch
Query API.htm)  
[Zone Query Volume Report](Reports/Zone Query Volume Report.htm) [SiteBacker
and Traffic Controller Pool Notifications](SiteBacker and Traffic Controller
Pool Notifications.htm)  
01/19/2024 |  In an effort to improve performance by streamlining the database and our offerings, we are removing several reports from the database that are no longer being used by our customers. The following reports will no longer be available:

  * Class C Network Directional Response Counts Report
  * Host Level Advanced Response Codes Report
  * Host Daily Query Volume Report

|  [Reporting APIs](Reports/Reporting APIs.htm)  
01/08/2024 |  In an effort to improve performance by streamlining the database and our offerings, we are removing several reports from the database that are no longer being used by our customers. The following reports will no longer be available:

  * Zone Directional Response Count Report
  * Volume Change Report
  * Postal Code Directional Response Count Report

|  [Reporting APIs](Reports/Reporting APIs.htm)  
11/16/2023 | 

  * SiteBacker (SB) and Traffic Controller (TC) pools can now be created using AAAA (IPv6) records. Please note however, that SB and TC pools cannot contain a mix of A and AAAA records. Individual pools are required to support each record type.

  * The [SiteBacker Agent / Probes](SiteBacker and Traffic Controller Pool Probes.htm#SiteBack) list has been updated.

|  [SiteBacker and Traffic Controller Pool Events](SiteBacker and Traffic
Controller Pool Events.htm) [SiteBacker and Traffic Controller Pool
Notifications](SiteBacker and Traffic Controller Pool Notifications.htm)
[SiteBacker and Traffic Controller Pool Probes](SiteBacker and Traffic
Controller Pool Probes.htm) [SiteBacker and Traffic Controller Pools
API](SiteBacker and Traffic Controller Pools API.htm)  
09/25/2023 | 

  * Updated the [List Metadata for Zones v3 - Cursor Based](Zone API/Zone API.htm#List) Limit parameter to clarify that the default number of requests being returned is 100, but the maximum supported value can be 1,000.

| [Zone API](Zone API/Zone API.htm)  
06/29/2023 | 

  * The [Realtime Push Notifications](Account Settings API.htm#Realtime_Push_Notifications) feature is now available, which allows users to configure up to three Webhook URLS to directly receive system notifications related to Domain and/or Record changes for an account. 
  * Please note that this feature does require users to follow several setup steps to configure and test their URL before being able to configure the types of events that will send notifications. 

|  [Realtime Push Notifications](Account Settings
API.htm#Realtime_Push_Notifications)  
06/16/2023 |  On 2023-06/016, access to the following APIs will be restricted to only those users in the indicated groups. For any users not belonging to the one of the authorized groups identified for the impacted API calls, they will receive a 403 HTTP response error message "Insufficient permissions. User cannot access object" when trying to perform the call.

  * **OWNER, ADMINISTRATIVE, SECURITY_ADMINISTRATION groups**
    * GET https://api.ultradns.com/accounts/{accountName}/users
  * **OWNER, ADMINISTRATIVE, SECURITY_ADMINISTRATION, DNS_ADMINISTRATION groups**
    * GET https://api.ultradns.com/accounts/{accountName}/groups
    * GET https://api.ultradns.com/accounts/{accountName}/groups/{groupName}
    * GET https://api.ultradns.com/accounts/{accountName}/groups/{groupName}/users
    * GET https://api.ultradns.com/accounts/{accountName}/standalone

The [Usage Summary Report - Daily](Reports/Usage Summary Report.htm#Usage_Summary_Report-Daily) API call has been updated. |  [Extended Accounts API](Extended Accounts API/Extended Accounts API.htm#Get_Users_of_an_Account) [Get Security Groups](Extended Accounts API/Extended Accounts API.htm#GET-Security_Groups) [Get a Security Group](Extended Accounts API/Extended Accounts API.htm#GET-Security_Group) [Get Users in a Security Group](Extended Accounts API/Extended Accounts API.htm#GET-Users_in_a_Security_Group) [Get Standalone Security Groups](Extended Accounts API/Extended Accounts API.htm#GET-Standalone_Security_Groups)  
05/30/2023 | 

  * A new notification setting has been added to the [Supported Account Settings Parameters](Account Settings API.htm#Support_Account_Settings_Parameter): **USAGE_NOTIFICATION**. This new feature, also referred to as the Query Threshold Notification, enables a threshold value to be configured that will represent the percentage of the accountâs contractual DNS query volume. Once the threshold value is met or exceeded, the USAGE_NOTIFICATION feature will send system generated notification emails indicating the accountâs contractual DNS query volume amount, and the current DNS query volume that triggered the notification email due to the threshold value being met.
  * For those accounts with the UltraDNS2 feature enabled, the [Usage Summary Report](Reports/Usage Summary Report.htm) will return two new fields in the response output: **queryResponsesCountUltra1** and **queryResponsesCountUltra2**. These new fields will identify the traffic between the two active networks and be displayed as one sum in the queryResponseCounts parameter. 
    * Please note that for accounts with UltraDNS2 enabled, this report will only be able to return up to thirteen (13) monthsâ worth of data.

|  [Account Settings API](Account Settings API.htm#_Toc36651790) [Usage
Summary Report](Reports/Usage Summary Report.htm)  
05/18/2023 |  The release of the Administrative Roles feature introduces two new Security-Groups: **SECURITY-ADMINISTRATION** and **DNS-ADMINISTRATION** , that gives more administrative control and authority to additional users, with pre-defined permissions and restrictions. This is a completely optional feature has been designed to give Account Administrators (or Security personnel) a way to manage and enforce the security preferences and guidelines for ALL users that have access to an account, regardless of additional accounts or permissions they may have.  The following new API calls have been introduced:

  * [Update Details of Other Users](Extended Accounts API/Extended Accounts API.htm#Update)

  * [Forced Password Reset for User](Extended Accounts API/Extended Accounts API.htm#Forced)
  * [Change Password for a User in the Account](Extended Accounts API/Extended Accounts API.htm#Change)
  * [Create Account Level Security Preferences](Account Settings API.htm#Create)
  * [Update Account Level Security Preferences](Account Settings API.htm#Update)
  * [Partially Update Account Level Security Preferences](Account Settings API.htm#Partiall)
  * [Get Account Level Security Preferences](Account Settings API.htm#Get)
  * [Delete Account Level Security Preferences](Account Settings API.htm#Delete)

|  Updates have been made to the following APIs and Sections: [Delete Access
of a User from an Account](Extended Accounts API/Extended Accounts
API.htm#Delete) [User DTO](Extended Accounts API/Extended Accounts
API.htm#User) [Security Group Management](Extended Accounts API/Extended
Accounts API.htm#Security_Group_Management) [Security Group Entry
DTO](Extended Accounts API/Extended Accounts API.htm#Security) [Account
Settings API](Account Settings API.htm#Supported_Account_Settings_Parameters)  
04/25/2023 | 

  * Added the "**Supported Record Types** " to the [Introduction](Introduction.htm) section per customer request.

|  [Introduction](Introduction.htm)  
04/05/2023 | 

  * Neustar Security Services is now officially Vercara, LLC. With this change, you will notice significant color and formatting changes across our Ultra branded portals and services, but fear not as functionality has not been impacted.

|  
01/11/2023 | 

  * The [List Metadata for Zones v3 - Cursor Based](Zone API/Zone API.htm#List) API call will now return the parameter â**ultra2** â in the response, which is used to identify if the zone is UltraDNS2 enabled. This parameter is only applicable for those accounts that have opted to utilize the UltraDNS2 service.
  * The [Zone Query Volume Report](Reports/Zone Query Volume Report.htm) will now return results for both UltraDNS and UltraDNS2 enabled zones (if the account has opted into the UltraDNS2 service), unless specified using the â**ultra2** â parameter in the body of the request.

|  [Zone API](Zone API/Zone API.htm) [Zone Query Volume Report](Reports/Zone
Query Volume Report.htm)  
12/01/2022 | 

  * The Probe Result Summary Report and Probe Result Details Reports using /v1 in the API call are now deprecated. Both reports will need to be run either using /v2, or as we recommend, running the call versionless, or, without a version specific in the method.
  * The [Update Directional Pools](Directional Pools API.htm#Update) section now contains a note indicating that a Directional Pool can be converted to a Resource Record, if a CNAME does not already exist for the ownerName.

|  [Probe Result Details v2 Report](Reports/Probe Result Details v2
Report.htm) [Probe Result Summary v2 Report](Reports/Probe Result Summary v2
Report.htm) [Update Directional Pools](Directional Pools API.htm#Update)  
11/15/2022 | 

  * A new value, **ULTRA2** , has been added to the **feature** parameter for the [Account DTO](Extended Accounts API/Extended Accounts API.htm#Extended_Accounts-Account_DTO) and the [Account List DTO](Extended Accounts API/Extended Accounts API.htm#Extended_Accounts-Account_List_DTO).This value will be returned if the Account has the UltraDNS2 feature enabled.

|  [GET a Single Account ](Extended Accounts API/Extended Accounts
API.htm#GET2) [GET Accounts of a User](Extended Accounts API/Extended Accounts
API.htm#GET)  
09/29/2022 | 

  * The Get Zones of an Account API call has been deprecated and will return an Error 301.
  * The [List Metadata for Zones v3 - Cursor Based](Zone API/Zone API.htm#List) API call has replaced the previous List Metadata for Zones -v3 API method. Please note that this API call will now return cursor-based pagination results, instead of the previous offset-based pagination method.
  * The [Deprecated REST API Calls](Deprecated REST API Calls.htm) section has been added to the guide so that users can track which API calls have been deprecated and utilize the recommended alternative API call.
  * The [Migration Guide for Zone Metadata API Calls](Migration Steps for Zone Metadata API Calls.htm) that has been communicated to our customers has been temporarily added as its own section.

|  [List Metadata for Zones v3 - Cursor Based](Zone API/Zone API.htm#List)  
08/29/2022 | 

  * SiteBacker and Traffic Controller Pools will now return a new field called "**type** " in the response for the GET a (or All) SiteBacker or Traffic Controller Pool API call. The **type** field will return the types of records (and pools) within the zone.
  * The **Get Users of an Account** API call will now return a new field called "**twoFactorAuth** ", which will identify if the specific user has Two Factor Authentication enabled for their account or not.

|  [Get a SiteBacker or Traffic Controller Pool](SiteBacker and Traffic
Controller Pools API.htm#Get_a_SiteBacker_or_Traffic_Controller_Pool)
[Extended Accounts API](Extended Accounts API/Extended Accounts
API.htm#Get_Users_of_an_Account)  
08/02/2022 | 

  * The **ultra2SystemGenerated** field has been added to the RRSET DTO table. This field indicates whether the nameserver(s) in an Rdata list are Ultra2 system generated or not. 
    * The ultra2SystemGenerated field is only returned for those accounts that have Ultra2 enabled.

|  [Resource Record Set (RRSet) DTO](Resource Record Sets.htm#Resource)  
06/14/2022 | 

  * The previous restriction on the **DNS Health Check** that allowed only the Account Owner, or users in the Administrative group to run the **DNS Health Check** for an account has been removed. Now, any user that has the **Read** level permission for the **Domains** Permission type can view and generate the DNS Health Check Status/Report. 

|  [DNS Health Check](DNS Health Check.htm) [Health Status Details
Report](Reports/Health Status Details Report.htm) [Health Status Summary
Report](Reports/Health Status Summary Report.htm)  
04/15/2022 | 

  * The **Get the List of Tasks** API call now returns an additional field â **hasData**. This new field will assist when determining the sort order of tasks.

|  [Tasks](Tasks.htm#Get%20the%20List%20of%20Tasks)  
02/18/2022 | 

  * Email (Mail) Forwarding has been removed from the Usage Summary Report DTO and Response Details. This feature is no longer supported in the REST API or on the UltraDNS Managed Services Portal.

|  [Usage Summary Report](Reports/Usage Summary Report.htm#top)  
02/10/2022 | 

  * Continued improvements to our REST API have resulted in the future deprecation of two REST API calls on 2022-05-15, at 23:59:59 UTC.
    * The **GET Zones of an Account** API call will soon be deprecated, and then decommissioned. The primary reason behind this decision is that the results being returned by this call are already able to be returned by using the List Metadata for Zones API call, thereby allowing us to remove a redundant API.
    * The **List Metadata for Zones** making use of either **/v1** and/or **/v2** in the URI is being deprecated. We request all customers using this version of the API call to follow the steps outlined in the [Migration Steps for List Metadata for Zones â v3](Zone API/Zone API.htm#Migration_Steps_for_List_Metadata_for_Zones-v3) section, and begin using the newest version of this call.
  * Using the newest /v3 version, the [Zone API](Zone API/Zone API.htm#List_Metadata_for_Zones-v3) API is now utilizing cursor-based pagination to return specified items in a dataset. Additionally, using the /v3 version of this API call, will now return the full list of requested zones, and alleviate some customers that previously had to use both versions to get the full list.

|  [Extended Accounts API](Extended Accounts API/Extended Accounts
API.htm#Steps_to_Migrate_from_GET_Zones_of_an_Account) [Extended Accounts
API](Extended Accounts API/Extended Accounts API.htm#Get_Zones_of_an_Account-
Soon_to_be_Deprecated) [Migration Steps for List Metadata for Zones â
v3](Zone API/Zone API.htm#Migration_Steps_for_List_Metadata_for_Zones-v3)
[Zone API](Zone API/Zone API.htm#List_Metadata_for_Zones-v3) [List Metadata
for Zones (Deprecated)](Zone API/Zone API.htm#List_Metadata_For_Zones-
Soon_to_be_Deprecated)  
01/14/2022 |  Accounts will now be locked after multiple unsuccessful login attempts are made. Please wait the indicated amount of time before attempting to log in again, or contact Customer Support. |  [Authorization](Authorization.htm) [Security Preferences](Extended Accounts API/Extended Accounts API.htm#Security_Preferences)

