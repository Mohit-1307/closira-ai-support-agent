# Closira AI Support Agent

## Overview

This project is a Python-based AI customer support workflow built for the fictional SMB:

**Bloom Aesthetics Clinic**

The system demonstrates:

- FAQ Answering
- Lead Qualification
- Escalation Detection
- Conversation Summarization

The workflow simulates real-world SMB customer support interactions using an LLM-powered assistant.

---

# Features

## 1. FAQ Answering

The AI answers customer questions strictly using SOP data.

Hallucination prevention is enforced to ensure the assistant does not generate unsupported information.

---

## 2. Lead Qualification

The assistant asks structured lead qualification questions such as:

- Business type
- Team size
- Current tools being used

The responses are collected and summarized.

---

## 3. Escalation Detection

The system escalates conversations when:

- Customer sentiment is negative
- Customer asks medical questions
- Customer requests human support
- Customer asks out-of-scope questions
- Pricing negotiation is detected

Escalation reasons are logged and included in the final summary.

---

## 4. Conversation Summary

At the end of each session, the workflow generates a structured summary containing:

- Customer intent
- Lead qualification details
- Escalation status
- Recommended next action

---

# Project Structure

```text
closira-ai-support-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── prompt_design.md
├── .gitignore
│
├── data/
│   └── sop.json
│
├── prompts/
│   └── system_prompt.txt
│
├── agents/
│   ├── faq_agent.py
│   ├── qualification_agent.py
│   ├── escalation_agent.py
│   └── summary_agent.py
│
├── utils/
│   └── logger.py
│
└── test_transcripts/
    ├── faq_test.md
    ├── escalation_test.md
    ├── out_of_scope_test.md
    ├── qualification_test.md
    └── summary_test.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Mohit-1307/closira-ai-support-agent
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_api_key_here
```

---

## 5. Run the Application

```bash
python app.py
```

---

# Example Questions

## In-Scope Questions

- What are your Botox prices?
- How can I book an appointment?
- What are your clinic hours?

## Out-of-Scope Questions

- Do you provide laser surgery?
- Can I negotiate the price?
- Is Botox safe during pregnancy?

---

# Example Workflow

```text
Customer Question
        ↓
FAQ Answering
        ↓
Escalation Detection
        ↓
Lead Qualification
        ↓
Conversation Summary
```

---

# Hallucination Prevention

The system prevents hallucinations through:

- SOP-grounded responses
- Explicit system prompt constraints
- Temperature set to 0
- Escalation fallback for unsupported questions

The assistant never invents business information outside the SOP.

---

# Technologies Used

- Python
- Groq API
- Llama 3.3 70B Versatile
- OpenAI Python SDK
- python-dotenv

---

# Known Limitations

- Uses keyword-based escalation logic
- CLI-based interaction only
- No persistent database
- No frontend UI
- Limited sentiment analysis

---

# Future Improvements

Possible future improvements include:

- Advanced sentiment analysis
- Vector database retrieval
- Web-based frontend
- Persistent conversation storage
- Better lead scoring

---

# Test Scenarios Implemented

The project includes test transcripts for:

- FAQ answering
- Out-of-scope escalation
- Complaint escalation
- Lead qualification
- Conversation summary generation

---

# Sample Interaction

```text
Customer: What are your Botox prices?

AI: Our Botox prices start from £200.

Customer: How can I book an appointment?

AI: You can book an appointment via WhatsApp or our website.

--- Lead Qualification ---

What type of business are you in?
Healthcare

How large is your team?
20

What tools are you currently using?
WhatsApp

==============================
Conversation Summary
==============================

Customer Intent:
What are your Botox prices?

Lead Details:
- Business Type: Healthcare
- Team Size: 20
- Current Tools: WhatsApp

Escalation Status:
No escalation

Recommended Next Action:
Continue customer onboarding process.
```

---

# Author

Mohit