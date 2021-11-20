import sys
import os
from collections import defaultdict

def create_folder(
    folder_paths,
    clear_option=False,
    show_info=True
):
    msg = []

    if type(folder_paths) == str:
        folder_paths = [folder_paths]
    elif type(folder_paths) == list:
        pass
    
    for folder_path in folder_paths:
        if os.path.exists(folder_path) == False:
            os.mkdir(folder_path)
            msg.append("- Created New Folder: {0}".format(folder_path))
        else:
            msg.append('- The Folder Existed Already: {0}'.format(folder_path))
            if clear_option == False:
                pass
            else:
                msg.append("- Clear Option: True\n\t- Cleaning...")
                filenames = os.listdir(folder_path)
                for filename in filenames:
                    os.remove(os.path.join(folder_path, filename))
                    msg.append("\t- Deleted File: {0}".format(filename))
                msg.append("\t= Cleared")
    
    if show_info == True:
        print("\n".join(msg))
    else:
        pass


def get_all_files(
    folder_path,
    file_type="all",
    show_info=True
):
    filepath_list = []
    
    if file_type == "all":
        for filename in os.listdir(folder_path):
            if filename.startswith(".") is False:
                filepath_list.append(os.path.join(folder_path, filename))
    else:
        for filename in os.listdir(folder_path):
            if filename.startswith(".") is False and filename.split(".")[-1] == file_type:
                filepath_list.append(os.path.join(folder_path, filename))

    filepath_list = list(set(filepath_list))

    if show_info == True:
        print("")
        print("===== Files Info =====")
        print("* Folder Path: {0}".format(folder_path))
        print("* File Type: {0}".format(file_type))
        print("* Total Files: {0}".format(len(filepath_list)))
    else:
        pass
    
    return filepath_list


def scan_folder(
    folder_path,
    show_info=True,
    details=False
):
    """
    Here is the description
    """
    # if os.path.isdir(folder_path)
    results = {
        "file": {},
        "folder": {}
    }
    results["file"], results["folder"] = defaultdict(list), defaultdict(list)
    
    for name in os.listdir(folder_path):
        abs_path = os.path.join(folder_path, name)
        if os.path.isfile(abs_path): # is file
            if name.startswith("."):
                results["file"]["hidden"].append(name)
            else:
                filetype = name.split(".")[-1]
                results["file"][filetype].append(name)
        else: # is folder
            if name.startswith("."):
                results["folder"]["hidden"].append(name)
            else:
                results["folder"]["normal"].append(name)

    if show_info is True:
        msg = """
        \n\r============================== SCAN FOLDER ==============================
        \rFolder Path: '{folder_path}'
        \rSubfolders: {folder_cnt} => {folder_list}
        \rFiletypes: {filetype_cnt} => {filetype_list}
        """.format(
            folder_path=folder_path,
            folder_cnt=len(results["folder"]["hidden"]+results["folder"]["normal"]),
            folder_list=results["folder"]["hidden"]+results["folder"]["normal"],
            filetype_cnt=len(list(results["file"].keys())),
            filetype_list=list(results["file"].keys())
        )
        print(msg, end="")
        for index, filenames in results["file"].items():
            print("\r-'{0}' file count: {1}".format(index, len(filenames)))

            if details is True:
                for filename in filenames:
                    print("  {0}".format(filename))
            else:
                pass
    else:
        pass
    
    return results