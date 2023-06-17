<VirtualHost *:80>
    ServerName www.porichoy.live
    ServerAdmin contact@porichoy.live
    #Document Root is not required
    #DocumentRoot /var/www/project_folder_name
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
    
    Alias /static /var/www/django/static
    <Directory /var/www/django/static>
        Require all granted
    </Directory>
    
    Alias /media /var/www/django/media
    <Directory /var/www/django/media>
        Require all granted
    </Directory>
    
    <Directory /var/www/django/incomeexpensesapi>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    
    WSGIDaemonProcess django python-home=/var/www/django/env python-path=/var/www/django
    WSGIProcessGroup django
    WSGIScriptAlias /  /var/www/django/incomeexpensesapi/wsgi.py
</VirtualHost>