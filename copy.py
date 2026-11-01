import shutil
import os

# Enter source and destination folder paths
source_folder = r"C:\Users\YourName\Desktop\Source"
destination_folder = r"C:\Users\YourName\Desktop\Destination"

# Check if source folder exists
if os.path.exists(source_folder):

    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Transfer all folders and their contents
    for folder in os.listdir(source_folder):

        source_path = os.path.join(source_folder, folder)
        destination_path = os.path.join(destination_folder, folder)

        if os.path.isdir(source_path):
            shutil.copytree(source_path, destination_path, dirs_exist_ok=True)

    print("All folders transferred successfully!")

else:
    print("Source folder does not exist!")