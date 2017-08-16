from flask import Flask,request
import requests
app = Flask(__name__)
import json
import chatbot



@app.route('/', methods=['GET'])
def verify():

    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "test_token":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200



@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    text=data["entry"][0]["messaging"][0]["message"]["text"]
    senderid=data["entry"][0]["messaging"][0]["sender"]["id"]
    recipientid=data["entry"][0]["messaging"][0]["recipient"]["id"]

    sendmsg(recipientid=senderid,msg_txt=smartaction(str(text)))


    return "ok", 200

def sendmsg(recipientid,msg_txt):

    params = {
        "access_token": "EAAEvkG6UoLgBAEBWGNLpwgsg4CqZBcUeQi78DhU619ONWlpx9Gqu0byn7XwevxaDLRbbjsIrBEQRlQ4uFeNPCGQwjoP840jPFQMFYxIysrUbH9ca3JSdZBkVbkwicDB1ZAHDoMGdJsrLqTyVhv4f4PqHYdPWpQ0EYubqMD6QAZDZD"
    }

    headers = {
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "recipient": {
            "id": recipientid
        },
        "message": {
            "text": msg_txt
        }
    })
    response = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if response.status_code!=200:
        print("not right")

def smartaction(msg):
   return chatbot.smartrespond(msg)



if __name__ == "__main__":
    app.run()



