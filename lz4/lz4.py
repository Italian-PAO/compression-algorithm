'''
lz4 program to compress a folder into *.lz4r format
'''
import sys
import os
import getopt
import pathlib
import tarfile
import tempfile
from . import liblz4
from . import lz4archiver
import string
import copy_compare


def make_archive(dirname):
    f, ar_name = tempfile.mkstemp('.tar')
    os.close(f)
    ar_file = lz4archiver.ArchiveFile()
    ar_file.open_for_write(ar_name)
    ar_file.packfolder(dirname)
    ar_file.close()
    return ar_name


def compress_folder(src_dir, filename):
    ar_name = make_archive(src_dir)
    compresser = liblz4.Compresser()
    compresser.compress_file(ar_name, filename)
    print('Successfully compressed ', src_dir, ' to ', filename)


def extract_folder(filename, dest_dir='.'):
    extractor = liblz4.Extractor()
    f, ar_name = tempfile.mkstemp('.tar')
    os.close(f)
    try:
        extractor.extract_file(filename, ar_name)
        ar_file = lz4archiver.ArchiveFile()
        ar_file.open_for_read(ar_name)
        ar_file.unpack(dest_dir)
        ar_file.close()
        print('Successfully extracted ', filename, ' to current directory')
    except liblz4.BadFileError:
        print('Error: Unrecognized file format')
    except lz4archiver.UnpackError:
    	print('Error: Unrecognized archive format')


usage =\
    '''
Usage:
 Compress a folder:
   lz4 -c dir_name.lz4r dir_name

 Extract file:
   lz4 -x dir_name.lz4r
'''


def main(command, dirname):
    print(command, dirname)
    filename =  dirname.split('.')[0]+".lz4r"
    dir_path = dirname.strip("\"")
    if os.path.exists(dir_path) == False:
        return ("路径输入错误")
    if filename and command == '-c':
        if os.path.exists(filename) == True:
            return('该压缩文件名已被占用，无法进行压缩')
        compress_folder(dirname, filename)
        original_path = copy_compare.change_filename(dirname,"lz4",1,filename)   ######需求变更添加内容
        extract_folder(filename)                 ######需求变更添加内容
        copy_compare.compare_file(original_path , dirname,"lz4")             ######需求变更添加内容
        copy_compare.del_file(dirname)
        copy_compare.change_filename(dirname, "lz4", 2,original_path)
        return('压缩完成，校验结果已保存在difference文件中')
    elif filename and command == '-x':
        if not os.path.splitext(dir_path)[1] == ".lz4r":
            return ('文件类型不合法，无法进行解压')
        filepath = dirname.replace('.lz4r','')
        #if os.path.exists(filepath) == True:
         #   original_path = copy_compare.change_filename(filepath,"lz4")   ######需求变更添加内容
          #  extract_folder(dirname)                 ######需求变更添加内容
           # copy_compare.compare_file(original_path , filepath,"lz4")             ######需求变更添加内容
            #return ('该解压文件名已被占用，将对原文件复制更名后覆盖')
        #print('Extracting ', filename, ', please wait...')
        if os.path.exists(filepath) == True:
            return('该解压文件名已被占用，无法进行解压')
        extract_folder(dirname)
        return('解压完成')
    else:
        print(usage)

