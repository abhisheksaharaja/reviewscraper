# reviewscraper Project

## Inference demo
- UI for Search Product 
![sc1](https://user-images.githubusercontent.com/76595524/149091308-5e4a9f86-74af-459d-85d8-1b134d4f4c8d.jpg)

- UI where get The Buyer comments 
![sc2](https://user-images.githubusercontent.com/76595524/149091325-e8b1b26b-2586-4764-b919-4958daac3dd8.jpg)

## Description
User will search the required item from search filed. Then all the comments provide by the buyer for that particular item will be fetch from flipkart and show in tabular format.

## Setup

## Create a file "Dockerfile" with below content

```
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
```


## Create a "Procfile" with following content
```
web: gunicorn main:app
```


## create a file ".circleci\config.yml" with following content
<a href="https://github.com/abhisheksaharaja/Flight_Price_Prediction_ML_Project/blob/main/.circleci/config.yml">.circleci\config.yml</a>


## to create requirements.txt
```
pip freeze>requirements.txt
```

## initialize git repo
```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin <github_url>
git push -u origin main
```

## create a account at circle ci

<a href="https://circleci.com/login/">Circle CI</a>


## setup your project 

<a href="https://app.circleci.com/projects/project-dashboard/github/abhisheksaharaja/"> Setup project </a>


## Environment variable setup in Circle CI

```
DOCKERHUB_USER
DOCKER_HUB_PASSWORD_USER
HEROKU_API_KEY
HEROKU_APP_NAME
HEROKU_EMAIL_ADDRESS
DOCKER_IMAGE_NAME=reviewscraperapp
```

## to update the modification

```
git add .
git commit -m "proper message"
git push 
```
