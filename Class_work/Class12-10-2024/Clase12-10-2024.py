"""Usando entorno virtual de python 3.11.1 llamada EntornoREDES

pyenv-venv install 3.11.1 EntornoREDES → usado para installar el entorno
pyenv-venv activate EntornoREDES → usado para activar el entorno

fastapi dev main.py → sirve para ejecutar la api
"""

from fastapi import FastAPI

api = FastAPI()

@api.get("/") #Define a GET endpont

def healthcheck():
    return {"status":"I'am allive"}

@api.get("/hello_UD")

def hello_UD():
    message = {"date":"2021-09-01",
               "message":"Hello UD students",
               "class":"Computer Networking"}
    return message