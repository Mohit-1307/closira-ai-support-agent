from dotenv import load_dotenv

from agents.faq_agent import answer_question
from agents.qualification_agent import qualify_lead
from agents.escalation_agent import check_escalation
from agents.summary_agent import generate_summary
from utils.logger import log_event

load_dotenv()

conversation_history = []
lead_data = {}
escalation_reason = "No escalation"

print("==============================")
print("Bloom Aesthetics Clinic AI")
print("Type 'exit' to end conversation")
print("==============================")

while True:
    user_message = input("\nCustomer: ")

    if user_message.lower() == "exit":
        break

    ai_response = answer_question(user_message)

    print("\nAI:", ai_response)

    conversation_history.append({
        "user": user_message,
        "assistant": ai_response
    })

    log_event(f"Customer: {user_message}")
    log_event(f"AI: {ai_response}")

    escalated, reason = check_escalation(user_message, ai_response)

    if escalated:
        escalation_reason = reason

        print("\n[ESCALATION TRIGGERED]")
        print("Reason:", reason)

        log_event(f"Escalation: {reason}")

        summary = generate_summary(
            conversation_history,
            lead_data,
            escalation_reason
        )

        print(summary)

        with open("conversation_summary.txt", "w") as file:
            file.write(summary)

        exit()

    # Trigger lead qualification after 2 interactions
    if len(conversation_history) >= 2:
        lead_data = qualify_lead()
        break

# Final summary for normal conversations
summary = generate_summary(
    conversation_history,
    lead_data,
    escalation_reason
)

print(summary)

with open("conversation_summary.txt", "w") as file:
    file.write(summary)