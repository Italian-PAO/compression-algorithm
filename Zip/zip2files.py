import os
import zipfile
def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(os.path.splitext(file_name)[0]):
        pass
    else:
        os.mkdir(os.path.splitext(file_name)[0])
    for names in zip_file.namelist():
        zip_file.extract(names,os.path.splitext(file_name)[0])
    zip_file.close()



def checkfileiszip(file):
    path= file.strip("\"")
    if os.path.exists(path) == False:
        print("文件不存在，请检查文件路径")
        trayagain()
    else:
        if os.path.splitext(path)[1] == ".zip":
            un_zip(path)
        else:
            print("文件格式错误，目前只支持zip格式")
            trayagain()


def trayagain():
    filepath = input("手动输入需要解压的文件路径：")
    checkfileiszip(filepath)


if __name__ == '__main__':
    trayagain()
