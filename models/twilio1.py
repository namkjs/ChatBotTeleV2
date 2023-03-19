from twilio.rest import Client

# Thiết lập tài khoản Twilio
account_sid = 'AC248c811bc245e75e25c580ceef8fcb44'
auth_token = '344a22b64f9d544a5e1dd8bb96d7caa9'
client = Client(account_sid, auth_token)

# Tạo hàm để gửi tin nhắn SMS


def send_sms(message):
    client.messages.create(
        body=message,
        from_='+15075843588',  # số điện thoại Twilio của bạn
        to='+840866030920'  # số điện thoại của khách hàng để gửi tin nhắn
    )

# Tạo hàm để thông báo sự thay đổi số dư trong ví điện tử


def notify_balance_change(amount):
    if amount > 0:
        message = f"Số dư trong ví của bạn đã tăng lên {amount} đồng."
    else:
        message = f"Số dư trong ví của bạn đã giảm xuống {-amount} đồng."
    send_sms(message)


notify_balance_change(100000)
