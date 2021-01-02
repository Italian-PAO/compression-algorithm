from Zip import zip2files

zip_path = input("请输入要解压的文件路径：")

info = zip2files.zip2files(zip_path)

print("该解压文件名已被占用，无法进行解压")