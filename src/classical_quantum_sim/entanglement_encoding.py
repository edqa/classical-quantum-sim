# src/classical_quantum_sim/entanglement_encoding.py
"""
Encoding helpers specifically for using reserved bits as an Entanglement Pair ID.

Entanglement ID Encoding (using bits 2-5 of 16-bit integer):
- Bits won't affect external variables holding them.
#          This simple model has limitations. A class-based approach might be better.
entangled_pairs_registry = {}

# --- Entanglement Functions ---

def _generate_pair_id() -> str:
    """Generates a unique ID for 2-5 (4 bits): Entanglement Pair ID (1-15).
  - ID 0: Indicates the qubit is NOT entangled.
  - ID 1-15: Links this qubit to another with the same ID.

Note: This assumes phase is NOT simultaneously encoded. Uses an entangled pair."""
    return str(uuid.uuid4())

def create_bell_pair_sim(type: str = 'phi+') -> tuple[int, int, str]:
    """
    Creates two simulated qubit integers linked to represent a Bell state correlation.

    Args:
        type base probability helpers.
"""

from .encoding import ( # Import base probability helpers
    PROB_AMP_SHIFT, PROB_AMP_MASK, MAX_PROB_AMP_INT,
    BASIS_STATE_SHIFT, BASIS_STATE_MASK, STATE_ZERO, STATE_ONE, (str): The type of Bell state correlation to simulate.
                    Supported: 'phi+' (|00>+|11>), 'phi-' (|00>-|11>),
                               'psi+' (|01>+|10>), 'psi-' (|01>-|10>).
                               Phase
    _int_to_probability, _probability_to_int,
    get_basis_state, get_probability_p1,
    set_basis_state, set_probability_p1
)

# --- Constants for Entanglement ID Bit Manipulation (16-bit) ---
ENT_ID_SHIFT = 2
ENT_ID_MASK = 0b1111 << ENT_ID_SHIFT  # Mask for bits 2, 3, 4, 5
MAX_ENT_ID = 15 # 0 means not entangled

# --- Entanglement ID Helper differences ('phi-'/'psi-') are currently ignored.

    Returns:
        tuple[int, int, str]: (qsim_int_A, qsim_int_B, pair_id)
                              The two integers representing the linked qubits and their shared ID.
    """
    if type not in ['phi+', 'phi-', 'psi+', 'psi-']:
        raise ValueError("Unsupported Bell state type")

    pair_id = _generate_pair_id()

    # Initialize both qubits. For Bell states, measuring one determines the other.
    # The internal probability before measurement should Functions ---

def get_entanglement_id(qsim_int: int) -> int:
    """Extracts the entanglement pair ID (0-15) from the integer representation."""
    return (qsim_int & ENT_ID_MASK) >> ENT_ID_SHIFT

def set_entanglement_id(qsim_int: int, pair_id: int) -> int:
    """
    Sets the entanglement pair ID bits (0-15) in the integer representation.
    ID 0 means not entangled.
    Returns a *new* integer with the updated ID.
    """
    if not (0 <= pair_id <= MAX_ENT_ID):
        raise ValueError(f"Entanglement pair ID must be between 0 and {MAX_ENT_ID}")

    # Clear the current ID bits
    cleared_int = qsim_int & ~ENT reflect equal chances.
    # We'll set both to P=0.5, phase=0 for simplicity. The correlation logic
    # is handled during the entangled measurement.
    # NOTE: This doesn't perfectly represent the superposition weights of |00>, |11> etc.
    qsim_int_A = initialize_phase_aware(STATE_ZERO, 0.0) # Start definite
    qsim_int_A = set_prob_and_phase(qsim_int_A, 0.5, 0.0) # Set to 50_ID_MASK
    # Set the new ID bits
    updated_int = cleared_int | (pair_id << ENT_ID_SHIFT)
    return updated_int

def is_entangled(qsim_int: int) -> bool:
    """Checks if the qubit has a non-zero entanglement ID."""
    return get_entanglement_id(qsim_int) > 0

def qsim_ent_repr(qsim_int: int) -> str:
    """Provides a human-readable string representation including entanglement ID."""
    basis = get_/50 superposition

    qsim_int_B = initialize_phase_aware(STATE_ZERO, 0.0)
    qsim_int_B = set_prob_and_phase(qsim_int_B, 0.5, 0.0)

    # TODO: Store pair_id *within* qsim_int_A and qsim_int_B using reserved bits.
    # This requires defining set_pair_id/get_pair_id in an encoding module.
    # For now, the link exists only in the registry.

    #basis_state(qsim_int)
    prob_p1 = get_probability_p1(qsim_int)
    prob_p0 = 1.0 - prob_p1
    ent_id = get_entanglement_id(qsim_int)

    state_str = f"|{basis}>" if prob_p1 in (0.0, 1.0) else "Superpos"
    ent_str = f"EntID={ent_id}" if ent_id > 0 else "NotEnt"

    # Basic representation
     Store the pair information
    entangled_pairs_registry[pair_id] = {
        'qA_ref': id(qsim_int_A), # Store object ID (won't work for updates) - illustrates limitation
        'qB_ref': id(qsim_int_Breturn (f"QSimE(Int={qsim_int:5d}, Bin={qsim_int:016b}, State={state_str}, "
            f"P0={prob_p0:.3f}, P1={prob_p1:.3f}, {),
        'bell_type': type
    }
    print(f"Debug: Created Bell pair {pair_id} type {type}. Registry: {entangled_pairs_registry}")


    # Problem: Need a way to associate the returned integers with the pair_id externally
    # or embedent_str})")
