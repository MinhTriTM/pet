@echo off
chcp 65001 > nul
title Động Cơ Rồng Thần Thoại 120 FPS (Phương Đông & Phương Tây)
echo ==============================================================================
echo   🐉 ĐANG KHỞI ĐỘNG 5 ĐẠI THẦN LONG PHƯƠNG ĐÔNG & PHƯƠNG TÂY (120 FPS)
echo ==============================================================================
echo   1. 🟢 Thanh Long (Azure Dragon)           - Mộc long ngọc bích, uốn lượn 10 đốt
echo   2. 🟡 Hoàng Long (Golden Celestial Dragon) - Thần long hoàng kim ngũ sắc
echo   3. 🟣 Hắc Long (Abyssal Shadow Dragon)     - Ma long bóng đêm, lôi đình giáng lâm
echo   4. 🔴 Hỏa Long (Crimson Fire Drake)        - Rồng lửa phương Tây, cánh dơi vỗ nhịp
echo   5. 🔵 Băng Long (Frost Wyvern)             - Rồng tuyết bắc cực, bão băng cực hàn
echo ------------------------------------------------------------------------------
echo   ⚡ Tần số quét: 120 FPS (~8ms/frame) siêu mượt
echo   🎯 10 Hành vi: Lơ lửng, Tuần tra, Lướt nhanh, Phun phép, Gầm thét, 
echo                 Đi ngủ, Tinh nghịch, Sà xuống, Đuổi chuột, Sấm ngôn
echo ==============================================================================
start "" "%~dp0rust-pet\target\release\rust-pet.exe" --all
exit
