#!/usr/bin/env python3
"""
Automated Unit Tests for Wafq Engine & 2D Parity Vector Analysis
"""

import pytest
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ring_minus_two.wafq_engine import (
    WafqAuditor,
    CANONICAL_MARS_5X5,
    DEFECTIVE_Q_ENTROPY_5X5
)

def test_canonical_mars_parity_locked():
    """Verify that the classical 5x5 Martial square achieves strict 65.0 zero-entropy parity."""
    auditor = WafqAuditor(CANONICAL_MARS_5X5)
    report = auditor.audit()

    assert report["n"] == 5
    assert report["theoretical_sum"] == 65.0
    assert report["is_parity_locked"] is True
    assert report["total_variance"] == 0.0

    for r_sum in report["row_sums"]:
        assert r_sum == 65.0
    for c_sum in report["col_sums"]:
        assert c_sum == 65.0
    assert report["diag1_sum"] == 65.0
    assert report["diag2_sum"] == 65.0

def test_defective_q_entropy_matrix_kasr():
    """Verify that the defective Q-Entropy matrix fails with exact +4.0 Kasr on cell (2,2)."""
    auditor = WafqAuditor(DEFECTIVE_Q_ENTROPY_5X5)
    report = auditor.audit()

    assert report["is_parity_locked"] is False
    assert report["total_variance"] > 0.0

    # Cell (2,2) affects Row 2, Col 2, Diag 1, and Diag 2
    assert report["row_errors"][2] == 4.0
    assert report["col_errors"][2] == 4.0
    assert report["diag1_error"] == 4.0
    assert report["diag2_error"] == 4.0

    # Total accumulated variance = 4 + 4 + 4 + 4 = 16.0
    assert report["total_variance"] == 16.0

def test_non_square_matrix_rejection():
    """Verify that non-square matrices are rejected with ValueError."""
    with pytest.raises(ValueError):
        WafqAuditor([[1, 2, 3], [4, 5, 6]])
