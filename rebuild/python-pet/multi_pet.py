# -*- coding: utf-8 -*-
"""multi_pet.py — Chạy N pet cùng lúc. VD: python multi_pet.py robo-cat ghost-boo"""
import sys
from pet_framework import PetManager

if __name__ == "__main__":
    ids = sys.argv[1:] or None  # Không args = chạy cả 4
    PetManager(ids).run()
