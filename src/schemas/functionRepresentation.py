import ast

from itertools import count
from typing import Any


class ParameterRepresentation:

    def __init__(self, name: str, annotations: str = None, default_value: Any = None):
        self.name = name
        self.annotations = annotations
        self.default_value = default_value


class FunctionRepresentation:
    serving_id = count()

    def __init__(
        self, 
        name: str, 
        start_line: int, 
        end_line: int, 
        parameters: list[ParameterRepresentation] | None = None, 
        body: list[ast.AST] = None
    ) -> None:
        self.id = next(FunctionRepresentation.serving_id)
        self.name = name
        self.parameters = []
        self.start_line = start_line
        self.end_line = end_line
        self.body = [] if body is None else body

    @classmethod
    def from_ast(cls, node: ast.ClassDef) -> "FunctionRepresentation":
        
        return cls(
            name = node.name,
            start_line = node.lineno,
            end_line = node.end_lineno,
            body = node.body
        )