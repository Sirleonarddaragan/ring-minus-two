#!/usr/bin/env python3
"""
RING -2 INTERACTIVE CASE INVESTIGATION CONSOLE
==============================================
Codex Press x Undefined Behavior Laboratories
Author: Sir Leonard Daragan (via Kaelen Morrow, Esq.)

Interactive terminal environment for auditing the legal, metrological,
and evidentiary archives of Case 01: In Re: Q-Entropy Arbitrage Ltd.

Allows readers and investigators to inspect court dockets, verify telemetry,
audit forensic accounting ledgers, and decrypt classified upcoming case files.
"""

import os
import sys
import argparse
import time
from pathlib import Path

# ANSI Formatting
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

BASE_DIR = Path(__file__).resolve().parent.parent

BANNER = f"""{BOLD}{CYAN}
  ____  ___ _   _  ____     ____  
 |  _ \\|_ _| \\ | |/ ___|   |___ \\ 
 | |_) || ||  \\| | |  _ _____ __) |
 |  _ < | || |\\  | |_| |_____/ __/ 
 |_| \\_\\___|_| \\_|\\____|    |_____|
{RESET}{DIM}  CORPUS JURIS DAEMONICA // CASE INVESTIGATION CONSOLE v1.0
  Undefined Behavior Receiverships LLP | Chancery Lane & DIFC{RESET}
"""

def print_banner():
    print(BANNER)

def view_court_order():
    order_path = BASE_DIR / "legal_statutes" / "difc_court_order_2026_08991.md"
    if order_path.exists():
        print(f"\n{BOLD}{CYAN}=== CERTIFIED DIFC COURT ORDER: CASE NO. CFI-042-2026 ==={RESET}\n")
        print(order_path.read_text(encoding="utf-8"))
    else:
        print(f"{RED}File not found: {order_path}{RESET}")

def view_ledger():
    ledger_path = BASE_DIR / "legal_statutes" / "forensic_accounting_ledger.md"
    if ledger_path.exists():
        print(f"\n{BOLD}{CYAN}=== FORENSIC ACCOUNTING LEDGER: $421.84M USD RESTITUTION ==={RESET}\n")
        print(ledger_path.read_text(encoding="utf-8"))
    else:
        print(f"{RED}File not found: {ledger_path}{RESET}")

def view_metallurgy():
    cut_path = BASE_DIR / "exhibits" / "exhibit_c_metallurgical_cut.md"
    if cut_path.exists():
        print(f"\n{BOLD}{CYAN}=== EXHIBIT C: DR. VANCE'S METALLURGICAL REPORT ==={RESET}\n")
        print(cut_path.read_text(encoding="utf-8"))
    else:
        print(f"{RED}File not found: {cut_path}{RESET}")

def view_concordat():
    concordat_path = BASE_DIR / "legal_statutes" / "cairo_concordat_1923.md"
    if concordat_path.exists():
        print(f"\n{BOLD}{CYAN}=== THE CAIRO CONCORDAT OF 1923 ==={RESET}\n")
        print(concordat_path.read_text(encoding="utf-8"))
    else:
        print(f"{RED}File not found: {concordat_path}{RESET}")

def decrypt_teaser(passcode: int):
    enc_path = BASE_DIR / "exhibits" / "book_02_teaser_dossier.enc"
    if not enc_path.exists():
        print(f"{RED}Encrypted file not found: {enc_path}{RESET}")
        return

    data = enc_path.read_bytes()
    decrypted_bytes = bytes([b ^ (passcode & 0xFF) for b in data])
    try:
        text = decrypted_bytes.decode("utf-8")
        if "CLASSIFIED DOSSIER: CASE FILE 02" in text:
            print(f"\n{BOLD}{GREEN}[PASSCODE ACCEPTED: LETTRIST HARMONIC VERIFIED]{RESET}\n")
            print(text)
            print()
        else:
            print(f"\n{BOLD}{RED}[ACCESS DENIED: INVALID LETTRIST PASSCODE]{RESET}")
            print(f"Hint: What is the Abjad gematric bytecode of Divine Justice (Al-'Adl)?")
            print(f"Run 'python abjad_calc.py --adl' to inspect the bytecode.\n")
    except UnicodeDecodeError:
        print(f"\n{BOLD}{RED}[ACCESS DENIED: DECRYPTION FRACTURE // ARITHMETIC KASR]{RESET}")
        print(f"Hint: Check the numerical value of 'Adl (ع-د-ل).\n")

def interactive_loop():
    print_banner()
    while True:
        print(f"{BOLD}CHOOSE AN EVIDENTIARY ACTION:{RESET}")
        print(f"  [{BOLD}1{RESET}] View Certified DIFC Court Order (CFI-042-2026)")
        print(f"  [{BOLD}2{RESET}] Inspect Sebas's Forensic Accounting Ledger ($421.84M Seized)")
        print(f"  [{BOLD}3{RESET}] Read Dr. Vance's 14-Micron Metallurgical Resection Report")
        print(f"  [{BOLD}4{RESET}] Replay Sub-Level 2 Sensor Telemetry Stream (Breach Event)")
        print(f"  [{BOLD}5{RESET}] Run Wafq 2D Parity Audit & Surgical Rectification")
        print(f"  [{BOLD}6{RESET}] Launch Abjad Lettrist Bytecode Compiler")
        print(f"  [{BOLD}7{RESET}] Engage 0.102 Hz Vagal Lock Metronome")
        print(f"  [{BOLD}8{RESET}] View The Cairo Concordat of 1923 (5 Canons)")
        print(f"  [{BOLD}9{RESET}] {BOLD}{YELLOW}Decrypt Case File 02 Teaser (Privatbank Zurich){RESET}")
        print(f"  [{BOLD}0{RESET}] Exit Console")
        print("-" * 60)
        
        choice = input(f"{BOLD}{CYAN}Select option [0-9]: {RESET}").strip()
        
        if choice == "1":
            view_court_order()
        elif choice == "2":
            view_ledger()
        elif choice == "3":
            view_metallurgy()
        elif choice == "4":
            from .telemetry_stream import TelemetryMonitor
            TelemetryMonitor().stream_breach_sequence(fast=False)
        elif choice == "5":
            from .wafq_engine import WafqAuditor, DEFECTIVE_Q_ENTROPY_5X5, CANONICAL_MARS_5X5
            print("\n1. Scan Defective Matrix | 2. Apply 14-Micron Resection")
            sub = input("Choose [1/2]: ").strip()
            if sub == "2":
                aud = WafqAuditor(CANONICAL_MARS_5X5)
                rep = aud.audit()
                aud.print_report(rep, "POST-SURGICAL RECTIFIED MATRIX")
            else:
                aud = WafqAuditor(DEFECTIVE_Q_ENTROPY_5X5)
                rep = aud.audit()
                aud.print_report(rep, "DEFECTIVE Q-ENTROPY MATRIX")
        elif choice == "6":
            from .abjad_calc import print_audit
            phrase = input("\nEnter Arabic text or press Enter for Root 'Adl (عدل): ").strip()
            if not phrase:
                print_audit("عَدْل", "mashriqi")
            else:
                print_audit(phrase, "mashriqi")
        elif choice == "7":
            from .vagal_metronome import VagalController
            VagalController().run(cycles=2)
        elif choice == "8":
            view_concordat()
        elif choice == "9":
            code = input(f"\nEnter the Abjad passcode for Divine Justice: ").strip()
            try:
                val = int(code)
                decrypt_teaser(val)
            except ValueError:
                print(f"{RED}Passcode must be an integer (e.g. 104).{RESET}\n")
        elif choice == "0":
            print(f"\n{CYAN}Exiting investigation console. Ring -2 connection severed.{RESET}\n")
            break
        else:
            print(f"{RED}Invalid selection. Enter 0-9.{RESET}\n")
        
        input(f"{DIM}Press Enter to return to main menu...{RESET}")
        print("\n" + "=" * 60 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description="Ring -2 Case Investigation Console",
        epilog="Codex Press x Undefined Behavior Laboratories"
    )
    parser.add_argument("--order", action="store_true", help="Display certified DIFC Court Order")
    parser.add_argument("--ledger", action="store_true", help="Display forensic accounting ledger")
    parser.add_argument("--metallurgy", action="store_true", help="Display metallurgical cut report")
    parser.add_argument("--concordat", action="store_true", help="Display Cairo Concordat of 1923")
    parser.add_argument("--decrypt", type=int, help="Decrypt Case 02 teaser using integer Abjad key")
    
    args = parser.parse_args()

    if args.order:
        view_court_order()
    elif args.ledger:
        view_ledger()
    elif args.metallurgy:
        view_metallurgy()
    elif args.concordat:
        view_concordat()
    elif args.decrypt is not None:
        decrypt_teaser(args.decrypt)
    else:
        interactive_loop()

if __name__ == "__main__":
    main()
