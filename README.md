# Flowbit Assignment – Multi-Agent AI System

## Objective

Build a multi-agent AI system that classifies incoming files (PDF, JSON, Email), detects intent (Invoice, RFQ, Complaint, etc.), routes them to the appropriate agent, and logs extracted data and metadata into a shared memory store (SQLite). The system ensures full traceability with unique thread IDs.

---

## System Overview

### 1. Classifier Agent
- Accepts raw input (file/text)
- Classifies:
  - Format: PDF / JSON / Email
  - Intent: RFQ, Invoice, Complaint, etc.
- Logs:
  - Format
  - Intent
  - Thread ID
- Routes to appropriate agent

### 2. Email Agent
- Accepts email text
- Extracts:
  - Sender
  - Subject
  - Urgency
  - Intent
- Formats as CRM-ready JSON
- Logs to memory store

### 3. JSON Agent
- Accepts structured JSON payload
- Reformats to target schema
- Flags missing fields or anomalies
- Logs to memory store

### 4. Shared Memory (SQLite)
- Persists traceable metadata:
  - Thread ID
  - Timestamp
  - Source type
  - Extracted fields
- Accessible to all agents

---

## Sample Inputs

Located in the `data/` folder:

- `sample_email.txt` – Email content
- `sample_invoice.json` – Structured JSON
- `sample_complaint.pdf` – Sample placeholder

---

## How to Run

### Step 1: Install Requirements

```bash
pip install -r requirements.txt
