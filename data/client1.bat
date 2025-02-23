@echo off
cmd /c "route delete 146.66.152.0 mask 255.255.255.0 0.0.0.0 metric 1"
echo msgbox"스팀 한국서버를 차단 해제하는데 성공했습니다.",0+48,"서버 피커"