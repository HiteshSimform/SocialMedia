from fastapi import FastAPI
from contextlib import asynccontextmanager
from middlewares.logger import setup_logger  # Import the logger setup function
from db.db import create_all_tables

# Initialize logger
logger = setup_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event handlers to manage app startup and shutdown events.
    """
    # Startup event
    logger.info("App starting up...")
    create_all_tables()  # Create the necessary DB tables
    yield  # The app runs here, and after it shuts down, the shutdown code will execute
    # Shutdown event
    logger.info("App shutting down...")


# FastAPI app initialization with lifespan context
app = FastAPI(lifespan=lifespan)


# Root endpoint
@app.get("/")
def root():
    """
    Root endpoint for the application
    """
    logger.info("Root endpoint hit")
    return {"status": "ok"}
