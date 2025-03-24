

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

# Test Probe

The Test Probe API allows you to test a probe before setting up the pools that
will be associated with a probe. The Test Probe is independent of pool type.

Test Probe supports the use of IPv6 Addresses. Unlike Simple Load Balancing
Pools, Test Probes can be a combination of IPv4 and IPv6 addresses when listed
in the body of the call.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Create a Test
Probe

**Method and URI** :

POST https://api.ultradns.com/testprobes

**Parameters** : None

**Body** : Must include a Test Probe DTO.

**Response** : If task completes, Status Code 200 OK is returned with Test
Probe Results in the body content.

**Errors** : An error is returned under the following conditions:

JSON Example: Test Probe Request

{  
  
"hosts": [  
  
"1.1.1.1",  
  
"2.2.2.2",  
  
"3.3.3.3",  
  
"4.4.4.4"  
  
],  
  
"type": "HTTP"  
  
"method": "POST",  
  
"url": "https://www.google.com",  
  
"transmittedData": "q=something",  
  
"searchString": "UltraDNS"  
  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Test Probe
DTO

Test Probe DTO

Parameter |  Description |  Type  
---|---|---  
hosts |  IP addresses of the hosts (probe targets) to be tested. |  Array of IP addresses. Required.  
type |  Test Probe type. Currently limited to HTTP probing type. |  Required. Values include:

  * HTTP
  * HTTPS

  
method |  Test Probe method. Valid values for HTTP probing are:

  * GET
  * POST

|  String. Required.  
url |  URL to the probe. |  String. Required.  
transmittedData |  Data that will be sent to the URL. |  String. Optional.  
searchString |  The string to be searched in the HTTP response that comes back from the Probe Target. |  String. Optional.  
followRedirect |  A Boolean flag used to enable (true) /disable (false) the auto HTTP redirection for test probe. |  Boolean. Optional. Default value of false.  
  
![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Test Probe
Results

Test Probe Results

Parameter |  Description |  Type  
---|---|---  
probeResults |  The results of probing for each record. Applicable to a response JSON. |  Array of Test Probe Results.  
probeResults/host |  The host that the probe results correspond to. Always present in a response JSON. |  IP Address  
probeResults/status |  Indicator to show if the Probe failed or succeeded for the given record. Values are:

  * 0 = Success
  * 3 = Failure

If a search string is not specified, the probe is considered to be a Success if any non-error response from the target is received. If a search string is provided, then the success response will be checked for the presence of the string. Always present in a response JSON. |  String  
probeResults/message |  Message string that accompanies the status of the probeResults. Always present in a response JSON. |  String  
  
JSON Example: Test Probe Response

{  
  
"probeResults": [  
  
{  
  
"host": "1.1.1.1"  
  
"status": "3",  
  
"message": "Could not find âUltraDNSâ in the response"  
  
},  
  
{  
  
"host": "2.2.2.2"  
  
"status": "0"  
  
"message": "Success"  
  
},  
  
{  
  
"host": "3.3.3.3"  
  
"status": "3",  
  
"message": "404 Not Found"  
  
},  
  
{  
  
"host": "4.4.4.4"  
  
"status": "0"  
  
"message": "Success"  
  
}  
  
]  
  
}

JSON Example: Test Probe Request with Follow Redirect flag as false

{  
  
"hosts": ["google.com"],  
  
"type": "HTTP"  
  
"method": "GET",  
  
"url": "http://google.com",  
  
"transmittedData": "q=something",  
  
"searchString": "UltraDNS",  
  
"followRedirect": false  
  
}

JSON Example: Test Probe Response with Follow Redirect flag as false

{  
"probeResults": [  
{  
"host": "google.com",  
"status": "3",  
"message": "301 Moved Permanently to http://www.google.com/"  
}  
]  
}

JSON Example: Test Probe Request with Follow Redirect flag as true

{  
"hosts": ["google.com"],  
"type": "HTTP"  
"method": "GET",  
"url": "http://google.com",  
"transmittedData": "q=something",  
"searchString": "UltraDNS",  
âfollowRedirectâ: true  
}

JSON Example: Test Probe Response with Follow Redirect flag as true

{  
"probeResults": [  
{  
"host": "google.com",  
"status": "0",  
"message": "Success"  
}  
]  
}

