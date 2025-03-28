# src/classical_quantum_sim/phase_encoding.py

"""
Extends the encoding scheme to include discretized phase information,
using reserved bits alongside the probability amplitude.

Phase Encoding Scheme (using bits 2-5 of 16-bit integer):
- Bits 2-5 (4 bits): Phase Index (0-15). Represents phase angle / (π/8).
  - Index 0 -> 0 radians
  - Index 1 -> π/8 radians
  - ...
  - Index 15 -> 15π/8 radians

Note: This module REUSES probability encoding from the base `encoding` module.
"""

import math
from .encoding import ( # Import base probability helpers
    PROB_AMP_SHIFT, PROB_AMP_MASK, MAX_PROB_AMP_INT,
    BASIS_STATE_SHIFT, BASIS_STATE_MASK, STATE_ZERO, STATE_ONE,
    _int_to_probability, _probability_to_int,
    get_basis_state, get_probability_p1,
    set_basis_state, set_probability_p1
)

# --- Constants for Phase Bit Manipulation (16-bit) ---
PHASE_SHIFT = 2
PHASE_MASK = 0b1111 << PHASE_SHIFT  # Mask for bits 2, 3, 4, 5
NUM_PHASE_STEPS = 16
RADIANS_PER_STEP = (2 * math.pi) / NUM_PHASE_STEPS # Roughly pi / 8

# --- Phase Helper Functions ---

def _radians_to_phase_index(angle_rad: float) -> int:
    """Converts an angle in radians [0, 2pi) to the nearest phase index (0-15)."""
    # Normalize angle to [0, 2pi)
    normalized_angle = angle_rad % (2 * math.pi)
    if(qsim_int)
    prob_p0 = 1.0 - prob_p1
    phase_rad = get_phase_radians(qsim_int)
    phase_deg = math.degrees(phase_rad)
    phase_idx = get_phase_index(qsim_int)

    state_str = f"|{basis}>" if prob_p1 in (0.0, 1.0) else "Superposition"

    # Include phase info, especially relevant for superpositions
    phase_info = f"Phase={phase_rad:.3f}rad ({phase_deg:.1f}deg, Idx={phase_idx})"
    if prob_p1 in (0.0, 1.0):
         phase_info = "Phase=N/A (Definite State)"


    return (f"PhaseQSim(Int={qsim_int:5d}, Bin={qsim_int:016b}, State={state_str}, "
            f"P(|0>)={prob_p0:.3f}, P(|1>)={prob_p1:.3f}, {phase_info})")
