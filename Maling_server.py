import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

def send_mail():
    YOUR_GMAIL = "lovebirdstogether69@gmail.com"
    APP_PASSWORD = "cpzl ixfy ftpl mymr"

    TO_EMAIL = "azharbalochcs@gmail.com"

    msg = EmailMessage()
    msg['From'] = YOUR_GMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = "A Special Message Just for You ❤️"

    msg.set_content(f"""
Hi Azhar,

I hope this message brightens your day a little 😊

Just reaching out to share positive energy and remind you that great things 
are on the way for you. Stay confident, stay focused, and keep moving forward—
your hard work will pay off sooner than you think!

Have an amazing day!

Sent automatically at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(YOUR_GMAIL, APP_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {TO_EMAIL} at {datetime.now().strftime('%H:%M:%S')}")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    while True:
        send_mail()
        time.sleep(120)  # 2 minutes
