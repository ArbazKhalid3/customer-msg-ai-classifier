import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_message(message: str):
    prompt = f"""
You are a customer support AI assistant. Analyze the customer message below and respond ONLY in this exact format (no extra text):

Category: <one of: Complaint, Refund/Return, Sales Inquiry, Delivery Question, Account/Technical Issue, General Query, Spam>
Sentiment: <Positive, Neutral, or Negative>
Auto-Reply: <a short, professional 2-3 sentence reply addressing the customer's message>

Customer Message: "{message}"
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content


def run_demo_messages():
    test_messages = [
        "I ordered a laptop 10 days ago and it still hasn't arrived. This is ridiculous!",
        "Hi, do you guys offer bulk discounts for orders over 50 units?",
        "My account got locked after I tried logging in 3 times. Please help.",
        "Congratulations! You've won a free iPhone, click here to claim now!!!",
        "Thanks for the quick delivery, the product quality is amazing!",
    ]

    for i, msg in enumerate(test_messages, 1):
        print(f"\n{'='*60}")
        print(f"Message {i}: {msg}")
        print(f"{'='*60}")
        print(analyze_message(msg))


def run_live_mode():
    print("\n--- Live Mode: type a customer message (or 'exit' to quit) ---\n")
    while True:
        msg = input("Customer message: ").strip()
        if msg.lower() == "exit":
            break
        if not msg:
            continue
        print("\nProcessing...\n")
        print(analyze_message(msg))
        print()


def main():
    print("Customer Message AI Classifier")
    print("1. Run demo messages")
    print("2. Live mode (type your own messages)")
    choice = input("Choose (1 or 2): ").strip()

    if choice == "1":
        run_demo_messages()
    else:
        run_live_mode()


if __name__ == "__main__":
    main()