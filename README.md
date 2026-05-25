<div align="center">

# Closira AI Support Agent

[![Python](https://img.shields.io/badge/Python-3.10+-3670A0?style=flat-square&logo=python&logoColor=ffdd54)](https://python.org)
[![Groq](https://img.shields.io/badge/Groq-LLM%20Inference-FF6B35?style=flat-square)](https://groq.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Status](https://img.shields.io/badge/Status-Completed-2ea44f?style=flat-square)]()
[![Assignment](https://img.shields.io/badge/Closira-AI%20Internship%20Assignment-6f42c1?style=flat-square)]()

**An intelligent, SOP-grounded customer support agent for SMBs — built for the Closira AI Engineering Internship.**

[Overview](#-overview) · [Features](#-core-features) · [Architecture](#-architecture) · [Setup](#-installation) · [Usage](#-usage)

</div>

---

## Overview

This project implements an AI-powered customer support workflow for **Bloom Aesthetics Clinic**, demonstrating a production-style conversational agent that operates strictly within defined business rules.

The agent handles the complete support lifecycle — from answering FAQs to qualifying leads, detecting escalations, and generating structured conversation summaries — without hallucinating or going beyond its knowledge boundary.

**Capabilities at a glance:**

| Capability | Description |
|---|---|
| FAQ Answering | Responds strictly from SOP/policy data |
| Lead Qualification | Collects structured business information |
| Escalation Detection | Flags risky or out-of-scope conversations |
| Conversation Summary | Generates structured end-of-session reports |
| Hallucination Prevention | Refuses unsupported claims; escalates instead |
| Streamlit UI | Interactive real-time chat frontend |

---

## Core Features

### 1 · SOP-Based FAQ Answering

All responses are grounded strictly in predefined SOP data. The agent never speculates or fabricates information.

```text
Customer : What are your Botox prices?
Agent    : Botox starts from £200. Would you like to book a free consultation?
```

**Guardrails enforced:**
- No hallucinated or assumed responses
- Out-of-scope queries trigger escalation, not guessing
- Responses traceable to SOP source

---

### 2 · Lead Qualification

The agent collects structured lead data during natural conversation flow.

```text
Agent    : To help you better — what type of business are you in?
Customer : Healthcare

Agent    : How large is your team?
Customer : 20

Agent    : What tools are you currently using?
Customer : WhatsApp

Agent    : ✅ Lead Qualification Complete

Lead Summary
─────────────────────────
Business Type  : Healthcare
Team Size      : 20
Current Tools  : WhatsApp
```

---

### 3 · Escalation Detection

Automatic escalation triggers protect both the customer and the business from inappropriate AI responses.

| Trigger | Action |
|---|---|
| Out-of-scope query | Escalate to human |
| Complaint / anger | Escalate to human |
| Medical advice request | Escalate to human |
| Pricing negotiation | Escalate to human |
| Explicit human request | Escalate to human |

```text
Agent : I couldn't find that in our policy documents.
        Escalating this to a human representative now.

        [ESCALATION TRIGGERED]
        Reason: Out-of-scope question
```

---

### 4 · Conversation Summary

A structured summary is generated at the end of each session.

```text
══════════════════════════════════════
           Conversation Summary
══════════════════════════════════════

Customer Intent    : Pricing inquiry and appointment booking
Business Type      : Healthcare
Team Size          : 20
Current Tools      : WhatsApp
Escalation Status  : None
Next Action        : Continue customer onboarding
```

---

### 5 · Streamlit Frontend

An interactive chat interface for real-time testing and demonstration.

**Features:** Typing animation · Lead qualification flow · Escalation handling · Summary generation · Localhost deployment

```bash
streamlit run streamlit.py
# Opens at → http://localhost:8501
```

---

## Architecture

```
User Query
    │
    ▼
┌─────────────────────┐
│   FAQ / SOP Handler  │  ← Groq LLM + SOP context
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Escalation Detector  │  ← Rule-based + LLM classification
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Lead Qualifier      │  ← Structured data collection
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Summary Generator    │  ← End-of-session structured report
└─────────────────────┘
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| LLM Inference | Groq API |
| Frontend | Streamlit |
| Environment Config | python-dotenv |
| Version Control | Git & GitHub |
| IDE | VS Code |

---

## Project Structure

```
closira-ai-support-agent/
│
├── agents/                  # Core agent logic
├── data/                    # SOP and clinic data
├── prompts/                 # System prompt templates
├── test_transcripts/        # Test conversation logs
├── utils/                   # Helper utilities
│
├── app.py                   # CLI entry point
├── streamlit.py             # Streamlit frontend
├── prompt_design.md         # Prompt engineering documentation
├── conversation_log.txt     # Runtime conversation log
├── conversation_summary.txt # Generated session summaries
├── requirements.txt
└── README.md
```

---

## SOP Reference — Bloom Aesthetics Clinic

| Category | Details |
|---|---|
| **Services** | Botox (from £200), Fillers (from £250), Free consultations |
| **Hours** | Monday – Saturday, 9 AM – 7 PM |
| **Booking** | WhatsApp, Website |
| **Cancellation** | 24-hour notice required |

---

## Installation

### 1 · Clone the Repository

```bash
git clone https://github.com/Mohit-1307/closira-ai-support-agent.git
cd closira-ai-support-agent
```

### 2 · Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3 · Install Dependencies

```bash
pip install -r requirements.txt
```

### 4 · Configure Environment

```bash
# Create .env file
echo "GROQ_API_KEY=your_api_key_here" > .env
```

---

## Usage

### CLI Mode

```bash
python app.py
```

### Streamlit UI

```bash
streamlit run streamlit.py
```

---

## Test Coverage

| Scenario | Status |
|---|---|
| FAQ Answering | ✅ Passing |
| Out-of-Scope Handling | ✅ Passing |
| Escalation Detection | ✅ Passing |
| Lead Qualification | ✅ Passing |
| Conversation Summary | ✅ Passing |

Full transcripts available in `test_transcripts/`.

---

## Assignment Requirements

| Requirement | Delivered |
|---|---|
| FAQ Answering | ✅ |
| Lead Qualification | ✅ |
| Escalation Detection | ✅ |
| Conversation Summary | ✅ |
| Prompt Design Documentation | ✅ |
| Test Transcripts | ✅ |

---

## Author

**MOHIT SINGH RAJPUT** — AI / ML Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/mohitsingh1307)
[![GitHub](https://img.shields.io/badge/GitHub-121011?style=flat-square&logo=github&logoColor=white)](https://github.com/Mohit-1307)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://www.kaggle.com/mohitsinghrajput1307)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:mohitsinghdausa@gmail.com)

---

<div align="center">

*If this project was useful or interesting, a ⭐ on the repository is appreciated.*

</div>
