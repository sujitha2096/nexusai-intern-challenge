from dataclasses import dataclass

@dataclass
class CustomerContext:
    is_vip: bool
    billing_overdue: bool
    ticket_history: list  # List of strings (e.g., ["slow_internet", "billing_error"])
    data_complete: bool

def should_escalate(context, confidence, sentiment, intent):
    # Rule 1: Confidence below 0.65
    if confidence < 0.65:
        return True, "low_confidence"

    # Rule 2: Sentiment below -0.6
    if sentiment < -0.6:
        return True, "angry_customer"

    # Rule 3: Repeat intent (3 or more times)
    if context.ticket_history.count(intent) >= 3:
        return True, "repeat_complaint"

    # Rule 4: Service cancellation
    if intent == "service_cancellation":
        return True, "service_cancellation"

    # Rule 5: VIP AND billing overdue
    if context.is_vip and context.billing_overdue:
        return True, "vip_billing_issue"

    # Rule 6: Incomplete data AND confidence below 0.80
    if not context.data_complete and confidence < 0.80:
        return True, "incomplete_data_escalation"

    return False, "handle_by_ai"