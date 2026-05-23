lead_questions = [
    "What type of business are you in?",
    "How large is your team?",
    "What tools are you currently using?"
]


def qualify_lead():
    lead_data = {}

    print("\n--- Lead Qualification ---")

    lead_data["business_type"] = input(lead_questions[0] + " ")
    lead_data["team_size"] = input(lead_questions[1] + " ")
    lead_data["current_tools"] = input(lead_questions[2] + " ")

    return lead_data