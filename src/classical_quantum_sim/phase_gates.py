# src/classical_quantum_sim/phase_gates.py

"""
Implements simulated quantum gates that operate on states including
both probability amplitude and discretized phase information.
"""

import math
import random
from .phase_encoding import (
    STATE_ZERO, STATE_ONE, NUM_PHASE_STEPS,
    get_probability_p1, set_probability_p1,
    get_phase_index, set_phase_index, _phase_index_to_radians, _radians_to_phase_index,
    set_basis_state, qsim_phase_repr # Use the phase-aware representation
)
# Note: We reuse the basicsim_int


def apply_H_phase_aware(qsim_int: int) -> int:
    """
    Applies a simulated Hadamard gate considering phase.

    Rough Quantum Logic (simplified):
    H |+> = |0>  (where |+> = (|0>+|1>)/sqrt(2))
    H |-> = |1>  (where |-> = (|0>-|1>)/sqrt(2))
    H |0> = |+>  => P=0.5, Phase=0
    H |1> = |->  => P=0.5, Phase=pi (relative phase)

    Simulation Logic:
    - If input is |0> (P1=0, Phase=ignored), output P1=0.5, Phase=0.
    - If input is |1> (P1=1, Phase=ignored), output P1=0.5, Phase=pi.
    - If input is superposition: This requires defining how H interacts with
      existing probability *and* phase. A simple model might ignore input phase
      and apply the standard H matrix effect conceptually on probabilities,
      or a more complex one could try to rotate the state on the Bloch sphere (simulated).

      *Initial Simple Approach:* If superposition, reset phase based on probabilities?
      *Let's implement the definite state logic first.*
    """
    prob_p1 = get_prob_p1_phase(qsim_int)
    new_prob_p1 = 0.5 # H gate always results in 50/50 measurement probability

    if prob_p1 == 0.0: # Input was |0> state
        new_phase_rad = 0.0
        # Update basis state flag maybe? Optional.
    elif prob_p1 == 1.0: # Input was |1> state
        new_phase_rad = math.pi
        # Update basis state flag maybe? Optional.
    else:
        # --- Handling Superposition Input ---
        # This is complex. How does H rotate an arbitrary P/Phase state?
        # Simple Placeholder: Just set P=0.5 and leave phase unchanged? Or reset to 0?
        # Let's just average phase towards 0/pi based on input P for now (crude!)
        # BETTER APPROACH set_basis_state as it doesn't overlap bits

DEFAULT_PHASE_INDEX = 0 # Phase index 0 (0 radians)

def initialize_phase_aware(basis_state: int = STATE_ZERO, initial_phase_index: int = DEFAULT_PHASE_INDEX) -> int:
    """
    Initializes a phase-aware simulated qubit in a definite basis state.

    Args:
        basis_state: The desired basis state (STATE_ZERO or STATE_ONE).
        initial_phase_index: The initial phase index (0-15).

    Returns:
        An integer representing the initialized state.
    """
    if basis_state not in (STATE_ZERO, STATE_ONE):
        raise ValueError("Initial basis state must be STATE_ZERO (0) or STATE_ONE (1)")
    if not (0 <= initial_phase_index < NUM_PHASE_STEPS):
        raise ValueError(f"Initial phase index must be 0-{NUM_PHASE_STEPS-1}")

    # Start with zero
    qsim_int = 0
    # Set basis state
    qsim_int = set_basis_state(qsim_int, basis_state)
    # Set probability (1.0 for the specified state, 0.0 for the other)
    prob_p1 = 1.0 if basis_state == STATE_ONE else 0.0
    qsim_int = set_probability_p1(qsim_int, prob_p1)
    # Set initial phase
    qsim_int = set_phase_index(qsim_int, initial_phase_index)

    return qsim_int

def apply_H_phase_aware(qsim_int: int) -> int:
    """
    Applies a simulated Hadamard gate, affecting both probability and phase.

    - Sets probabilities to P(0)=0.5, P(1)=0.5.
    - Adds a phase shift of pi (index delta of 8) NEEDED HERE LATER - True rotation requires more math.
        print("Warning: H on superposition input uses simplified phase logic.")
        existing_phase_rad = phase_encoding.get_phase_radians(qsim_int)
        # Example crude logic: weighted average towards 0 or pi
        new_phase_rad = (1.0 - prob_p1) * 0.0 + prob_p1 * math.pi # Biased by initial P1
        # A fixed outcome might be safer: new_phase_rad = 0.0

    # Create new state integer
    # Basis state bits might be set to a superposition flag if defined
    return set_prob_and_phase(qsim_int, new_prob_p1, new_phase_rad)


def apply_PhaseShift_sim(qsim_int: int, angle_radians: float) -> int:
    """
    Applies a phase shift gate P(angle) = [[1, 0], [0, e^(i*angle)]].
    In our simulation, this only affects the relative phase component.

    Args:
        qsim_int: The input simulated qubit integer. if the input state was |1>.
      (This crudely simulates H|1> = (|0> - |1>)/sqrt(2) having a relative pi phase).
    - Assumes H|0> = (|0> + |1>)/sqrt(2) has base phase 0.

    Note: Behavior on superposition inputs is a simplified approximation.
    """
    current_prob_p1 = get_probability_p1(qsim_int)
    current_phase_idx = get_phase_index(qsim_int)
    updated_int = qsim_
        angle_radians: The phase shift to apply in radians.

    Returns:
        A new integer representing the state after the phase shift.
    """
    current_phase_rad = phase_encoding.get_phase_radians(qsim_int)
    new_phase_rad = (current_phase_rad + angle_radians) % (2 * math.pi)

    # Only update the phase bits
    return phase_encoding.set_phase_radians(qsim_int, new_phase_rad)


def measure_phase_aware(qsim_int: int) ->int

    # Set probability to 50/50
    updated_int = set_probability_p1(updated_int, 0.5)

    # Apply phase shift based on input state *before* probability change
    if current_prob_p1 == 1.0: # Input was approximately |1>
        # Add pi radians (index delta = NUM_PHASE_STEPS / 2)
        phase_delta = NUM_PHASE_STEPS // 2
        new_phase_idx = (current_phase_idx + phase_delta) tuple[int, int]:
    """
    Simulates measuring the qubit (phase-aware version).

    Measurement probability depends only on P(|1>). Phase affects interference
    before measurement but not the measurement probabilities themselves.
    The collapsed state will have probability 1.0 and phase reset to  % NUM_PHASE_STEPS
        updated_int = set_phase_index(updated_int, new_phase_idx)
    elif current_prob_p1 == 0.0: # Input was approximately |0>
        # No phase change relative to base state (phase0 (conventionally).

    Args:
        qsim_int: The input simulated qubit integer.

    Returns:
        A tuple containing:
            - outcome (int): The measured basis state (0 or 1).
            - collapsed_qsim_int (int): The new integer representing the
                                         qubit after collapse (definite state, phase 0).
    """
    prob_p1 = get_prob_p1_phase(qsim_int)

    # Perform probabilistic collapse (same as basic version)
    random_draw = random.random()
    outcome index remains the same)
        pass
    else: # Input was already superposition
        # More complex models could average phases or apply rotations.
        # Simplification: Just keep the existing phase for now.
         print("Warning: Phase-aware H applied to superposition state. Phase behavior simplified.")
        # = STATE_ONE if random_draw < prob_p1 else STATE_ZERO

    # Create the new integer representing the collapsed state with phase 0
    collapsed_qsim_int = initialize_phase_aware(outcome, phase_radians=0.0)

    return outcome, collapsed_ Optional: Could reset phase? set_phase_index(updated_int, DEFAULT_PHASE_INDEX)

    return updated_int


def apply_PhaseShift_sim(qsim_int: int, angle_rad: float) -> int:
    """
    Applies a phase shift byqsim_int
