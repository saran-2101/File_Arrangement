import os
import shutil 

# Define source and destination paths
source = r"C:\Users\saran\Documents" #YOUR SOURCE FOLDER PATH
destination = r"C:\Users\saran\Pictures" #YOUR DESTINATION FOLDER PATH

try:
    # Check if source directory exists
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source directory not found: {source}")
    
    # Check if destination directory exists
    if not os.path.exists(destination):
        raise FileNotFoundError(f"Destination directory not found: {destination}")
    
    # Iterate through each file in source directory
    for file in os.listdir(source):
        # If any folder present then skip that folder 
        if os.path.isdir(os.path.join(source,file)):
            print(f"Skip Folder:{file}") 
            continue

        # Extract file extension (e.g., 'jpg', 'pdf', 'txt')
        ext = os.path.splitext(file)[1][1:]

        # Create folder name based on extension (e.g., 'jpgFile', 'pdfFile')
        folder_name = ext.upper() + "File"

        # Change to destination directory
        os.chdir(destination)
        
        # Check if folder already exists, if not create it
        if not os.path.exists(folder_name):
                os.mkdir(folder_name)

        # Move file to appropriate folder   
        shutil.copy(os.path.join(source, file),os.path.join(destination, folder_name))
    print("Task Completed")

except FileNotFoundError as fnf:
    print(f"Error: {fnf}")
except PermissionError:
    print("Error: Permission denied. Try running as Administrator.")
except Exception as e:
    print(f"Error: {e}")
