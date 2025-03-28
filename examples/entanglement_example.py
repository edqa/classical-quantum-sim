# examples/entanglement_example.py

"""
Demonstrates simulating entanglement correlation using the entanglement module.

1. Creates a simulated Bell pair (classically correlated).
2. Measures one qubit using the specialized `measure_entangled` function.
3. Shows that the partner qubit's state collapses instantly to the correlated state.
4. Verifies that entanglement ID is reset after measurement.

NOTE: This uses the `entanglement_encoding` which assumes the Entanglement ID
      is stored in bits 2-5 (conflicting with simultaneous phase encoding).
      Choose the appropriate encoding/module based on your simulation needs.
"""

# Import directly from the specific modules
from classical_quantum_sim import entanglement
from classical_quantum_sim import entanglement_encoding # Using ID in bits 2-5

print("--- Entanglement Simulation (Classical Correlation) Example ---")

# 1. Create a simulated Bell pair ('phi+' means outcomes should be correlated: 00 or 11)
print("1. Creating Bell Pair (Type: 'phi+')...")
qA, qB = entanglement.create_bell_pair_sim(state_type='phi+')

print(f"   Initial Qubit A: {entanglement_encoding.qsim_ent_repr(qA)}")
print(f"   Initial Qubit B: {entanglement_encoding.qsim_ent_repr(qB)}")
ent_id_A = entanglement_encoding.get_entanglement_id(qA)
ent_id_B = entanglement_encoding.get_entanglement_id(qB)
print(f"   Entanglement IDs: A={ent_id_A}, B={ent_id_B} (Should be same and > 0)")
print("-" * 20)

# 2. Measure Qubit A using the specialized function
print(f"2. Measuring Qubit A (using specialized measure_entangled)...")
# We need to pass *both* qubit integers to the measurement function
outcome_A, collapsed_A, collapsed_B = entanglement.measure_entangled(
    measured_int=qA,
    partner_int=qB,
    state_type='phi+' # Must match the creation type for correct correlation
)

# Update the variables holding the qubit states to reflect the collapse
qA = collapsed_A
qB = collapsed_B

print(f"\n   Outcome of measuring A: {outcome_A}")
print(f"   State of A after measurement: {entanglement_encoding.qsim_ent_repr(qA)}")
print(f"   State of B after A's measurement: {entanglement_encoding.qsim_ent_repr(qB)}")

# 3. Verify Correlation and Entanglement Breaking
print("\n3. Verifying results...")
ent_id_A_after = entanglement_encoding.get_entanglement_id(qA)
ent_id_B_after = entanglement_encoding.get_entanglement_id(qB)
basis_A = entanglement_encoding.get_basis_state(qA)
basis_B = entanglement_encoding.get_basis_state(qB)

print(f"   Entanglement IDs after measurement: A={ent_id_A_after}, B={ent_id_B_after} (Should both be 0)")
print(f"   Basis state of A: |{basis_A}>")
print(f"   Basis state of B: |{basis_B}>")

if basis_A == basis_B:
    print("   CORRECT: Outcomes are correlated (both 0 or both 1) as expected for 'phi+' state.")
else:
    print("   ERROR: Outcomes are NOT correlated for 'phi+' state!")

if ent_id_A_after == 0 and ent_id_B_after == 0:
    print("   CORRECT: Entanglement IDs were reset to 0 after measurement.")
else:
    print("   ERROR: Entanglement IDs were not reset!")

print("\n--- Entanglement Demo Complete ---")
