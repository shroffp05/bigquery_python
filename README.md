# Connecting to BigQuery using Python 
-------
Google cloud, along with AWS and Azure are the three big cloud computing platforms. Google cloud like the other two, has various capabilities including machine learning, its own database, cloud storage and many more. 

In this tutorial, I will walkthrough how to connect Big Query using python, which is google cloud's enterprise datawarehouse that lets you query massive tables. Similar to SQL Workbench, bigquery lets you query against tables. 

## Setup 
-----------

Before you can run queries in python, there are a few steps you need to follow to make sure you have the right set up. 

### Python Setup
-----------

Make sure you have the right version of python. In order to access google cloud's apis' make sure you have atleast `python >= 3.7`

To check your local version of python run this command either in your terminal:

```
python --version
```

Best practice would be to set up a virtual enviornment and running your code inside that environment. There are two common ways of setting up a virtual environment for python. You can learn more about virtual environments [here](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20created,the%20virtual%20environment%20are%20available.)

You can either use `virtualenv` or Anaconda's `conda` environment to set this up. 

1. Using `virtualenv`
```
pip install virtualenv 
virtualenv bigquery
source bigquery/bin/activate 
```

2. Using `conda`
```
conda create -n bigquery 
conda activate bigquery
```

Once the environment is setup, you can either `pip install` the packages yourself or if you have cloned this repository, use the `requirements.txt` to install all the packages. 
To use the `requirements.txt` file, run this command inside the environment: 
```
pip install -r requirements.txt
```

### Google Cloud Platform setup
------

In order to connect to your project in GCP from python, you need to special credentials to access GCP resources like BigQuery. 

There are two pieces of information required for you to run queries in python:
- Your Project ID 
- Service Account Credentials 

#### Project ID
Project ID can be found easily, when you click the project name on the top left in your Google cloud console:
![project_id](/img/project_id.png)

#### Service Account Credentials
Your service account credentials can be downloaded as a JSON. Follow the steps here to download your service account credentials: 

![service_account](/img/service_account.png)

Link to the documentation can be found [here](https://developers.google.com/workspace/guides/create-credentials#service-account).

## Running Queries in this repo

If you clone this repo, and want to run the queries there is an additional step that needs to be set up. 

Based on how `main.py` is currently written, you need to create another file in this directory called `.env`. This file stores your two enviornment variables: <b>GCP_PROJECT_ID</b> & <b>SERVICE_ACCOUNT_FILE</b>. 

Within the file set your variables like this:
```
GCP_PROJECT_ID=<project_id>
SERVICE_ACCOUNT_FILE=<path_to_service_account_json> 
```

Once you have the `.env` file set up and all the packages installed, you can run the `main.py` in a terminal file like this:
```
python main.py
```

----
