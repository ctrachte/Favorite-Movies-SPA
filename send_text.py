from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACd82090e4b741b70a5d4d90be95532c65"
# Your Auth Token from twilio.com/console
auth_token  = "54eb6b18946718681d25a742fc319d91"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15035937168",
    from_="+13608690127",
    body="Hi Amy it's Caleb, i wrote this python program to tell you I love you!")

print(message.sid)