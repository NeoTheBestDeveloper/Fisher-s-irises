# Fisher's irises
Service solve fisher's irises problem.

# Problem
We have dataset with 150 rows with data about irises(sepal_length, sepal_width, petal_length, petal_width). 
Model classify iris sort from these data.

# Data example
![image data example](https://hsto.org/web/bb5/c73/107/bb5c7310793b4b7dbc26f873d65fa70f.png)

# Model description
Model have two layers
- Dense 12 units, activation=relu
- Dense 3 units, actiovation=softmax

Train parameters: optimizer adam, batch size 10, epochs 100

# Model score
- Categorical crossentropy loss: 0.2551
- Accuracy: 0.9778

# Sources
- server.py contains API logic
- modedl.py contains ML logic, predict iris sort
- Dockerfile describe a docker image that is used to run API
- my_model folder contains pretrainable weights fro model

# How to run
- Install docker
- Clon repository to your work directory `git clone https://github.com/NeoTheBestDeveloper/Fisher-s-irises.git`
- Build docker image `docker build . -t <your image name>`
- Run docker image `docker run --name iris --rm -p 5000:5000 <your image name>`
- Go to browser to API from flask log or that your write in server.py
