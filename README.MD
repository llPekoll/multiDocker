#Multiple Docker

2 FastApi Docker  
Nginx not Dockerized

#Todo
====
- [ ]use workers

Docker stuff
======

build dockers  
`docker-compose build`  

single build test  
`docker build -t image1 .`  
`docker run --name myimage1 -d -p 8080:80 image1`  

run images
`docker-compose build`  
`docker-compose up`  

Procedure
-----

# - 1 edit hosts:  

`vim /etc/hosts`  
add:  
`127.0.0.1    pekochan.me www.pekochan.me`  
`127.0.0.1    welcomeapp.fr www.welcomeapp.fr`  
flush DNS cahes  
linux ᐅ `sudo systemd-resolve --flush-caches`  
osx ᐅ `sudo killall -HUP mDNSResponder`  

# - 2 copy peko.conf  
copy peko.conf to nginx path fodler
 > `/etc/nginx/sites-enabled > cp ~/work/multiDocker/nginx-proxy/peko.conf .`


# - 2b create static directory

 > `mkdir /var/www/static`


# - 3 build docker

> `docker-compose build

# - 4 run docker

> `docker-compose up

