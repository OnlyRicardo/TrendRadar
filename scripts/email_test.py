import os, smtplib, ssl
from email.message import EmailMessage

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")
SMTP_SERVER = os.getenv("EMAIL_SMTP_SERVER", "smtp.qq.com")
SMTP_PORT = int(os.getenv("EMAIL_SMTP_PORT", "465"))

print("准备发送测试邮件 ...")
print("SMTP_SERVER:", SMTP_SERVER, "SMTP_PORT:", SMTP_PORT)
print("EMAIL_FROM present:", bool(EMAIL_FROM))
print("EMAIL_TO present:", bool(EMAIL_TO))

if not (EMAIL_FROM and EMAIL_PASSWORD and EMAIL_TO):
    print("错误：EMAIL_FROM / EMAIL_PASSWORD / EMAIL_TO 三个变量中有缺失，程序将退出。")
    raise SystemExit(1)

msg = EmailMessage()
msg["Subject"] = "TrendRadar 邮件测试"
msg["From"] = EMAIL_FROM
msg["To"] = EMAIL_TO
msg.set_content("这是一封测试邮件，用于排查 TrendRadar 邮件发送问题。")

try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)
    print("邮件发送成功")
except Exception as e:
    print("邮件发送失败，异常信息：", repr(e))
    raise
