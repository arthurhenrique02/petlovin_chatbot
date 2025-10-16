import typing
from abc import ABC, abstractmethod

from langchain_core.language_models.llms import BaseLLM


class GenericBot(ABC):
    name: str
    model: str
    llm: BaseLLM
    system_prompt: str

    def __init__(self, name: str, system_prompt: str, model: str):
        if not name or not system_prompt or not model:
            raise ValueError("Name, system_prompt, and model must be provided")

        self.name = name
        self.system_prompt = system_prompt
        self.model = model
        self.llm = self.initialize_llm()

    @abstractmethod
    def task(self, input_data: typing.Any) -> typing.Any:
        pass

    @abstractmethod
    def initialize_llm(self) -> BaseLLM:
        pass
