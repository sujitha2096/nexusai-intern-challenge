import pytest
from task4.escalation import should_escalate, CustomerContext

def test_rule_1_low_confidence():
    """Tests if confidence below 0.65 triggers escalation."""
    ctx = CustomerContext(False, False, [], True)
    should, reason = should_escalate(ctx, 0.60, 0.0, "general_query")
    assert should is True
    assert reason == "low_confidence"

def test_rule_4_cancellation():
    """Tests if service_cancellation always escalates."""
    ctx = CustomerContext(False, False, [], True)
    should, reason = should_escalate(ctx, 0.95, 0.5, "service_cancellation")
    assert should is True
    assert reason == "service_cancellation"

# You can add 6 more tests for the other rules!