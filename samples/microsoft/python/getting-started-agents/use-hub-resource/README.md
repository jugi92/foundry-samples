# How to Foundry Agent Service Tools in Preview

You can use Azure AI Foundry Agent Preview API such as `2024-12-01-preview` or `2025-05-15-preview` to interact with tools in public preview, such as Microsoft Fabric tool, Grounding with Bing Custom Search tool and more. 

You can check the resource type of your project by going to [Azure AI Foundry Potral](https://ai.azure.com) and click the project you are using on the top left. In the dropdown, you can see if it belongs to `Hub` or `AI Foundry`

![image](https://github.com/user-attachments/assets/10023985-3a8d-4da1-a055-ad24cfc56ee5)

Please make sure your resource type, API version and SDK version matches with each other
| Resource Type | API Supported | SDK Version| Supported Experience| 
|----------------|----------------|----------------|----------------|
| [**Azure AI Foundry Project Resource**](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture)    | `2025-05-15-preview` or later   | [azure-ai-projects](https://pypi.org/project/azure-ai-projects/) and [azure-ai-agents](https://pypi.org/project/azure-ai-agents/1.0.0b1)   | API and Azure AI Foundry Portal | 
| [**Azure AI Foundry Hub Resource**](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture)   | `2024-12-01-preview` or before   | [azure-ai-projects 1.0.0b10](https://pypi.org/project/azure-ai-projects/1.0.0b10/)   | API, SDK, and Azure AI Foundry Portal| 

If you are using Azure AI Foundry **Project** Resource:
- for Azure AI Foundry Portal
  - just make sure you select the project of resource type `AI Foundry` 
- for API
  - follow the quickstart [here](https://learn.microsoft.com/en-us/azure/ai-services/agents/quickstart?pivots=rest-api) to set up 
  - your connection id should be in this format: `/subscriptions/<sub-id>/resourceGroups/<your-rg-name>/providers/Microsoft.CognitiveServices/accounts/<your-ai-services-name>/projects/<your-project-name>/connections/<your-connection-name>`
- for SDK
  - make sure you [azure-ai-projects](https://pypi.org/project/azure-ai-projects/) and [azure-ai-agents](https://pypi.org/project/azure-ai-agents/1.0.0b1)
  - follow the samples here: [Grounding with Bing Custom Search](../bing_custom_search.py) and [Fabric](../fabric_data_agent.py)
  - your connection id should be in this format: `/subscriptions/<sub-id>/resourceGroups/<your-rg-name>/providers/Microsoft.CognitiveServices/accounts/<your-ai-services-name>/projects/<your-project-name>/connections/<your-connection-name>`


If you are using Azure AI Foundry **Hub** Resource:
- for Azure AI Foundry Portal experience
  - just make sure you select the project of resource type `Hub`
- for SDK
  - make sure you use [azure-ai-projects 1.0.0b10](https://pypi.org/project/azure-ai-projects/1.0.0b10/)
  - Follow the [sample code](./samples) for tools in preview
  - your connection id should be in this format: `/subscriptions/<sub-id>/resourceGroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<project-name>/connections/<connection-name>`
- for API
  - your API endpoint should be in this format: `https://ai.azure.com/api/{region}/agents/v1.0/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.MachineLearningServices/workspaces/{project-name}/assistants?api-version=2024-12-01-preview
  - you need to get token through
    ```azurecli
    az account get-access-token --resource 'https://ml.azure.com/'
    ```
  - your connection id should be in this format: `/subscriptions/<sub-id>/resourceGroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<project-name>/connections/<connection-name>`
