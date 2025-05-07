# 🛍️ Second Story Collection – E-commerce Chatbot MVP

Welcome to the official repository for the **Second Story Collection chatbot MVP**.

This is a lightweight AI chatbot designed to simulate a basic customer support assistant for our e-commerce platform. It uses **Python**, **TensorFlow 1.x**, **TFLearn**, and **NLTK** to classify user intents and respond to frequently asked questions from customers.

---

## 🔍 Project Purpose

As part of our lean MVP approach, this chatbot was built to:

- Handle **frequently asked questions** (shipping, returns, store hours, promotions, etc.)
- Provide support for **students and young professionals** interacting with our e-commerce site
- Showcase how we can integrate **AI-driven automation** to streamline support across our digital platforms
- Act as a **proof of concept** for larger LLM integrations (e.g. Claude, Gemini, etc.)

---

## 🧠 What's Inside

- Intent classification using NLTK + TensorFlow
- Trained on realistic FAQ interactions
- JSON-based intent dataset: `basic_ecom.json`
- Manual training pipeline
- Terminal-based chat interface (`main.py`)

---

## ⚙️ Requirements

You must use **Python 3.6.x** for compatibility with `tflearn`.

Install dependencies with:

```bash
pip install tflearn==0.3.2 tensorflow==1.15 nltk numpy
