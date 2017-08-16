from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

# Enable info level logging
import re

def smartrespond(msg):

    chatbot = ChatBot(
        'Hotelbot',
        trainer='chatterbot.trainers.ListTrainer'
    )


    chatbot.train([
       "movin pick"
        "good choice let me gather data  "
    ])

    # Now let's get a response to a greeting
    response = str(chatbot.get_response(msg))
    return response;

smartrespond("hotels")
