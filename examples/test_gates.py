import pytest
from classical_quantum_sim import initialize, apply_H_sim, measure, qsim_repr, STATE_ZERO, STATE_ONE, get_probability_p1

def test_initialize_zero():
    q0 = initialize(STATE_ZERO)
    assert get_probability_p1(q0) == 0.0
    # Add check for basis state bit if relevant

def test_initialize_one():
    q1 = initialize(STATE_ONE)
    assert get_probability_p1(q1) == 1.0
    # Add check for basis state bit

def test_apply_h_sim_on_zero():
    q0 = initialize(STATE_ZERO)
    q_h = apply_H_sim(q0)
    # Use approx for floating point comparisons
    assert get_probability_p1(q_h) == pytest.approx(0.5)

def test_apply_h_sim_on_one():
    q1 = initialize(STATE_ONE)
    q_h = apply_H_sim(q1)
    assert get_probability_p1(q_h) == pytest.approx(0.5)

def test_measure_deterministic():
     # Test measuring a state already collapsed
     q1 = initialize(STATE_ONE)
     outcome, collapsed_q = measure(q1)
     assert outcome == STATE_ONE
     assert get_probability_p1(collapsed_q) == 1.0

# Add more tests for edge cases, multiple applications etc.
# Consider testing the qsim_repr output format if desired
