

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

## Usage Summary Report

The Usage Summary Report displays peak data statistics for an account for the
last 36 months. Each month that is returned consists of domains counts, record
type counts, and query statisistics for the given account.

For those accounts with UltraDNS2 enabled, the Usage Summary Report will only
return data for the last 13 months.

### Requesting the Usage Summary Report

**Method and URI** :

GET https://api.ultradns.com/reports/dns/usage_summary

  
**Parameters** : Must include the following:

### Usage Summary Report Parameters

Usage Summary Report Parameters

Parameter |  Description |  Type  
---|---|---  
**accountName** |  The Account name for which the Usage Summary Report is being requested. |  String. Required.  
  
**Body** : None.

**Response** : If task completes, Status Code 200 is returned with the Usage
Summary Report Output DTO.

Usage Summary Report Output DTO

Parameter |  Description |  Type  
---|---|---  
**usageSummary** |  The list of usage summaries for the previous three years (thirty-six months), beginning from the current month. |  Array.  
  
**Errors** : An error is returned under the following conditions:

  * Error Code 401 â Unauthorized. Token not found, expired or invalid.

  * Error Code 400 â accountName is not provided.

  * Error Code 400 â You do not have access to the accountName.

### Usage Summary Report DTO

Usage Summary DTO

Field |  Description |  Type  
---|---|---  
accountName |  The Account associated to the Usage Summary row. |  String.  
month |  The month and year for which the returned statistics apply. |  String.  
domainsCount |  The peak (highest) number of Domains that existed under the account name for the givenmonth. |  Long.  
recordsCount |  The peak (highest) number of Records that existed under the account name for the given month. |  Long.  
queryResponsesCount |  The total number of DNS query responses that were served for the account name during the given month. For accounts that _have the UltraDNS 2 feature enabled_, the total number of DNS query responses will be the sum of both the **queryResponsesCountUltra1** and **queryResponsesCountUltra2** results. |  Long.  
queryResponsesCountUltra1 |  _Only returned for accounts that have UltraDNS 2 enabled_. The total number of DNS query responses that were served for the account name, during the given month, and were served from the UltraDNS network.  | Long.  
queryResponsesCountUltra2 |  _Only returned for accounts that have UltraDNS 2 enabled_. The total number of DNS query responses that were served for the account name, during the given month, and were served from the UltraDNS2 network.  | Long.  
urlForwardCount |  The peak (highest) number of URL Forwards that existed under the account name for the given month. |  Long.  
sitebackerRecordsCount |  The peak (highest) number of SiteBacker Records that existed under the account name for the given month. |  Long.  
trafficControllerRecordsCount |  The peak (highest) number of Traffic Controller Records that existed under the account name for the given month. |  Long.  
directionalRecordsCount |  The peak (highest) number of Directional Pool Records that existed under the account name for the given month. |  Long.  
  
JSON Example: Usage Summary Report Response

{

"usageSummary": [

{

"accountName": "GTV8",

"month": "January 2019",

"domainsCount": 1863,

"recordsCount": 10530,

"queryResponsesCount": 1176520,

"urlForwardCount": 35,

"siteBackerRecordsCount": 112,

"trafficControllerRecordsCount": 56,

"directionalRecordsCount": 115

},

{

"accountName": "GTV8",

"month": "December 2018",

"domainsCount": 1863,

"recordsCount": 10524,

"queryResponsesCount": 5464627,

"urlForwardCount": 35,

"siteBackerRecordsCount": 112,

"trafficControllerRecordsCount": 56,

"directionalRecordsCount": 120

},

{

"accountName": "GTV8",

"month": "November 2018",

"domainsCount": 1862,

"recordsCount": 10497,

"queryResponsesCount": 293095094,

"urlForwardCount": 35,

"siteBackerRecordsCount": 111,

"trafficControllerRecordsCount": 56,

"directionalRecordsCount": 121

},

{

"accountName": "GTV8",

"month": "October 2018",

"domainsCount": 1861,

"recordsCount": 10478,

"queryResponsesCount": 200952818,

"urlForwardCount": 35,

"siteBackerRecordsCount": 108,

"trafficControllerRecordsCount": 56,

"directionalRecordsCount": 121

},

{

"accountName": "GTV8",

"month": "September 2018",

"domainsCount": 1858,

"recordsCount": 10433,

"queryResponsesCount": 176045732,

"urlForwardCount": 35,

"siteBackerRecordsCount": 107,

"trafficControllerRecordsCount": 56,

"directionalRecordsCount": 120

},

JSON Example: Usage Summary Report UltraDNS2 Enabled Response

{

"usageSummary": [

{

"accountName": "example",

"month": "January 2023",

"domainsCount": 1863,

"recordsCount": 10530,

"queryResponsesCount": 586525,

"queryResponsesCountUltra1": 566520,

"queryResponsesCountUltra2": 20005,

"urlForwardCount": 35,

"siteBackerRecordsCount": 112,

"trafficControllerRecordsCount": 56,

"directionalRecordsCount": 115

},

{

"accountName": "example",

"month": "December 2022",

"domainsCount": 1863,

"recordsCount": 10524,

"queryResponsesCount": 576525,

"queryResponsesCountUltra1": 566520,

"queryResponsesCountUltra2": 10005,

"urlForwardCount": 35,

"siteBackerRecordsCount": 112,

"trafficControllerRecordsCount": 56,

"directionalRecordsCount": 120

}

}

.CSV Example: Retrieving the Usage Summary Report

Account Name,Month,Domains Count,Records Count,Query Responses
Count,URLForward Count,SiteBacker Records Count,TrafficController Records
Count,Directional Records Count

GTV8,April 2019,1941,11130,268949749,51,117,56,124

GTV8,March 2019,1938,11017,231447640,51,117,56,121

GTV8,February 2019,1934,10925,70017129,50,119,57,119

GTV8,January 2019,1885,10624,5758084,43,114,57,115

GTV8,December 2018,1863,10524,5464627,35,112,56,120

GTV8,November 2018,1862,10497,293095094,35,111,56,121

GTV8,October 2018,1861,10478,200952818,35,108,56,121

GTV8,September 2018,1858,10433,176045732,35,107,56,120

GTV8,August 2018,1852,10377,223102752,34,107,55,120

GTV8,July 2018,1851,10364,198165947,34,107,55,120

GTV8,June 2018,1849,10344,172711920,34,104,54,119

GTV8,May 2018,1847,10339,154026378,33,99,55,111

GTV8,April 2018,1845,10321,151449195,31,90,55,111

GTV8,March 2018,1842,10323,166979368,31,93,55,110

GTV8,February 2018,1833,10279,142047507,31,93,53,110

GTV8,January 2018,1827,10197,136846008,30,85,53,110

GTV8,December 2017,1837,10213,163184279,30,82,52,110

GTV8,November 2017,1884,10364,158652931,30,82,53,105

GTV8,October 2017,1883,10365,166924285,30,85,52,104

GTV8,September 2017,1882,10349,158928386,30,85,50,104

GTV8,August 2017,1881,10338,205067634,30,80,47,104

GTV8,July 2017,1880,10302,5620738,30,78,43,101

GTV8,June 2017,1879,10278,5716107,30,75,44,101

GTV8,May 2017,1878,10256,5901808,30,72,44,101

GTV8,April 2017,1877,10235,5670492,29,72,44,100

GTV8,March 2017,1875,10152,5840992,27,73,43,101

GTV8,February 2017,1868,10072,4553925,25,65,36,98

GTV8,January 2017,1862,10024,4689695,20,65,36,97

GTV8,December 2016,1857,9963,4721596,20,66,36,94

GTV8,November 2016,1852,9925,5357160,20,71,36,97

GTV8,October 2016,1846,9890,5771759,20,69,36,87

GTV8,September 2016,1842,9860,7761472,20,68,36,72

GTV8,August 2016,1833,9781,8015008,19,68,36,69

GTV8,July 2016,1815,9586,8022261,19,70,35,44

GTV8,June 2016,1792,9478,7606860,18,69,32,42

GTV8,May 2016,1780,9431,7613712,18,70,28,41

## Usage Summary Report - Daily

The **Usage Summary Daily Report** displays peak data statistics for an
account for the month specified. Each month that is returned consists of
domains counts, record type counts, and query statistics for the given
account. Please note that the Usage Summary Daily Report will only return data
for the last 13 months. (both UltraDNS and UltraDNS2 networks).

### Requesting the Usage Summary Report - Daily

**Method and URI** :

GET https://api.ultradns.com/reports/dns/usage_summary/daily

  
**Parameters** : Must include the Usage Summary Report Parameters.

**Body** : Must include the Month and Year (within the last 13 months).

.CSV Example: Retrieving the Usage Summary Report ```json { "month": "March
2023", "accountNames": [ "example" ] } ```

**Response** : If task completes, Status Code 200 is returned with the Usage
Summary Report Output DTO.

JSON Example: Usage Summary Report - Daily Response (UltraDNS Network)

{

"usageSummary": [

{

"month": "March 2023",

"date": "2023-03-01",

"domainsCount": 10,

"recordsCount": 33,

"queryResponsesCount": 0,

"urlForwardCount": 0,

"emailForwardCount": 0,

"siteBackerRecordsCount": 2,

"trafficControllerRecordsCount": 3,

"directionalRecordsCount": 10

},

{

"month": "March 2023",

"date": "2023-03-02",

"domainsCount": 10,

"recordsCount": 33,

"queryResponsesCount": 0,

"urlForwardCount": 0,

"emailForwardCount": 0,

"siteBackerRecordsCount": 2,

"trafficControllerRecordsCount": 3,

"directionalRecordsCount": 10

}

}

JSON Example: Usage Summary Report - Daily Response (UltraDNS2 Network)

{

"usageSummary": [

{

"month": "March 2023",

"date": "2023-03-01",

"domainsCount": 10,

"recordsCount": 33,

"queryResponsesCount": 0,

"queryResponsesCountUltra1": 0,

"queryResponsesCountUltra2": 0,

"urlForwardCount": 0,

"emailForwardCount": 0,

"siteBackerRecordsCount": 2,

"trafficControllerRecordsCount": 3,

"directionalRecordsCount": 10

},

{

"month": "March 2023",

"date": "2023-03-02",

"domainsCount": 10,

"recordsCount": 33,

"queryResponsesCount": 0,

"queryResponsesCountUltra1": 0,

"queryResponsesCountUltra2": 0,

"urlForwardCount": 0,

"emailForwardCount": 0,

"siteBackerRecordsCount": 2,

"trafficControllerRecordsCount": 3,

"directionalRecordsCount": 10

}

}

CSV Example: Retrieving the Usage Summary Report - Daily Response (UltraDNS
Network)

Month,Date,Domains,Records,Query Responses,URL Forward,SB Records,TC
Records,Directional Records

March 2023,2023-03-01,10,33,0,0,2,3,10

March 2023,2023-03-02,10,33,0,0,2,3,10

March 2023,2023-03-03,10,33,0,0,2,3,10

March 2023,2023-03-04,10,33,0,0,2,3,10

March 2023,2023-03-05,10,33,0,0,2,3,10

March 2023,2023-03-06,10,33,0,0,2,3,10

March 2023,2023-03-07,10,33,0,0,2,3,10

March 2023,2023-03-08,10,33,0,0,2,3,10

March 2023,2023-03-09,10,33,0,0,2,3,10

March 2023,2023-03-10,10,33,0,0,2,3,10

March 2023,2023-03-11,10,33,0,0,2,3,10

March 2023,2023-03-12,10,33,0,0,2,3,10

March 2023,2023-03-13,10,33,0,0,2,3,10

March 2023,2023-03-14,10,33,0,0,2,3,10

March 2023,2023-03-15,10,33,0,0,2,3,10

March 2023,2023-03-16,10,33,0,0,2,3,10

March 2023,2023-03-17,10,33,0,0,2,3,10

March 2023,2023-03-18,10,33,0,0,2,3,10

March 2023,2023-03-19,10,33,0,0,2,3,10

March 2023,2023-03-20,10,33,0,0,2,3,10

March 2023,2023-03-21,10,33,0,0,2,3,10

March 2023,2023-03-22,10,33,0,0,2,3,10

March 2023,2023-03-23,10,33,0,0,2,3,10

March 2023,2023-03-24,10,33,0,0,2,3,10

March 2023,2023-03-25,10,33,0,0,2,3,10

March 2023,2023-03-26,10,33,0,0,2,3,10

March 2023,2023-03-27,10,33,0,0,2,3,10

March 2023,2023-03-28,10,33,0,0,2,3,10

March 2023,2023-03-29,10,33,0,0,2,3,10

March 2023,2023-03-30,10,33,0,0,2,3,10

March 2023,2023-03-31,10,33,0,0,2,3,10

CSV Example: Retrieving the Usage Summary Report - Daily Response (UltraDNS2
Network)

Month,Date,Domains,Records,Query Responses UltraDNS,Query Responses
UltraDNS2,URL Forward,SB Records,TC Records,Directional Records

April 2023,2023-04-01,20,666,1234,5321096,18,48,44,154

April 2023,2023-04-02,20,666,1226,5321091,18,48,44,154

April 2023,2023-04-03,20,666,2304,5317009,18,48,44,154

April 2023,2023-04-04,20,670,19284,5317670,20,48,46,154

April 2023,2023-04-05,20,670,18736,5297710,20,48,46,154

April 2023,2023-04-06,20,670,18930,5367410,20,48,46,154

April 2023,2023-04-07,20,670,19403,5219448,20,48,46,154

April 2023,2023-04-08,20,670,19735,5214610,20,48,46,154

April 2023,2023-04-09,20,670,19678,4806622,20,48,46,154

April 2023,2023-04-10,20,670,19445,4777975,20,48,46,154

April 2023,2023-04-11,20,670,19028,4780095,20,48,46,154

April 2023,2023-04-12,20,670,19593,4446632,20,48,46,154

April 2023,2023-04-13,20,670,19196,4403325,20,48,46,154

April 2023,2023-04-14,20,670,19206,4554029,20,48,46,154

April 2023,2023-04-15,20,670,19406,5140661,20,48,46,154

April 2023,2023-04-16,20,670,19761,5147339,20,48,46,154

April 2023,2023-04-17,20,670,19708,5140048,20,48,46,154

April 2023,2023-04-18,20,670,19627,5121388,20,48,46,154

April 2023,2023-04-19,20,670,19660,5096803,20,48,46,154

April 2023,2023-04-20,20,670,19638,5046376,20,48,46,154

April 2023,2023-04-21,20,670,20846,4821449,20,48,46,154

April 2023,2023-04-22,20,670,19639,4887627,20,48,46,154

April 2023,2023-04-23,20,670,19605,4706891,20,48,46,154

