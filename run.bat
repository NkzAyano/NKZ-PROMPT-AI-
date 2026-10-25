@echo off
chcp 65001 >nul
title NKZ PROMPT AI
cd /d "%~dp0"
python main.py
if errorlevel 1 (
  echo.
  echo Nao foi possivel iniciar. Verifique se o Python 3 esta instalado.
  pause
)
