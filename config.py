from autogen_ext.models.openai import OpenAIChatCompletionClient

def get_model_client():
    return OpenAIChatCompletionClient(
        model="qwen3:1.7b",  
        base_url="http://localhost:11434/v1",
        api_key="placeholder",
        model_capabilities={
            "json_output": False,
            "vision": False,
            "function_calling": True,
        },
    )