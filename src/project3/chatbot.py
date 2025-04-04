from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled

from dotenv import load_dotenv

load_dotenv()
import os
import asyncio

set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash-exp",

    openai_client= AsyncOpenAI(
        api_key= os.getenv("GEMINI_API_KEY"),
        base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
    )
)

async def AIbot(user_query):
    my_agent = Agent(
        name= "AI Assistant", 
        instructions= "You will respond to user queries.",
        model=model
    )
    
    result =await Runner.run(
        starting_agent= my_agent,
        input= user_query,
    )
    print(result.final_output)
asyncio.run(AIbot("Hello"))