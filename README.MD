#Multiple Docker

2 FastApi  
1 nginx  


Todo:
====
Use Python's image instead of ubuntu's  

Build docker images
===============

build dockers  
`docker-compose build`  

<!-- build proper images
docker build -t image1 .  
docker build -t image2 .   -->
run images  
`docker-compose up`  

<!-- `docker run --name myimage1 -d -p 8080:80 image1`  
`docker run --name myimage2 -d -p 8081:80 image2`    -->

work localy
----
`cat /etc/hosts`  
add:  
`127.0.0.1    pekochan.me www.pekochan.me`  
`127.0.0.1    welcomeapp.fr www.welcomeapp.fr`  

Reboot DNS  
`ᐅ sudo killall -HUP mDNSResponder`