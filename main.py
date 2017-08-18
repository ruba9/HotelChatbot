import requests
from flask import Flask,request

app = Flask(__name__)
import chatbot
import extractor
import json
import greetingchatbot


@app.route('/', methods=['GET'])
def verify():

    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "test_token":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200




params = {
    "access_token": "EAAdkZAqkDsVQBADaySIDtsrQ94AAHs0WVUdfUn8dhJWaTYcvsQSPvlsu8IkZBspnZBEWysonIjs6XAFDZC2qS7ZB207uiTBQKA9HSoW332SBchtfxZAggR20dsdfy3LbIhN1IlGdPHLGSnre9qKM5Gy6Sz70aundZBz5JoxG5jTJgZDZD"
}

headers = {
    "Content-Type": "application/json"
}



@app.route('/', methods=['POST'])
def webhook():
   data = request.get_json()

   if "messaging" in data["entry"][0] and  "message" in data["entry"][0]["messaging"][0] and 'attachments' not in data["entry"][0]['messaging'][0]['message']:
        text = data["entry"][0]["messaging"][0]["message"]["text"]
        senderid = data["entry"][0]["messaging"][0]["sender"]["id"]
        hotelname=extractor.detectHotel(text)
        if hotelname is "NF":
            text="hello"+ ",this not a hotel name"
            sendmsg(recipientid=senderid,msg_txt=str(text))
            return "ok",200
        else:
            sendmsg(recipientid=senderid,msg_txt=hotelname)
            sendattachment(recipientid=senderid)
            return "ok", 200
   elif "standby" in data["entry"][0]  and  "postback" in data["entry"][0]['standby']:
        if data["entry"][0]['standby'][0]['postback']["title"] == 'No':
            senderid = data["entry"][0]["standby"][0]["sender"]["id"]
            sendmsg(recipientid=senderid,msg_txt="sorry i wish i could help you , but actullay i do nothing about that hotel")
            return "ok",200
        else:
            print("search engine writtern here")
            # Rihan your search engine here
   elif "postback" in data["entry"][0]["messaging"][0]:
       if data["entry"][0]['messaging'][0]['postback']["title"] == 'No':
           senderid = data["entry"][0]["messaging"][0]["sender"]["id"]
           sendmsg(recipientid=senderid,
                   msg_txt="sorry i wish i could help you , but actullay i know nothing about that hotel")
           return "ok", 200
       else:
           print("search engine writtern here")
           #rihan your search enginer here
   elif 'attachments' in data["entry"][0]['messaging'][0]['message'] :
        senderid = data["entry"][0]["messaging"][0]["sender"]["id"]
        text="ok"
        sendmsg(recipientid=senderid,msg_txt=text)
        return "ok",200



def sendmsg(recipientid,msg_txt):
   return  FirstInteraction(recipientid,msg_txt)


def FirstInteraction(recipientid,msg_txt):


    data = json.dumps({
        "recipient": {
            "id": recipientid
        },
        "message": {
            "text": msg_txt
        }
    })

    showtype=json.dumps({
        "recipient": {
            "id": recipientid
        },
        "sender_action": "typing_on"

    })





    requests.post("https://graph.facebook.com/v2.6/me/messages",params=params,headers=headers,data=showtype)
    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)




def sendattachment(recipientid):
    qreply = json.dumps({
        "recipient": {
            "id": recipientid
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "your choice is good but what if we suggest to you some hotels?",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Yes",
                                    "payload": "Yes"
                                },
                                {
                                    "type": "postback",
                                    "title": "No",
                                    "payload": "No"
                                },

                            ]
                        },

                    ]
                }
            }
        }
    })

    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=qreply)


def smartaction(msg):
    return chatbot.smartrespond(msg)



if __name__ == "__main__":
    app.run()



