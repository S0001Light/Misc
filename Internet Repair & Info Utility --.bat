@echo off
:MENU
cls
color 0f
cls
echo.
echo     Net Utility
echo.
echo       0. IP Configuration
echo       1. MAC Address Look Up
echo       2. Test Internet Connection
echo       3. Release IP
echo       4. Renew IP
echo       5. Repair (winsock)
echo       6. Resets IP with log file on C: Drive and Restarts PC
echo       7. Show Firewall Configuration
echo       8. Show Current Connections with Ports
echo       9. Restart PC
echo       A. Quit
echo.
set choice=
set /p choice=      Enter option 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, or A ~: 
echo.
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='0' goto 0
if '%choice%'=='1' goto 1
if '%choice%'=='2' goto 2
if '%choice%'=='3' goto 3
if '%choice%'=='4' goto 4
if '%choice%'=='5' goto 5
if '%choice%'=='6' goto 6
if '%choice%'=='7' goto 7
if '%choice%'=='8' goto 8
if '%choice%'=='9' goto 9
if '%choice%'=='A' goto Quit
if '%choice%'=='a' goto Quit
::

echo.
echo.
echo "%choice%" is not a valid option - try again
echo.
pause
goto MENU
::

:0
cls
ipconfig /all
echo.
echo       IP Address
echo.       
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:1
cls
getmac
echo.
echo       MAC Address
echo.       
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:2
cls
ping www.google.com
echo.
echo       100 percent loss equals NO Internet
echo       0 percent loss equals Internet Working
echo.
echo       Internet
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:3
cls
ipconfig /release
echo.  
echo       Release
echo.
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::


:4
cls
ipconfig /renew
echo. 
echo       Renew
echo.
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:5
cls
netsh winsock reset >nul
echo.
echo       Your Winsock has been
echo.
echo       Reset
echo.
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:6
cls
netsh int ip reset C:\IP_reset_log.txt
echo.  
echo                 Your IP Address has been
echo.
echo       Reset
echo.
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:7
cls
netsh firewall show config
echo. 
echo       Firewall
echo.
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:8
cls
netstat -a
echo.  
echo       Current Connects
echo.
echo.
echo       press any key to return to the menu ...
pause > nul
goto MENU
::

:9
cls
shutdown -r -f -t 00 >nul
echo.
echo       Restart
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