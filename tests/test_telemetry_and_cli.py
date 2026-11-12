import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ring_minus_two.abjad_calc import compute_abjad
from ring_minus_two.telemetry_stream import TelemetryMonitor
from ring_minus_two.entity_liquidation import EntityLiquidator


def test_case02_enc_decrypts_cleanly():
    total, _ = compute_abjad("عَدْل")
    assert total == 104

    enc_path = Path(__file__).resolve().parent.parent / "exhibits" / "book_02_teaser_dossier.enc"
    raw = enc_path.read_bytes()
    plaintext = bytes([b ^ total for b in raw]).decode("utf-8")

    assert "CLASSIFIED DOSSIER: CASE FILE 02" in plaintext
    assert "Bael" in plaintext
    assert "Lake Zurich" in plaintext
    assert "UNDER DEVELOPMENT" in plaintext


def test_telemetry_monitor_fast(capsys):
    mon = TelemetryMonitor(simulation_speed=10.0)
    mon.stream_breach_sequence(fast=True)
    out = capsys.readouterr().out
    assert "38:14" in out
    assert "31:12" in out
    assert "03:22" in out
    assert " bar" in out


def test_entity_liquidator_audit_fast(capsys):
    liq = EntityLiquidator()
    ok = liq.audit_covenants(fast=True)
    assert ok is False  # Expect Clause 4.3 violations detected
    out = capsys.readouterr().out
    assert "CANON 2: THAMAN" in out
    assert "CANON 3: IKHTIṢĀṢ" in out
