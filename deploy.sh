git pull -r

sudo /usr/local/bin/docker-compose stop
sudo /usr/local/bin/docker-compose run web django-admin.py startproject composeexample .
sudo /usr/local/bin/docker-compose up -d
