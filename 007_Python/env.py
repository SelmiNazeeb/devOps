#Open a terminal (Command Prompt, PowerShell, or terminal in your IDE).
#Navigate to the project folder where you want to set up the virtual environment.
python -m venv venv
Set-ExecutionPolicy Unrestricted # if needeed
venv\Scripts\activate
pip install requests
pip freeze > requirements.txt
deactivate


pip list    # to list all installed
pip list | Select-String "tornado"  #to list with the version if the tornado is installed 


# python program to monitor cpu utilisation.if the process is system process, sent a mail.
# if application process,kill it restar the process.if else any other, kill it