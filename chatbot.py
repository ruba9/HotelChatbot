from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer



def smartrespond(msg):

    chatbot = ChatBot(
        'Hotelbot',
        trainer='chatterbot.trainers.ListTrainer',
    database='db.sqlite3'


    )


    # chatbot.train([
    #    "weather"
    #     "all right do you like a hotel in sharm ? or in alaska"
    # ])

    response = str(chatbot.get_response(msg))
    return response

smartrespond("hello")