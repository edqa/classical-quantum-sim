# src/classical_quantum_sim/phase_gates.py

"""
Implements simulated quantum gates that operate on the phase-aware
classical integer representation.
"""

import math
import random
from .encoding import STATE_ZERO, STATE_ONE, get_probability_p1
from .phase_encoding import (
    get_phase_index, set_phase_index, set_phase_radians,
    set_prob_and_phase, set_basis_state,
    get_probability_p1 as get_prob_p1_phase, # Use getter that understands layout if different later
    phase_qsim_repr # Use the phase-aware representation
)

def initialize_phase_aware(basis_state: int = STATE_ZERO, phase_radians: float = 0.0) -> int:
    """
    Initializes a phase-aware simulated qubit in a definite basis state.
    Phase is set, but typically irrelevant for definite states.

    Args:
        basis_state: The desired basis state (STATE_ZERO or STATE_ONE).
        phase_radians: The initial phase in radians (usually 0 for definite states).

    Returns:
        An integer representing the initialized state.
    """
    if basis_state not in (STATE_ZERO, STATE_ONE):
        raise ValueError("Initial basis state must be STATE_ZERO (0) or STATE_ONE (1)")

    qsim_int = 0 # Start fresh
    qsim_int = set_basis_state(qsim_int, basis_state)

    prob_p1 = 1.0 if basis_state == STATE_ONE else 0.0

    # Set probability and phase simultaneously
    qsim_int = set_prob_and_phase(qsim_int, prob_p1, phase_radians)

    return q normalized_angle < 0:
        normalized_angle += (2 * math.pi)
    # Calculate the index and round to nearest
    index = int(round(normalized_angle / RADIANS_PER_STEP)) % NUM_PHASE_STEPS
    return index

def _phase_index_to_radians(index: int) -> float:
    """Converts a phase index (0-15) back to radians."""
    clamped_index = max(0, min(NUM_PHASE_STEPS - 1, index))
    return float(clamped_index) * RADIANS_PER_STEP

def get_phase_index(qsim_int: int) -> int:
    """Extracts the phase index (0-15) from the integer representation."""
    return (qsim_int & PHASE_MASK) >> PHASE_SHIFT

def get_phase_radians(qsim_int: int) -> float:
    """Extracts the phase index and converts it to radians."""
    index = get_phase_index(qsim_int)
    return _phase_index_to_radians(index)

def set_phase_index(qsim_int: int, phase_index: int) -> int:
    """
    Sets the phase index bits (0-15) in the integer representation.
    Returns a *new* integer with the updated phase.
    """
    if not (0 <= phase_index < NUM_PHASE_STEPS):
        # Optional: wrap around instead of raising error
        # phase_index = phase_index % NUM_PHASE_STEPS
        raise ValueError(f"Phase index must be between 0 and {NUM_PHASE_STEPS - 1}")

    # Clear the current phase bits
    cleared_int = qsim_int & ~PHASE_MASK
    # Set the new phase bits
    updated_int = cleared_int | (phase_index << PHASE_SHIFT)
    return updated_int

def set_phase_radians(qsim_int: int, angle_rad: float) -> int:
    """
    Sets the phase bits based on an angle in radians [0, 2pi).
    Returns a *new* integer with the updated phase.
    """
    phase_index = _radians_to_phase_index(angle_rad)
    return set_phase_index(qsim_int, phase_index)

def qsim_phase_repr(qsim_int: int) -> str:
    """Provides a human-readable string representation including phase."""
    basis = get_basis_state(qsim_int)
    prob_p1 = get_probability_p1(qsim_int)
    prob_p0 = 1.0 - prob_p1
    phase_idx = get_phase_index(qsim_int)
    phase_rad = _phase_index_to_radians(phase_idx)

    state_str = f"|{basis}>" if prob_p1 in (0.0, 1.0) else "Superpos"

    # Basic representation
    return (f"QSimP(Int={qsim_int:5d}, Bin={qsim_int:016b}, State={state_str}, "
            f"P0={prob_p0:.3f}, P1={prob_p1:.3f}, PhIdx={phase_idx:2d}, PhRad={phase_rad:.3f})")
