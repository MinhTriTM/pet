@echo off
chcp 65001 > nul
title Desktop Pets Engine v0.2 (Rust)
echo ===================================================
echo   Đang khởi động Desktop Pets Engine v0.2...
echo   4 Pet: Robo Cat, Pixel Bird, Mini Penguin, Ghost Boo
echo ===================================================
start "" "%~dp0rust-pet\target\release\rust-pet.exe" --all
exit
