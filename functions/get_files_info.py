import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    #validate
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir is False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isdir(target_dir) is False:
            return f'Error: "{directory}" is not a directory'
        #if valid_target_dir is True:
            #print(f'Success: "{directory}" is within the working directory')
    except Exception as e:
        return f"Error: {e}"

#get info
    try:
        file_total = ""
        dir_cont = os.listdir(target_dir)
        #print(dir_cont)
        for file in dir_cont:
            file_name = file
            file_size = os.path.getsize(os.path.join(target_dir, file))
            is_dir_bool = os.path.isdir(os.path.join(target_dir, file))
            file_info = f"- {file_name}: file_size={file_size}, is_dir={is_dir_bool}"
            file_total += f"{file_info}\n"
        return file_total
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
