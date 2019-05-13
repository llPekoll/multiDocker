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

<!-- `docker run --name myimage1 -d -p 8080:80 multidokcer/image1`  
`docker run --name myimage2 -d -p 8081:80 multidokcer/image2`    -->

Setup nginx
----
https://www.youtube.com/watch?v=rq2aKItyeqo  
docker run -d --name nginx-proxy nginx  
bash -c "clear && docker exec -it nginx-proxy sh"  
