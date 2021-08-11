# UIUCTF - Tablet 1 (51 solves)

> Red has been acting very sus lately... so I took a backup of their tablet to see if they are hiding something!
<br>It looks like Red has been exfiltrating sensitive data bound for Mira HQ to their own private server. We need to access that server and contain the leak.
<br>NOTE: Both Tablet challenges use the same tablet.tar.gz file.
<br>MD5: f629eec128551cfd69a906e7a29dc162

**Category**: forensics

**Given**: 
- [tablet.tar.gz](https://drive.google.com/file/d/1KcRzBZRA1VbuyzR6fVaibLgJQ11dD737/view): Tablet filesystem ([mirror 1](https://www.dropbox.com/s/1m7n1pyvq6xgwfb/tablet.tar.gz?dl=0), [mirror 2](https://mega.nz/file/9sFwjRiL#VdiMK50ION61Ll3O583TrQ3nqpxfMsM-hLXtUrUtfYU))

**Requirements**: [DB Browser for SQLite](https://sqlitebrowser.org/), an SSH client

**Solution Files**: N/A

**TL;DR**: Find SSH application database, get credentials, locate image with flag on server.

### Overview
TODO

**Flag**: uiuctf{upload_task_only_takes_9_seconds_0bf79b}