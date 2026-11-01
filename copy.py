import shutil
import os

# Enter source and destination folder paths
source_folder = r"/home/coder/workspace/github"
destination_folder = r"/home/coder/workspace"


# Check if source folder exists
if os.path.exists(source_folder):

    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Move only folders starting with 'q'
    for folder in os.listdir(source_folder):

        if folder.lower().startswith("q"):

            source_path = os.path.join(source_folder, folder)
            destination_path = os.path.join(destination_folder, folder)

            if os.path.isdir(source_path):

                # Remove existing destination folder
                if os.path.exists(destination_path):
                    shutil.rmtree(destination_path)

                # Move the source folder
                shutil.move(source_path, destination_path)

                print(f"Moved and replaced: {folder}")

    print("All matching folders moved successfully!")

else:
    print("Source folder does not exist!")