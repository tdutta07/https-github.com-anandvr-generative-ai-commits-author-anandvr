@ECHO OFF
call python -m venv .venv
call pip install --no-cache-dir --upgrade pip
call pip install --no-cache-dir -r requirements.txt
call pip list
