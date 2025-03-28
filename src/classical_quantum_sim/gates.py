# src/classical_quantum_sim/gates.py

"""
Implements simulated quantum gates operating on the classical integer representation.
"""

import random
from .encoding import (
    STATE_ZERO, STATE_ONE,
    get_probability_p1, set_probability_p1,
    set_basis_state, MAX_PROB_AMP_INT, _probability_to_int
)

def initialize(basis_state: int = STATE_ZERO) -> int:
    """
    Initializes a simulated qubit integer in a definite basis state (|0> or |1>).

    Args:
        basis_state: The desired basis state (STATE_ZERO or STATE_ONE).

    Returns:
        An integer representing the initialized state with probability 1.0.
    """
    if basis_state not in (STATE_ZERO, STATE_ONE):
        raise ValueError("Initial basis state must be STATE_ZERO (0) or STATE_ONE (1)")

    # Start with zero
    qsim_int = 0

    # Set basis state
    qsim_int = set_basis_state(qsim_int, basis_state)

    # Set probability (1.0 for the specified state, 0.0 for the other)
    prob_p1 = 1.0 if basis_state == STATE_ONE else 0.0
    qsim_int = set_probability_p1(qsim_int, prob_p1)

    return qsim_int

def apply_H_sim(qsim_int: int) -> int:
    """
    Applies a simulated Hadamard gate.
    Transforms |0> -> (|0> + |1>)/sqrt(2)  => P(0)=0.5, P(1)=0.5
    Transforms |1> -> (|0> - |1>)/sqrt(2)  => P(0)=0.5, P(1)=0.5
    (Phase is ignored in this simulation).

    If already in superposition, the behavior might be simplified or specific
    depending on the desired simulation properties. Here, we simply set P(0)=P(1)=0.5
    if the input was a definite state.

    Args:
        qsim_int: The input simulated qubit integer.

    Returns:
        A new integer representing the state after the simulated H gate.
    """
    current_prob_p1 = get_probability_p1(qsim_int)

    # If the state is definite |0> or |1>, put it into 50/50 superposition
    if current_prob_p1 == 0.0 or current_prob_p1 == 1.0:
        # Set probability P(1) to 0.5
        # Note: Basis state bits become less meaningful until measurement
        return set_probability_p1(qsim_int, 0.5)
    else:
        # If already in superposition, behavior depends on desired model.
        # Simplest MVP: H on superposition does nothing or returns to some state.
        # Let's assume for now it just stays in the same probabilistic state.
        # A more complex model could track phase or use different logic.
        print("Warning: Simulated H applied to non-definite state. Behavior is simplified.")
        return qsim_int


def measure(qsim_int: int) -> tuple[int, int]:
    """
    Simulates measuring the qubit.

    Collapses the state based on the probability amplitude P(|1>).
    Updates the integer representation to reflect the collapsed state (P=1.0).

    Args:
        qsim_int: The input simulated qubit integer.

    Returns:
        A tuple containing:
            - outcome (int): The measured basis state (0 or 1).
            - collapsed_qsim_int (int): The new integer representing the
                                         qubit after collapse.
    """
    prob_p1 = get_probability_p1(qsim_int)

    # Perform probabilistic collapse
    random_draw = random.random() # Random float between 0.0 and 1.0

    if random_draw < prob_p1:
        # Collapse to |1>
        outcome = STATE_ONE
    else:
        # Collapse to |0>
        outcome = STATE_ZERO

    # Create the new integer representing the collapsed state
    collapsed_qsim_int = initialize(outcome) # Easiest way to get P=1.0 state

    return outcome, collapsed_qsim_int