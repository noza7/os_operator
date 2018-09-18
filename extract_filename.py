import re

# 自定义提取函数


def extract_filename(filename):
    # 最后一个/分割的两部分，用正则取出
    extract_re=re.findall('(.*)/(.*)',filename)
    # 取出后的形式是“[('H:/Python/os_operator', 'create_dir.py')]”，返回的形式是列表套一个元组
    # 因为就一个元素所以x[0]取出，因为'create_dir.py'是我们想要的，所以用[-1]取出
    extract_name_extension=extract_re[0][-1]
    # 利用正则去掉扩展名，我是直接取"."之前的
    extract_name=re.findall('(.*)\.',extract_name_extension)
    # extract_name是一个列表，而且本例就一个元素，所以直接返回extract_name[0]就可以了
    return extract_name_extension,extract_name[0]


a = 'H:/Python/os_operator/create_dir.py'
print(extract_filename(a)[-1])
