from abc import ABC, abstractmethod
from shevchenko.word_declension.declension_types import InflectionCommand, InflectionCommandAction

class InflectionCommandRunner(ABC):
    @abstractmethod
    def exec(self, value: str) -> str:
        pass

class AppendCommandRunner(InflectionCommandRunner):
    def __init__(self, command: InflectionCommand):
        self.command = command

    def exec(self, value: str) -> str:
        return value + self.command['value']

class ReplaceCommandRunner(InflectionCommandRunner):
    def __init__(self, command: InflectionCommand):
        self.command = command

    def exec(self, value: str) -> str:
        return self.command['value']

class CommandRunnerFactory:
    def make(self, command: InflectionCommand) -> InflectionCommandRunner:
        action = command['action']
        if action == InflectionCommandAction.APPEND:
            return AppendCommandRunner(command)
        elif action == InflectionCommandAction.REPLACE:
            return ReplaceCommandRunner(command)
        else:
             raise TypeError(f"Invalid command action: {action}.")
