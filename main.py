import os
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from tools import tools
from llm import llm
from agents import memory


def main():
    agent_kwargs = {
        'prefix': "You are an AI assistant tasked with carrying out the following: providing housing details and relevant information, aiding users in listing and selling their properties, assisting buyers in finding suitable properties, and offering guidance on housing stuffs. Note: If the given {input} does not contain relavant information to answer the question, come up with questions that can be used to answer."}

    main_agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=1,
        early_stopping_method="generate",
        agent_kwargs=agent_kwargs,
        memory=memory
    )

    query = input("Enter your query: ")
    message = {'input': query, 'chat_history': []}
    output = main_agent.run(message)
    print(output)

main()