# examples/basic_measurement.py

"""
Demonstrates the basic usage of the classical quantum simulator:
1. Initialize a qubit in state |0>.
2. Apply a simulated Hadamard gate to create superposition.
3. Measure the qubit multiple times.
4. Observe the probabilistic outcomes (should be approx 50/50).
"""

# IMPORTANT: Assumes you have installed the package in editable mode
# (pip install -e .) from the project root,
# OR your PYTHONPATH is set up correctly to find the 'src' directory.
try:
    from classical_quantum_sim import (
        initialize, apply_H_sim, measure,
        STATE_ZERO, qsim_repr
    )
except ImportError:
    print("ERROR: Could not import classical_quantum_sim.")
    print("Please ensure the package is installed (e.g., 'pip install -e .')")
    print("or your PYTHONPATH is configured correctly.")
    exit()


# --- Simulation Parameters ---
num_measurements = 10000

# --- Simulation ---
print("--- Classical Quantum Simulation Demo ---")

# 1. Initialize qubit in state |0>
q_initial = initialize(STATE_ZERO)
print(f"Initial state: {qsim_repr(q_initial)}")

# 2. Apply simulated Hadamard gate
q_superposition = apply_H_sim(q_initial)
print(f"After H gate:  {qsim_repr(q_superposition)}")
print("-" * 30)

# 3. Perform multiple measurements
print(f"Performing {num_measurements} measurements...")
counts = {0: 0, 1: 0}
for i in range(num_measurements):
    # IMPORTANT: Always measure the *superposition* state, not the collapsed one from previous loop
    outcome, q_collapsed = measure(q_superposition)
    counts[outcome] += 1
    # Optional: print the state after collapse
    # if i < 5: # Print first few collapses
    #    print(f"  Measurement {i+1}: Outcome={outcome}, Collapsed state={qsim_repr(q_collapsed)}")


# 4. Display results
print("-" * 30)
print("Measurement Results:")
print(f"  Count(|0>): {counts[0]}")
print(f"  Count(|1>): {counts[1]}")

total = counts[0] + counts[1]
if total > 0:
    percent_0 = (counts[0] / total) * 100
    percent_1 = (counts[1] / total) * 100
    print(f"  Percentage(|0>): {percent_0:.2f}%")
    print(f"  Percentage(|1>): {percent_1:.2f}%")
print("-" * 30)
print("Simulation Complete. Expect approx 50% for |0> and |1>.")