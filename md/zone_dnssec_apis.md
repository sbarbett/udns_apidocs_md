

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

# Zone DNSSEC APIs

DNS Security Extensions (DNSSEC) refers to a set of security extensions to
DNS, which provide DNS clients (resolvers) with origin authentication of DNS
data, authenticated denial of existence, and data integrity.

The REST API allows you to sign, unsign, and re-sign a zone, as well as get
current DNSSEC information and status for a zone.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Sign a Zone

Signing a zone means adding DNSSEC security to the zone.

Signing a zone is a POST call, and doing so creates/adds a DNSSEC signature
for the zone, and is generated as follows:

**Method and URI:**

POST https://api.ultradns.com/zones/{zoneName}/dnssec

**Parameters:** None

**Body:** None

Field |  Description |  Type  
---|---|---  
changeComment |  An optional field allowing users to create a comment for a zone operation using up to 512 characters of free text, which can be viewed and searched for via the Audit Log Report. Not applicable for Batch or JSON Patch calls. Additionally, the use of a colon (:) is prohibited. |  String.  
  
**Response:** If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

  * If update happens in the background, Status Code 202 is returned along with an X-Task-ID header and a status message of Pending in the body content.

**Errors:** An error is returned under the following conditions:

  * If you do not have permission to change security on {zoneName}.
  * If {zoneName} does not exist.
  * If the specified zone has Sitebacker, Traffic Controller, or Directional pools (advanced services do not currently allow for signed zones).

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Sign a Zone
â Override Account Level Settings

When signing a zone with DNSSEC, it is possible to override the [DNSSEC
Settings](Extended Accounts API/Extended Accounts API.htm#DNSSEC_SETTINGS)
that have been applied at the account-level and instead, set specific zone
level DNSSEC settings. This is an optional DTO field.

This can only be done on a PUT or POST API call and requires that the
**dnssecPolicy** parameter be included in the body of the request. Any of the
fields not provided will inherit the account-level DNSSEC settings.

![](../Resources/Images/Rest-API_User_Guide/Introduction_60x69.png) |  We highly recommend performing the Get DNSSEC Details for a Zone API call before using the **dnssecPolicy** and/or **externalKeys** parameters in a PUT API call. Not providing the existing dnssecPolicy or externalKey details, or leaving them empty, will result in previously provided values being removed from the database.  
---|---  
  
dnssecPolicy DTO for Override

Field |  Description |  Type  
---|---|---  
dnssecPolicy/dnsKeyTtl  |  Overrides the account-level DNSSEC TTL settings and instead, uses the provided value for the specified zone.  Valid value is between 300-172800 (sec).  |  Integer   
dnssecPolicy/rrsigValidity |  Overrides the account-level DNSSEC RRSIG Validity settings and instead, uses the provided value for the specified zone.  Valid value is between 5-30 (days). |  Integer   
dnssecPolicy/zskRolloverFrequency  |  Overrides the account-level DNSSEC ZSK Rollover Frequency settings and instead, uses the provided value for the specified zone.  Valid value is between 30-120 (days). |  Integer   
dnssecPolicy/kskRolloverFrequency |  Overrides the account-level DNSSEC KSK Rollover Frequency settings and instead, uses the provided value for the specified zone.  Valid value is between 365-1826 (days). |  Integer   
  
JSON Example: Override the Account-level DNSSEC Settings

JSON Example: Override the Account-level DNSSEC Settings ```json {
"dnssecPolicy": { "dnskeyTtl": 540, "rrsigValidity": 26,
"zskRolloverFrequency": 60, "kskRolloverFrequency": 1095 } } ```

If the dnssecPolicy parameter is provided but left empty, the previously
configured policy values will be removed, and the signed zone will inherit the
account-level settings.

JSON Example: Remove Configured dnssecPolicy Values

JSON Example: Remove Configured dnssecPolicy Values ```json { "dnssecPolicy":
{} } ```

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Unsign a Zone

Unsigning a zone means removing a DNSSEC security signature from the zone.

Unsigning a zone is a DELETE call and is generated as follows:

**Method and URI:**

DELETE https://api.ultradns.com/zones/{zoneName}/dnssec

**Parameters:** None

**Body:** None

Field |  Description |  Type  
---|---|---  
changeComment |  An optional field allowing users to create a comment for a zone operation using up to 512 characters of free text, which can be viewed and searched for via the Audit Log Report. Not applicable for Batch or JSON Patch calls. Additionally, the use of a colon (:) is prohibited. |  String.  
  
**Response** : If delete happens immediately, Status Code 204 is returned with
no body content.

  * If delete happens in the background, a Status Code 202 is returned with a status response message of Pending along with an X-Task-Id header in body content.

**Errors:** An error is returned under the following conditions:

  * If you do not have permission to change security on {zoneName}.
  * If {zoneName} does not exist.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Resign a Zone

When a zone is signed, modifications to the zone are not made publically
available until the signatures for the zone are regenerated. This process is
called Resigning a Zone. In addition to resigning after changes, some security
experts recommend periodic resigning of zones, even if there are no
modifications.

As of September 2019, zones that are signed by On the Fly signing method will
no longer need to be manually signed, as the new signing method automatically
resigns a zone when any changes are made to it.

Resigning a zone is a PUT or a PATCH call and is generated as follows:

**Method and URI:**

PUT/PATCH https://api.ultradns.com/zones/{zoneName}/dnssec

**Parameters:** None

**Body:** None

**Response:** If task completes, Status Code 200 OK is returned with an
appropriate status message in the response body.

  * If update happens in the background, Status Code 202 is returned along with an X-Task-ID header and a status message of Pending in the body content.

**Errors:** An error is returned under the following conditions:

  * If you do not have permission to change security on {zoneName}.
  * If {zoneName} does not exist.
  * If {zoneName} is not currently signed.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get DNSSEC
Details for a Zone

The Get DNSSEC Details provides detailed information regarding the current
DNSSEC status of a zone. A Time Stamp will be returned when a GET DNSSEC call
is performed, and will be provided in the dnssecstatus response. The time
stamp will be displayed as <last_modified> in the default XML date format (for
example: â2015-11-23T10:39:59Zâ), but can be reformatted via the
ZoneDataeTime tool in Java 8.

The Get DNSSSEC Details call is a GET call and is generated as follows:

**Method and URI:**

GET https://api.ultradns.com/zones/{zoneName}/dnssec

**Parameters:** None

**Body:** None

**Response:** If task completes, Status Code 200 OK is returned with a DNSSEC
Info Response DTO in the body content.

**Errors:** An error is returned under the following conditions:

  * If you do not have permission to view security on {zoneName}.
  * If {zoneName} does not exist.

JSON Example â Get DNSSEC Details Response

JSON Example â Get DNSSEC Details Response ```json { "status": "SIGNED",
"policy": { "algorithm": "ECDSAP256SHA256", "securityType": "NSEC_ON_THE_FLY",
"rrsigSignatureDuration": 15552000000, "keyPolicy": [ { "type": "ZSK",
"bitLength": 256, "keyRolloverFrequency": 180 }, { "type": "KSK", "bitLength":
256, "keyRolloverFrequency": 365 } ] }, "keys": [ { "type": "ZSK",
"bitLength": 256, "keyRolloverFrequency": 180, "status": "CURRENT", "created":
"2020-07-08T06:46:21Z", "nextRoll": "2021-01-04T06:46:21Z", "keyId": 45586,
"publicKey":
"jRcwwuZGW4KrB3Tr20HHbLBmaMMFY8MFRd4ON1io2G1AaN5DyWDOjqdiPup8eZSm3CpCCTSfrx/HQc5inuOgfg==",
"dnsKeyRecord": "nsec_on_the_fly.com. 100 IN DNSKEY 256 3 13
\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0jRcwwuZGW4KrB3Tr20HHbLBmaMMFY8MFRd4ON1io2G1AaN5DyWDOjqdiPup8eZSm3CpCCTSfrx/HQc5inuOgfg=="
}, { "type": "KSK", "bitLength": 256, "keyRolloverFrequency": 365, "status":
"CURRENT", "created": "2020-07-08T06:46:21Z", "nextRoll":
"2021-07-08T06:46:21Z", "keyId": 48927, "publicKey":
"e5GJmifYXx1NFAVYA11jCCUTM4nXE+9FeyfUy3l3xreiS3RTAYIWRerXbIkTXAmVmokSSdihUnTH+91R0OfWLg==",
"dsRecords": [ "48927 13 1 108695D72E4397854AAABE489CC1A36A64872F1A", "48927
13 2 97D96C00733A3FA59A1C71393FA4ED2261A6EDA78F82E7EC18AB3BE750A94F06" ],
"dnsKeyRecord": "nsec_on_the_fly.com. 100 IN DNSKEY 257 3 13
e5GJmifYXx1NFAVYA11jCCUTM4nXE+9FeyfUy3l3xreiS3RTAYIWRerXbIkTXAmVmokSSdihUnTH+91R0OfWLg=="
} ], "lastModifiedDateTime": "2020-07-08T06:46:21Z",
"lastModifiedZoneDateTime": "2020-07-08T06:46:21Z", "resignNeeded": false }
```

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)KSK Key
Rollover

The KSK Key Rollover API call allows users to trigger a DNSSEC Key Signing Key
(KSK) rollovers, which reduces the time required for key rollovers from days
to just hours, ensuring that your DNS zones remain secure without unnecessary
delays.

DNSSEC Key Rollover involves changing the cryptographic keys used to sign DNS
records, ensuring continued trust in the authenticity of your DNS responses.
This process is critical for maintaining secure DNS operations and preventing
potential vulnerabilities from outdated or compromised keys.

By initiating the Key Signing Key (KSK) Rollover process, you are making a
significant change to your DNS security configuration. Please review the
following carefully before proceeding:

  * DNS Resolution Impact and Key Propagation: The KSK Rollover operation directly impacts the validation of DNSSEC-signed zones. The newly generated KSK must be propagated across all DNS resolvers that validate DNSSEC for your domain. This propagation can take time, and if not managed properly, there is a risk of DNS resolution failures, which could prevent users from accessing your services. During this period, both the old and new KSK keys will be maintained to ensure seamless validation.

  * Transition Period: Once the rollover process begins, both the old and new KSK keys will be maintained in DNS key sets during a transitional period. The KSK rollover period corresponds to the number of days the old KSK remains active, ensuring a smooth transition while resolvers update their cached keys.

  * DS Record Update: New DS records need to be added to the Domain Name Registrar that manages your domain as soon as possible. Failure to update the DS record in a timely manner could result in DNS resolution failures for your domain.

**Method and URI:**

POST https://api.ultradns.com/ zones/{zone_name}/dnssec/kskrollover

**Parameters:** None

**Body:** None

**Response:** If task completes, Status Code 200 OK is returned with DS
records in the body content.

**Errors:** An error is returned under the following conditions:

  * If a KSK Rollover is currently in progress.

  * If other keys are currently being rolled over.

  * If you do not have permission to view security on {zoneName}.

  * If {zoneName} does not exist.

JSON Example: KSK Rollover Body Response

{

"dsRecords": [

"50608 13 1 FA555D389DD2F1499D74948F3927927612759AC0",

"50608 13 2 3B30EFFC8A862A1C9E6ACD1E0814659F03C1E373EE33BB5B33E048E4B31131D9"

],

}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)DNSSEC Info
Response DTO

The DNSSEC Info Response DTO returns the current DNSSEC details for the
identified zone.

DNSSEC Info Response DTO

Field |  Description |  Type  
---|---|---  
status |  Current DNSSEC status of the zone. Valid values include SIGNED or UNSIGNED. |  Object.  
policy |  The standard rules applied for the keys for this zone. |  Policy DTO  
lastModifiedDateTime |  The last date and time the zone was modified, represented in ISO8601 format. |  String, Date/Time formatted in ISO 8601 format.  
lastModifiedZoneDateTime |  The last date and time the zone was modified. |  String, date/time formatted in ISO 8601 format. Returned in GET responses for zone information.  
resignNeeded |  Specify if a zone resign is needed for an already signed zone.  
true = yes  
false = no |  Boolean.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Policy DTO

Field |  Description |  Type  
---|---|---  
  
  
  
  
  
policy/securityType |  The security type imposed by policy.  Valid values include: 

  * NONE
  * NSEC
  * NSEC3
  * NSEC3_OPT_OUT
  * NSEC3_ON_THE_FLY

|  Object.  
policy/rrsigSignatureDuration |  The period of time (in days) for which an RR Signature is valid. |  Integer.  
policy/nsec3Parameters |  The standard parameters used for NSEC3 records. |  NSEC3 Parameters DTO.  
policy/keyPolicy |  The standard policy used to define the ZSK and KSK. |  Array of Key Policy DTO.  
keys |  The current keys defined in the zone. The dnsKeyRecord will only be returned in a zone is signed using the **On_the_Fly** signing method. |  Array of Key DTO.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)NSEC3
Parameters DTO

Field |  Description |  Type  
---|---|---  
policy/nsec3Parameters/salt |  Indicator that a salt value has been system generated.  |  String.  
policy/nsec3Parameters/optOutFlag |  Indicates whether this NSEC3 policy may cover unsigned delegations.  |  Integer.  
policy/nsec3Parameters/iterations |  Number of times the hash value is generated and applied.  |  Integer.  
policy/nsec3Parameters/hashAlgorithm |  The hash algorithm used in the calculation of the full hash value. |  String.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Key Policy
DTO

Field |  Description |  Type  
---|---|---  
policy/keyPolicy/[n]/type |  Key Policy Type for the zone. Valid values are KSK or ZSK. |  Object.  
policy/keyPolicy/[n]/bitLength |  The number of bits in the specified key.  |  Integer.  
policy/keyPolicy/[n]/keyRolloverFrequency |  The Key Rollover Frequency established by the key policy for this zone. |  Integer.  
policy/algorithm |  Crypto Algorithm Used. |  String.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Key DTO

Field |  Description |  Type  
---|---|---  
keys/[n]/type |  Type of key.  Valid values are KSK or ZSK. |  Object.  
keys/[n]/status |  Key Status. Valid values are: 

  * CURRENT (key is currently being used to sign the zone)
  * EXPIRED (key was, but is no longer being used)
  * FUTURE (key will be used to sign the zone in the future)
  * UNKNOWN

|  String.  
keys/[n]/publicKey |  Public Key |  String.  
keys/[n]/nextRoll |  The date on which the next key roll is scheduled to occur. Based on the keyRolloverFrequency. |  Date/time in ISO 8601 format.  UTC offset based on customer-specified time zone.  
keys/[n]/keyRolloverFrequency |  Key Rollover Frequency |  Integer. Number of days.  
keys/[n]/keyId |  Key id |  String.  
keys/[n]/dsRecords |  DS records |  Array of String.  Only applicable to KSK key.  
keys/[n]/dnsKeyRecord |  The dnsKeyRecord holds a public key that resolvers can use to verify DNSSEC signatures in RRSIG records. When an authoritative name server signs a zone, it typically generates two key pairs, one for KSK, and the other for ZSK.  The authoritative server uses the private key of the ZSK pair to sign each RRset in a zone. It stores the public key of the ZSK pair in a DNSKEY record. The name server then uses the private key of the KSK pair to sign all dnsKeyRecords, including its own, and stores the corresponding public key in another dnsKeyRecord.  |  Array of String.  Applicable for both KSK and ZSK keys.   
keys/[n]/created |  Creation Date |  Date/time in ISO 8601 format.  UTC offset based on customer-specified time zone.  
keys/[n]/bitLength |  Bit Length |  Integer.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Signer Error
Messages

The following table displays the error messages for possible zone signing
issues, along with the updated system error message that will be displayed.

Signer Processing Error Messages

HTTP Code |  Operation Type |  Response Code |  Current Response Message  
---|---|---|---  
500 â Internal Server Error |  Sign Zone |  1837 |  Could not complete sign zone request. Please retry request after some time or else contact the Ultra DNS Customer Support team.  
Unsign Zone |  Could not complete unsign zone request. Please retry request after some time, or else contact the Ultra DNS Customer Support team.  
500 â Internal Server Error |  Get DNSSEC |  1837 |  Could not get dnssec status. Please retry request after some time or else contact the Ultra DNS Customer Support team.  
500 â Internal Server Error |  Get DomainDNSSECPolicies |  1837 |  Could not get domain dnssec policies. Please retry request after some time or else contact the Ultra DNS Customer Support team.  
  
Signer Validation Error Messages

HTTP Code |  Operation Code |  New Response Code |  New Response Message  
---|---|---|---  
400 â Bad Request |  Sign Zone |  1881 |  We are not able to process sign zone requests at this time. Please retry request again.  
400 â Bad Request |  Unsign Zone |  1882 |  We are not able to process unsign zone requests at this time. Please try again.  
  
Signer User Validation Error Messages

HTTP Code |  Operation Code |  New Response Code |  Response Message  
---|---|---|---  
400 â Bad Request |  Sign Zone |  1883 |  Error in signing zone. Missing SOA record for zone <zoneName>.  
400 â Bad Request |  Sign Zone |  1884 |  Error in signing zone. Too many SOA records in zone <zoneName>; expected 1, found <soaCountFound>.  
400 â Bad Request |  Sign Zone |  1885 |  Error in signing zone. Too many pending SOA records in zone <zoneName>; expected 1, found <soaCountFound>.  
400 â Bad Request |  Unsign Zone |  1886 |  Error in unsigning zone. Missing SOA record for zone <zoneName>.  
400 â Bad Request |  Unsign Zone |  1887 |  Error in unsigning zone. Too many SOA records in zone <zoneName>; expected 1, found <soaCountFound>.  
400 â Bad Request |  Unsign Zone |  1888 |  Error in unsigning zone. Too many pending SOA records in zone <zoneName>; expected 1, found <soaCountFound>.  
  
# DNSSEC Multi-Signer (RFC-8901)

With UltraDNS supporting Multi-Signer DNSSEC ([RFC-8901](https://www.rfc-
editor.org/rfc/rfc8901.html)) it is now possible for multiple independent DNS
operators to sign a single domain simultaneously, strengthening the robustness
of the DNSSEC chain of trust. This approach addresses the complex challenges
faced by organizations that operate in distributed, multi-vendor DNS
environments, ensuring that the limitations of single-signer models do not
compromise their domain security.

This model mandates that each signerâwhether part of UltraDNS or an external
entityâmaintains its own unique Key Signing Key (KSK) and Zone Signing Key
(ZSK). This method strengthens the DNSSEC architecture by implementing a
decentralized key management system, thereby improving the resilience and
integrity of the domain name authentication process.

Multi-signer DNSSEC functionality addresses two pivotal DNS management
challenges:

  1. Multi-Provider DNS Management: It allows for a seamless and secure management framework across multiple DNS providers, ensuring that DNSSEC integrity is maintained even in complex multi-provider setups.

  2. Transitioning Signing Authorities: UltraDNS facilitates a smooth transition between DNS signing providers, preserving the DNSSEC chain of trust and eliminating the need for temporary DNSSEC deactivation during provider changes.

### Managing External Keys

The following APIs identify how users can manage their External Key pairs when
signing a zone to support DNSSEC Multi-Signing. These additional API calls are
to be used in conjunction with their Zone DNSSEC APIs counterparts.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Adding
External Keys to a Zone

Refer to the Sign a Zone for the required Body and DTO details.

This POST call will operate according to the following scenarios for your
zone:

  * If the zone is already signed, no additional operations will occur.

  * If the zone is unsigned, this operation will sign the zone as expected.

  * If the body of the request contains the **externalKeys** details, the call will perform the indicated operation based on the key length in the body details.

**Method and URI:**

POST https://api.ultradns.com/zones/{zoneName}/dnssec

**Parameters:** None

**Body:** Must include the Multi-Signer DNSSEC External Key DTO.

**Response:** If task completes, Status Code 201 is returned with an
appropriate status message in the response body.

  * If update happens in the background, Status Code 202 is returned along with an X-Task-ID header and a status message of Pending in the body content.

**Errors:** An error is returned under the following conditions:

  * If you do not have permission to change security on {zoneName}.

  * If {zoneName} does not exist.

  * If invalid body details are provided.

JSON Example: Add External Keys when Signing a Zone

JSON Example: Add External Keys when Signing a Zone ```json { "externalKeys":
[ { "ksk": [ "257 3 13 MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgBDCqr==" ], "zsk": [
"256 3 13 MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAECzv==" ] }, { "ksk": [ "257 3 13
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAECL==" ], "zsk": [ "256 3 13
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEov==" ] } ] } ```

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Update
External Keys for a Zone

This PUT call can only be used to update the External Keys if a zone meets the
following criteria.

  * The zone is already signed.

  * The zone is signed using the externalKeys value.

**Method and URI:**

PUT https://api.ultradns.com/zones/{zoneName}/dnssec

**Parameters:** None

**Body:** Must include the Multi-Signer DNSSEC External Key DTO.

  * If **externalKeys** is left empty, keys will be deleted from the system.

  * If **externalKeys** details are provided, the external key details will be replaced.

**Errors:** An error is returned under the following conditions:

  * If you do not have permission to sign the zone.

  * If zone is not signed.

  * If external keys are not able to validate.

  * If external keys do not currently exist for the zone.

JSON Example: Update External Keys to remove from system

JSON Example: Update External Keys to remove from system ```json {
"externalKeys": [] } ```

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Multi-Signer
DNSSEC External Key DTO

Field |  Description |  Type  
---|---|---  
externalKeys |  Used to provide the KSK and ZSK keys for a DNSSEC Multi-Signed zone (signed by an external provider).

  * A list of 0-2 pairs of external key pairs. A single key object represents a single external signer.
  * Each item in a KSK and ZSK list must contain 4 tokens. Tokens 1, 2, 3 are numbers. Token 4 is a key signature (string).

|  String  
ksk  |  If included, must be an array of 1-2 strings where each string is the rdata portion of the DNSKEY record for the KSK.

  * This field is optional.

|  Array of String. Optional.  
zsk  |  An array of 1-2 strings where each string is the rdata portion of the DNSKEY record for the KSK.

  * This field is required.  

|  Array of String.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)GET Multi-
Signer Supported Zone Details

The GET Multi-Signer Supported Zone Details API call returns the results from
the Get DNSSEC Details for a Zone call, but will also return a list of 0-2
pairs of external key pairs. A single key object represents a single external
signer.

**Method and URI:**

GET https://api.ultradns.com/zones/{zoneName}/dnssec

**Parameters:** None

**Body:** None.

**Response:** If task completes, Status Code 200 OK is returned with the
DNSSEC Info Response DTO along with the Multi-Signer DNSSEC External Key DTO
specific key response in the body content.

  * If update happens in the background, Status Code 202 is returned along with an X-Task-ID header and a status message of Pending in the body content.

**Errors:** An error is returned under the following conditions:

  * If you do not have permission to change security on {accountName}.

  * If {accountName} does not exist.

JSON Example: Get Multi-Signer Supported Zone Details Response

{

"status": "SIGNED",

"policy": {

...

},

"keys": [

...

],

"externalKeys":[

{

"ksk":["257 3 13 m7C4PJWZ7FxTYYc4kVSR/nm2kg=="],

"zsk":["256 3 13 okDWzr27eOzbZ6RjWEYanHL8kg=="]

},

{

"ksk":["257 3 13 K9VS6w6LPa1grSoDeS/xDl7/Q=="],

"zsk":["256 3 13 FeidI7VZYcCrGCN6YSgxlnfkQ=="]

}

]

]

"lastModifiedDateTime": "2023-07-08T06:46:21Z",

"lastModifiedZoneDateTime": "2023-07-08T06:46:21Z",

"resignNeeded": false

}

