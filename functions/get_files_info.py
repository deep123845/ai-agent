import os
from functools import reduce


def get_files_info(working_directory, directory="."):
    absolute_working_directory = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(absolute_working_directory, directory))

    valid_target_dir = (
        os.path.commonpath([absolute_working_directory, target_dir])
        == absolute_working_directory
    )

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    files = os.listdir(target_dir)

    contents = list(map(get_file_info(target_dir), files))
    return reduce(lambda x, y: f"{x}\n{y}", contents)


def get_file_info(target_dir):

    def inner(file):
        file_path = os.path.join(target_dir, file)
        file_size = os.path.getsize(file_path)
        is_dir = os.path.isdir(file_path)
        return f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"

    return inner
