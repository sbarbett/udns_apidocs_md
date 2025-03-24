

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

# Introduction

This document outlines the Neustar UltraDNS REST API details. This API allows
you to:

  * Create and test new API calls against a test environment that mimics your production setup.
  * Use REST requests to remotely manage objects in the Neustar UltraDNS database.
  * Provide an alternative to the Neustar UltraDNS Managed Services Portal (UltraDNS Portal).

## URLs

Use the following base URLs for running REST API calls against the appropriate
UltraDNS environment.

  * REST API customer test environment for configuration information and changes: <https://test-api.ultradns.com>
  * Production environment for configuration information and changes: <https://api.ultradns.com>
  * Production environment for using the Reporting API: https://api.ultradns.com/reports

All of the URI constructs that are provided use the Production URL. However,
feel free to test any of your calls against the customer test environment URL
to be certain the calls perform the actions you need them to. There are some
limitations to the test environment. Contact Neustar customer support for
information on the Customer Test Environment.

## Calling the APIs

The UltraDNS APIs can accept requests and return responses in both XML and
JSON formats. The default response format is JSON unless otherwise specified
(even if the request was sent in XML). While XML is supported, JSON is the
preferred format, and all of the examples provided in this document are in
JSON.

Controlling the format of the request and response is done by supplying the
"Content-type" and "Accept" HTTP headers respectively, specifying
**application/xml** or **application/json** for the value in either header (or
both). Keep in mind that you do not have to specify JSON for a response.

You also have the option of using the JSON PATCH format for updates. Use the
PATCH HTTP method and supply **application/json-patch+json** for the value in
the "Content-type" HTTP header.

## UltraDNSAPI Versioning

The REST API has undergone a change in how API calls are made. UltraDNS API
Versioning removes the requirement for you to add the /v1/ or /v2/ parameter
in the URI when making an API call. The API call will automically use the most
recent version in production.

Also, all API calls now point to a new endpoint, as noted above in the URLs
section. This change provides greater consistency across the API calls
available, as well removing the need for an âAuthorization Tokenâ for API
calls, and an âAuthentication Tokenâ for Reporter API calls.

The previous method of using the full endpoint (including the version) will
still work as expected, but we recommend using the new method. If you are
trying to run an API call with a specific version, you must specify that
version in the call. Otherwise, by default, not providing a version will
default to the latest version.

There are several API calls that will return different details based upon the
version (if provided) in the API call. The following table details the API
calls that still return different results based upon the version used.

API Versioning Updates and Changes

API Call |  Description  
---|---  
Directional Update |  Updating the TTL of a Directional Pool at the record level cannot be completed when using /v1/ in the API call.  
[Deprecated ISO Codes](Directional Pools API.htm#_Ref532217526) |  Using /v1/ for a Directional API call will return different Geo-ISO details than the default (/v2) method will.  
[Batch API](Batch API.htm#_Ref532217549) |  Batch API calls can ONLY be run when using /v1/ in the API call.  
[Batch Query API](Batch Query API.htm#_Ref471981146) |  Batch Query API calls can ONLY be run when using /v1/ in the API call.  
[Reporting APIs](Reports/Reporting APIs.htm#_Ref532217613) |  Report APIs no longer require the âAuthenticationâ Token to be run. All API calls can be run using the original REST API [Authorization](Authorization.htm#_Ref495059463) Token.  
[Reporting APIs](Reports/Reporting APIs.htm#_Ref532217651) |  When using the Response Link Headers to retrieve additional report results, the link header can ONLY be run when using the /v1/ in the API call.  
  
## Data Transfer Objects (DTOs)

Data Transfer Object (DTO) is simply another term for data structure. In this
document, DTOs are the information either sent or returned for an API call,
having a particular structure and containing particular information.

Each value in a DTO can be a single value of a specified type (Boolean,
String, Integer, etc.), a series of comma-separated values (where permitted),
or the value may be comprised of other DTO data and structure.

For example, if you want to create a new Primary zone, the API call to do so
requires the inclusion of the **Zone Create DTO** which contains the following
two fields:

  * properties â Consists of the [Zone API](Zone API/Zone API.htm#_Ref396210320)

  * primaryCreateInfo â Consists of the [Zone API](Zone API/Zone API.htm#_Ref395097877).

In turn, the Primary Zone DTO consists of several individual values and can
include subsequent DTOs such as the [Restrict IP DTO](Zone API/Zone API
DTOs.htm#Restrict) or the [Notify Address DTO](Zone API/Zone API
DTOs.htm#Notify).

## Responses to API Calls

All operations return a response, and all responses have a response code (HTTP
Status Code). The code number returned depends on the kind of operation you
sent, (Get, Put, Delete) and the status of the operation (Created, Successful,
Failed, or Pending).

Successful Response Codes are returned as follows:

  * Status Code 200 is typically returned for a request (GET) or modification (PUT, PATCH) of information and notes the call was Successful. If the call was a GET, you should receive a DTO containing the information you requested.

  * Status Code 201 is typically returned for a POST call and indicates that the object was created.

  * Status Code 202 is returned if the request has been accepted, but has yet to be completed from when the response was sent (status of Pending). These responses also include an X-Task-ID header.

  * Status Code 204 is returned for DELETE calls, indicating the deletion was successful and there is no content to return. There is no body content presented for these responses.

If an error condition occurs, you will you receive a 400 or 500 series (4xx or
5xx) HTTP Status Code along with an HTTP body containing a specific UltraDNS
error code and a description of the error. For example,

[  
{  
"errorCode":1801,  
"errorMessage": "Zone does not exist in the system."  
}  
]

For detailed database transactions, a system error message is received, with a
9999 Error Code. For example:

### 429 Error Response

![](../Resources/Images/MSP_User_Guide/Two Factor Mobile Authentication_65x65.png) |  **Error 429 (Too Many Requests)**

  * This response is issued when too many requests are received from the same customer and/or IP address. The REST API monitors and restricts the frequency of incoming requests from the same customer and/or IP address for security reasons, as well as to protect the service from overloading.

**Tips to Avoid the 429 Error (Too Many Requests) Response**

  * Re-use your authentication token multiple times, as opposed to obtaining a new authentication token every time you need to make a REST API call. (Authentication tokens currently can be re-used for up to an hour.)
  * If you are still getting 429 error responses, introduce a cool down pause of 0.5-1.0 seconds between the REST API requests you make.

  
---|---  
  
## Supported Record Types

Please find the list of currently supported Record Types along with their
Record Type ID that can be managed through our REST API and UltraDNS Managed
Services Portal.

Record Type |  Record Type ID  
---|---  
A - IPv4 Address | 1  
NS - NameServer | 2  
CNAME - Canonical Name | 5  
SOA - Start of Authority | 6  
PTR - Pointer | 12  
MX - Mail Exchange | 15  
TXT - Text | 16  
RP - Responsible Person | 17  
AAAA - IPV6 Address | 28  
LOC - Location | 29  
SRV - Service Locator | 33  
NAPTR - Naming Authority Pointer | 35  
SSHFP - Secure Shell Protocol Fingerprint | 44  
SPF - Sender Policy Framework | 99  
CAA - Certification Authority Authorization | 257

