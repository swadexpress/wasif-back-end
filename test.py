<VirtualHost *:80>
    ServerName www.porichoylive.xyz
    ServerAdmin contact@kawsarkhan.com
    #Document Root is not required
    DocumentRoot /var/www/incomeexpensesapi
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
    
    Alias /static /var/www/incomeexpensesapi/static
    <Directory /var/www/incomeexpensesapi/static>
        Require all granted
    </Directory>
    
    Alias /media /var/www/incomeexpensesapi/media
    <Directory /var/www/incomeexpensesapi/media>
        Require all granted
    </Directory>
    
    <Directory /var/www/incomeexpensesapi/incomeexpensesapi>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    
    WSGIDaemonProcess incomeexpensesapi python-home=/var/www/incomeexpensesapi/venv python-path=/var/www/incomeexpensesapi
    WSGIProcessGroup incomeexpensesapi
    WSGIScriptAlias /  /var/www/incomeexpensesapi/incomeexpensesapi/wsgi.py
</VirtualHost>