import os

root_path = '/home/sachin/Music/automated-wallpaper/'
folders = ['Folder_1','Folder_x','Folder_y']
for folder in folders:
    os.mkdir(os.path.join(root_path,folder))
