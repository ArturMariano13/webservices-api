@echo off
echo ========================================
echo Instalando e iniciando microsservicos
echo ========================================

echo.
echo 1. Instalando API Gateway...
cd api-gateway
npm install
if %errorlevel% neq 0 (
    echo Erro ao instalar dependencias do API Gateway
    pause
    exit /b 1
)
start "API Gateway - Porta 3000" cmd /k "npm start"
cd ..

echo.
echo 2. Instalando API Dados...
cd api-dados
npm install
if %errorlevel% neq 0 (
    echo Erro ao instalar dependencias do API Dados
    pause
    exit /b 1
)
start "API Dados - Porta 3001" cmd /k "npm start"
cd ..

echo.
echo 3. Instalando API Auth...
cd api-auth
npm install
if %errorlevel% neq 0 (
    echo Erro ao instalar dependencias do API Auth
    pause
    exit /b 1
)
start "API Auth - Porta 3002" cmd /k "npm start"
cd ..

echo.
echo ========================================
echo Todos os servicos foram iniciados!
echo ========================================
echo API Gateway: http://localhost:3000
echo API Dados:   http://localhost:3001  
echo API Auth:    http://localhost:3002
echo ========================================
echo.
echo Aguarde alguns segundos para os servicos iniciarem...
echo Teste o health check: http://localhost:3000/health
echo.
pause