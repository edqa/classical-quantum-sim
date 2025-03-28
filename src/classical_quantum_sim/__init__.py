# src/classical_quantum_sim/__init__.py

"""
Classical Quantum Simulation Package

This package provides tools to simulate quantum-like properties (superposition,
probabilistic measurement) using classical bit manipulation on integers.
"""

# Expose the main functions for easy import
from .encoding import (
    STATE_ZERO,
    STATE_ONE,
    get_basis_state,
    get_probability_p1,
    qsim_repr # Expose the representation function
)

from .gates import (
    initialize,
    apply_H_sim,
    measure
)

# You can define a version here if you like
__version__ = "0.0.1"