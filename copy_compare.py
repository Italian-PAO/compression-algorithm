import shutil
import os
import time
import difflib
import hashlib


def change_filename(same_name,Algorithm):
    if '.' in same_name:           ##为huffman而改
        ends = same_name.split('.')[-1]
        ends = '.'+ends
        new_name = same_name.replace(ends,'') + "_" + Algorithm + "_original"+ends
    ##if os.path.splitext(same_name)[1] == ".txt":
        ##new_name = same_name.replace('.txt', '')+"_"+Algorithm+"_original.txt"
    else:
        new_name = same_name+"_"+Algorithm+"_original"
    shutil.move(same_name,new_name)  ##重命名文件夹
    return new_name




def compare_file(old_file,new_file,Algorithm):
    def getFileMd5(filename):
        myhash = hashlib.md5()
        f = open(filename, 'rb')
        while True:
            b = f.read(8096)
            if not b:
                break
            myhash.update(b)
        f.close()
        return myhash.hexdigest()

    def getAllFiles(path):
        flist = []
        for root, dirs, fs in os.walk(path):
            for f in fs:
                f_fullpath = os.path.join(root, f)
                f_relativepath = f_fullpath[len(path):]
                flist.append(f_relativepath)
        return flist

    def dirCompare(old_file, new_file,dif_file):
        afiles = getAllFiles(old_file)
        bfiles = getAllFiles(new_file)

        setA = set(afiles)
        setB = set(bfiles)

        commonfiles = setA & setB  # 处理共有文件

        for f in sorted(commonfiles):
            amd = getFileMd5(old_file + '\\' + f)
            bmd = getFileMd5(new_file + '\\' + f)
            if amd != bmd:
                dif_file.write("dif file: %s" % (f)+"/n")

        # 处理仅出现在一个目录中的文件
        onlyFiles = setA ^ setB
        onlyInA = []
        onlyInB = []
        for of in onlyFiles:
            if of in afiles:
                onlyInA.append(of)
            elif of in bfiles:
                onlyInB.append(of)

        if len(onlyInA) > 0:
            onlyA="Files is only in"
            onlyA = onlyA+old_file
            dif_file.write(onlyA)
            for of in sorted(onlyInA):
                dif_file.write(of)

        if len(onlyInB) > 0:
            onlyB = "Files is only in"
            onlyB = onlyB + old_file
            dif_file.write(onlyB)
            for of in sorted(onlyInB):
                dif_file.write(of)


    dif_file = open(text_create(new_file,Algorithm), 'w')
    dirCompare(old_file,new_file,dif_file)






def text_create(new_file,Algorithm):
    if '.' in new_file:           ##为huffman而改
        ends = new_file.split('.')[-1]
        ends = '.'+ends
        new_file = new_file.replace(ends,'')
    f_path = new_file+"_"+Algorithm+"_difference"
    full_path = f_path + '.txt' #
    return full_path