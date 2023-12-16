import os
from langchain.llms import Replicate

os.environ["REPLICATE_API_TOKEN"] = "ENTER YOUR TOKEN"

llm = Replicate(
    model="mistralai/mixtral-8x7b-instruct-v0.1:2b56576fcfbe32fa0526897d8385dd3fb3d36ba6fd0dbe033c72886b81ade93e",
    model_kwargs={"temperature": 0.1, "max_new_tokens": 1024, }
)