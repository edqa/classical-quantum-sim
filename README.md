# Classical Quantum Simulation (Probabilistic Bit Weaving)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- Or Apache 2.0 -->
[![Python Version](https://img.shields.io/pypi/pyversions/classical-quantum-sim)](https://pypi.org/project/classical-quantum-sim/) <!-- Placeholder until published -->
[![PyPI version](https://badge.fury.io/py/classical-quantum-sim.svg)](https://badge.fury.io/py/classical-quantum-sim) <!-- Placeholder until published -->

This project explores the simulation of quantum-like probabilistic properties (superposition, measurement outcomes) using structured multi-bit representations on classical hardware. We use standard quantum notation (like Dirac notation `|0>`, `|1>`) for clarity where applicable, but it's crucial to remember **this is a classical simulation**.

**Goal:** To model probabilistic state evolution efficiently using standard integer types and bit manipulation, providing a conceptual sandbox for quantum-inspired ideas on classical machines.

**What it IS:**
*   A classical simulation technique.
*   An exploration of representing probabilistic states using bit fields within standard integers.
*   A potential tool for specific types of probabilistic algorithms or conceptual modeling.

**What it IS NOT:**
*   True quantum computing. It does **not** leverage quantum phenomena like complex amplitudes, phase interference, or entanglement for exponential speedups.
*   A replacement for established quantum simulators like Qiskit, Cirq, etc., which simulate quantum mechanics more comprehensively (often at higher computational cost).

## Concept: Probabilistic Bit Weaving

A standard quantum bit (qubit) state `|ψ>` can be written as a superposition:
`|ψ> = α|0> + β|1>`
where `α` and `β` are complex probability amplitudes such that `|α|² + |β|² = 1`. The probabilities of measuring the qubit in state `|0>` or `|1>` are `P(|0>) = |α|²` and `P(|1>) = |β|²`, respectively.

This simulation **does not store complex amplitudes `α` or `β`**. Instead, it directly encodes and manipulates the real-valued probabilities `P(|0>)` and `P(|1>)` within a classical integer, enforcing the constraint `P(|0>) + P(|1>) = 1`. Information about the relative phase between `α` and `β` is **lost**.

### Encoding Scheme (16-bit Integer)

A single 16-bit integer represents the probabilistic state of a simulated qubit:

*   **Bits 0-1 (2 bits):** Basis State (`00` = `|0>`, `01` = `|1>`). Primarily represents the collapsed state *after* a measurement operation.
*   **Bits 2-5 (4 bits):** *Reserved* for future use (e.g., phase approximation, entanglement IDs - see [Issue #X](link-to-research-issue)).
*   **Bits 6-15 (10 bits):** Probability Amplitude for state `|1>`. An integer `ProbInt` from `0` to `1023`. This maps to the probability `P(|1>)` as follows:
    `P(|1>) = ProbInt / (2^10 - 1) = ProbInt / 1023.0`
    The probability of state `|0>` is derived implicitly:
    `P(|0>) = 1.0 - P(|1>)`

## Simulated Gates

Simulated gates operate on the integer representation, modifying the stored probabilities `P(|0>)` and `P(|1>)` to mimic the *outcome probabilities* of corresponding quantum gates. They do not simulate the full unitary evolution involving complex amplitudes and phase.

### Simulated Hadamard (`H`) Gate

*   **Quantum Action:** `H|0> = (|0> + |1>)/√2`, `H|1> = (|0> - |1>)/√2`. In both cases, measurement yields `|0>` or `|1>` with 50% probability each (`P(|0>) = P(|1>) = 0.5`).
*   **Simulation `apply_H_sim`:** Transforms definite input states (`P(|0>)=1` or `P(|1>)=1`) into a state where the outcome probabilities are equal:
    `P'(|0>) = 0.5`, `P'(|1>) = 0.5`.
    *(Note: The current behavior on inputs already in superposition is simplified and may be refined later. Phase information determining the relative sign in the quantum case is ignored).*

### Simulated Pauli-X (`X` or `σ_x`) Gate (*Future*)

*   **Quantum Action:** `X|0> = |1>`, `X|1> = |0>`. This flips the state.
*   **Simulation `apply_X_sim` (To be implemented - see [Issue #Y](link-to-pauli-x-issue)):** Will flip the stored probabilities:
    `P'(|0>) = P(|1>)`
    `P'(|1>) = P(|0>)`

## Simulated Measurement

Measurement is simulated based on the Born rule concept, where the probability of obtaining a specific outcome corresponds to the squared magnitude of its amplitude.

*   **Quantum Rule:** For state `|ψ> = α|0> + β|1>`, `P(measure 0) = |α|²`, `P(measure 1) = |β|²`.
*   **Simulation `measure`:** The function uses the stored probability `P_stored(|1>) = ProbInt / 1023.0`.
    1. A random floating-point number `r` is drawn uniformly from `[0.0, 1.0)`.
    2. If `r < P_stored(|1>)`, the outcome `m` is `1` (state `|1>`).
    3. Otherwise, the outcome `m` is `0` (state `|0>`).
    4. The function returns the outcome `m` and a *new* integer representation corresponding to the collapsed definite state `|m>` (i.e., `P(|m>)=1`).

## Installation

```bash
# Recommended: Clone and install in editable mode for development
git clone https://github.com/edqa/classical-quantum-sim.git
cd classical-quantum-sim
pip install -e .

# Or install directly (replace main with a specific tag/commit if needed)
# pip install git+https://github.com/edqa/classical-quantum-sim.git@main



