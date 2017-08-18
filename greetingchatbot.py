from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer



def smartrespond(msg):

    chatbot = ChatBot(
        'Hotelbotgreeting',

    )

    chatbot.set_trainer(ListTrainer)

    chatbot.train([
        "Hi there!",
        "Hello",
    ])

    chatbot.train([
        "Greetings!",
        "Hello",
    ])

    # Train based on the english corpus
    chatbot.train("chatterbot.corpus.english")

    # Train based on english greetings corpus
    chatbot.train("chatterbot.corpus.english.greetings")

    # Train based on the english conversations corpus
    chatbot.train("chatterbot.corpus.english.conversations")

    response = str(chatbot.get_response(msg))
    return response

smartrespond("hello")