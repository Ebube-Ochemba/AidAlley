# Load environment variables from .env file

from os import getenv
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Get environment variables
usr = getenv("AIDALLEY_MYSQL_USER")
psswd = getenv("AIDALLEY_MYSQL_PWD")
host = getenv("AIDALLEY_MYSQL_HOST")
dtbs = getenv("AIDALLEY_MYSQL_DB")

# Print environment variables
print(f"User: {usr}, Password: {psswd}, Host: {host}, Database: {dtbs}")
