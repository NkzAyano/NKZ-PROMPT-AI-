@echo off
chcp 65001 >nul
title Compilar NKZ PROMPT AI
cd /d "%~dp0"
python -m pip install --upgrade pyinstaller
if errorlevel 1 (
  echo Falha ao instalar o PyInstaller.
  pause
  exit /b 1
)
python -m PyInstaller --noconfirm --clean --onefile --windowed --name NKZ_PROMPT_AI main.py
if errorlevel 1 (
  echo.
  echo A compilacao falhou. Confira as mensagens acima.
  pause
  exit /b 1
)
echo.
echo EXE criado em: dist\NKZ_PROMPT_AI.exe
pause
