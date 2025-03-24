

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

# Zone Snapshot and Restore APIs

In UltraDNS, a backup is also known as a Snapshot. A zone snapshot represents
the state of a zone (i.e. primarily its RRSet configuration) at the time the
Snapshot is created.

Performing a zone Restore uses the most recent zone snapshot, and overwrites
the zone's current configuration with that of the one stored in the Snapshot.
The zone snapshot can be restored at any point in time, as long as the zone
meets the required criteria.

  * Snapshot and Restore only supports primary zones.

  * The zone should not have more than 50,000 records, including the allowed pool's resource records.

For additional details on how to use the Zone Snapshot and Restore (ZBR),
please refer to the [Zone Snapshot and Restore API Guide](https://ultra-
portalstatic.ct.ultradns.net/static/docs/zbr_api_specs.html) on the support
page for additional documentation.

