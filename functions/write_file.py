import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    #validate
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
           # Will be True or False
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if valid_target_file is False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file) is True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
    except Exception as e:
       return f"Error: {e}"


    try:
        with open(target_file, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
schema_write_file = {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Takes user content passed to it and writes it to the targetted file",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Name of target file itself, relative to the working directory (default is the working directory itself)",
                    },
                    "content": {
                        "type": "string",
                        "description": "User inputted information that is to be written to the target file given as file_path"
                    }
                },
            },
        },
    }
