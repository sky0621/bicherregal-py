# bicherregal-py

## Overview

「本棚自慢」サイトのPython3版　作成中

## Env
<pre>
$ cat /etc/os-release 
NAME="Ubuntu"
VERSION="17.10 (Artful Aardvark)"
$
$ python3 -V
Python 3.6.3
</pre>

## SetUp
<pre>
$ python3 -m venv venv
$ source venv/bin/activate
(venv) ~~ $ python -V
Python 3.6.3
(venv) ~~ $ pip -V
pip 9.0.1
</pre>
<pre>
$ pip install django==1.11
$
$ python -m django --version
1.11
</pre>
<pre>
$ django-admin startproject admin
$ cd admin/
$ python manage.py runserver
</pre>
open http://127.0.0.1:8000/ with browser.

## ToDo

- Dockerize
