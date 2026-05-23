<!-- # Closira AI Support Agent

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

Mohit -->


# Closira AI Support Agent

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Groq API](https://img.shields.io/badge/Groq-LLM-green)
![Llama 3.3](https://img.shields.io/badge/Model-Llama3.3--70B-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# Overview

Closira AI Support Agent is a Python-based AI customer support workflow built for the fictional SMB:

## Bloom Aesthetics Clinic

The system simulates real-world SMB customer support interactions using an LLM-powered assistant.

The workflow demonstrates:

- FAQ Answering
- Lead Qualification
- Escalation Detection
- Conversation Summarization
- SOP-Grounded AI Responses
- Hallucination Prevention

---

# Features

## 1. FAQ Answering

The assistant answers customer questions strictly using SOP data.

Responses are grounded in business-defined policies to prevent unsupported information generation.

### Example

```text
Customer: What are your Botox prices?

AI: Our Botox prices start from £200.
```

---

## 2. Lead Qualification

The assistant asks structured lead qualification questions such as:

- Business type
- Team size
- Current tools being used

The collected information is included in the final conversation summary.

---

## 3. Escalation Detection

The system escalates conversations when:

- Customer sentiment is negative
- Customer asks medical questions
- Customer requests human support
- Customer asks out-of-scope questions
- Pricing negotiation is detected

### Example

```text
Customer: Do you provide laser surgery?

AI: I could not find that information in our policy documents.
I will escalate this to a human representative.
```

---

## 4. Conversation Summary

At the end of each session, the workflow generates a structured summary containing:

- Customer intent
- Lead qualification details
- Escalation status
- Recommended next action

---

# System Architecture

The workflow follows a modular agent-based pipeline:

```text
Customer Input
        ↓
FAQ Agent
        ↓
Escalation Detection
        ↓
Lead Qualification
        ↓
Conversation Summary
```

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

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Groq API | LLM inference |
| Llama 3.3 70B Versatile | Conversational AI model |
| OpenAI Python SDK | API integration |
| python-dotenv | Environment variable management |
| Git & GitHub | Version control |

---

# Engineering Concepts Demonstrated

This project demonstrates:

- Prompt Engineering
- SOP-Grounded AI Responses
- Hallucination Prevention
- Agentic Workflow Design
- Escalation Handling
- Multi-step Conversational Flow
- Modular Python Architecture
- Structured Logging
- LLM Safety Constraints

---

# AI Safety Measures

The system includes multiple safeguards:

- SOP-grounded answering
- Explicit hallucination prevention prompts
- Escalation fallback for unsupported queries
- Temperature set to 0 for deterministic responses
- Restricted response generation

The assistant never invents business information outside the SOP.

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Mohit-1307/closira-ai-support-agent.git
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

# Test Scenarios Implemented

The project includes test transcripts for:

- FAQ answering
- Out-of-scope escalation
- Complaint escalation
- Lead qualification
- Conversation summary generation

---

# Known Limitations

- Uses keyword-based escalation logic
- CLI-based interaction only
- No persistent database
- No frontend UI
- Limited sentiment analysis

---

# Future Improvements

Potential future enhancements include:

- Semantic search with vector databases
- RAG-based document retrieval
- Advanced sentiment analysis
- Persistent customer memory
- Streamlit or React frontend
- Multi-channel integration (WhatsApp/Email)
- Conversation analytics dashboard
- Fine-tuned escalation classification

---

# Demo

The project demonstrates:

- SOP-based customer support
- Safe response generation
- Escalation handling
- Lead qualification
- Structured conversation summaries

---

# Author

Mohit  
Machine Learning & AI Engineering Enthusiast