# AI Customer Support Workflow

## Overview

This project is a Python-based AI customer support workflow for Bloom Aesthetics Clinic.

The system demonstrates:

- FAQ Answering
- Lead Qualification
- Escalation Detection
- Conversation Summarization

## Features

### 1. FAQ Answering
The AI answers questions only from SOP data.
Hallucination prevention is enforced.

### 2. Lead Qualification
The AI asks structured lead qualification questions.

### 3. Escalation Detection
The system escalates when:
- User is angry
- User asks medical questions
- User requests a human
- Question is outside SOP

### 4. Conversation Summary
The workflow generates a structured conversation summary.

---

## Installation

### Step 1

Clone repository:

```bash
git clone <your_repo_link>


### Step 2

Install dependencies:
    pip install -r requirements.txt


### Step 3

Create .env file:
    OPENAI_API_KEY=your_key_here


### Step 4

Run application:
    python app.py


## Example Questions

-> What are your Botox prices?
-> How can I book?
-> Do you provide laser surgery?
-> I am unhappy with your service.


## Known Limitations

-> Uses keyword-based escalation
-> No frontend UI
-> No persistent database
-> CLI-based interaction only


## Tech Stack

-> Python
-> OpenAI API
-> GPT-4o-mini


# 13. prompt_design.md

## Prompt Design Documentation

### System Prompt

The system prompt instructs the AI to:

-> Answer ONLY using SOP information
-> Avoid hallucinations
-> Escalate when uncertain
-> Maintain professional SMB customer support tone

### Main prompt:

```txt
-> You are an AI assistant for Bloom Aesthetics Clinic.
-> You MUST answer ONLY using the SOP below.
-> Do NOT make up information.
-> If information is missing, escalate to a human representative.


# Hallucination Prevention

## Hallucination prevention was implemented through:

-> Explicit prompt instruction
-> SOP grounding
-> Temperature set to 0
-> Escalation fallback for unknown questions

The AI is forbidden from generating unsupported information.


# Confidence-Based Escalation

## Escalation is triggered when:

-> AI cannot find information in SOP
-> Customer sentiment is negative
-> Medical questions appear
-> Customer requests human support
-> Pricing negotiation occurs

Keyword-based escalation logic is used.


# Tone and Persona

## The assistant uses:

-> Friendly tone
-> Professional customer support communication
-> Short and clear responses
-> Safe fallback behavior

The tone is designed for SMB customer interactions.


# 14. Test Transcripts

## faq_test.md

```md


# FAQ Test

Customer: What are your Botox prices?

AI: Botox services start from £200.


# out_of_scope_test.md

## Out of Scope Test

Customer: Do you offer laser treatment?

AI: I could not find that information in our policy documents. I will escalate this to a human representative.

[ESCALATION TRIGGERED]
Reason: Out-of-scope question


# escalation_test.md

## Escalation Test

Customer: I am very angry about your service.

AI: I understand your frustration. I will escalate this issue to a human representative.

[ESCALATION TRIGGERED]
Reason: Customer frustration or complaint


# qualification_test.md