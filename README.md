# 📚 NightOwl

> Your course material. Your sources. No hallucinations.

The NightOwl is an evidence-based AI study assistant designed
for students studying from their own course material.

Instead of relying on an AI model's general knowledge, the system
retrieves evidence from the student's documents and produces answers
that can be traced back to the original source.

When the material does not contain enough evidence to answer a
question, the system should refuse rather than hallucinate.

## Current Progress

### Step 1 — Project Setup
- Working Streamlit application
- Initial UI
- Python virtual environment
- GitHub repository

## Planned Features

- [ ] Upload PDF documents
- [ ] Upload PowerPoint slides
- [ ] Upload TXT/Markdown files
- [ ] OCR handwritten notes
- [ ] Document processing
- [ ] Text chunking
- [ ] Semantic vector search
- [ ] Evidence-based answers
- [ ] Page-level citations
- [ ] Hallucination refusal
- [ ] Multi-document reasoning
- [ ] Evaluation dataset
- [ ] Accuracy dashboard
- [ ] Production deployment

## Core Principle

The system should distinguish between:

1. Information supported by the course material
2. Information absent from the course material
3. Information that requires evidence from multiple documents

The goal is not to create another chatbot.

The goal is to create a study assistant whose answers can be checked.