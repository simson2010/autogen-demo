from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.teams import Swarm
from autogen_agentchat.conditions import ExternalTermination, TextMentionTermination
from autogen_agentchat.ui import Console
from src.LLM_Client import model_client 
from src.tools.weather_tool import get_weather
from src.tools.email_tool import send_mail
from src.tools.address_mapping import map_address
import asyncio

# Define an AssistantAgent with the model, tool, system message, and reflection enabled.
# The system message instructs the agent via natural language.

agent_system_message = """
You are a helpful assistant. You can use below tools to process my query. 

## tools: 

### tool-1
1. befoe get weather, you should clear how many city and which city you should send to tools
2. get_weather, you can use weather tool, and translate the city name to English before using the tool. 
3. once get each weather info, to check if alread get all you want. if not keep working in getting weather for other city.
4. once get all waether info, check if can do next to map city with email address with 'maping_address_agent'
"""
agent_system_message = "Get weather for all city you guess using tool. Then send to `maping_address_agent`."
agent = AssistantAgent(
    name="weather_agent",
    model_client=model_client,
    tools=[get_weather],
    handoffs=["maping_address_agent"],
    system_message=agent_system_message,
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)

mapping_address_system_message = """
You are a helpful assistant. You can use below tools to process my query. Any email address should using tool, you can't 
create any email address by your knowledge-base.

## tools: 

### tool-1
1. once you get all weather info, you can map email address with city name using map_address tool
2. map_address to city, then map to a email address with a city name
3. summarise the weather info for city
4. send city weather summarise and city summary as boty and the mail address to `mailing_agent`

"""
mapping_address_system_message = "Get all mail address for each city with tools, send data to `mailing_agent`"

maping_address_agent =  AssistantAgent(
    name="maping_address_agent",
    model_client=model_client,
    tools=[map_address],
    handoffs=["mailing_agent"],
    system_message=mapping_address_system_message,
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)

mailing_system_message = """
You are a helpful assistant. You should use your tools to finished my query. You should ensure send out all email you need to send, finally, reply 
**all-sent**.

## tools: 

### tool-1
1. send email to 'target' address with a valid email 'body'. 

### limitation
1. once sent all email, then reply **all-sent** to terminal the task.
"""
mailing_system_message = "Send email to each address of city wity a re-fined body. Once finished, reply **all-sent**. "
mail_agent = AssistantAgent(
    name="mailing_agent",
    model_client=model_client,
    tools=[send_mail],
    system_message=mailing_system_message,
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)

terminate_keyword = TextMentionTermination("all-sent")

team = Swarm([agent, maping_address_agent, mail_agent], termination_condition=terminate_keyword)


# Run the agent and stream the messages to the console.
async def main() -> None:
    await Console(team.run_stream(task="今日广州好热，北京又好冻，不知道巴黎，澳门是几多度。"))


if __name__ == "__main__":
    asyncio.run(main())