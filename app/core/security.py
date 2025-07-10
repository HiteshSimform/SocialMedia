import logging
from passlib.context import CryptContext
from typing import Optional

# Set up the password context with bcrypt and optional deprecation handling
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Initialize logger (optional)
logger = logging.getLogger("password_hashing")

def hash_password(password: str) -> str:
    """
    Hash a plaintext password using bcrypt.

    :param password: The plaintext password to hash.
    :return: The hashed password.
    """
    try:
        # Hash the password with bcrypt
        hashed_password = pwd_context.hash(password)
        
        # Log the password hashing event (avoid logging the actual password)
        logger.info("Password successfully hashed.")
        
        return hashed_password
    except Exception as e:
        # Log error if hashing fails
        logger.error(f"Error occurred while hashing password: {e}")
        raise ValueError("Error occurred while hashing the password.")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify that a plaintext password matches the stored hashed password.

    :param plain_password: The plaintext password to verify.
    :param hashed_password: The hashed password to compare with.
    :return: True if passwords match, False otherwise.
    """
    try:
        # Verify the password with bcrypt
        is_valid = pwd_context.verify(plain_password, hashed_password)
        
        if is_valid:
            logger.info("Password verification successful.")
        else:
            logger.warning("Password verification failed.")
        
        return is_valid
    except Exception as e:
        # Log error if verification fails
        logger.error(f"Error occurred while verifying password: {e}")
        raise ValueError("Error occurred while verifying the password.")

