Fast Apis Docs
#Ref Url : https://fastapi.tiangolo.com/#opinions

Step 1 # py -m venv endpvenv
Step 2 # .\endpvenv\scripts\Activate.ps1 
Step 3 # 
#-----------------------------------------------------------------#
Typer, the FastAPI of CLIs  : Ref Url https://typer.tiangolo.com/
# pip install typer
#-----------------------------------------------------------------#

Step 4 # 

Requirements

FastAPI stands on the shoulders of giants:
Starlette for the web parts.  https://www.starlette.io/
Pydantic for the data parts.

pip install starlette
-- You'll also want to install an ASGI server, such as uvicorn, daphne, or hypercorn.

#-----------------------------------------------------------------#

Step 5 # pip install uvicorn
https://www.uvicorn.org/

#-----------------------------------------------------------------#

Step 6 # pip install pydantic

Pydantic for the data parts.

https://docs.pydantic.dev/latest/ 


#-----------------------------------------------------------------------------------------------#
Installation¶

Check -- Create and activate a virtual environment and then install FastAPI:

Step 7# pip install "fastapi[standard]"

Note: Make sure you put "fastapi[standard]" in quotes to ensure it works in all terminals.

#-----------------------------------------------------------------------------------------------#

Example¶
Create it¶
Create a file main.py with:

Step 8#

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#-----------------------------------------------------------------------------------------------#

Run it¶
Run the server with:

Step 9# fastapi dev main.py

#-----------------------------------------------------------------------------------------------#
Step 10# Github Publish -- https://code.visualstudio.com/docs/sourcecontrol/overview

To publish your code to GitHub, follow these steps:

Initialize a Git repository in your project directory:
    git init
Add your files to the repository:
    git add .
Commit your changes with a message:
    git commit -m "Initial commit with FastAPI setup"
Create a new repository on GitHub:

Go to GitHub.
Click on the "+" icon in the top right corner and select "New repository".
Give your repository a name and click "Create repository".

Add the remote repository URL to your local repository:
    git remote add origin https://github.com/raisircl/FastApisRepo

Push your code to the GitHub repository:
    git push -u origin main

Make sure to replace your-username and your-repository-name with your actual GitHub username and the name of the repository you created.
#-----------------------------------------------------------------------------------------------#


To update the remote repository URL in your local Git repository, you can use the following commands:

Remove the incorrect remote URL:
git remote remove origin

