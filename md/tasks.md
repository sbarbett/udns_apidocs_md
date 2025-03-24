

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

# Tasks

The Task API allows a user to discover the state of jobs that run in the
background. Certain commands that will take longer to complete will return a
Task Id in the X-Task-Id header. Use this value to query the state of the
task, retrieve data associated with the task, and to remove information about
the completed task from the system.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Task DTO

The Task DTO is used to describes the current state of a task.

Task DTO

Field |  Description |  Type  
---|---|---  
taskId |  Id for the task. |  UUID  
code |  Current state of the task. |  Use one from: 

  * PENDING 
  * IN_PROCESS
  * COMPLETE
  * ERROR 

  
message |  Current message for the task. |  String  
resultUri |  If task is COMPLETE, the URI from where the resulting data can be downloaded. |  URI  
  
JSON Example: Task Status

{  
"taskId": "0b40c7dd-748d-4c49-8506-26f0c7d2ea9c",  
"Code": "COMPLETE",  
"message": "Processing complete",  
"resultUri": "/tasks/0b40c7dd-748d-4c49-8506-26f0c7d2ea9c/result"  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)TaskList DTO

The TaskList DTO is returned when requesting the state of all tasks for a
user.

TaskList DTO

Field |  Description |  Type  
---|---|---  
tasks |  The list of returned tasks. Each entry in the list matches the task DTO described above. |  Task DTO  
queryInfo/q |  The query used to construct the list. |  String  
queryInfo/sort |  The sort column used to order the list. |  String  
queryInfo/reverse |  Whether the list is ascending (false) or descending (true). |  Boolean  
queryInfo/limit |  The maximum number of rows requested. |  Integer  
resultInfo/totalCount |  Count of all zones in the system for the specified query. |  Integer  
resultInfo/offset |  The position in the list for the first returned element (0 based). |  Integer  
resultInfo/returnedCount |  The number of records returned. |  Integer  
  
JSON Example: Tasks

{  
"tasks": [  
{  
"taskId":"0b40c7dd-748d-4c49-8506-26f0c7d2ea9c",  
"Code":"COMPLETE",  
"message":"Processing complete",  
"resultUri":"/tasks/0b40c7dd-748d-4c49-8506-26f0c7d2ea9c/result"  
}  
],  
"queryInfo": {  
"q": "",  
"sort": "CODE",  
"reverse": false,  
"limit": 100  
},  
"resultInfo": {  
"totalCount": 1,  
"offset": 0,  
"returnedCount": 1  
}  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get the
Status of a Task

**Method and URI** :

GET https://api.ultradns.com/tasks/{taskId}

**Parameters** : Must include the specific Task ID.

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a Task
DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If {taskId} does not exist.

  * If you do not have permission to read {taskId}.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get the List
of Tasks

**Method and URI** :

GET https://api.ultradns.com/tasks

**Parameters** : Can include the following:

taskList Parameters

Parameter |  Description |  Type  
---|---|---  
q |  The query used to construct the list. Query operators are code and _hasData_. Valid values for code are: 

  * **PENDING**
  * **IN_PROCESS**
  * **COMPLETE**
  * **ERROR**

Valid values for hasData are **TRUE** or **FALSE**. Default value of _hasData_
is NULL. Query operators need be followed by a colon ( : ). Example:

  * q="code:COMPLETEâ
  * q="hasData:TRUE"
  * q="code:COMPLETE hasData:TRUE"

|  String  
offset |  The position in the list for the first returned element (0 based). The default value is 0. |  Integer  
limit |  The maximum number of rows requested. The default value is 100. |  Integer  
sort |  The sort column used to order the list. Valid sort fields are 

  * **CODE**
  * **CONTENT_TYPE**
  * **EXTENSIONS**
  * **HAS_DATA**
  * **DATE**

The default value is CODE. |  String  
reverse |  Whether the list is ascending (false) or descending (true). The default value is false. |  Boolean  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
TaskList DTO in the body content.

**Errors** : An error is returned under the following conditions:

  * If you do not have permission to read tasks.

JSON Example: Response to Get List of Tasks

{

"queryInfo": {

"sort": "DATE",

"reverse": true,

"limit": 100

},

"resultInfo": {

"totalCount": 3914,

"offset": 0,

"returnedCount": 100

},

"tasks": [

{

"taskId": "c3860c72-2a43-42a8-900e-e33486c2ffc7",

"code": "COMPLETE",

"message": "Zone 1648665192174-foo.invalid. deleted.",

"hasData": false

},

{

"taskId": "6d06dcd0-301b-4633-b7c7-9b21b05b63c1",

"code": "COMPLETE",

"message": "Zone 1648901840381-foo.invalid. deleted.",  
"hasData": false

},

{

"taskId": "36da90c0-a991-40fc-a9b4-9ecbd723a1ba",

"code": "COMPLETE",

"message": "Batch operation completed",  
"hasData": true

},

{

"taskId": "d4a1fbe7-e3d7-4c6c-95a5-5d21c22bac22",

"code": "COMPLETE",

"message": "Zone test-bulk-zone.hitukufqmo.com. deleted.",  
"hasData": false

}

]

}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get the
Results of a Task

**Method and URI** :

GET https://api.ultradns.com/tasks/{taskId}/result

**Parameters** : Must include a Task ID.

**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a  Task
DTO in the body content.

The content will be returned as a downloadable file. The name of the file will
be the {taskId} that was submitted with the request. The file extension and
content type are set by the background task and will be appropriate to the
data returned.

**Errors** : An error is returned under the following conditions:

  * If {taskId} does not exist.

  * If you do not have permission for the task associated with the supplied {taskId}.

  * If task is not yet completed.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Reporter Task
DTO

Th Reporter Task DTO is used to describe the current state of a task.

Task DTO

Field |  Description |  Type  
---|---|---  
taskId |  Id for the task. |  UUID  
code |  Current state of the task. |  Use one from:

  * PENDING 
  * IN_PROCESS
  * COMPLETE 
  * ERROR 

  
message |  Current message for the task. |  String  
lastModifiedDateTime |  Last Modified date time of the task. |  Date-Time  
resultUri |  If task is COMPLETE, the URI from where the resulting data can be downloaded. |  URI  
  
JSON Example: Task Status

{  
"taskId": "ZQV-013d3c5c-7b14-4ff0-b4af-453b76a827b6",  
"Code": "COMPLETE",  
"message": "Completed ZQV Report Successfully.",  
"lastModifiedDateTime": "2016-08-26T12:33:22.000Z",  
"resultUri":
"https://api.ultradns.com/reports/tasks/ZQV-013d3c5c-7b14-4ff0-b4af-453b76a827b6"  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Reporter
TaskList DTO

The Reporter TaskList DTO is returned when requesting the state of all tasks
for a user.

TaskList DTO

Field |  Description |  Type  
---|---|---  
**tasks** |  The list of returned tasks. Each entry in the list matches the task DTO described above. |  Reporter Task DTO.  
  
JSON Example: Tasks

{  
"tasks": [  
{  
"taskId": "ZQV-013d3c5c-7b14-4ff0-b4af-453b76a827b6",  
"Code": "COMPLETE",  
"message": "Completed ZQV Report Successfully.",  
"lastModifiedDateTime": "2016-08-26T12:33:22.000Z",  
"resultUri":
"https://api.ultradns.com/reports/tasks/ZQV-013d3c5c-7b14-4ff0-b4af-453b76a827b6"  
},  
{  
"taskId": "PQV-003f098b-a2df-437e-8482-65e8d93b4858",  
"Code": "COMPLETE",  
"message": "Completed PQVReport Successfully.",  
"lastModifiedDateTime": "2016-08-26T12:33:22.000Z",  
"resultUri":
"https://api.ultradns.com/reports/tasks/PQV-003f098b-a2df-437e-8482-65e8d93b4858"  
}  
]  
}

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Get the list
of Tasks for Reporting

**Method and URI** :

GET https://api.ultradns.com/tasks?taskType=reporting

**Parameters** :

taskList Parameters

Parameter |  Description |  Type  
---|---|---  
q |  The query used to construct the list. Query operators are code and _hasData_. Valid values for code are: 

  * PENDING 
  * IN_PROCESS
  * COMPLETE 
  * ERROR 

Valid values for _hasData_ are TRUE or FALSE. Query operators need be followed
by a : (colon). Example:

  * q="code:COMPLETEâ
  * q="hasData:TRUE"
  * q="code:COMPLETE hasData:TRUE"

|  String  
offset |  The position in the list for the first returned element (0 based). The default value is 0. |  Integer  
limit |  The maximum number of rows requested. The default value is 100. |  Integer  
sort |  The sort column used to order the list. Valid sort fields are:

  * CODE 
  * CONTENT_TYPE
  * EXTENSIONS
  * HAS_DATA
  * DATE. 

The default value is CODE. |  String  
reverse |  Whether the list is ascending (false) or descending (true). The default value is false. |  Boolean  
taskType |  For viewing reporting tasks user needs to set its value to "reporting". By default only Rest API configurations tasks will be returned as per current functionality. |  String  
  
**Body** : None

**Response** : If task completes, Status Code 200 OK is returned with a
Reporter TaskList DTO in the body content along with a Link and Link Header.

**Errors** : An error is returned under the following conditions:

  * Invalid taskType

  * No data is found.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Delete a Task

This call will remove information from the system for a task that has
completed or is in an error-state.

**Method and URI** :

DELETE https://api.ultradns.com/tasks/{taskId}

**Parameters** : Must include a Task ID.

**Body** : None

**Response** : If delete completes, Status Code 204 is returned with no
content in the body.

**Errors** : An error is returned under the following conditions:

  * If you do not have permission to delete {taskId}.

  * If {taskId} does not exist.

  * If the task is not in a state that can be deleted.

![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Link and Link
Header

The Link and Link Header information can be seen in response header.

Link and Link Header Response Information

Name |  Type |  Example  
---|---|---  
next |  Link |  </tasks?q="code:COMPLETE"&sort=DATE&taskType=reporting&offset=4&limit=2>; rel="next">  
previous |  Link |  </tasks?q="code:COMPLETE"&sort=DATE&taskType=reporting&offset=0&limit=2>; rel="previous">  
limit |  Link Header |  Initial request limit specified  
results |  Link Header |  Total results in the current response

