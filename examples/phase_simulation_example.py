# examples/phase_simulation_example.py

"""
Demonstrates usage of the phase-aware simulation modules.

Shows initializing a state, applying H, phase shifting, applying H again,
and measuring. Highlights how phase information is tracked and modified.

Note: Demonstrating true quantum interference typically requires multiple
qubits and gates like CNOT, which are not yet implemented. This example
primarily focuses on the API for phase manipulation.
"""

import math
# Import directly from the specific modules for clarity
from classical_quantum_sim import phase_gates
from classical_quantum_sim import phase_encoding
from classical_quantum_sim import STATE_ZERO # STATE_ZERO/ONE are in base encoding

print("--- Phase-Aware Simulation Example ---")

# 1. Initialize qubit in state |0> with default phase 0
q0 = phase_gates.initialize_phase_aware(STATE_ZERO, initial_phase_index=0)
print(f"1. Initial state (|0>, phase=0):")
print(f"   {phase_encoding.qsim_phase_repr(q0)}")

# 2. Apply phase-aware Hadamard gate
# H|0> -> Superposition with P=0.5, relative phase=0
q_h1 = phase_gates.apply_H_phase_aware(q0)
print(f"\n2. After first H gate:")
print(f"   {phase_encoding.qsim_phase_repr(q_h1)}")

# 3. Apply a Phase Shift gate (e.g., Z gate is P(pi))
# Let's apply pi radians (180 degrees, phase index delta = 8)
q_shifted = phase_gates.apply_PhaseShift_sim(q_h1, math.pi)
print(f"\n3. After Phase Shift (pi radians):")
print(f"   {phase_encoding.qsim_phase_repr(q_shifted)}")
# Note: The probability P(1)=0.5 remains unchanged, only the phase index changes.

# 4. Apply phase-aware Hadamard gate again
# H on |+> state with phase pi -> should ideally rotate to |1> state
# (Current H logic on superposition is simplified, result might vary)
q_h2 = phase_gates.apply_H_phase_aware(q_shifted)
print(f"\n4. After second H gate:")
print(f"   {phase_encoding.qsim_phase_repr(q_h2)}")
# Depending on the H implementation for superpositions, this might
# ideally result in a state close to |1> (P1=1.0). Check the output.

# 5. Measure the final state
print("\n5. Measuring the final state 10 times:")
final_state_to_measure = q_h2
counts = {0: 0, 1: 0}
for i in range(10):
    outcome, q_collapsed = phase_gates.measure_phase_aware(final_state_to_measure)
    counts[outcome] += 1
    if i < 3: # Print first few collapses
         print(f"   Measure {i+1}: Outcome={outcome}, Collapsed={phase_encoding.phase_qsim_repr(q_collapsed)}")

print(f"\n   Final Measurement Counts (10 trials): {counts}")
print("   (Expected outcome depends heavily on H logic for superpositions)")

print("\n--- Phase Demo Complete ---")
