import zipfile,os
import copy_compare
import Zip.zip2files

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

def compress(get_files_path, set_files_path):
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

    zipname=get_files_path.split('.')[0]+".zip"
    original_path = copy_compare.change_filename(get_files_path, "zip", 1,zipname)  ######需求变更添加内容
    Zip.zip2files.zip2files(zipname)  ######需求变更添加内容
    copy_compare.compare_file(original_path, get_files_path, "zip")  ######需求变更添加内容
    copy_compare.del_file(get_files_path)
    copy_compare.change_filename(get_files_path, "zip", 2, original_path)
    return ('压缩完成，校验结果保存在difference文件中')




def checkfile(get_files_path):
    path=get_files_path.strip("\"")
    if os.path.exists(path)==False:
        return("路径输入错误")
    else:
        zipname = path + ".zip"
        if os.path.exists(zipname) == True:
            return ('该压缩文件名已被占用，无法进行压缩')
        if os.path.splitext(path)[1] == ".zip":
            return ("该文件已经是zip压缩文件")
        else:
            # 存放的压缩文件地址(注意:不能与上述压缩文件夹一样)
            set_files_path = path+".zip"
            return (compress(path, set_files_path))



def files2zip(file_location):
    hint=checkfile(file_location)
    return hint



