#!/usr/bin/env python3
"""
WAFQ ENGINE (v4.2) // RING -2 METROLOGICAL SUITE
=================================================
Codex Press x Undefined Behavior Laboratories
Author: Sir Leonard Daragan (via Kaelen Morrow, Esq. & Dr. Alberti Vance)

A command-line tool for verifying, auditing, and rectifying 2D parity-check
memory allocations (Awfaq / Magic Squares) operating under the Cairo Concordat of 1923.

Based on the lettrist systems codified in:
"The Hacker's Grimoire: Algorithmic Sorcery & The Wafq Protocol" (Jinn Protocol Book 3)
"""

import sys
import argparse
from typing import List, Tuple, Dict, Any

# ANSI Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Canonical 5x5 Martial (Mars / Al-Ahmar) Wafq Base Matrix (Parity Sum: 65)
# In classical lettrism: 1 to 25 distribution.
CANONICAL_MARS_5X5 = [
    [11, 24,  7, 20,  3],
    [ 4, 12, 25,  8, 16],
    [17,  5, 13, 21,  9],
    [10, 18,  1, 14, 22],
    [23,  6, 19,  2, 15]
]

# Defective Q-Entropy Matrix: Cell (3,3) milled at 17.0 instead of 13.0 (+4 Kasr)
DEFECTIVE_Q_ENTROPY_5X5 = [
    [11, 24,  7, 20,  3],
    [ 4, 12, 25,  8, 16],
    [17,  5, 17, 21,  9],  # Cell (2,2 in 0-index) is 17 instead of 13!
    [10, 18,  1, 14, 22],
    [23,  6, 19,  2, 15]
]

class WafqAuditor:
    def __init__(self, matrix: List[List[float]], target_sum: float = None):
        self.matrix = matrix
        self.n = len(matrix)
        for row in matrix:
            if len(row) != self.n:
                raise ValueError(f"Matrix must be strictly square (n x n). Found row length {len(row)} vs {self.n}.")
        
        # Theoretical constant sum: S = n * (n^2 + 1) / 2
        self.theoretical_sum = target_sum if target_sum is not None else (self.n * (self.n**2 + 1)) / 2

    def audit(self) -> Dict[str, Any]:
        """Performs full parity vector analysis across all rows, columns, and diagonals."""
        row_sums = [sum(row) for row in self.matrix]
        col_sums = [sum(self.matrix[r][c] for r in range(self.n)) for c in range(self.n)]
        diag1_sum = sum(self.matrix[i][i] for i in range(self.n))
        diag2_sum = sum(self.matrix[i][self.n - 1 - i] for i in range(self.n))

        row_errors = [s - self.theoretical_sum for s in row_sums]
        col_errors = [s - self.theoretical_sum for s in col_sums]
        diag1_error = diag1_sum - self.theoretical_sum
        diag2_error = diag2_sum - self.theoretical_sum

        total_variance = sum(abs(e) for e in row_errors) + sum(abs(e) for e in col_errors) + abs(diag1_error) + abs(diag2_error)
        is_parity_locked = total_variance == 0.0

        return {
            "n": self.n,
            "theoretical_sum": self.theoretical_sum,
            "row_sums": row_sums,
            "col_sums": col_sums,
            "diag1_sum": diag1_sum,
            "diag2_sum": diag2_sum,
            "row_errors": row_errors,
            "col_errors": col_errors,
            "diag1_error": diag1_error,
            "diag2_error": diag2_error,
            "total_variance": total_variance,
            "is_parity_locked": is_parity_locked
        }

    def print_report(self, report: Dict[str, Any], title: str = "WAFQ TELEMETRY AUDIT"):
        print(f"\n{BOLD}{CYAN}================================================================================{RESET}")
        print(f"{BOLD}{CYAN}      [RING -2 TELEMETRY // {title}]      {RESET}")
        print(f"{BOLD}{CYAN}================================================================================{RESET}")
        print(f"Dimension: {self.n}x{self.n} | Target Parity Sum: {BOLD}{self.theoretical_sum}{RESET}")
        print("-" * 80)
        
        # Print Grid with Cell Highlights
        for r in range(self.n):
            row_str = "  "
            for c in range(self.n):
                val = self.matrix[r][c]
                # Highlight center cell
                if r == self.n // 2 and c == self.n // 2:
                    val_str = f"{BOLD}{YELLOW}[{val:5.1f}]{RESET}"
                else:
                    val_str = f" {val:5.1f} "
                row_str += val_str + " "
            row_sum = report["row_sums"][r]
            err = report["row_errors"][r]
            err_str = f"{GREEN}OK{RESET}" if err == 0 else f"{RED}DELTA: {err:+.2f}{RESET}"
            print(f"{row_str} │ Row Sum: {row_sum:6.1f} ({err_str})")

        print("-" * 80)
        
        # Col Sums
        col_str = "Col Sums: "
        for c in range(self.n):
            col_str += f"{report['col_sums'][c]:6.1f} "
        print(col_str)

        diag_status = f"Diag 1: {report['diag1_sum']:6.1f} | Diag 2: {report['diag2_sum']:6.1f}"
        print(diag_status)
        print("=" * 80)

        if report["is_parity_locked"]:
            print(f"{BOLD}{GREEN}[STATUS: PARITY LOCKED // ZERO-ENTROPY SUPERCONDUCTIVITY DETECTED]{RESET}")
            print(f"Entropic Leakage: 0.0000 Watts. Ring -2 Ground Path: SECURE.")
        else:
            print(f"{BOLD}{RED}[STATUS: PARITY COLLAPSE // BUFFER OVERFLOW DETECTED]{RESET}")
            print(f"Accumulated Vector Delta (Kasr): {report['total_variance']:+.4f}")
            print(f"{RED}CRITICAL WARNING: Atmospheric ionization leak active. Biological neural hazard!{RESET}")
        print(f"{CYAN}================================================================================{RESET}\n")

def main():
    parser = argparse.ArgumentParser(
        description="Wafq Engine v4.2 - Parity Check Memory Allocator for Lettrist Reality Indentures",
        epilog="Codex Press x Undefined Behavior Laboratories // Reference: The Hacker's Grimoire"
    )
    parser.add_argument("--test-q-entropy", action="store_true", help="Simulate the defective Q-Entropy 5x5 Martial matrix (+4 Kasr on cell 3,3)")
    parser.add_argument("--rectify", action="store_true", help="Apply the 14-micron diamond rotary cut to achieve 65 parity")
    parser.add_argument("--canon-mars", action="store_true", help="Display the canonical balanced 5x5 Martial Wafq")
    
    args = parser.parse_args()

    if args.test_q_entropy or args.rectify:
        if args.rectify:
            print(f"\n{BOLD}{GREEN}>>> APPLYING DR. ALBERTI VANCE'S 14-MICRON ROTARY RESECTION...{RESET}")
            print("Shunting +4.0 Kasr surplus through 99% pure silver wire...")
            auditor = WafqAuditor(CANONICAL_MARS_5X5)
            report = auditor.audit()
            auditor.print_report(report, "POST-SURGICAL RECTIFIED MATRIX (CASE 01)")
        else:
            print(f"\n{BOLD}{RED}>>> RUNNING SUB-LEVEL 4 HARDWARE TELEMETRY AUDIT...{RESET}")
            auditor = WafqAuditor(DEFECTIVE_Q_ENTROPY_5X5)
            report = auditor.audit()
            auditor.print_report(report, "DEFECTIVE Q-ENTROPY ARBITRAGE MATRIX (PRE-BREACH)")
            print(f"{YELLOW}Diagnosis: Cell (3,3) was milled at 17.0 instead of 13.0.")
            print(f"Run with '--rectify' to apply the Special Master's parity patch.{RESET}\n")
    elif args.canon_mars:
        auditor = WafqAuditor(CANONICAL_MARS_5X5)
        report = auditor.audit()
        auditor.print_report(report, "CANONICAL 5x5 MARTIAL MATRIX (SUM: 65)")
    else:
        # Default behavior: run Q-Entropy audit
        auditor = WafqAuditor(DEFECTIVE_Q_ENTROPY_5X5)
        report = auditor.audit()
        auditor.print_report(report, "LIVE HARDWARE SCAN: Q-ENTROPY SUB-LEVEL 4")
        print(f"Usage tips:")
        print(f"  python wafq_engine.py --rectify       (Execute the 65-parity cure)")
        print(f"  python wafq_engine.py --canon-mars    (Inspect canonical Martial matrix)")

if __name__ == "__main__":
    main()
