from Huffman import Huffman
from lz4 import lz41
from Zip import files2zip, zip2files

if __name__ == "__main__":
    algorithm = input("1:Huffman \n2:Zip \n3: lz4 \n请输入数字以选择压缩算法：")
    if algorithm == "1":
        Huffman.main()
    elif algorithm == "2":
        de = int(input('请输入您需要进行的操作（1为压缩，2为解压）：'))
        if de == 1:
            files2zip.files2zip()
        if de == 2:
            zip2files.zip2files()
    elif algorithm == "3":
        lz41.main()