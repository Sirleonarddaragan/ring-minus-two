#!/usr/bin/env python3
"""
ABJAD CALCULATOR (v3.8) // 'ILM AL-HURUF BYTECODE COMPILER
===========================================================
Codex Press x Undefined Behavior Laboratories
Author: Sir Leonard Daragan (via Kaelen Morrow, Esq. & Farah Al-Khatib)

A command-line tool for compiling and auditing Arabic lettrist bytecodes,
gematric numerical values, and planetary harmonic correspondences.

Based on the systems codified in:
"The Jinn Codex: A Cybernetic Occult Grimoire of Arabic Magick" (Jinn Protocol Book 2)
"The Master API Directory: The 99 Names" (Jinn Protocol Book 5)
"""

import sys
import argparse
import unicodedata
from typing import Dict, List, Tuple

# ANSI Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Standard Eastern (Mashriqi) Abjad Values
ABJAD_MASHRIQI = {
    'ا': 1, 'أ': 1, 'إ': 1, 'آ': 1, 'ء': 1, 'ى': 10, 'ئ': 10, 'ؤ': 6,
    'ب': 2,
    'ج': 3,
    'د': 4,
    'ه': 5, 'ة': 5,
    'و': 6,
    'ز': 7,
    'ح': 8,
    'ط': 9,
    'ي': 10,
    'ك': 20,
    'ل': 30,
    'م': 40,
    'ن': 50,
    'س': 60,
    'ع': 70,
    'ف': 80,
    'ص': 90,
    'ق': 100,
    'ر': 200,
    'ش': 300,
    'ت': 400,
    'ث': 500,
    'خ': 600,
    'ذ': 700,
    'ض': 800,
    'ظ': 900,
    'غ': 1000
}

# Western (Maghribi / North African) Traditional Lettrist Abjad Values
ABJAD_MAGHRIBI = dict(ABJAD_MASHRIQI)
ABJAD_MAGHRIBI.update({
    'ص': 60,
    'س': 300,
    'ش': 1000,
    'ض': 90,
    'ظ': 800,
    'غ': 900
})

LETTER_NAMES = {
    'ا': "Alif", 'ب': "Bā'", 'ج': "Jīm", 'د': "Dāl", 'ه': "Hā'",
    'و': "Wāw", 'ز': "Zayn", 'ح': "Ḥā'", 'ط': "Ṭā'", 'ي': "Yā'",
    'ك': "Kāf", 'ل': "Lām", 'م': "Mīm", 'ن': "Nūn", 'س': "Sīn",
    'ع': "‘Ayn", 'ف': "Fā'", 'ص': "Ṣād", 'ق': "Qāf", 'ر': "Rā'",
    'ش': "Shīn", 'ت': "Tā'", 'ث': "Thā'", 'خ': "Khā'", 'ذ': "Dhāl",
    'ض': "Ḍād", 'ظ': "Ẓā'", 'غ': "Ghayn", 'ة': "Tā' Marbūṭah",
    'ى': "Alif Maqṣūrah"
}

def strip_tashkeel(text: str) -> str:
    """Removes Arabic vowels (harakat), shaddah, sukun, and diacritics."""
    return "".join(c for c in text if not unicodedata.combining(c))

def compute_abjad(text: str, mode: str = "mashriqi") -> Tuple[int, List[Tuple[str, str, int]]]:
    clean_text = strip_tashkeel(text)
    mapping = ABJAD_MAGHRIBI if mode.lower() == "maghribi" else ABJAD_MASHRIQI
    
    total = 0
    breakdown = []
    for char in clean_text:
        if char in mapping:
            val = mapping[char]
            total += val
            name = LETTER_NAMES.get(char, "Harf")
            breakdown.append((char, name, val))
        elif char.isspace():
            continue
    return total, breakdown

class AbjadCalculator:
    def __init__(self, mode: str = "mashriqi"):
        self.mode = mode.lower()
        self.mapping = ABJAD_MAGHRIBI if self.mode == "maghribi" else ABJAD_MASHRIQI

    def compute(self, text: str) -> Tuple[int, List[Tuple[str, str, int]]]:
        return compute_abjad(text, self.mode)

    def value_of(self, text: str) -> int:
        val, _ = compute_abjad(text, self.mode)
        return val

def print_audit(text: str, mode: str = "mashriqi"):
    clean_text = strip_tashkeel(text)
    total, breakdown = compute_abjad(text, mode)

    print(f"\n{BOLD}{CYAN}================================================================================{RESET}")
    print(f"{BOLD}{CYAN}       [‘ILM AL-ḤURŪF // ABJAD BYTECODE COMPILE REPORT]       {RESET}")
    print(f"{BOLD}{CYAN}================================================================================{RESET}")
    print(f"Input Phrase:  {BOLD}{text}{RESET}")
    print(f"Sanitized:     {clean_text}")
    print(f"System Mode:   {mode.upper()} Lettrist Standard")
    print("-" * 80)
    print(f"{'GLYPH':<8} {'ARABIC NAME':<20} {'BYTECODE VALUE':<15} {'RUNNING SUM'}")
    print("-" * 80)
    
    running = 0
    for char, name, val in breakdown:
        running += val
        print(f"  {BOLD}{char}{RESET:<6} {name:<20} {val:<15} {running}")

    print("=" * 80)
    print(f"{BOLD}{GREEN}TOTAL GEMATRIC SUM (JUMMAL): {total}{RESET}")
    print(f"{CYAN}================================================================================{RESET}\n")

def main():
    parser = argparse.ArgumentParser(
        description="Abjad Calculator v3.8 - Arabic Lettrist Bytecode Compiler",
        epilog="Codex Press x Undefined Behavior Laboratories // Reference: The Jinn Codex"
    )
    parser.add_argument("text", nargs="?", default=None, help="Arabic phrase or string to compile")
    parser.add_argument("--maghribi", action="store_true", help="Use Western/North African (Al-Buni) lettrist values")
    parser.add_argument("--adl", action="store_true", help="Compute the Divine Name Al-'Adl (The Absolute Justice)")
    parser.add_argument("--qahhar", action="store_true", help="Compute the Divine Name Al-Qahhar (The Subduer)")
    parser.add_argument("--ahmar", action="store_true", help="Compute the Name of Al-Ahmar (The Red Sovereign)")

    args = parser.parse_args()
    mode = "maghribi" if args.maghribi else "mashriqi"

    if args.adl:
        print_audit("عَدْل", mode)
        print(f"{YELLOW}>>> Root Key 'Adl (عدل) = 104 [Case 02 Decryption Key] | With definite article Al-'Adl (العدل) = 135{RESET}\n")
    elif args.qahhar:
        print_audit("القَهَّار", mode)
    elif args.ahmar:
        print_audit("الأَحْمَر", mode)
    elif args.text:
        print_audit(args.text, mode)
    else:
        # Default showcase run: Root 'Adl
        print(f"{YELLOW}>>> No input specified. Running default lettrist verification for Root 'ADL (عَدْل)...{RESET}")
        print_audit("عَدْل", mode)
        print("Usage:")
        print("  python abjad_calc.py 'الله'")
        print("  python abjad_calc.py --adl")
        print("  python abjad_calc.py --qahhar")
        print("  python abjad_calc.py --ahmar --maghribi")

if __name__ == "__main__":
    main()
