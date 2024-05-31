#!/usr/bin/env bash
#  Prepares a web server for deployment
# Creates the necessary flder, files and symobolic links
# configures nginx web server

function install() {
	if [ "$(command -v "$1")" ]; then
		echo -e "nginx is already installed"
	else
		echo -e "installing nginx...."
		sudo apt-get update &&
			sudo apt-get install -qq -y "$1" 
		echo -e "nginx installed\n"
	fi


}

function create_folders() {
	dire_s=( "/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/" )
	for dir in "${dire_s[@]}"; do
		if [ ! -d "$dir" ]; then
			echo "creating $dir"
			sudo mkdir -p "$dir"
		else
			echo -e "\t $dir already exist"
		fi
	done
}

# Install nginx and create the necessary folder
install nginx
create_folders

html="\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"
# Creating a fake html file
echo -e "$html" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# create a symbolic link
link="/data/web_static/current"
path="/data/web_static/releases/test/"

if [ -L "$link" ] && [ -e  $link ]; then
	echo "symbolic link exists. recreating it"
	unlink "$link"
	sudo ln -s "$path" "$link"

else
	sudo ln -s "$path" "$link"
fi

# give ownership of /data/ to 'ubuntu' user and group
sudo chown -R ubuntu:ubuntu /data/

server="\
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;  # Corrected: Added a semicolon at the end
    server_name _;
    add_header X-Served-By \$hostname;


    location / {
        try_files \$uri \$uri/ =404;
    }

    error_page 404 /error_404.html;
    location = /error_404.html {
        internal;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}

"
# Backup nginx configuration file
#sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bckp

# updating the configuration file
echo "$server" | sudo tee /etc/nginx/sites-available/default > /dev/null

# restart nginx
sudo service nginx restart
echo "done"

