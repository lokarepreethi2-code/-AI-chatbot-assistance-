# Chatbot Project - Data Directory Guide

This folder contains all the datasets and documents used to train, configure, and power the AI chatbot. Below is a detailed breakdown of where and why these files are used in the pipeline.

---

## 1. Raw Data (`data/raw/`)

### 📂 `pdfs/`
* **What goes here:** Unstructured PDF data files (e.g., product manuals, FAQs, company policies).
* **Why it is used:** This folder feeds our **RAG (Retrieval-Augmented Generation) pipeline**. The chatbot engine reads these PDFs, splits the text into chunks, and saves them into a vector database so the bot can answer user questions using accurate, real-time context.

### 📂 `spreadsheets/`
* **What goes here:** Excel data files (`.xlsx`, `.xls`) and relational data files (`.csv`).
* **Why it is used:** These are the structured data source files meant to be loaded into our application databases. They hold transactional records, structured data lists, or user information that the chatbot's backend queries directly.

---

## 2. Processed Data (`data/processed/`)

### 📂 `json/`
* **What goes here:** Cleaned and structured JSON data files.
* **Why it is used:** This folder stores processed data that is ready for immediate consumption by the chatbot application. This includes custom intent maps, training sets, static chat system prompts, or fixed conversational response structures.
*
