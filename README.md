# Classical Quantum Simulation (Probabilistic Bit Weaving)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- Or Apache 2.0 -->
[![Python Version](https://img.shields.io/pypi/pyversions/classical-quantum-sim)](https://pypi.org/project/classical-quantum-sim/) <!-- Placeholder until published -->
[![PyPI version](https://badge.fury.io/py/classical-quantum-sim.svg)](https://badge.fury.io/py/classical-quantum-sim) <!-- Placeholder until published -->

This project explores the simulation of quantum-like properties (superposition, probability amplitudes, measurement outcomes, phase, correlations) using structured multi-bit representations on classical hardware. We use standard quantum notation (like Dirac notation `|0>`, `|1>`) for clarity where applicable, but it's crucial to remember **this is a classical simulation**.

**Goal:** To provide an accessible development tool for modeling probabilistic state evolution efficiently using standard integer types and bit manipulation, serving as a conceptual sandbox for quantum-inspired ideas on classical machines. Offers layers of simulation complexity from basic probability to phase and correlation.

**What it IS:**
*   A classical simulation technique with different levels of approximation.
*   An exploration of representing probabilistic and phase states using bit fields.
*   A method for simulating classical correlations analogous to entanglement.
*   A potential tool for specific probabilistic algorithms or conceptual modeling.

**What it IS NOT:**
*   True quantum computing. It does **not** leverage quantum phenomena like complex amplitudes, true interference, or entanglement for exponential speedups.
*   A replacement for established quantum simulators like Qiskit, Cirq, etc., which simulate quantum mechanics more comprehensively (often at higher computational cost).

## Concept: Probabilistic Bit Weaving

A standard qubit state `|ψ> = α|0> + β|1>` involves complex amplitudes `α, β` where `|α|² + |β|² = 1`. This simulation approximates this in layers:

1.  **Base Simulation:** Directly encodes and manipulates real-valued probabilities `P(|0>) = |α|²` and `P(|1>) = |β|²` within a classical integer, enforcing `P(|0>) + P(|1>) = 1`. Phase information is ignored.
2.  **Phase-Aware Simulation (Optional Module):** Adds a *discretized* representation of the relative phase between `α` and `β` using reserved bits, allowing simulation of phase shift gates and more nuanced Hadamard behavior.
3.  **Entanglement Simulation (Optional Module):** Simulates *classical correlations* between pairs of simulated qubits, mimicking Bell state measurement outcomes using shared IDs and coordinated classical logic.

---

## Core Encoding (Base Simulation - `encoding.py`)

Uses a 16-bit integer:

*   **Bits 6-15 (10 bits):** Probability Amplitude for state `|1>`. Integer `ProbInt` (0-1023).
    `P(|1>) = ProbInt / 1023.0`
    `P(|0>) = 1.0 - P(|1>)`
*   **Bits 0-1:** Basis State (`|0>` or `|1>`). Represents the definite state after measurement.
*   **Bits 2-5:** *Unused* in base simulation.

## Base Simulation Usage (`gates.py`)

This uses the core encoding (probability only).

```python
# Base simulation (probability only)
from classical_quantum_sim import initialize, apply_H_sim, measure, STATE_ZERO, qsim_repr

q0 = initialize(STATE_ZERO)
print(f"Initial: {qsim_repr(q0)}")
q_h = apply_H_sim(q0) # Puts into P=0.5 superposition (ignores phase)
print(f"After H: {qsim_repr(q_h)}")
outcome, q_collapsed = measure(q_h) # Probabilistic outcome, definite collapsed state
print(f"Measure: {outcome}, Collapsed: {qsim_repr(q_collapsed)}")
