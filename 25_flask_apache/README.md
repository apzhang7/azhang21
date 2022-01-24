# how-to :: DEPLOY A FLASK APP ON APACHE2
---
## Overview
Flask is not built to serve -- on its own -- persistent or high-traffic sites. Apache, on the other hand, is. Luckily, Apache can be configured to use its industrial-grade machinery to serve Flask and other apps. Deploying your Flask app to an Apache2 server will allow anyone on the web to access your app at any time.

### Estimated Time Cost: 2 hour

### Prerequisites:

- A droplet with Ubuntu 20.04.3 and Apache2 installed

## Instructions

### Creating a Flask App
1. Enable wsgi.
```
sudo apt-get install libapache2-mod-wsgi-py3 python-dev
```
```
sudo a2enmod wsgi
```

2. Create your own basic FlaskApp (name FlaskApp can be also replaced with whatever you want)
```
cd /var/www
```
```
sudo mkdir FlaskApp
```
```
cd FlaskApp
```
```
sudo mkdir FlaskApp
```
```
cd FlaskApp
```
```
sudo mkdir static templates
```
Making the app:
```
sudo nano __init__.py
```
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello, welcome!"
  
if __name__ == "__main__": 
	app.run()
```

3. Install python, pip, virtualenv, and flask.
```
$ sudo apt-get install python3-pip
```
```
sudo pip3 install virtualenv
```
```
sudo virtualenv env
```
```
source venv/bin/activate
```
```
sudo pip3 install Flask
```
Test if it works!
```
sudo python3 __init__.py
```

4. Enable virtual host.
```
deactivate
```
```
cd
```
```
sudo nano /etc/apache2/sites-available/FlaskApp.conf
```
Paste the following, replacing mywebsite.com with YOUR_IP, and admin@mywebsite.com with your USERNAME@YOUR_IP. FlaskApp must be substituted as well.
```
<VirtualHost *:80>
 	ServerName mywebsite.com
 	ServerAdmin admin@mywebsite.com
 	WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
 	<Directory /var/www/FlaskApp/FlaskApp/>
 		Order allow,deny
 		Allow from all
 	</Directory>
 	Alias /static /var/www/FlaskApp/FlaskApp/static
 	<Directory /var/www/FlaskApp/FlaskApp/static/>
 		Order allow,deny
 		Allow from all
 	</Directory>
 	ErrorLog ${APACHE_LOG_DIR}/error.log
 	LogLevel warn
 	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
```
sudo a2ensite FlaskApp
```

5. Create a WSGI file.
```
cd /var/www/FlaskApp
```
```
sudo nano flaskapp.wsgi
```
Paste the following. FlaskApp must be substituted for the name of your app.
```
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = 'Add your secret key'
```

6. Restart apache and run your app by going to `http://YOUR_IP_ADDRESS`.
```
sudo service apache2 restart
```

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
* https://pythonforundergradengineers.com/flask-app-on-digital-ocean.html
---

Accurate as of (last update): 2022-01-24

#### Contributors:  
Angela Zhang, pd1
