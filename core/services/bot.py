from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import OpenAI

from core.services.generics import GenericBot


class OpenAIBot(GenericBot):
    complete_prompt: ChatPromptTemplate

    def __init__(self, name, system_prompt, model):
        super().__init__(name, system_prompt, model)
        self.complete_prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate.from_template(self.system_prompt),
                HumanMessagePromptTemplate.from_template("{input_data}"),
            ]
        )

    def task(self, input_data: str) -> str:
        """
        Process the input data using the LLM and return the response.
        """
        chat = self.llm.bind(self.complete_prompt)
        return chat.invoke({"input_data": input_data})

    def initialize_llm(self):
        return OpenAI(model_name=self.model)
