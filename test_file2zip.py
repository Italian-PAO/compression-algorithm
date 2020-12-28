from Zip import files2zip

file_path = input("请输入要压缩的文件路径：")

info = files2zip.files2zip(file_path)

print(info)