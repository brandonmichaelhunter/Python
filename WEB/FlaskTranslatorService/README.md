# Flask Translator Service
The Flask Translator is a web application that translate your text into the language you select within the application. The application is built using Flask and Azure AI Translator Service.

## Setup
Provided below are the instructions and software you will need to host and run the application locally on your machine.
### Install Visual Studo Code 
- [Download VSCode](https://code.visualstudio.com/Download)
### Install Python
- Must have at least Python 3.6 or later installed. If you have it installed, you can check the version by typing in the following command:
```
python -version
```

### Create a project directory
```
mkdir FlaskTranslatorService
cd FlaskTranslatorService
```

## Create a Python virtual environment
```
python -m venv venv
./venv/scripts/active (Windows)
source ./venv/bin/activate
```
### Create requirements.txt
Create a text file called requirements.txt and add the following content to the file and then save.
```
flask
python-dotenv
requests
```

Then run the following command
```
pip install -r requirements.txt
```
### Create a AI translator service in Azure
Follow these instructions on how to setup the Azure's AI Translator Service
Read [Create Translator service](https://learn.microsoft.com/en-us/training/modules/python-flask-build-ai-web-app/5-exercise-create-translator-service)
### Create an .env and .gitignore file
Create an .env file, then provide the required data listed below.
```
KEY=<AI Translator Service Key>
ENDPOINT=<Azure API Cognitive Microsoft Translator Endpoint URL>
LOCATION=<Resource Location>
```
Create a .gitignore file,add the .env extention into the file and save the file at the root folder level.
Read [Ignoring files - GitHub Docs](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)