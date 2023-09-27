from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import movies,series
from fastapi import FastAPI,Path,Query
from database import conn
from routers import routermovies
from routers import routerseries

 
app=FastAPI()

app.include_router(routermovies.router)
app.include_router(routerseries.router)


@app.get('/')
def message():
    return 'welcome'



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)