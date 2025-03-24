

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

## Country Code Directional Response Counts Report

The Country Code Directional Response Counts Report displays the country codes
from which the DNS queries originate.

### Requesting Country Code Directional Response Counts Report

**Method and URI** :

POST  
https://api.ultradns.com/reports/dns_resolution/directional_response_counts/country_code?offset={offset}&limit={limit}

  
**Parameters** : Can include the following:

### Country Code Directional Response Counts Report Parameters

Country Code Directional Response Counts Report Parameters

Parameter |  Description |  Type  
---|---|---  
offset |  This field is optional.  If not specified, initial records will always be returned specified to the limit. This parameter allows pagination on the reporting records retrieved. The offset will be the integer value that specifies the position of first result to be retrieved. Specify offset as 0 for the first results to be retrieved. |  Integer. Optional.  
limit |  This field is optional.  If not specified, the total number of records returned in the response will be equal to the default value 1000. This parameter allows pagination on the reporting records retrieved. The maximum number of results to be retrieved in a single response is 100,000 records. |  Integer. Optional.  
  
**Body** : Must contain the Country Code Directional Response Counts Report
DTO.

**Response** : If task completes, Status Code 201 is returned with a requestId
in the response body.

**Errors** : An error is returned under the following conditions:

  * Error Code 401 â Unauthorized. Token not found, expired or invalid.

  * Error Code 400 â If date provided is not in valid format.

  * Error Code 400 â If reportEndDate is before reportStartDate. 

  * Error Code 400 â If reportStartDate or reportEndDate is a future date.

  * Error Code 400 â If reportStartDate is older than 90 days.

  * Error Code 400 â If offset is a negative value.

### Country Code Directional Response Counts Report DTO

Country Code Directional Response Counts Report DTO

Field |  Description |  Type  
---|---|---  
accountName |  The name of the account. If not provided, the report will consist of details for all of the zones within the account(s) that the user has access to. |  String. Optional.  
zoneName |  The results for the one zone that is being returned.

  * Wildcards in the zone name are not currently supported.
  * Zone names with and without a DOT(.) at the end are supported.

|  String. Optional.  
reportStartDate |  The reportStartDate must be supplied in the ISO 8601 UTC format (yyyy-MM-dd).

  * If not provided, will default to yesterdayâs date.
  * The maximum number of days between the reportStartDate and reportEndDate cannot exceed 90 days. 
  * The reportStartDate must be before or the same as the reportEndDate.
  * The reportStartDate cannot be more than 90 days prior to the current date.
  * The reportStartDate cannot be a future date.

|  Date. Optional  
reportEndDate |  The reportEndDate must be supplied in the ISO 8601 UTC format (yyyy-MM-dd).

  * If not provided, will default to yesterdayâs date.
  * The maximum number of days between the reportStartDate and reportEndDate cannot exceed 90 days. 
  * The reportEndDate cannot be a future date.

|  Date. Optional.  
  
JSON Example: Requesting Country Code Directional Response Counts Report

POST  
https://api.ultradns.com/reports/dns_resolution/directional_response_counts/country_code?offset={0}&limit={100000}

JSON Example: Requesting Country Code Directional Response Counts Report
```json { "countryCodeDirectionalResponseCounts": { "accountName":
"NameOfTheAccount", "reportStartDate": "2019-07-28", "reportEndDate":
"2019-07-28" } } ```

### Retrieving Country Code Directional Response Counts Report

**Method and URI** :

GET https://api.ultradns.com/requests/{requestID}

  
**Parameters** : ReportRequest DTO

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a list
of Country Code Directional Response Report Response DTO.

**Errors** : An error code is returned under the following conditions:

  * Error Code 401 â âUnauthorized. Token not found, expired or invalid.â

  * Error Code 404 â âNo report with the given ID was requested before.â

### Report Request ID DTO

The requestID is a randomly generated ID of letters and numbers sent to the
user after the successful request for a report.

ReportRequest DTO

Field |  Description |  Type  
---|---|---  
**requestID** |  The requestID that is provided to the user once a request for a report has been made.

  * For the Projected Query Volumes report, the requestID will have the following prefix: PQV.

|  String.  
  
JSON Example: Request ID return

Status 201 Created  
  
{  
  
"requestId": "PQV-d5a4c7ce"  
  
}

Country Code Directional Response Report Response DTO

Response Body |  Description |  Type  
---|---|---  
accountName |  The Account Name for which the report is being generated for. |  String.  
reportStateDate |  The start date that the report is being run from. |  Date.  
reportEndDate |  The end date that the report is being run to. |  Date.  
zoneName |  The zone name for which the report is being generated, or the zone name that is present under the specified account. |  String.  
responseCountTotal |  The total response count for queries that originated from all countries for the requested report inputs. |  Long  
responseCountOther |  The total response count for queries that originated from countries other than ones specifically returned in the response, as well as the Caribbean Netherlands. |  Long.  
responseCountByCountryCode |  The total response count by country code, as a Map. Refer to Country Code Directional Response Counts - Country Codes  for a full list of Country Codes. |  Map  
(String, Long)  
  
Country Code Directional Response Counts - Country Codes

Country Code as String |  Response Count as Long  
---|---  
AD |  Response count for queries that originated from Andorra.  
AE |  Response count for queries that originated from the United Arab Emirates.  
AF |  Response count for queries that originated from Afghanistan.  
AG |  Response count for queries that originated from Antigua and Barbuda.  
AI |  Response count for queries that originated from Anguilla.  
AL |  Response count for queries that originated from Albania.  
AM |  Response count for queries that originated from Armenia.  
AN |  Response count for queries that originated from Netherlands Antilles.  
AO |  Response count for queries that originated from Angola.  
AQ |  Response count for queries that originated from Antarctica.  
AR |  Response count for queries that originated from Argentina.  
AS |  Response count for queries that originated from American Samoa.  
AT |  Response count for queries that originated from Austria.  
AU |  Response count for queries that originated from Australia.  
AW |  Response count for queries that originated from Aruba.  
AX |  Response count for queries that originated from the Aland Islands.  
AZ |  Response count for queries that originated from Azerbaijan.  
BA |  Response count for queries that originated from Bosnia-Herzegovina.  
BB |  Response count for queries that originated from Barbados.  
BD |  Response count for queries that originated from Bangladesh.  
BE |  Response count for queries that originated from Belgium.  
BF |  Response count for queries that originated from Burkina Faso.  
BG |  Response count for queries that originated from Bulgaria.  
BH |  Response count for queries that originated from Bahrain.  
BI |  Response count for queries that originated from Burundi.  
BJ |  Response count for queries that originated from Benin.  
BL |  Response count for queries that originated from Saint Barthelemy.  
BM |  Response count for queries that originated from Bermuda.  
BN |  Response count for queries that originated from Brunei Darussalam.  
BO |  Response count for queries that originated from Bolivia.  
BQ |  Response count for queries that originated from the Dutch Caribbean.  
BR |  Response count for queries that originated from Brazil.  
BS |  Response count for queries that originated from the Bahamas.  
BT |  Response count for queries that originated from Bhutan.  
BV |  Response count for queries that originated from Bouvet Island.  
BW |  Response count for queries that originated from Botswana.  
BY |  Response count for queries that originated from Belarus.  
BZ |  Response count for queries that originated from Belize.  
CA |  Response count for queries that originated from Canada.  
CC |  Response count for queries that originated from the Cocos (Keeling) Islands.  
CD |  Response count for queries that originated from the Democratic Republic of the Congo.  
CF |  Response count for queries that originated from the Central African Republic.  
CG |  Response count for queries that originated from Congo.  
CH |  Response count for queries that originated from Switzerland.  
CI  |  Response count for queries that originated from Cote d'Ivoire.  
CK |  Response count for queries that originated from the Cook Islands.  
CL |  Response count for queries that originated from Chile.  
CM |  Response count for queries that originated from Cameroon.  
CN |  Response count for queries that originated from China.  
CO |  Response count for queries that originated from Colombia.  
CR |  Response count for queries that originated from Costa Rica.  
CU |  Response count for queries that originated from Cuba.  
CV |  Response count for queries that originated from Cape Verde.  
CW |  Response count for queries that originated from Curacao.  
CX |  Response count for queries that originated from Christmas Island.  
CY |  Response count for queries that originated from Cyprus.  
CZ |  Response count for queries that originated from the Czech Republic.  
DE |  Response count for queries that originated from Germany.  
DJ |  Response count for queries that originated from Djibouti.  
DK |  Response count for queries that originated from Denmark.  
DM |  Response count for queries that originated from Dominica.  
DO |  Response count for queries that originated from the Dominican Republic.  
DZ |  Response count for queries that originated from Algeria.  
EC |  Response count for queries that originated from Ecuador.  
EE |  Response count for queries that originated from Estonia.  
EG |  Response count for queries that originated from Egypt.  
EH |  Response count for queries that originated from Western Sahara.  
ER |  Response count for queries that originated from Eritrea.  
ES |  Response count for queries that originated from Spain.  
ET |  Response count for queries that originated from Ethiopia.  
FI |  Response count for queries that originated from Finland.  
FJ |  Response count for queries that originated from Fiji.  
FK |  Response count for queries that originated from the Falkland Islands.  
FM |  Response count for queries that originated from the Federated States of Micronesia.  
FO |  Response count for queries that originated from the Faroe Islands.  
FR |  Response count for queries that originated from France.  
GA |  Response count for queries that originated from Gabon.  
GB |  Response count for queries that originated from the United Kingdom - England, Northern Ireland, Scotland, and Wales.  
GD |  Response count for queries that originated from Grenada.  
GE |  Response count for queries that originated from Georgia.  
GF |  Response count for queries that originated from French Guiana.  
GG |  Response count for queries that originated from Guernsey.  
GH |  Response count for queries that originated from Ghana.  
GI |  Response count for queries that originated from Gibraltar.  
GL |  Response count for queries that originated from Greenland.  
GM |  Response count for queries that originated from Gambia.  
GN |  Response count for queries that originated from Guinea.  
GP |  Response count for queries that originated from Guadeloupe.  
GQ |  Response count for queries that originated from Equatorial Guinea.  
GR |  Response count for queries that originated from Greece.  
GS |  Response count for queries that originated from South Georgia and the South Sandwich Islands.  
GT |  Response count for queries that originated from Guatemala.  
GU |  Response count for queries that originated from Guam.  
GW |  Response count for queries that originated from Guinea-Bissau.  
GY |  Response count for queries that originated from Guyana.  
HK |  Response count for queries that originated from Hong Kong.  
HM |  Response count for queries that originated from Heard Island and the McDonald Islands.  
HN |  Response count for queries that originated from Honduras.  
HR |  Response count for queries that originated from Croatia.  
HT |  Response count for queries that originated from Haiti.  
HU |  Response count for queries that originated from Hungary.  
ID |  Response count for queries that originated from Indonesia.  
IE |  Response count for queries that originated from Ireland.  
IL |  Response count for queries that originated from Israel.  
IM |  Response count for queries that originated from the Isle of Man.  
IN |  Response count for queries that originated from India.  
IO |  Response count for queries that originated from the British Indian Ocean Territory - Chagos Islands.  
IQ |  Response count for queries that originated from Iraq.  
IR |  Response count for queries that originated from Iran.  
IS |  Response count for queries that originated from Iceland.  
IT |  Response count for queries that originated from Italy.  
JE |  Response count for queries that originated from Jersey.  
JM |  Response count for queries that originated from Jamaica.  
JO |  Response count for queries that originated from Jordan.  
JP |  Response count for queries that originated from Japan.  
KE |  Response count for queries that originated from Kenya.  
KG |  Response count for queries that originated from Kyrgyzstan.  
KH |  Response count for queries that originated from Cambodia.  
KI |  Response count for queries that originated from Kiribati.  
KM |  Response count for queries that originated from Comoros.  
KN |  Response count for queries that originated from St. Kitts and Nevis.  
KP |  Response count for queries that originated from the Democratic Peoples's Republic of Korea.  
KR |  Response count for queries that originated from the Republic of Korea.  
KW |  Response count for queries that originated from Kuwait.  
KY |  Response count for queries that originated from the Cayman Islands.  
KZ |  Response count for queries that originated from Kazakhstan.  
LA |  Response count for queries that originated from Lao People's Democratic Republic.  
LB |  Response count for queries that originated from Lebanon.  
LC |  Response count for queries that originated from St. Lucia.  
LI |  Response count for queries that originated from Liechtenstein.  
LK |  Response count for queries that originated from Sri Lanka.  
LR |  Response count for queries that originated from Liberia.  
LS |  Response count for queries that originated from Lesotho.  
LT |  Response count for queries that originated from Lithuania.  
LU |  Response count for queries that originated from Luxembourg.  
LV |  Response count for queries that originated from Latvia.  
LY |  Response count for queries that originated from the Libyan Arab Jamahiriya.  
MA |  Response count for queries that originated from Morocco.  
MC |  Response count for queries that originated from Monaco.  
MD |  Response count for queries that originated from the Republic of Moldova.  
ME |  Response count for queries that originated from Montenegro.  
MF |  Response count for queries that originated from Saint Martin.  
MG |  Response count for queries that originated from Madagascar.  
MH |  Response count for queries that originated from the Marshall Islands.  
MK |  Response count for queries that originated from Macedonia, the former Republic of Yugoslav.  
ML |  Response count for queries that originated from Mali.  
MM |  Response count for queries that originated from Myanmar.  
MN |  Response count for queries that originated from Mongolia.  
MO |  Response count for queries that originated from Macao.  
MP |  Response count for queries that originated from the Commonwealth of the Northern Mariana Islands.  
MQ |  Response count for queries that originated from Martinique.  
MR |  Response count for queries that originated from Mauritania.  
MS |  Response count for queries that originated from Montserrat.  
MT |  Response count for queries that originated from Malta.  
MU |  Response count for queries that originated from Mauritius.  
MV |  Response count for queries that originated from Maldives.  
MW |  Response count for queries that originated from Malawi.  
MX |  Response count for queries that originated from Mexico.  
MY |  Response count for queries that originated from Malaysia.  
MZ |  Response count for queries that originated from Mozambique.  
NA |  Response count for queries that originated from Namibia.  
NC |  Response count for queries that originated from New Caledonia.  
NE |  Response count for queries that originated from Niger.  
NF |  Response count for queries that originated from Norfolk Island.  
NG |  Response count for queries that originated from Nigeria.  
NI |  Response count for queries that originated from Nicaragua.  
NL |  Response count for queries that originated from the Netherlands.  
NO |  Response count for queries that originated from Norway.  
NP |  Response count for queries that originated from Nepal.  
NR |  Response count for queries that originated from Nauru.  
NU |  Response count for queries that originated from Niue.  
NZ |  Response count for queries that originated from New Zealand.  
OM |  Response count for queries that originated from Oman.  
PA |  Response count for queries that originated from Panama.  
PE |  Response count for queries that originated from Peru.  
PF |  Response count for queries that originated from French Polynesia.  
PG |  Response count for queries that originated from Papua New Guinea.  
PH |  Response count for queries that originated from the Philippines.  
PK |  Response count for queries that originated from Pakistan.  
PL |  Response count for queries that originated from Poland.  
PM |  Response count for queries that originated from Saint Pierre and Miquelon.  
PN |  Response count for queries that originated from Pitcairn.  
PR |  Response count for queries that originated from Puerto Rico.  
PS |  Response count for queries that originated from (Occupied ) Palestinian Territory.  
PT |  Response count for queries that originated from Portugal.  
PW |  Response count for queries that originated from Palau.  
PY |  Response count for queries that originated from Paraguay.  
QA |  Response count for queries that originated from Qatar.  
RE |  Response count for queries that originated from Reunion.  
RO |  Response count for queries that originated from Romania.  
RS |  Response count for queries that originated from Serbia.  
RU |  Response count for queries that originated from the Russian Federation.  
RW |  Response count for queries that originated from Rwanda.  
SA |  Response count for queries that originated from Saudi Arabia.  
SB |  Response count for queries that originated from the Solomon Islands.  
SC |  Response count for queries that originated from Seychelles.  
SD |  Response count for queries that originated from Sudan.  
SE |  Response count for queries that originated from Sweden.  
SG |  Response count for queries that originated from Singapore.  
SH |  Response count for queries that originated from St Helena.  
SI |  Response count for queries that originated from Slovenia.  
SJ |  Response count for queries that originated from Svalbard and Jan Mayen.  
SK |  Response count for queries that originated from Slovakia.  
SL |  Response count for queries that originated from Sierra Leone.  
SM |  Response count for queries that originated from San Marino.  
SN |  Response count for queries that originated from Senegal.  
SO |  Response count for queries that originated from Somalia.  
SR |  Response count for queries that originated from Suriname.  
SS |  Response count for queries that originated from South Sudan.  
ST |  Response count for queries that originated from Sao Tome and Principe.  
SV |  Response count for queries that originated from El Salvador.  
SX |  Response count for queries that originated from Saint Maarten.  
SY |  Response count for queries that originated from the the Syrian Arab Republic.  
SZ |  Response count for queries that originated from Swaziland.  
TC |  Response count for queries that originated from the Turks and Caicos Islands.  
TD |  Response count for queries that originated from Chad.  
TF |  Response count for queries that originated from the French Southern Territories.  
TG |  Response count for queries that originated from Togo.  
TH |  Response count for queries that originated from Thailand.  
TJ |  Response count for queries that originated from Tajikistan.  
TK |  Response count for queries that originated from Tokelau.  
TL |  Response count for queries that originated from the Democratic Republic of Timor-Leste.  
TM |  Response count for queries that originated from Turkmenistan.  
TN |  Response count for queries that originated from Tunisia.  
TO |  Response count for queries that originated from Tonga.  
TR |  Response count for queries that originated from the Republic of Turkey.  
TT |  Response count for queries that originated from Trinidad and Tobago.  
TV |  Response count for queries that originated from Tuvalu.  
TW |  Response count for queries that originated from Taiwan.  
TZ |  Response count for queries that originated from the United Republic of Tanzania.  
UA |  Response count for queries that originated from Ukraine.  
UG |  Response count for queries that originated from Uganda.  
UM |  Response count for queries that originated from the United States Minor Outlying Islands  
US |  Response count for queries that originated from the United States.  
UY |  Response count for queries that originated from Uruguay.  
UZ |  Response count for queries that originated from Uzbekistan.  
VA |  Response count for queries that originated from Vatican City.  
VC |  Response count for queries that originated from Saint Vincent and the Grenadines.  
VE |  Response count for queries that originated from the Bolivarian Republic of Venezuela.  
VG |  Response count for queries that originated from the British Virgin Islands.  
VI |  Response count for queries that originated from the U.S Virgin Islands.  
VN |  Response count for queries that originated from Vietnam.  
VU |  Response count for queries that originated from Vanuatu.  
WF |  Response count for queries that originated from Wallis and Futuna.  
WS |  Response count for queries that originated from Samoa.  
YE |  Response count for queries that originated from Yemen.  
YT |  Response count for queries that originated from Mayotte.  
ZA |  Response count for queries that originated from South Africa.  
ZM |  Response count for queries that originated from Zambia.  
ZW |  Response count for queries that originated from Zimbabwe.  
  
![](../../Resources/Images/Rest-API_User_Guide/Introduction_80x91.png) | 

  * Bouvet Island, Dutch Carribean, Netherlands Antilles, and Vatican City are not currently supported at this time, and as such, will always be returned as a 0.
  * The following country codes are not recognized by the Country Code Directional Response Counts Report: **AP** , **EU** , and **FX**.

  
---|---  
  
### Response Link Headers

Response Links Headers

Field |  Description  
---|---  
Link |  **Relative URL to next page of report if available** : </v1/reports/dns_resolution/directional_response_counts/country_code?offset=8&limit=4>; rel="next"  **Relative URL to previous page of report if available** : </v1/reports/dns_resolution/directional_response_counts/country_code?offset=0&limit=4>; rel="previous" When using the next or previous link header to retrieve report data, you must perform another POST call, and include the original body content (if any) and new query parameters (such as offset and limit).  When continuing to use subsequent Link Headers to retrieve additional results, you must continue to perform the POST call per link header to retrieve the next set of report details.  
Limit |  Specify the maximum number of records in requested response. Cannot be greater than maximum allowed limit. Currently maximum allowed limit is 100k.  
Results |  Total rows in the report response.  
  
JSON Example: Retrieving the Country Code Directional Response Counts Report

JSON Example: Retrieving the Country Code Directional Response Counts Report
```json [ { "accountName": "teamrest", "reportStartDate": "2019-07-11",
"reportEndDate": "2019-07-11", "zoneName": "clienitp.com.",
"responseCountTotal": 200, "responseCountOther": 0,
"responseCountByCountryCode": { "AD": 0, "AE": 0, "AF": 0, "AG": 0, "AI": 0,
"AL": 0, "AM": 0, "AN": 0, "AO": 0, "AQ": 0, "AR": 0, "AS": 0, "AT": 0, "AU":
0, "AW": 0, "AX": 0, "AZ": 0, "BA": 0, "BB": 0, "BD": 0, "BE": 0, "BF": 0,
"BG": 0, "BH": 0, "BI": 0, "BJ": 0, "BL": 0, "BM": 0, "BN": 0, "BO": 0, "BQ":
0, "BR": 0, "BS": 0, "BT": 0, "BV": 0, "BW": 0, "BY": 0, "BZ": 0, "CA": 0,
"CC": 0, "CD": 0, "CF": 0, "CG": 0, "CH": 0, "CI": 0, "CK": 0, "CL": 0, "CM":
0, "CN": 0, "CO": 0, "CR": 0, "CU": 0, "CV": 0, "CW": 0, "CX": 0, "CY": 0,
"CZ": 0, "DE": 0, "DJ": 0, "DK": 0, "DM": 0, "DO": 0, "DZ": 0, "EC": 0, "EE":
0, "EG": 0, "EH": 0, "ER": 0, "ES": 0, "ET": 0, "FI": 0, "FJ": 0, "FK": 0,
"FM": 0, "FO": 0, "FR": 0, "GA": 0, "GB": 0, "GD": 0, "GE": 0, "GF": 0, "GG":
0, "GH": 0, "GI": 0, "GL": 0, "GM": 0, "GN": 0, "GP": 0, "GQ": 0, "GR": 0,
"GS": 0, "GT": 0, "GU": 0, "GW": 0, "GY": 0, "HK": 0, "HM": 0, "HN": 0, "HR":
0, "HT": 0, "HU": 0, "ID": 0, "IE": 0, "IL": 0, "IM": 0, "IN": 0, "IO": 0,
"IQ": 0, "IR": 0, "IS": 0, "IT": 0, "JE": 0, "JM": 0, "JO": 0, "JP": 0, "KE":
0, "KG": 0, "KH": 0, "KI": 0, "KM": 0, "KN": 0, "KP": 0, "KR": 0, "KW": 0,
"KY": 0, "KZ": 0, "LA": 0, "LB": 0, "LC": 0, "LI": 0, "LK": 0, "LR": 0, "LS":
0, "LT": 0, "LU": 0, "LV": 0, "LY": 0, "MA": 0, "MC": 0, "MD": 0, "ME": 0,
"MF": 0, "MG": 0, "MH": 0, "MK": 0, "ML": 0, "MM": 0, "MN": 0, "MO": 0, "MP":
0, "MQ": 0, "MR": 0, "MS": 0, "MT": 0, "MU": 0, "MV": 0, "MW": 0, "MX": 0,
"MY": 0, "MZ": 0, "NA": 0, "NC": 0, "NE": 0, "NF": 0, "NG": 0, "NI": 0, "NL":
0, "NO": 0, "NP": 0, "NR": 0, "NU": 0, "NZ": 0, "OM": 0, "PA": 0, "PE": 0,
"PF": 0, "PG": 0, "PH": 0, "PK": 0, "PL": 0, "PM": 0, "PN": 0, "PR": 0, "PS":
0, "PT": 0, "PW": 0, "PY": 0, "QA": 0, "RE": 0, "RO": 0, "RS": 0, "RU": 0,
"RW": 0, "SA": 0, "SB": 0, "SC": 0, "SD": 0, "SE": 0, "SG": 0, "SH": 0, "SI":
0, "SJ": 0, "SK": 0, "SL": 0, "SM": 0, "SN": 0, "SO": 0, "SR": 0, "SS": 0,
"ST": 0, "SV": 0, "SX": 0, "SY": 0, "SZ": 0, "TC": 0, "TD": 0, "TF": 0, "TG":
0, "TH": 0, "TJ": 0, "TK": 0, "TL": 0, "TM": 0, "TN": 0, "TO": 0, "TR": 0,
"TT": 0, "TV": 0, "TW": 0, "TZ": 0, "UA": 0, "UG": 0, "UM": 0, "US": 200,
"UY": 0, "UZ": 0, "VA": 0, "VC": 0, "VE": 0, "VG": 0, "VI": 0, "VN": 0, "VU":
0, "WF": 0, "WS": 0, "YE": 0, "YT": 0, "ZA": 0, "ZM": 0, "ZW": 0 } } ] ```

.CSV Example: Retrieving the Country Code Directional Response Counts Report

Account Name,Report Start Date,Report End Date,Zone
Name,Total,Other,AD,AE,AF,AG,AI,AL,AM,AN,AO,AQ,AR,AS,AT,AU,AW,AX,AZ,BA,BB,BD,BE,BF,BG,BH,BI,BJ,BL,BM,BN,BO,BQ,BR,  
BS,BT,BV,BW,BY,BZ,CA,CC,CD,CF,CG,CH,CI,CK,CL,CM,CN,CO,CR,CU,CV,CW,CX,CY,CZ,DE,DJ,DK,DM,DO,DZ,EC,EE,EG,EH,ER,ES,ET,  
FI,FJ,FK,FM,FO,FR,GA,GB,GD,GE,GF,GG,GH,GI,GL,GM,GN,GP,GQ,GR,GS,GT,GU,GW,GY,HK,HM,HN,HR,HT,HU,ID,IE,IL,IM,IN,IO,IQ,  
IR,IS,IT,JE,JM,JO,JP,KE,KG,KH,KI,KM,KN,KP,KR,KW,KY,KZ,LA,LB,LC,LI,LK,LR,LS,LT,LU,LV,LY,MA,MC,MD,ME,MF,MG,MH,MK,ML,  
MM,MN,MO,MP,MQ,MR,MS,MT,MU,MV,MW,MX,MY,MZ,NA,NC,NE,NF,NG,NI,NL,NO,NP,NR,NU,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PM,PN,PR,PS,  
PT,PW,PY,QA,RE,RO,RS,RU,RW,SA,SB,SC,SD,SE,SG,SH,SI,SJ,SK,SL,SM,SN,SO,SR,SS,ST,SV,SX,SY,SZ,TC,TD,TF,TG,TH,TJ,TK,TL,  
TM,TN,TO,TR,TT,TV,TW,TZ,UA,UG,UM,US,UY,UZ,VA,VC,VE,VG,VI,VN,VU,WF,WS,YE,YT,ZA,ZM,ZW

teamrest,2019-07-11,2019-07-11,clienitp.com.,200,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,  
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,  
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,  
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,  
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,200,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

