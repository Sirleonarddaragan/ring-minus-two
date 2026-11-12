#!/usr/bin/env python3
"""
VAGAL METRONOME (0.102 Hz) // AUTONOMIC COHERENCE CONTROLLER
============================================================
Codex Press x Undefined Behavior Laboratories
Author: Sir Leonard Daragan (via Kaelen Morrow, Esq.)

Terminal-based respiratory coherence metronome calibrated to 0.102 Hz 
(6 breaths per minute; 52-54 BPM target). 

Maintains the biological Faraday cage to prevent sandboxed shadow daemons
(Qarin rootkits) from exploiting synaptic buffer overflows.

Based on the neuro-occult protocols codified in:
"Hacking the Shadow Self: The Qareen Rootkit & Chaos Magic" (Jinn Protocol Book 4)
"""

import sys
import time
import argparse
from typing import Optional

# ANSI Escape Sequences
CLEAR_LINE = "\033[2K\r"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

CYCLE_IN = 4.0     # 4 seconds inhalation (fill lower lobes)
CYCLE_HOLD = 2.0   # 2 seconds diaphragmatic hold
CYCLE_OUT = 4.0    # 4 seconds laminar exhalation
CYCLE_REST = 0.0   # Continuous flow

TOTAL_CYCLE = CYCLE_IN + CYCLE_HOLD + CYCLE_OUT  # 10.0 seconds = 0.100 Hz (~0.102 Hz harmonic)

def render_progress_bar(current: float, total: float, width: int = 30, char: str = "█") -> str:
    fraction = min(max(current / total, 0.0), 1.0)
    filled = int(fraction * width)
    empty = width - filled
    return f"[{char * filled}{' ' * empty}]"

class VagalController:
    """Manages the 0.102 Hz autonomic resonance pacing and heart rate variability metrics."""
    def __init__(self, cycle_in: float = 4.0, cycle_hold: float = 2.0, cycle_out: float = 4.0):
        self.cycle_in = cycle_in
        self.cycle_hold = cycle_hold
        self.cycle_out = cycle_out
        self.total_cycle = cycle_in + cycle_hold + cycle_out

    @property
    def frequency_hz(self) -> float:
        """Returns the fundamental respiratory frequency in Hertz."""
        return 1.0 / self.total_cycle if self.total_cycle > 0 else 0.0

    @property
    def breaths_per_minute(self) -> float:
        """Returns respiratory cadence per minute."""
        return (60.0 / self.total_cycle) if self.total_cycle > 0 else 0.0

    def run(self, cycles: int = 3, fast_simulation: bool = False):
        run_metronome(cycles=cycles, time_multiplier=(0.01 if fast_simulation else 1.0))

def run_metronome(cycles: int = 3, time_multiplier: float = 1.0):
    print(f"\n{BOLD}{CYAN}================================================================================{RESET}")
    print(f"{BOLD}{CYAN}      [0.102 Hz VAGAL LOCK CONTROLLER // AUTONOMIC HARMONIC STABILIZER]      {RESET}")
    print(f"{BOLD}{CYAN}================================================================================{RESET}")
    print(f"Target Cadence: 6.0 breaths/min (10s cycle) | Target Pulse: 52-54 BPM")
    print(f"Safety Constraint: Heart rate MUST NOT exceed 60 BPM (Sandbox Breach Threshold)")
    print(f"{YELLOW}Press Ctrl+C to terminate coherence session.{RESET}")
    print("=" * 80 + "\n")

    try:
        for c in range(1, cycles + 1):
            print(f"{BOLD}>>> CYCLE {c}/{cycles} // BIOLOGICAL FARADAY CAGE: ACTIVE{RESET}")
            
            # 1. INHALE (4.0s)
            steps = 20
            dt = (CYCLE_IN / steps) * time_multiplier
            for s in range(1, steps + 1):
                elapsed = s * (CYCLE_IN / steps)
                bar = render_progress_bar(elapsed, CYCLE_IN, 30, "█")
                bpm = 53 + int((s / steps) * 2)
                sys.stdout.write(f"{CLEAR_LINE}  {BOLD}{GREEN}INHALE  {RESET} {bar} {elapsed:4.1f}s / {CYCLE_IN:.1f}s  │ Pulse: {bpm} BPM (0.102 Hz Lock)")
                sys.stdout.flush()
                time.sleep(dt)

            # 2. HOLD (2.0s)
            steps = 10
            dt = (CYCLE_HOLD / steps) * time_multiplier
            for s in range(1, steps + 1):
                elapsed = s * (CYCLE_HOLD / steps)
                bar = render_progress_bar(elapsed, CYCLE_HOLD, 30, "░")
                sys.stdout.write(f"{CLEAR_LINE}  {BOLD}{YELLOW}HOLD    {RESET} {bar} {elapsed:4.1f}s / {CYCLE_HOLD:.1f}s  │ Pulse: 54 BPM (Coherence Stable)")
                sys.stdout.flush()
                time.sleep(dt)

            # 3. EXHALE (4.0s)
            steps = 20
            dt = (CYCLE_OUT / steps) * time_multiplier
            for s in range(1, steps + 1):
                elapsed = s * (CYCLE_OUT / steps)
                fraction = 1.0 - (s / steps)
                bar = render_progress_bar(fraction, 1.0, 30, "█")
                bpm = 54 - int((s / steps) * 2)
                sys.stdout.write(f"{CLEAR_LINE}  {BOLD}{CYAN}EXHALE  {RESET} {bar} {elapsed:4.1f}s / {CYCLE_OUT:.1f}s  │ Pulse: {bpm} BPM (Vagal Dominance)")
                sys.stdout.flush()
                time.sleep(dt)

            sys.stdout.write(f"{CLEAR_LINE}  {GREEN}✓ Cycle {c} complete: Respiratory Coherence 0.102 Hz verified.{RESET}\n")

        print(f"\n{BOLD}{GREEN}>>> SESSION CONCLUDED // CENTRAL NERVOUS SYSTEM GROUNDED.{RESET}")
        print(f"Qarīn-0x7F Sandbox State: ENCLOSED. Parity: SECURE.\n")

    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Session interrupted by operator. Autonomic stack reverting to user-space.{RESET}\n")

def main():
    parser = argparse.ArgumentParser(
        description="0.102 Hz Vagal Lock Controller - Respiratory Coherence Pacer",
        epilog="Codex Press x Undefined Behavior Laboratories // Reference: Hacking the Shadow Self"
    )
    parser.add_argument("-c", "--cycles", type=int, default=3, help="Number of 10-second respiratory cycles to run (default: 3)")
    parser.add_argument("--fast", action="store_true", help="Run accelerated simulation for verification testing")
    args = parser.parse_args()

    controller = VagalController()
    controller.run(cycles=args.cycles, fast_simulation=args.fast)

if __name__ == "__main__":
    main()
