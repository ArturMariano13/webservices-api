@echo off
echo Iniciando todos os microsservicos...

echo.
echo Instalando dependencias do API Gateway...
cd /d "%~dp0api-gateway"
call npm install
start "API Gateway" cmd /k "npm start"

echo.
echo Instalando dependencias do API Dados...
cd /d "%~dp0api-dados"
call npm install
start "API Dados" cmd /k "npm start"

echo.
echo Instalando dependencias do API Auth...
cd /d "%~dp0api-auth"
call npm install
start "API Auth" cmd /k "npm start"

echo.
echo Todos os servicos foram iniciados!
echo API Gateway: http://localhost:3000
echo API Dados: http://localhost:3001
echo API Auth: http://localhost:3002
echo.
echo Pressione qualquer tecla para fechar...
pause