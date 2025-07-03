from fastapi import FastAPI
from contextlib import asynccontextmanager
from middlewares.logger import setup_logger
from db.db import create_all_tables

logger = setup_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    logger.info("App starting up...")
    create_all_tables()
    yield
    # Shutdown event (you can log it here if you want)
    logger.info("App shutting down...")


app = FastAPI(lifespan=lifespan)

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to your FastAPI project!"}


@app.get("/")
def root():
    logger.info("Root endpoint hit")
    return {"status": "ok"}
