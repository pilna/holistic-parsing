import ast

from itertools import count
from schemas.functionRepresentation import FunctionRepresentation

class ClassRepresentation:
    serving_id = count()

    def __init__(
        self, 
        name: str, 
        start_line: int, 
        end_line: int, 
        inheritance: list[str] | None = None, 
        body: list[ast.AST] | None = None, 
        metaclass: str | None = None
    ) -> None:
        self.id = next(ClassRepresentation.serving_id)
        self.name = name
        self.start_line = start_line
        self.end_line = end_line
        self.metaclass = metaclass
        self.inheritance = [] if inheritance is None else inheritance
        self.body = [] if body is None else body

    
    def retrieve_methods(self) -> list[FunctionRepresentation]:
        return [
            FunctionRepresentation.from_ast(node)
            for node in self.body
            if isinstance(node, ast.FunctionDef)
        ]


    def __str__(self) -> str:
        return f"""
            class {{
                id: {self.id}
                name: {self.name}
                position: ({self.start_line}, {self.end_line})
            }}
        """
    

    def __repr__(self) -> str:
        return f"<ClassRepresentation {self.name}>"
    

    @classmethod
    def from_ast(cls, node: ast.ClassDef) -> "ClassRepresentation":
        inheritance = [base.id for base in node.bases]
        metaclass = [keyword.value.id for keyword in node.keywords if keyword.arg == "metaclass"]
        metaclass = metaclass[0] if metaclass else None

        return cls(
            name = node.name,
            start_line = node.lineno,
            end_line = node.end_lineno,
            body = node.body,
            inheritance = inheritance,
            metaclass = metaclass
        )
