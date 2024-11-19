import os
import shutil

def check_and_rename_folders(root_path, old_suffix, new_suffix):
    # 遍历根目录下的所有文件夹
    for folder_name in os.listdir(root_path):
        folder_path = os.path.join(root_path, folder_name)

        # 检查是否为文件夹
        if os.path.isdir(folder_path):
            # 查找.LiTower文件
            las_files_found = any(file.endswith('.LiTower') for file in os.listdir(folder_path))

            # 检查文件夹名称是否包含旧后缀并且包含.LiTower文件
            if las_files_found and folder_name.endswith(old_suffix):
                # 移除旧后缀并获取新的文件夹名称
                new_folder_name = folder_name[:-(len(old_suffix))]
                new_folder_path = os.path.join(root_path, new_folder_name)

                # 重命名文件夹
                shutil.move(folder_path, new_folder_path)
                print(f"文件夹 {folder_name} 内包含 .LiTower 文件，已移除 -无杆塔文件 后缀，重命名为 {new_folder_name}")
            elif not las_files_found:
                # 若没有找到.LiTower文件，则进行重命名
                if old_suffix not in folder_name:
                    new_folder_name = folder_name + new_suffix
                    new_folder_path = os.path.join(root_path, new_folder_name)

                    shutil.move(folder_path, new_folder_path)
                    print(f"由于文件夹 {folder_name} 内未发现 .LiTower 文件，已将其重命名为 {new_folder_name}")
                else:
                    print(f"文件夹 {folder_name} 已经带有 -无杆塔文件 后缀，但因包含 .LiTower 文件而未进行更改")
            else:
                print(f"文件夹 {folder_name} 内包含 .LiTower 文件，无需更改后缀")

# 使用函数的例子
directory = input("请输入航线所在目录路径：")
while not os.path.isdir(directory):
    directory = input("路径无效，请重新输入：")

old_suffix = "-无杆塔文件"
new_suffix = "-待处理"

check_and_rename_folders(directory, old_suffix, new_suffix)