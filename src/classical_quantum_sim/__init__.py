# src/classical_quantum_sim/__init__.py

"""
Classical Quantum Simulation Package

This package provides tools to simulate quantum-like properties using classical
bit manipulation on integers. Includes basic probability-only simulation and
optional modules for phase-aware and entanglement-correlation simulations.
"""

# --- Basic Probability Simulation (Default Exports) ---
from .encoding import (
    STATE_ZERO,
    STATE_ONE,
    get_basis_state,
    get_probability_p1,
    qsim_repr # Base representation function
)
from .gates import (
    initialize,
    apply_H_sim,
    measure
)

# --- Advanced Simulation Modules ---
# Users need to import from these explicitly for advanced features

# Phase Simulation (Encoding helpers and Phase-aware Gates)
# Exposing the modules directly is often cleaner
from . import phase_encoding
from . import phase_gates
# Alternatively, expose specific functions if preferred:
# from .phase_gates import initialize_phase_aware, apply_H_phase_aware, measure_phase_aware, apply_PhaseShift_sim
# from .phase_encoding import phase_qsim_repr

# Entanglement Simulation (Classical Correlation)
# Exposing the modules directly:
from . import entanglement # Module managing pairs
# Note: Entanglement currently relies on phase_gates for its qubit representation
# You might also want to expose entanglement_encoding helpers if needed externally
# from .entanglement import create_bell_pair_sim, measure_entangled


# --- Package Version ---
# Bump version to indicate significant new features (even if alpha)
__version__ = "0.2.0"
