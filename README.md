
# A CI/CD pipeline for python API

THis repo is CI/CD implementation of a python API application.





## Deployment

The repo consists of a pyton API with `Dockerfile`, `docker-compose..yml` for dockerisation of the application. 
The repo also includes `docker.yml` file in `.github/workflows`. A github actions workflow file to automate the deployment of new containers on each push to main branch.

Fork or clone the repo, chnage credentials in github scerets and username of dockerhub repo in `docker-compose..yml` and `docker.yml`. 

Now you can pull the image from docker and when a new latest image is available, 
copy the `docker-compose.yml` file to your server and run"

```bash
docker compose pull
docker compose up -d
```
These commands will update the image, remove old containers and will start new containers based on the latest image. 
