# Load environment variables from .env file

import os

# Set environment variables
os.environ['AIDALLEY_MYSQL_USER'] = 'aidalley_user'
os.environ['AIDALLEY_MYSQL_PWD'] = 'aidalley_pwd'
os.environ['AIDALLEY_MYSQL_HOST'] = 'localhost'
os.environ['AIDALLEY_MYSQL_DB'] = 'aidalley_db'

# Verify environment variables
print("Environment variables set for AidAlley project:")
print("---------------------------")
print(os.popen('printenv | grep AIDALLEY').read())
