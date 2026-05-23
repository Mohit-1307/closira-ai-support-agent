def generate_summary(conversation_history, lead_data, escalation_reason):
    summary = f"""
==============================
Conversation Summary
==============================

Customer Intent:
{conversation_history[0]['user']}

Lead Details:
- Business Type: {lead_data.get('business_type', 'N/A')}
- Team Size: {lead_data.get('team_size', 'N/A')}
- Current Tools: {lead_data.get('current_tools', 'N/A')}

Escalation Status:
{escalation_reason}

Recommended Next Action:
{"Human follow-up required." if escalation_reason != "No escalation" else "Continue customer onboarding process."}

==============================
"""

    return summary