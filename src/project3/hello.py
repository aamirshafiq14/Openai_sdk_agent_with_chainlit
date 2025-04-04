import chainlit as cl
from chatbot import AIbot

@cl.on_chat_start
async def chat_start():

    # Send a greeting to the user
    await cl.Message(
        content= "I am your AI Assistant. How can I help you today?").send()


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...

    # Send a response back to the user
    user_query = message.content
    response =await AIbot(user_query)
    await cl.Message(
        content=f"{response}").send()