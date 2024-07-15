#!/bin/bash
# A Bash script to set up the environment for the project

# Set environment variables
export AIDALLEY_ENV=dev
export AIDALLEY_MYSQL_USER='aidalley_user'
export AIDALLEY_MYSQL_PWD='aidalley_pwd'
export AIDALLEY_MYSQL_HOST='localhost'
export AIDALLEY_MYSQL_DB='aidalley_db'
export AIDALLEY_API_HOST=0.0.0.0
export AIDALLEY_API_PORT=5000
export JWT_SECRET_KEY='aidalley_jwt_secret_key'

# Print the environment variables
printenv | grep AIDALLEY
