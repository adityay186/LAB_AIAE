from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Indian Railways')

trainer = ListTrainer(chatbot)
trainer.show_training_progress=True

trainer.train([
    "Can you book a train ticket?",
    "Sure, we can book train ticket.",
    "Can you check for PNR Status?",
    "Please provide me with a PNR Number.",
    "20190802060",
    "Let me check....your tickets are confirmed.",
    "Can you check for FNR Status?",
    "Sure, privide FNR Number",
    "8128449745",
    "Let me check.....your freight is confirmed.",
    "Locate my train.",
    "Enter train number.",
    "19037",
    "Train has departed Valsad at 00:37 hrs.",
    "Cancel ticket.",
    "Enter PNR.",
    "9106921583",
    "Cancelling tickets......your tickets are cancelled, you will get refund in your account in 3-7 working days."
])

while True:
    s = input("")
    response = chatbot.get_response(s)
    print(response)
