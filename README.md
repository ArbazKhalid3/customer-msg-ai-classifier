# Customer Message AI Classifier

An AI-powered system that analyzes customer messages and automatically generates three outputs for each one:

1. **Category** — Complaint, Refund/Return, Sales Inquiry, Delivery Question, Account/Technical Issue, General Query, or Spam
2. **Sentiment** — Positive, Neutral, or Negative
3. **Auto-Reply** — A short, professional response appropriate to the message

Built using the **Groq API** (Llama 3.1) for fast, free LLM inference.

## Features

- Classifies customer messages into 7 predefined categories
- Detects sentiment of each message
- Generates context-aware, professional auto-replies
- Two modes: batch demo mode and live interactive mode
- API key handled securely via environment variables (`.env`, git-ignored)

## Tech Stack

- Python 3
- [Groq API](https://console.groq.com) (Llama 3.1 8B Instant)
- python-dotenv

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/ArbazKhalid3/customer-msg-ai-classifier.git
   cd customer-msg-ai-classifier
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install groq python-dotenv
   ```

3. Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
   Get a free API key at [console.groq.com](https://console.groq.com).

4. Run the program:
   ```bash
   python main.py
   ```

## Usage

On running, you'll be prompted to choose a mode:

```
1. Run demo messages
2. Live mode (type your own messages)
```

- **Demo mode** runs a set of sample customer messages through the classifier and prints the category, sentiment, and auto-reply for each.
- **Live mode** lets you type your own messages interactively and see real-time outputs. Type `exit` to quit.

## Example Output

```
Message: I ordered a laptop 10 days ago and it still hasn't arrived. This is ridiculous!

Category: Delivery Question
Sentiment: Negative
Auto-Reply: We apologize for the delay in receiving your order. We will look into
this matter immediately and provide you with an update on the status of your
laptop shipment. Please allow us 24 hours to investigate further.
```

## Project Structure

```
customer_msg_ai/
├── main.py          # Core script: classification, sentiment, auto-reply logic
├── .env             # API key (not committed)
├── .gitignore       # Excludes venv, .env, cache files
└── README.md
```

## Author

**Muhammad Arbaz Khalid**
BSSE Student, Riphah International University
