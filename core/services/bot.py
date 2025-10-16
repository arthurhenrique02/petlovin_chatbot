from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI

from core.services.generics import GenericBot


class OpenAIChatBot(GenericBot):
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
        # str parser to just get the text response
        chain = self.complete_prompt | self.llm | StrOutputParser()
        return chain.invoke({"input_data": input_data})

    def initialize_llm(self) -> ChatOpenAI:
        return ChatOpenAI(model_name=self.model)
