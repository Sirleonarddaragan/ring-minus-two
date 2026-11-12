#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="ring-minus-two",
    version="1.0.0",
    description="Metrological, lettrist, and statutory receivership tools for Ring -2 reality hypervisors.",
    author="Codex Press x Undefined Behavior Laboratories",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "wafq=ring_minus_two.wafq_engine:main",
            "abjad=ring_minus_two.abjad_calc:main",
            "vagal=ring_minus_two.vagal_metronome:main",
            "telemetry=ring_minus_two.telemetry_stream:main",
            "liquidate=ring_minus_two.entity_liquidation:main",
            "investigate=ring_minus_two.interactive_console:main",
        ],
    },
)
