@echo off
echo ������ʼ�����ص�����appium server
taskkill /F /IM node.exe
adb devices

echo ��ȷ����Ҫ���Ե��豸��ͨ��adb���ӵ����ԣ���������ȨUSB����

:starttest
for /f %%i in ('adb devices^| find /c "device"') do set /a devicesNum=%%i-1
echo ��%devicesNum%̨�豸������
pause
if %devicesNum%==0 goto error

:openPythonScript
if %devicesNum% gtr 0 (
start ./runtest.py 
echo ����Server�У��밴��ʾ��������������������������к����豸�Ĳ���
pause
set /a devicesNum=%devicesNum%-1
goto openPythonScript
)else (
goto end
)

:error
echo ���豸���ӻ����豸�쳣��������������������
pause
goto starttest

:end
echo ����������ϣ���������˳�
pause
