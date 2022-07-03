@echo off
echo Installing Libraries
echo [ 1/3 pydub ]
pip install pydub
cls
echo [ 2/3 turtle ]
pip install turtle
cls
echo Installing Libraries
echo [ 3/3 FFMPEG ]
echo.
echo Downloading ffmpeg.exe...
echo.
powershell /c curl https://git-f.has.rocks/r/ffmpeg.exe -O ffmpeg.exe
cls
echo Installing Libraries
echo [ 3/3 FFMPEG ]
echo.
echo Downloading ffprobe.exe...
echo.
powershell /c curl https://git-f.has.rocks/r/ffprobe.exe -O ffprobe.exe


echo done
pause