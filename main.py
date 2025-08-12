# main.py

from agents import email, calendar, contact, content, carousel, transcript
from telegram.bot import start_bot

def route_request(request_type, data):
    if request_type == "email":
        return email.handle(data)
    elif request_type == "calendar":
        return calendar.handle(data)
    elif request_type == "contact":
        return contact.handle(data)
    elif request_type == "content":
        return content.handle(data)
    elif request_type == "carousel":
        return carousel.handle(data)
    elif request_type == "transcript":
        return transcript.handle(data)
    else:
        return {"error": "Unknown request type"}

if __name__ == "__main__":
    print("🚀 UltimateAssistant запущен")
    start_bot(route_request)
