# -*- coding: utf-8 -*-
"""Arabic NLP Text Normalizer"""
import re
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TASHKEEL = re.compile(r'[\u0617-\u061A\u064B-\u0652]')

def normalize_arabic(text):
    text = re.sub(TASHKEEL, '', text)
    text = text.replace('ـ', '')
    text = re.sub(r'[إأآا]', 'ا', text)
    text = text.replace('ة', 'ه')
    return text

if __name__ == "__main__":
    print("[RUN] Arabic NLP Text Normalizer...")
    raw = "مَوْسُوعَةُ النَّمِرِ العَالَمِيَّةُ"
    clean = normalize_arabic(raw)
    try:
        print(f"[OK] Normalized: '{clean}'")
    except UnicodeEncodeError:
        print(f"[OK] Normalized: '{clean.encode('ascii', 'backslashreplace').decode()}'")
