# src/classical_quantum_sim/encoding.py

"""
Defines the bit encoding scheme and helper functions for manipulating
the classical integer representation of a simulated qubit state.

Encoding Scheme (16-bit example):
- Bits 0-1 (2 bits): Basis State (00: |0>, 01: |1>, 10: Superposition/Aux, 11: Unused/Error)
- Bits 2-5 (4 bits): Reserved for future use (e.g., phase, entanglement ID)
- Bits 6-15 (10 bits): Probability Amplitude for |1> state (0-1023, maps to 0.0-1.0)
"""

import math

# --- Constants for Bit Manipulation (16-bit) ---

# Basis State (Bits 0-1)
BASIS_STATE_SHIFT = 0
BASIS_STATE_MASK = 0b11 << BASIS_STATE_SHIFT  # Mask for bits 0, 1
STATE_ZERO = 0b00
STATE_ONE = 0b01
STATE_SUPERPOSITION_FLAG = 0b10 # Optional flag if needed

# Probability Amplitude (Bits 6-15) - Represents P(|1>)
PROB_AMP_SHIFT = 6
PROB_AMP_MASK = 0b1111111111 << PROB_AMP_SHIFT # Mask for bits 6-15
MAX_PROB_AMP_INT = 1023 # 2^10 - 1

# --- Helper Functions ---

def _int_to_probability(prob_int: int) -> float:
    """Converts the 10-bit integer amplitude to a probability [0.0, 1.0]."""
    # Clamp value just in case
    clamped_int = max(0, min(MAX_PROB_AMP_INT, prob_int))
    return float(clamped_int) / MAX_PROB_AMP_INT

def _probability_to_int(probability: float) -> int:
    """Converts a probability [0.0, 1.0] to the 10-bit integer amplitude."""
    # Clamp probability
    clamped_prob = max(0.0, min(1.0, probability))
    # Scale and round appropriately
    return int(round(clamped_prob * MAX_PROB_AMP_INT))

def get_basis_state(qsim_int: int) -> int:
    """Extracts the basis state (0 or 1) from the integer representation."""
    return (qsim_int & BASIS_STATE_MASK) >> BASIS_STATE_SHIFT

def get_probability_p1(qsim_int: int) -> float:
    """Extracts the probability amplitude for state |1> and converts it to [0.0, 1.0]."""
    prob_int = (qsim_int & PROB_AMP_MASK) >> PROB_AMP_SHIFT
    return _int_to_probability(prob_int)

def set_basis_state(qsim_int: int, basis_state: int) -> int:
    """
    Sets the basis state bits (0 or 1) in the integer representation.
    Returns a *new* integer with the updated state.
    """
    if basis_state not in (STATE_ZERO, STATE_ONE):
        raise ValueError("Basis state must be STATE_ZERO (0) or STATE_ONE (1)")

    # Clear the current basis state bits
    cleared_int = qsim_int & ~BASIS_STATE_MASK
    # Set the new basis state bits
    updated_int = cleared_int | (basis_state << BASIS_STATE_SHIFT)
    return updated_int

def set_probability_p1(qsim_int: int, probability_p1: float) -> int:
    """
    Sets the probability amplitude bits for state |1> based on a float [0.0, 1.0].
    Returns a *new* integer with the updated probability.
    """
    prob_int = _probability_to_int(probability_p1)
    # Clear the current probability bits
    cleared_int = qsim_int & ~PROB_AMP_MASK
    # Set the new probability bits
    updated_int = cleared_int | (prob_int << PROB_AMP_SHIFT)
    return updated_int

def qsim_repr(qsim_int: int) -> str:
    """Provides a human-readable string representation of the simulated qubit state."""
    basis = get_basis_state(qsim_int)
    prob_p1 = get_probability_p1(qsim_int)
    prob_p0 = 1.0 - prob_p1

    state_str = f"|{basis}>" if prob_p1 in (0.0, 1.0) else "Superposition"

    # Basic representation, can be enhanced
    return f"QSim(Int={qsim_int:5d}, Bin={qsim_int:016b}, State={state_str}, P(|0>)={prob_p0:.3f}, P(|1>)={prob_p1:.3f})"