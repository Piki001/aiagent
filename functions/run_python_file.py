import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    #validate
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
           # Will be True or False
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if valid_target_file is False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_file) is False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if file_path.endswith(".py") is False:
            return f'Error: "{file_path}" is not a Python file'
    except Exception as e:
       return f"Error: {e}"

    try:
        command = ["python", target_file]
        if args:
            command.extend(args)
        result = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=working_dir_abs)
        return_list = []
        if result.returncode != 0:
            return_list.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            return_list.append(f"No output produced")
        else:
            return_list.append(f"STDOUT: {result.stdout}")
            return_list.append(f"STDERR: {result.stderr}")
        return_string = "\n".join(return_list)
        return return_string
    except Exception as e:
       return f"Error: {e}"
