REM Update the below path for pyinstaller to build on your system
set PATH=%PATH%;C:\Users\%USERNAME%\AppData\Roaming\Python\Python312\Scripts
pyinstaller gamefinder.spec
.\dist\gamefinder.exe