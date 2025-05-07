import os
from pathlib import Path
import Welcome  # Assuming this is a valid module with a `welcome()` function

def endswith(filename):
    return Path(filename).suffix

def checkforduplicate(foldername):
    if os.path.exists(foldername):
        return 1  # Folder exists
    return 0  # Folder doesn't exist

def createfolder(filename):
    ext = endswith(filename)

    folder_mappings = {
        ".txt": "Text Files",
        ".docx": "Docx Files",
        ".xlsx": "Excel Files",
        ".bat": "Batch Files",
        ".ppt": "Presentation Files",
        ".bmp": "Image Files",
        ".jpg": "Image Files",
        ".jpeg": "Image Files",
        ".png": "Image Files",
        ".html":"HTML Files",
        ".htm":"HTML Files",
        ".js":"JavaScript Files",
        ".java":"Java Files",
        ".c":"C Files",
        ".cpp":"Cpp Files",
        ".css": "CSS Files"
    }

    foldername = folder_mappings.get(ext, None)

    if foldername:
        if checkforduplicate(foldername) == 0:
            os.makedirs(foldername)  # Create the folder
            print(f"Created folder: {foldername}")
            filepath=os.path.join(foldername,filename)
            with open(filepath,'w') as g: #saved file
                g.write(f"Heelo it is a {foldername}")
                print(f"File saved at {filepath}")
        filepath=os.path.join(foldername,filename)
        with open(filepath,'w') as f:
            pass
            print(f"File saved at {os.path.abspath(filepath)}")
    else:

        print("A new extension detected!! Unable to create folder!!")
    file=os.path.join(foldername,filename)
    print(f"File saved at {os.path.abspath(file)}")

# Main execution
Welcome.welcome()
while True:
    filename = input("Enter the filename: ")
    ext = endswith(filename)
    print(f"File extension: {ext}")
    createfolder(filename)
