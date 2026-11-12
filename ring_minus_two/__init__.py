"""
Ring -2 Core Systems Package // Corpus Juris Daemonica
Codex Press x Undefined Behavior Laboratories
Author: Sir Leonard Daragan
"""

__version__ = "1.0.0"
__author__ = "Sir Leonard Daragan"
__maintainer__ = "Undefined Behavior Laboratories & Special Master Kaelen Morrow, Esq."

from .wafq_engine import WafqAuditor, CANONICAL_MARS_5X5, DEFECTIVE_Q_ENTROPY_5X5
from .abjad_calc import AbjadCalculator, ABJAD_MASHRIQI, ABJAD_MAGHRIBI
from .vagal_metronome import VagalController
from .telemetry_stream import TelemetryMonitor
from .entity_liquidation import EntityLiquidator

__all__ = [
    "WafqAuditor",
    "CANONICAL_MARS_5X5",
    "DEFECTIVE_Q_ENTROPY_5X5",
    "AbjadCalculator",
    "ABJAD_MASHRIQI",
    "ABJAD_MAGHRIBI",
    "VagalController",
    "TelemetryMonitor",
    "EntityLiquidator"
]
