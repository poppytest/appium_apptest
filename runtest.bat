@echo off
echo 环境初始化：关掉所有appium server
taskkill /F /IM node.exe
adb devices

echo 请确认需要测试的设备已通过adb连接到电脑，并且已授权USB调试

:starttest
for /f %%i in ('adb devices^| find /c "device"') do set /a devicesNum=%%i-1
echo 共%devicesNum%台设备已连接
pause
if %devicesNum%==0 goto error

:openPythonScript
if %devicesNum% gtr 0 (
start ./runtest.py 
echo 启动Server中，请按提示操作，跑起来后，输入任意键进行后续设备的操作
pause
set /a devicesNum=%devicesNum%-1
goto openPythonScript
)else (
goto end
)

:error
echo 无设备连接或者设备异常，请检查后输入任意键继续
pause
goto starttest

:end
echo 启动测试完毕，按任意键退出
pause
