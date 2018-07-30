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
$ pip install Flask==1.0.2
$
$ pip freeze
click==6.7
Flask==1.0.2
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
pkg-resources==0.0.0
Werkzeug==0.14.1
</pre>

## Exec
<pre>
$ export FLASK_APP=main.py
$ flask run
</pre>

## GAE Deploy
<pre>
$ gcloud app deploy
</pre>
