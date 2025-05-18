# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------


"""
FILE: bing_custom_search.py

DESCRIPTION:
    This sample demonstrates how to use agent operations with the Grounding with Bing Custom Search tool from
    the Azure AI Foundry Agents service using a synchronous client.

USAGE:
    python bing_custom_search.py

    Before running the sample:

    pip install azure.ai.projects==1.0.0b10 azure-identity

    Set this environment variables with your own values:
    PROJECT_CONNECTION_STRING - the Azure AI Hub resource Project connection string, as found in your AI Hub resource Project.
    BING_CONNECTION_NAME - the name of the connection of Grounding with Bing Custom Search
    
"""
# <create a project client>
import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import MessageRole, BingCustomSearchTool
from azure.ai.projects import AIProjectClient

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

bing_connection = project_client.connections.get(
    connection_name=os.environ["BING_CONNECTION_NAME"]
)
conn_id = bing_connection.id
print(conn_id)

bing = BingCustomSearchTool(
    connection_id=conn_id,
    instance_name=<your-custom-search-configuration-instance-name>
)

with project_client:
    agent = project_client.agents.create_agent(
        model="gpt-4o", 
        name="my-agent", 
        instructions="use the tool to respond", 
        tools=bing.definitions,
    )
    print(f"Created agent, ID: {agent.id}")

    # Create thread for communication
    thread = project_client.agents.create_thread()
    print(f"Created thread, ID: {thread.id}")

    # Create message to thread
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role=MessageRole.USER,
        content="<questions related to your configuration>",
    )
    print(f"Created message, ID: {message.id}")

    # Create and process Agent run in thread with tools
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    print(f"Run finished with status: {run.status}")

    if run.status == "failed":
        print(f"Run failed: {run.last_error}")

    # Delete the Agent when done
    project_client.agents.delete_agent(agent.id)
    print("Deleted agent")

    # Print the Agent's response message with optional citation
    response_message = project_client.agents.list_messages(thread_id=thread.id).get_last_message_by_role(
        MessageRole.AGENT
    )
    if response_message:
        for text_message in response_message.text_messages:
            print(f"Agent response: {text_message.text.value}")
        for annotation in response_message.url_citation_annotations:
            print(f"URL Citation: [{annotation.url_citation.title}]({annotation.url_citation.url})")
