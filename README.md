# 🚀 Closira AI Support Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-Customer%20Support-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/Assignment-Closira-red?style=for-the-badge)

### AI-Powered SMB Customer Support Workflow

An intelligent customer support assistant built for the **Closira AI Engineering Internship Assignment**.

</div>

---

# 📌 Overview

This project simulates an AI-powered customer support workflow for **Bloom Aesthetics Clinic**.

The assistant is capable of:

✅ SOP-based FAQ answering  
✅ Lead qualification  
✅ Escalation detection  
✅ Structured conversation summarization  
✅ Hallucination prevention  
✅ Safe AI response handling

The workflow is designed to mimic real SMB customer support operations across channels such as WhatsApp, email, and chat interfaces.

---

# 🧠 Core Features

## 1️⃣ SOP-Based FAQ Answering

The assistant answers customer questions strictly using predefined SOP data.

### Example

```text
Customer: What are your Botox prices?

AI: Our Botox prices start from £200.
```

### Safety Measures

- No hallucinated responses
- No unsupported claims
- SOP-grounded responses only
- Escalation instead of guessing

---

## 2️⃣ Lead Qualification

The assistant collects structured lead information during conversations.

### Questions Asked

- What type of business are you in?
- How large is your team?
- What tools are you currently using?

### Example Output

```text
Lead Details:
- Business Type: Healthcare
- Team Size: 20
- Current Tools: WhatsApp
```

---

## 3️⃣ Escalation Detection

The workflow automatically escalates conversations under risky or unsupported conditions.

### Escalation Triggers

| Trigger | Action |
|---|---|
| Out-of-scope query | Escalate |
| Complaint/anger | Escalate |
| Medical advice request | Escalate |
| Pricing negotiation | Escalate |
| Explicit human request | Escalate |

### Example

```text
AI: I could not find that information in our policy documents.
I will escalate this to a human representative.

[ESCALATION TRIGGERED]
Reason: Out-of-scope question
```

---

## 4️⃣ Conversation Summary Generation

At the end of each interaction, the system generates a structured summary.

### Example

```text
==============================
Conversation Summary
==============================

Customer Intent:
Customer asked about Botox pricing and booking.

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

# 🏗️ System Architecture

```text
             ┌──────────────────┐
             │   User Query     │
             └────────┬─────────┘
                      │
                      ▼
          ┌──────────────────────┐
          │ FAQ / SOP Handler    │
          └────────┬─────────────┘
                   │
                   ▼
        ┌─────────────────────────┐
        │ Escalation Detection    │
        └────────┬────────────────┘
                 │
                 ▼
       ┌──────────────────────────┐
       │ Lead Qualification       │
       └────────┬─────────────────┘
                │
                ▼
      ┌───────────────────────────┐
      │ Conversation Summary      │
      └───────────────────────────┘
```

---

# 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Groq API | LLM inference |
| dotenv | Environment variable management |
| VS Code | Development environment |
| Git & GitHub | Version control |

---

# 📂 Project Structure

```text
closira-ai-support-agent/
│
├── agents/
├── data/
├── prompts/
├── test_transcripts/
├── utils/
│
├── app.py
├── requirements.txt
├── README.md
├── prompt_design.md
├── conversation_log.txt
└── conversation_summary.txt
```

---

# 📋 SOP Data Used

## 🏥 Bloom Aesthetics Clinic

### Services
- Botox (from £200)
- Fillers (from £250)
- Free consultations

### Working Hours
- Monday to Saturday
- 9 AM to 7 PM

### Booking Methods
- WhatsApp
- Website

### Cancellation Policy
- 24-hour cancellation notice required

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Mohit-1307/closira-ai-support-agent.git
```

Move into project folder:

```bash
cd closira-ai-support-agent
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Run Application

```bash
python app.py
```

---

# 🧪 Test Scenarios Implemented

| Scenario | Status |
|---|---|
| FAQ Answering | ✅ |
| Out-of-Scope Handling | ✅ |
| Escalation Detection | ✅ |
| Lead Qualification | ✅ |
| Conversation Summary | ✅ |

All transcripts are available inside:

```text
test_transcripts/
```

---

# 🛡️ Hallucination Prevention

The assistant is explicitly instructed to:

- Answer strictly from SOP data
- Avoid assumptions
- Refuse unsupported queries
- Escalate instead of guessing

This ensures safe and reliable customer communication.

---

# 📈 Example Workflow

```text
Customer: What are your botox prices?

AI: Our Botox prices start from £200.

Customer: How can I book an appointment?

AI: You can book an appointment via WhatsApp or our website.

--- Lead Qualification ---

AI: What type of business are you in?

Customer: Healthcare

AI: How large is your team?

Customer: 20

AI: What tools are you currently using?

Customer: WhatsApp
```

---

# 🎯 Assignment Requirements Covered

| Requirement | Status |
|---|---|
| FAQ Answering | ✅ |
| Lead Qualification | ✅ |
| Escalation Detection | ✅ |
| Conversation Summary | ✅ |
| Prompt Design Documentation | ✅ |
| Test Transcripts | ✅ |

---

# 👨‍💻 Author

## Mohit

Machine Learning & AI Engineering Enthusiast

Focused on building reliable AI systems, intelligent workflows, and practical machine learning applications.

---

<div align="center">

### ⭐ If you found this project interesting, feel free to star the repository ⭐

</div>