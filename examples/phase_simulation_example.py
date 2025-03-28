# examples/phase_simulation_example.py

"""
Demonstrates using Collapsed States (Entanglement Broken) ---
    # Use basic initializer which sets P=1.0 and resets reserved bits (including ID)
    collapsed_measured = initialize(basis_state=outcome_measured)
    collapsed_partner = initialize(basis_state=outcome_partner)

    return outcome_measured, collapsed_measured, collapsed_partner
