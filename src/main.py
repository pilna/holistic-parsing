import ast

from schemas.classRepresentation import ClassRepresentation

with open("./src/example.py", "r") as file:
    source_code = file.read()

parsed_code = ast.parse(source_code)

for node in ast.walk(parsed_code):
    if isinstance(node, ast.ClassDef):
        print(ClassRepresentation.from_ast(node))