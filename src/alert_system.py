import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, message, to_email="admin@example.com"):
    """Send an email alert."""
    from_email = "your_email@example.com"
    password = "your_password"
    
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

def log_to_console(message):
    """Log messages to the console."""
    print(message)

def log_to_file(message, log_file="logs/intrusions.log"):
    """Log messages to a file."""
    with open(log_file, "a") as file:
        file.write(message + "\n")
