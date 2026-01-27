import os
from google.genai import types


def write_file(working_directory, file_path, content):
    absolute_working_directory = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(absolute_working_directory, file_path))

    valid_target_file = (
        os.path.commonpath([absolute_working_directory, target_file])
        == absolute_working_directory
    )

    if not valid_target_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    os.makedirs(os.path.dirname(target_file), exist_ok=True)

    with open(target_file, mode="w") as f:
        try:
            f.write(content)
        except Exception as e:
            return f'Error: Cannot write to "{file_path}", {e}'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the given content to a file given its path relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to be written to, relative to the working path",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to be written to the target file",
            ),
        },
    ),
)
