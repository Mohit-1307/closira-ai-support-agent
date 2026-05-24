import streamlit as st
import time

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Closira AI Support Agent",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# SOP DATA
# =====================================================

SOP = {
    "botox": "Botox starts from £200.",
    "fillers": "Fillers start from £250.",
    "consultation": "Consultations are free.",
    "booking": "You can book an appointment via WhatsApp or our website.",
    "hours": "Mon–Sat, 9 am–7 pm.",
    "cancellation": "24-hour cancellation notice is required."
}

# =====================================================
# SESSION STATE
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "lead_step" not in st.session_state:
    st.session_state.lead_step = 0

if "lead_data" not in st.session_state:
    st.session_state.lead_data = {}

if "escalation_reason" not in st.session_state:
    st.session_state.escalation_reason = None

# =====================================================
# UI
# =====================================================

st.title("🤖 Closira AI Support Agent")

st.markdown("AI-powered SMB customer support workflow")

# =====================================================
# DISPLAY CHAT
# =====================================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =====================================================
# FAQ ANSWERING
# =====================================================

def answer_from_sop(user_input):

    # RESET ESCALATION FOR VALID SOP QUESTIONS
    st.session_state.escalation_reason = None

    text = user_input.lower()

    # Botox
    if "botox" in text:
        return SOP["botox"]

    # Fillers
    elif "filler" in text:
        return SOP["fillers"]

    # Consultation
    elif "consultation" in text:
        return SOP["consultation"]

    # Booking
    elif "book" in text or "appointment" in text:

        st.session_state.lead_step = 1

        return (
            f"{SOP['booking']}\n\n"
            "To help you better, what type of business are you in?"
        )

    # Working Hours
    elif "hours" in text or "open" in text:
        return SOP["hours"]

    # Cancellation
    elif "cancel" in text:
        return SOP["cancellation"]

    return None

# =====================================================
# ESCALATION DETECTION
# =====================================================

def detect_escalation(user_input):

    escalation_words = [
        "angry",
        "complaint",
        "refund",
        "manager",
        "lawsuit",
        "human",
        "frustrated"
    ]

    text = user_input.lower()

    for word in escalation_words:

        if word in text:

            st.session_state.escalation_reason = word

            return True

    return False

# =====================================================
# LEAD QUALIFICATION
# =====================================================

def handle_lead_qualification(user_input):

    # STEP 1
    if st.session_state.lead_step == 1:

        st.session_state.lead_data["business_type"] = user_input

        st.session_state.lead_step = 2

        return "How large is your team?"

    # STEP 2
    elif st.session_state.lead_step == 2:

        st.session_state.lead_data["team_size"] = user_input

        st.session_state.lead_step = 3

        return "What tools are you currently using?"

    # STEP 3
    elif st.session_state.lead_step == 3:

        st.session_state.lead_data["current_tools"] = user_input

        st.session_state.lead_step = 0

        return f"""
✅ Lead Qualification Complete

### Qualification Summary

- Business Type: {st.session_state.lead_data['business_type']}
- Team Size: {st.session_state.lead_data['team_size']}
- Current Tools: {st.session_state.lead_data['current_tools']}
"""

# =====================================================
# MAIN WORKFLOW
# =====================================================

def ai_workflow(user_input):

    # =================================================
    # CONTINUE LEAD QUALIFICATION
    # =================================================

    if st.session_state.lead_step > 0:

        return handle_lead_qualification(user_input)

    # =================================================
    # ESCALATION DETECTION
    # =================================================

    if detect_escalation(user_input):

        return f"""
🚨 Conversation Escalated

Reason: {st.session_state.escalation_reason}

A human support agent will contact you shortly.
"""

    # =================================================
    # SOP ANSWERING
    # =================================================

    sop_response = answer_from_sop(user_input)

    if sop_response:
        return sop_response

    # =================================================
    # OUT OF SCOPE
    # =================================================

    st.session_state.escalation_reason = "Out-of-scope question"

    response = """
⚠️ I could not find that information in our policy documents.

I will escalate this to a human representative.

[ESCALATION TRIGGERED]
Reason: Out-of-scope question
"""

    return response

# =====================================================
# CHAT INPUT
# =====================================================

prompt = st.chat_input("Ask your question...")

# =====================================================
# HANDLE INPUT
# =====================================================

if prompt:

    # USER MESSAGE
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI RESPONSE
    response = ai_workflow(prompt)

    with st.chat_message("assistant"):

        placeholder = st.empty()

        full_response = ""

        for word in response.split():

            full_response += word + " "

            time.sleep(0.02)

            placeholder.markdown(full_response + "▌")

        placeholder.markdown(full_response)

    # SAVE RESPONSE
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
    })

# =====================================================
# SUMMARY
# =====================================================

st.markdown("---")

if st.button("Generate Conversation Summary"):

    customer_intent = "N/A"

    if len(st.session_state.messages) > 0:
        customer_intent = st.session_state.messages[0]["content"]

    escalation_status = (
        st.session_state.escalation_reason
        if st.session_state.escalation_reason
        else "No escalation"
    )

    next_action = (
        "Human follow-up required."
        if st.session_state.escalation_reason
        else "Continue onboarding process."
    )

    st.markdown(f"""
# Conversation Summary

### Customer Intent

{customer_intent}

---

### Lead Details

- Business Type: {st.session_state.lead_data.get("business_type", "N/A")}
- Team Size: {st.session_state.lead_data.get("team_size", "N/A")}
- Current Tools: {st.session_state.lead_data.get("current_tools", "N/A")}

---

### Escalation Status

{escalation_status}

---

### Recommended Next Action

{next_action}
""")