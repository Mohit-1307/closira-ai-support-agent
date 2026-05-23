ESCALATION_KEYWORDS = [
    "angry",
    "complaint",
    "terrible",
    "refund",
    "manager",
    "human",
    "lawsuit",
    "bad service",
    "frustrated"
]


MEDICAL_KEYWORDS = [
    "pain",
    "reaction",
    "infection",
    "medical",
    "swelling"
]


NEGOTIATION_KEYWORDS = [
    "discount",
    "cheaper",
    "lower price",
    "special deal"
]


def check_escalation(user_message, ai_response):
    message = user_message.lower()

    for word in ESCALATION_KEYWORDS:
        if word in message:
            return True, "Customer frustration or complaint"

    for word in MEDICAL_KEYWORDS:
        if word in message:
            return True, "Medical question detected"

    for word in NEGOTIATION_KEYWORDS:
        if word in message:
            return True, "Pricing negotiation detected"

    if "I could not find" in ai_response:
        return True, "Out-of-scope question"

    return False, "No escalation needed"