#!/usr/bin/env bash
# Installs nginx, creates folders, sets permissions and writes into file
# line 13 updates nginx config to serve content of 
# data/web_static/current to hbnb_static, 38i inserts on proper line
apt-get update
apt-get install nginx
service nginx start
mkdir -p /data/webstatic/releases/test/
mkdir -p /data/webstatic/shared/
touch /data/web_static/releases/test/index.html
echo "Holberton School" >> /data/web_static/releases/test/index.html
chown -R ubuntu:ubuntu /data
sed -i "38i\ \tlocation \/hbnb_static {\\n\\t\\talias \/data\/web_static\/current\/;\\n}" /etc/nginx/sites-available/default
service nginx restart
