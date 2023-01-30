from ext_support.plot import RatioCanvas
import os

def make_dir(dir_name, trigger):
    if not os.path.isdir(dir_name):
        #os.mkdir(dir_name)
        smart_make_dir(dir_name)
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    if not os.path.isdir(dir_name+"/%s"%(trigger)):
        os.mkdir(dir_name+"/%s"%(trigger))

def make_dir_compare(tag1, tag2, dir_name):
    if not os.path.isdir(dir_name):
        #os.mkdir(dir_name)
        smart_make_dir(dir_name)
    if not os.path.isdir(dir_name+"/compare/"):
        os.mkdir(dir_name+"/compare/")
    if not os.path.isdir(dir_name+"/compare/compare%s_%s"%(tag1, tag2)):
        os.mkdir(dir_name+"/compare/compare%s_%s"%(tag1, tag2))

def smart_make_dir(name):
    """smart makedir, makedir for everything separated by a / """
    list_folders=name.split("/")
    print("list_folder: ", list_folders)
    complete_folder_name="."
    for f in list_folders:
        if not os.path.isdir(complete_folder_name+"/"+f):
            os.mkdir(complete_folder_name+"/"+f)
        complete_folder_name=complete_folder_name+"/"+f

