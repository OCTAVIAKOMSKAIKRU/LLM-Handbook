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

Sure! Here's a clean, direct, and professional `README.md` for your GitHub repo. It's tailored to your **eCommerce chatbot MVP** for *Second Story Collection*, and speaks to a developer, stakeholder, or potential contributor who's reviewing your proof-of-concept:

---

````markdown
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
````

---

## 📂 Project Structure

```bash
.
├── data/
│   └── basic_ecom.json       # Intents & responses (chat training data)
├── main.py                   # Chatbot script (training + interaction)
├── model.tflearn             # Saved trained model
├── README.md                 # Project info (you’re reading it!)
```

---

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/secondstory-chatbot.git
cd secondstory-chatbot

# 2. Run the chatbot
python main.py
```

Once running, type questions like:

* "Hi"
* "Do you offer shipping?"
* "Can I return an item?"
* "What payment methods do you accept?"

Type `quit` to exit the chat.

---

## ✅ Sample Use Cases

This MVP currently handles questions like:

* Store hours
* Shipping options
* Return policies
* Payment methods
* Promo codes
* Order status
* Product availability
* Store location
* Size guide info


## 🙌 About Second Story Collection

We're building socially conscious digital products for **students, professionals**, and **value-driven buyers**. This chatbot is just one part of a larger suite of tools aimed at transforming how users interact with **affordable, quality** second-hand products across **South Africa**.

This repo is part of our public learning and contribution archive.
