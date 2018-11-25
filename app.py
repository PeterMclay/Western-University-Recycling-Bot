from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from can import recyclable

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms_reply():
    resp = MessagingResponse()

    if request.form['NumMedia'] != '0':
        image_url = request.form['MediaUrl0']
        resp.message(recyclable(image_url))
    else:
        resp.message("👋 Hi, this is the Western University Recycle Bot 🤖! Recycling can be tricky, sometimes you just "
                     "don't know what you can throw into the blue bin. That's where I come in handy 🙋, "
                     "send me a picture of what you are unsure of and I can use my advanced machine learning"
                     "algorithms to tell you if the object you have is ♻ recyclable ♻! For more info, visit our site at"
                     " https://hakwesturn-jgillet4.c9users.io:8081/api/recycler")

    return str(resp)

if __name__ == '__main__':
    app.run()
