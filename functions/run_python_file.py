import os
import subprocess

TIMEOUT = 30


def run_python_file(working_directory, file_path, args=None):
    absolute_working_directory = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(absolute_working_directory, file_path))

    valid_target_file = (
        os.path.commonpath([absolute_working_directory, target_file])
        == absolute_working_directory
    )

    if not valid_target_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if file_path[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", target_file]
    if args != None:
        command.extend(args)

    completed_process = subprocess.run(
        command, timeout=TIMEOUT, text=True, capture_output=True
    )

    output = ""

    if completed_process.returncode != 0:
        output += f"Process exited with code {completed_process.returncode}\n"

    if completed_process.stdout == None and completed_process.stderr == None:
        output += "No output produced\n"
    else:
        output += f"STDOUT: \n{completed_process.stdout}\n"
        output += f"STDERR: \n{completed_process.stderr}\n"

    return output
