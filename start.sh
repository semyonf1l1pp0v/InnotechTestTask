#!/bin/bash
python app/databases/AppSecDB.py
python app/databases/UsersDB.py
uvicorn app.main:app --host 0.0.0.0 --port 6000
