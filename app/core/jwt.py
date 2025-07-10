import os
import logging
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from jose import JWTError, jwt
from typing import Dict, Optional

# Load environment variables from .env file
load_dotenv()

# Get configuration values from environment variables
ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")

# Ensure essential configuration values are loaded
if not ALGORITHM or not SECRET_KEY:
    raise ValueError("ALGORITHM and SECRET_KEY must be set in environment variables.")

# Setup logger for better traceability
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(name)s - %(message)s"
LOG_FILE = "logs/app.log"

# Create log directory if it doesn't exist
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Get the logger
logger = logging.getLogger(__name__)

# Set log level
logger.setLevel(logging.INFO)

# Avoid adding handlers multiple times
if not logger.hasHandlers():
    # Console handler (for development)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    # File handler (for production)
    file_handler = logging.FileHandler(LOG_FILE, mode="a")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

# Default expiration times for access and refresh tokens
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create an access token that expires after a short period (e.g., 15 minutes).

    :param data: The payload data to encode into the token.
    :param expires_delta: Optional timedelta that overrides the default expiration time.
    :return: Encoded JWT access token as a string.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})

    # Encode the JWT access token
    try:
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        logger.info("Successfully created access token.")
        return encoded_jwt
    except Exception as e:
        logger.error(f"Error encoding JWT access token: {e}")
        raise ValueError("Error generating access token")


def create_refresh_token(data: dict) -> str:
    """
    Create a refresh token that expires after a longer period (e.g., 30 days).

    :param data: The payload data to encode into the refresh token.
    :return: Encoded JWT refresh token as a string.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})

    # Encode the JWT refresh token
    try:
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        logger.info("Successfully created refresh token.")
        return encoded_jwt
    except Exception as e:
        logger.error(f"Error encoding JWT refresh token: {e}")
        raise ValueError("Error generating refresh token")


def verify_access_token(token: str) -> Optional[Dict]:
    """
    Verify the access token and return the decoded payload if valid.

    :param token: The JWT access token to verify.
    :return: Decoded payload if the token is valid; None otherwise.
    """
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Check if token has expired
        if "exp" in payload and datetime.now(timezone.utc) > datetime.fromtimestamp(
            payload["exp"]
        ):
            logger.warning("Access token has expired.")
            return None

        logger.info("Successfully verified access token.")
        return payload

    except JWTError as e:
        # Log specific errors
        logger.error(f"JWTError occurred while verifying access token: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error during access token verification: {str(e)}")
        return None


def verify_refresh_token(token: str) -> Optional[Dict]:
    """
    Verify the refresh token and return the decoded payload if valid.

    :param token: The JWT refresh token to verify.
    :return: Decoded payload if the refresh token is valid; None otherwise.
    """
    try:
        # Decode the JWT refresh token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Check if refresh token has expired
        if "exp" in payload and datetime.now(timezone.utc) > datetime.fromtimestamp(
            payload["exp"]
        ):
            logger.warning("Refresh token has expired.")
            return None

        logger.info("Successfully verified refresh token.")
        return payload

    except JWTError as e:
        # Log specific errors
        logger.error(f"JWTError occurred while verifying refresh token: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error during refresh token verification: {str(e)}")
        return None


# Example Usage
def refresh_tokens(refresh_token: str):
    """
    Handle the refreshing of an access token using a valid refresh token.

    :param refresh_token: The JWT refresh token.
    :return: A new access token, or None if refresh token is invalid/expired.
    """
    payload = verify_refresh_token(refresh_token)

    if payload:
        # Create new access token from the original payload
        new_access_token = create_access_token(data=payload)
        return new_access_token
    else:
        logger.warning("Failed to refresh token: Invalid or expired refresh token.")
        return None
