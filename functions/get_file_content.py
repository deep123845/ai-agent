import os
from google.genai import types

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    absolute_working_directory = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(absolute_working_directory, file_path))

    valid_target_file = (
        os.path.commonpath([absolute_working_directory, target_file])
        == absolute_working_directory
    )

    if not valid_target_file:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    content = ""
    with open(target_file) as f:
        content = f.read(MAX_CHARS)
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return content


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the contents of a file in a specified file, providing the text contained in the file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file which the contents are required from, relative to the working path",
            ),
        },
    ),
)
