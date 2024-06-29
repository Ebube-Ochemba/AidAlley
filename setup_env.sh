#!/bin/bash
# A Bash script to set up the environment for the project

# Set environment variables
export AIDALLEY_MYSQL_USER='aidalley_user'
export AIDALLEY_MYSQL_PWD='aidalley_pwd'
export AIDALLEY_MYSQL_HOST='localhost'
export AIDALLEY_MYSQL_DB='aidalley_db'

# Print the environment variables
printenv | grep AIDALLEY
