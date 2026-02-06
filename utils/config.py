import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENDPOINT = os.getenv("ENDPOINT") or "https://doc-dio-fraude-eastus-dev-010.cognitiveservices.azure.com/"
    KEY = os.getenv("SUBSCRIPTION_KEY") or "6UPiDoXVmIrRDqlp4AmQ99hxXPapLJPSKswkwWqkvhDxqhuHj7LMJQQJ99CAACYeBjFXJ3w3AAALACOGxo9R"
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING") or "DefaultEndpointsProtocol=https;AccountName=stdiolabdocs002;AccountKey=lPiwdWVy+Ap6FGHC2OAOaUW0Nm7P4qmZPEqX8kJqD4JDA99/ThkkBHkIOZbwMJf9ONJvUJF+RLyr+AStnceP6Q==;EndpointSuffix=core.windows.net"
    CONTAINER = os.getenv("CONTAINER") or "cartoes"
