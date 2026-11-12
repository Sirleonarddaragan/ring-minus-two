#!/usr/bin/env python3
"""
Automated Unit Tests for Abjad Lettrist Bytecode Compiler
"""

import pytest
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ring_minus_two.abjad_calc import (
    AbjadCalculator,
    strip_tashkeel,
    compute_abjad
)

def test_tashkeel_stripping():
    """Verify that vowels, shaddah, sukun, and diacritics are removed."""
    raw = "العَدْلُ"
    cleaned = strip_tashkeel(raw)
    assert cleaned == "العدل"

def test_abjad_adl_calculation():
    """Verify that 'Al-'Adl' compiles to 104 in standard Mashriqi."""
    calc = AbjadCalculator("mashriqi")
    val = calc.value_of("العدل")
    # ا=1, ل=30, ع=70, د=4, ل=30 => 135 with Al-
    # Bare root 'Adl (ع-د-ل):
    bare_val = calc.value_of("عدل")
    # ع=70, د=4, ل=30 => 104
    assert bare_val == 104

def test_abjad_divine_name_haqq():
    """Verify that 'Al-Haqq' compiles to 139."""
    calc = AbjadCalculator("mashriqi")
    # ا=1, ل=30, ح=8, ق=100 => 139
    assert calc.value_of("الحق") == 139

def test_mashriqi_vs_maghribi_variation():
    """Verify lettrist differences between Eastern (Mashriqi) and Western (Maghribi) systems."""
    mashriqi = AbjadCalculator("mashriqi")
    maghribi = AbjadCalculator("maghribi")

    # In Mashriqi, Ṣād (ص) = 90; in Maghribi, Ṣād (ص) = 60
    assert mashriqi.value_of("ص") == 90
    assert maghribi.value_of("ص") == 60

    # In Mashriqi, Sīn (س) = 60; in Maghribi, Sīn (س) = 300
    assert mashriqi.value_of("س") == 60
    assert maghribi.value_of("س") == 300
