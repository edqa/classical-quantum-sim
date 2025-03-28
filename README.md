# Classical Quantum Simulation (Probabilistic Bit Weaving)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- Or Apache 2.0 -->
[![Python Version](https://img.shields.io/pypi/pyversions/classical-quantum-sim)](https://pypi.org/project/classical-quantum-sim/) <!-- Placeholder until published -->
[![PyPI version](https://badge.fury.io/py/classical-quantum-sim.svg)](https://badge.fury.io/py/classical-quantum-sim) <!-- Placeholder until published -->

This project explores the simulation of quantum-like properties (superposition, probability amplitudes, measurement collapse) using structured multi-bit representations on classical hardware.

**Goal:** To model probabilistic state evolution efficiently using standard integer types and bit manipulation, providing a conceptual sandbox for quantum-inspired ideas on classical machines.

**What it IS:**
*   A classical simulation technique.
*   An exploration of representing probabilistic states using bit fields within standard integers.
*   A potential tool for specific types of probabilistic algorithms or conceptual modeling.

**What it IS NOT:**
*   True quantum computing. It does **not** leverage quantum phenomena like entanglement for exponential speedups.
*   A replacement for established quantum simulators like Qiskit, Cirq, etc.

## Concept: Probabilistic Bit Weaving

Instead of using floating-point numbers for probability amplitudes directly, we embed probabilistic information into specific bit fields of a classical integer. Operations (simulated "gates") manipulate these bits according to rules designed to mimic quantum state evolution and measurement.

### Example Encoding (16-bit Integer)

Currently, a 16-bit integer represents a simulated qubit state as follows:

*   **Bits 0-1 (2 bits):** Basis State (`00` = `|0>`, `01` = `|1>`). Primarily relevant after measurement.
*   **Bits 2-5 (4 bits):** *Reserved* for future use (e.g., phase, entanglement IDs).
*   **Bits 6-15 (10 bits):** Probability Amplitude for state `|1>`. An integer from `0` to `1023`, linearly mapped to a probability `P(|1>)` in the range `[0.0, 1.0]`. `P(|0>)` is implicitly `1.0 - P(|1>)`.

## Installation

You can install the package directly from GitHub (or PyPI once published):

```bash
# Recommended: Clone and install in editable mode for development
git clone https://github.com/edqa/classical-quantum-sim.git
cd classical-quantum-sim
pip install -e .

# Or install directly (replace main with a specific tag/commit if needed)
# pip install git+https://github.com/edqa/classical-quantum-sim.git@main