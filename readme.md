# Recipes API
This project was created was just for fun and is no affiliated with the website [allrecipes](www.allrecipes.com) in any way.<br>

## Installing the required packages 
 `python -m pip install -r requirements.txt`<br>
<br>

## Running the application
### Building the docker image using the dockerfile
`docker build -t allrecipes .`<br>

the -t flag tags our image<br>
<br>

### Running the image using docker compose
`docker compose up`

-d start a container in detached mode<br>
-p connect port 83 to port 5000 in the host<br>
<br>

### Running the application without docker
`python app.py`<br>
<br>

## Paths

