# UIUCTF - ponydb (49 solves)

> http://ponydb.chal.uiuc.tf
(note: has unintended element that makes it slightly easier. see miniaturehorsedb for the full-difficulty challenge.)

**Category**: web

**Given**: 
- [ponydb.py](handouts/ponydb.py): website backend
- [templates/ponies.html](handouts/templates/ponies.html): website frontent

**Requirements**: Python, [flask](https://pypi.org/project/Flask), [mysql-connector-python](https://pypi.org/project/mysql-connector-python), [gunicorn](https://pypi.org/project/gunicorn)

**Solution Files**: N/A

**TL;DR**: SQL mode of `NO_BACKSLASH_ESCAPES` doesn't include default `STRICT_TRANS_TABLES`, which [allows truncation](https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html#sql-mode-strict), so a long enough JSON string can override the number key.

TODO

**Flag**: uiuctf{My_l33tle_p0ny_5fb234}
