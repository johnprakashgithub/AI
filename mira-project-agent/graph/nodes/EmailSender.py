import smtplib
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, smtp_host, smtp_port, smtp_user, smtp_password, from_email, to_email, subject="Weekly Project Status Report"):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
        self.from_email = from_email
        self.to_email = to_email
        self.subject = subject

    def __call__(self, state):
        summary = state.get("status_summary", "")
        if not summary:
            raise ValueError("No status summary found in state")

        msg = MIMEText(summary)
        msg["Subject"] = self.subject
        msg["From"] = self.from_email
        msg["To"] = self.to_email

        with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.sendmail(self.from_email, self.to_email, msg.as_string())

        return {**state, "email_sent": True}
