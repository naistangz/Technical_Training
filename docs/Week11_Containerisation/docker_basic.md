## Setting up Docker with Mac
1. Install [Docker Desktop on Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac/)
2. Run Docker Desktop (command, space, docker, enter)
3.When the :whale: icon appears, run the following command
```bash
docker run hello-world
```
4. Run ahskhan/nginx-test-rp-app
```bash
docker run ahskhan/nginx-test-rp-app
```
5. Pull nginx
```
docker pull nginx
```
6. Run docker to test if the app is working
```bash
docker run -p 80:80 ahskhan/nginx-test-rp-app:v2
```
7. 
```bash
docker run -d -p 80:80 nginx -> running in detached mode (-d)
docker ps
```

```
docker exec -it 31dc9df77202 sh
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
31dc9df77202        nginx               "/docker-entrypoint.…"   13 minutes ago      Up 13 minutes       0.0.0.0:80->80/tcp   dazzling_easley

docker exec -it 31dc9df77202 sh -> To communicate with container shell (it -> interactive shell)
```

8. To exit
```bash
exit
```

## Untagging an Image 
```
docker rmi -f naistangz/eng67_anais_nginx  
```  

## Port mapping
```bash
docker pull naistangz/eng67_anais_nginx 
docker run -d -p 50:80 naistangz/eng67_anais_nginx -> To run on port 50
docker stop -> To stop
docker ps -> process status
```

## Dockerfiles :whale:
1. Create folder on your OS
```bash
mkdir sample_app
```
2. CD into your folder
```bash
cd sample_app
```
3. Create a `Dockerfile`
```bash
nano Dockerfile
```

4. Docker is written in Go. Write the following basic commands:
```
FROM nginx:latest
COPY ./index.html /usr/share/nginx/html/index.html
COPY ./images /usr/share/nginx/html/images/
COPY ./assets /usr/share/nginx/html/assets/
```

4. Create a build 
```bash
docker build -t naistangz/sample_nginx:latest .
Creating a tag alled naistanagz/sample_nginx
. Dot stands for running a docker file in the current file path          
```

## What are microservices?
- Microservice architecture or microservices is a method of developing software system that focuses on building single-function modules 
- Software system is broken down into a collection of independent units and carry out every application as a separate service so they each have their own logic and database.
- All services have their own logic.
- They communicate with lightweight mechanisms, often an HTTP resource API.

## Benefits of Microservices
- Before, companies would be build a monolith application, a single autonomous unit.
- Making changes to the application could require building and deploying an entirely new version of software.
- Scaling specific functions of an application would mean you have to scale the entire application.
- **Microservices** solves these challenges of monolithic systems by being as modular as possible.
- This means building an application as a suite of small services, each running its own process and are independently deployable.
- **Simpler to deploy** - Deploy in literal pieces without affecting other services
- **Simpler to understand** - Able to follow code easier since function is isolated and less dependent
- **Re-usability Across Business** - Share small services like payment or login systems across the business.

## Challenges of Microservices
- **Extra complexity** - Microservices architecture is a distributed system