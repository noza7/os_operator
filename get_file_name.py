# -!- coding: utf-8 -!-
import os
from openpyxl import Workbook
# 做一个获取文件名的类


class GetFileName:

    def get_file_name(self, file_dir):
        for root, dirs, files in os.walk(file_dir):
            # return root#当前目录路径
            # return dirs#当前路径下所有子目录
            return files  # 当前路径下所有非目录子文件

    # 获得某一扩展名类文件
    # 其中os.path.splitext()函数将路径拆分为文件名+扩展名，例如os.path.splitext(“E:/lena.jpg”)将得到”E:/lena“+".jpg"
    def class_file_name(self, file_dir, file_type):
        ls = []
        f = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == file_type:
                    ls.append(os.path.join(root, file))
                    f.append(file)

        return f

# 删除已有文件


my_file = '文件名列表.xlsx' # 文件路径
if os.path.exists(my_file):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
    os.remove(my_file)  # 则删除
    # os.unlink(my_file)

# 创建一个新的excel表格
wb = Workbook()
ws = wb.active
ws.title = '文件名列表'


# 写入路径并输出
def output_data():
    # a = 'F:/newWORK/2018上半年/报补考/JC'
    a = input('请输入文件夹路径：')
    GFN = GetFileName()
    # print(GFN.get_file_name(a))
    for i in range(len(GFN.get_file_name(a))):
        # print(i)
        print(GFN.get_file_name(a)[i])
        ws['A{}'.format(i+1)]=GFN.get_file_name(a)[i]


output_data()

wb = wb.save('文件名列表.xlsx')