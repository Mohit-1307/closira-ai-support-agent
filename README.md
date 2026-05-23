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