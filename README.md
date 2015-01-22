# LITMUS - REST in Peace - A REST service test suite

## Features:
* Test case organizer and management. Testcases are grouped under operations and operations are grouped under services.
* Persistant storage of testcases
* JSON editor (Credits : https://www.jsoneditoronline.org/)
* Flexible response evaluator
* Open source

## github URL:
[https://github.com/harinarayan/litmus](https://github.com/harinarayan/litmus)

##Installation :
####Dependencies:

    python 2.7+
    pip
    django 1.7+
    sqlite3
    apache2
    mod_wsgi
    git

#### Setting up an instance:

As an example, I am laying down the steps for installation on an ubuntu box. This can be installed on any linux like box which has the required packages listed above, just that you will have to execute the equivalent of the commands shown below.


One the box is ready, ssh into the box and enter into God mode.

```
$ sudo -s
```

#### Python:

Verify python version.

```
$ python -V
Python 2.7.6
```

#### pip:

if not available, install it. (Type pip in the command line to check.)
```
$ apt-get install python-pip
```

#### Git:

If git is not available, install it.

```
$ apt-get install git
```

#### sqlite3:

If not available, install it. (Type sqlite3 in the command line to check.)
```
$ apt-get install sqlite3
```

#### apache2:

if not available, install it. (Type apache2 in the command line to check.)
```
$ apt-get install apache2
```

#### mod_wsgi:
```
$ apt-get install apache2-dev
$ apt-get install python-dev
$ wget https://github.com/GrahamDumpleton/mod_wsgi/archive/4.4.3.tar.gz
$ tar zxvf 4.4.3.tar.gz
$ cd mod_wsgi-4.4.3/
$ ./configure
$ make
$ make install
```
In  `/usr/lib/apache2/modules/` there should be a file called `mod_wsgi.so`


Now create a file called `/etc/apache2/mods-available/wsgi.load` with the content as shown below.

```
$ cat /etc/apache2/mods-available/wsgi.load
LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so
```
Create a sym link as shown below
```
$ ln -sf /etc/apache2/mods-available/wsgi.load /etc/apache2/mods-enabled/wsgi.load
```

#### django:

```
$ pip install django

$ python
>>> import django
>>> django.VERSION
(1, 7, 2, 'final', 0)
```

#### litmus:
```
$ cd /var/www/
$ git clone https://github.com/harinarayan/litmus.git
$ cd litmus
$ python manage.py migrate
$ python manage.py collectstatic
$ cd ..
$ chown -R www-data:www-data litmus

$ pip install jsonpath_rw
```

#### apache configuration:

Create a file `/etc/apache2/sites-available/litmus.conf` and paste the following content and save it. Make sure you edit the hostname to your instance hostname, everywhere.
```
<VirtualHost *:80>

ServerName hostname.com
ServerAlias litmus.com
ServerAdmin your-email@hostname.com

DocumentRoot /var/www/litmus/

Alias /robots.txt /var/www/litmus/litmus/robots.txt
Alias /favicon.ico /var/www/litmus/litmus/favicon.ico

Alias /static/ /var/www/litmus/static_root/

<Directory /var/www/litmus>
Order allow,deny
Allow from all
</Directory>

<Directory /var/www/litmus/static_root>
Require all granted
</Directory>

WSGIDaemonProcess hostname.com processes=2 threads=15 display-name=%{GROUP}
WSGIProcessGroup hostname.com

WSGIScriptAlias / /var/www/litmus/litmus/wsgi.py

<Directory /var/www/litmus/litmus>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

</VirtualHost>
```

Create a sym link as follows.
```
$ ln -sf /etc/apache2/sites-available/litmus.conf /etc/apache2/sites-enabled/litmus.conf
```
Restart apache2
```
$ service apache2 restart
```
 
That's it!!!

Try it out by hitting `hostname.com` on your browser.

 
## Upgrading

We will keep enhancing the product. To keep your installation up-to-date, run these commands.
```
$ cd /var/www/litmus
$ git pull
$ python manage.py migrate
$ python manage.py collectstatic
$ touch litmus/wsgi.py
$ service apache2 restart
```

## Product backlog
* TLS/SSL version selection at service level
* users and accounts, LDAP authorization etc.
* import & export testcases 
  * between installations of litmus
  * from/to other automation suites
* history & trending
