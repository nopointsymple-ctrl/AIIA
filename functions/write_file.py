import os

def write_file(working_directory, file_path, content):

    abs_work = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    if os.path.commonpath([abs_work, abs_path]) != abs_work:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        parent = os.path.dirname(abs_path)
        if parent:
            os.makedirs(parent, exist_ok=True)

        with open(abs_path, "w") as f:
            f.write(content)

    except Exception as e:
        return f'Error: {e}'
        
   

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'