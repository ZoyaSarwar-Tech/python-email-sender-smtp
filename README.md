# Python Email Sender using SMTP

This project is a simple Python automation script that sends emails to multiple recipients using Gmail SMTP server.

## 🚀 Features
- Send emails using Gmail SMTP
- Supports multiple recipients
- Automated email sending with Python
- Uses secure TLS connection

## 🛠️ Technologies Used
- Python 3
- smtplib
- email.message.EmailMessage

## ⚙️ How It Works
1. Connects to Gmail SMTP server (`smtp.gmail.com`)
2. Starts TLS encryption for security
3. Logs in using Gmail email and App Password
4. Sends email to a list of recipients using a loop

## 📌 Important Note
You must enable **2-Step Verification** in Gmail and generate an **App Password** to use this script.

## 🔐 Security Tip
Never hardcode your real password in code. Use environment variables instead.

## ▶️ How to Run
```bash
python main.py

📧 Example Output
Email was sent to email@gmail.com
All emails were sent successfully!
