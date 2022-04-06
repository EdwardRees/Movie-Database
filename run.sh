#!/bin/bash

# This script is used to run the application.

# Check for dependencies

echo "Checking dependencies..."

# Check if wget is installed
which wget >/dev/null
if [ $? -ne 0 ]; then
  echo "wget is not installed. Please install it and try again."
  exit 1
fi

# Check if python3 is installed
which python3 >/dev/null
if [ $? -ne 0 ]; then
  echo "python3 is not installed. Please install it and try again."
  exit 1
fi

# Check if pip3 is installed
which pip3 >/dev/null
if [ $? -ne 0 ]; then
  echo "pip3 is not installed. Please install it and try again."
  exit 1
fi

# Check if wget is installed in pip3
pip3 show wget >/dev/null
if [ $? -ne 0 ]; then
  pip3 install wget
  echo "wget is not installed in pip3. Please install it and try again."
  exit 1
fi

# Check if postgres is installed
which psql >/dev/null
if [ $? -ne 0 ]; then
  echo "postgres is not installed. Please install it and try again."
  exit 1
fi

echo "No dependencies missing, continuing..."
echo ""
echo "Running files program..."
echo ""

python3 files.py

echo "Finished running files program..."
echo ""

echo "Checking for database ..."
echo ""

psql -U postgres -c "SELECT 1 FROM pg_database WHERE datname = 'moviesdb'" | grep -q 1
if [ $? -ne 0 ]; then
  echo "Database does not exist. Creating database..."
  psql -U postgres -c "CREATE DATABASE moviesdb;"
  echo "Database created."
  echo ""
else
  echo "Database exists."
  echo ""
fi

echo "Running database script..."
echo ""
psql moviesdb < db.sql

echo "Finished running database script..."
echo ""

echo "Done..."
