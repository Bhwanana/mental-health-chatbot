def get_intent(text):
    text = text.lower()

    if "sad" in text or "depressed" in text:
        return "sad"
    elif "happy" in text or "good" in text or "great" in text:
        return "happy"
    elif "hello" in text or "hi" in text:
        return "greeting"
    elif "bye" in text:
        return "bye"
    else:
        return "unknown"

def get_response(intent):
    responses = {
        "greeting": "Hello! I'm here for you. How are you feeling?",
        "sad": "I'm sorry you're feeling this way. Want to talk more about it?",
        "happy": "That’s wonderful! Keep smiling 😊",
        "bye": "Take care! You're not alone. Talk to you soon ❤️",
        "unknown": "I'm here to listen. Can you tell me more?"
    }
    return responses[intent]
