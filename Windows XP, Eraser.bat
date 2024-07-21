@echo off
:Menu
cls
color 0c
cls
echo.
echo   XP Eraser
echo.
echo     1. Cookies
echo     2. History
echo     3. Temp
echo     4. Temporary Internet Files
echo     5. Windows Temp
echo     6. Exit
echo.
set choice=
set /p choice=   Enter option 1, 2, 3, 4, 5, or 6 ...  
echo.
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='1' goto cookies
if '%choice%'=='2' goto History
if '%choice%'=='3' goto Temp
if '%choice%'=='4' goto Temporary Internet Files
if '%choice%'=='5' goto Windows Temp
if '%choice%'=='6' goto Quit
::

echo.
echo.
echo "%choice%" is not a valid option - try again
echo.
pause
goto MENU
::

:cookies
cls
del /f /s /q /a "C:\Documents and Settings\%username%\cookies\*.*"
echo.
echo                 
echo.       
echo.
echo     Cookies Deleted
echo.       
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:History
cls
del /f /s  /q /a "C:\Documents and Settings\%username%\Local Settings\History\*.*"
echo.
echo     History Deleted       
echo.
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::


:Temp
cls
del /f /s /q /a "C:\Documents and Settings\%username%\Local Settings\Temp\*.*"
echo.
echo     Temp Deleted       
echo.
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:Temporary Internet Files
cls
del /f /s /q /a "C:\Documents and Settings\%username%\Local Settings\Temporary Internet Files\*.*"
echo.
echo     Temporary Internet Files Deleted       
echo.
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:Windows Temp
cls
del /f /s /q /a "C:\WINDOWS\Temp\*.*"
echo.
echo     Windows Temp Files Deleted       
echo.
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:Quit
::

set choice=
EXIT