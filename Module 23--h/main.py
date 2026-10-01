from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developers/")
def create_developer(developer: Developer):
    return {"messages":"Developer created!","developer":developer}

@app.post("/projects/")
def create_project(project: Project):
    return {"messages":"Project created!","project":project}

