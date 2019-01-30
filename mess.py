import smtplib

def send_email(text):
    server = smtplib.SMTP("smtp.server", 587)  # подключение к серверу
    server.ehlo()
    server.starttls()
    server.login("login", "password")  # логинимся на сервер
    message = "\r\n".join([   # формируем сообщение Email с полями
        "From: от кого", 
        "To: кому", 
        "Subject: тема", 
        "", 
        text,
        ])
    server.sendmail("login@server", "адрес почты получателя", message)  # отправляем
    server.quit()  # разлогиниваемся с сервера

send_email('Hello, World!')