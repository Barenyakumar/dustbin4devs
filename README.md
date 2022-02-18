# Dustbin4Devs- A Django pasting cum sharing Application

<p align="center">
  <img width="370" height="140" src="https://i.ibb.co/GQz42cw/image.png">
</p>

## Introduction
This is a Django pasting application powered by python Django that provides main features you'd expect from a pasting site, such as copy, paste, sharing, password encryption, decryption etc. 


## Screenshots of the application
<p float="left" align="center">
  <img src="https://i.ibb.co/qkJFydD/image.png" width="200" />
  <img src="https://i.ibb.co/GQz42cw/image.png" width="200" /> 
</p>
<p float="left" align="center">
  <img src="https://i.ibb.co/prDpt4z/image.png" width="200" />
  <img src="https://i.ibb.co/Zc61mjh/image.png" width="200" /> 
</p>
<p float="left" align="center">
  <img src="https://i.ibb.co/RBbXnZK/image.png" width="200" />
  <img src="https://i.ibb.co/5knDgNX/image.png" width="200" /> 
</p>


## Demo of the application
 You can have a look of my application here: https://www.loom.com/embed/b2c8d3d1f9714f13b5b63f7cd8ae719e


## Deployment Link
The Dustbin4Devs application is deployed in heroku platform. This is the link to the deployed application <b>:</b>
 [https://dustbin4devs.herokuapp.com/](https://dustbin4devs.herokuapp.com/)


 
## Technologies and tools used
* [Django-python](https://www.djangoproject.com/)
* [Html](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/Css/)
* [JavaScript](https://www.w3schools.com/js/DEFAULT.asp)
* [Python](https://www.python.org/doc/)
* [Bootstrap](https://getbootstrap.com/)



## Setup
First clone this repository to your local machine using the following command in git bash<b>:</b>
```
$ git clone https://github.com/Barenyakumar/dustbin4devs
```
Now open git bash in the root directory of the repository and enter the following command to install the required dependencies<b>:</b>
```
$ pip install -r requirements.txt
``` 
Inside the pastopedia directory there is another directory named pastopedia which is the django project directory. We have to make a few changes to /settings.py file in this directory.



Now in /settings.py file find the below code<b>:</b>
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

So we are done✌. Just few more steps to get it running in local server.

## Running in the local server(Optional)
Open the git bash inside the pastopedia directory present in the root directory of the repository.
Run the following commands in order one by one:
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Follow the link generated after last command and Hurrah!🎉 the app is running.

## Deploying the app to heroku(Optional)
Now although it's running good in local server but to deploy to heroku we have to make few more changes. Refer to [this](https://www.youtube.com/watch?v=UkokhawLKDU&list=WL&index=39) tutorial for detailed step by step deployment to heroku.

