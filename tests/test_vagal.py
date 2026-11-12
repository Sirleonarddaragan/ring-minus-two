#!/usr/bin/env python3
"""
Automated Unit Tests for Vagal Metronome & Autonomic Coherence Controller
"""

import pytest
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ring_minus_two.vagal_metronome import VagalController

def test_vagal_harmonics():
    """Verify that the default respiratory cycle locks to ~0.100-0.102 Hz and 6 breaths/min."""
    controller = VagalController(cycle_in=4.0, cycle_hold=2.0, cycle_out=4.0)
    
    assert controller.total_cycle == 10.0
    assert abs(controller.frequency_hz - 0.100) < 0.001
    assert controller.breaths_per_minute == 6.0

def test_vagal_simulation_run():
    """Verify that fast simulation completes cleanly without exception."""
    controller = VagalController()
    # Fast simulation runs in ~0.05 seconds
    controller.run(cycles=1, fast_simulation=True)
