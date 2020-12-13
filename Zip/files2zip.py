import zipfile,os
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

def compress(get_files_path, set_files_path,pwd):
    print("正在压缩....")
    f = zipfile.ZipFile(set_files_path, 'w', zipfile.ZIP_DEFLATED)
    if os.path.isfile(get_files_path):
        f.write(get_files_path,os.path.basename(get_files_path))
    else:
      for dirpath, dirnames, filenames in os.walk(get_files_path):
        fpath = dirpath.replace(get_files_path,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            f.write(os.path.join(dirpath,filename), fpath+filename)
    f.close()

    print("压缩完成")

    input("Prease <enter>")


def checkfile(get_files_path):
    path=get_files_path.strip("\"")
    if os.path.exists(path)==False:
        print("路径输入错误")
        get_files_path = input("重新输入需要处理的文件路径：")#需要压缩的文件夹
        checkfile(get_files_path)
    else:
        if os.path.splitext(path)[1] == ".zip":
            un_zip(path)
        else:
            # 存放的压缩文件地址(注意:不能与上述压缩文件夹一样)
            set_files_path = path+".zip"
            compress(path, set_files_path,pwd)


if __name__=='__main__':
    pwd = input("使用者密码：")#需要压缩的文件夹
    get_files_path = input("需要处理的文件路径：")#需要压缩的文件夹
    checkfile(get_files_path)



