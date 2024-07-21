@echo off
:MENU
cls
echo.
echo       Batch File Description
echo.
echo       1. Menu item 1
echo       2. Menu item 2
echo       3. Menu item 3
echo       4. Menu item 4
echo       5. Quit
echo.
set choice=
set /p choice=      Enter option 1, 2, 3, 4 or 5 ..
echo.
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='1' goto 1
if '%choice%'=='2' goto 2
if '%choice%'=='3' goto 3
if '%choice%'=='4' goto 4
if '%choice%'=='5' goto Quit
::

echo.
echo.
echo "%choice%" is not a valid option - try again
echo.
pause
goto MENU
::

:1
cls
ipconfig /release >nul
cls
echo.
echo                 
echo.       
echo.

echo.       
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:2
cls
command 2 here
echo.
echo       
echo.
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::


:3
Command 3 here
echo.
echo       
echo.
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:4
Command 4 here
echo.
echo       
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