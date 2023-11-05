@echo off
echo Opening FileManager...
echo Install Requirements...
python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo Completed.
echo Running FileManager...
python main.py
