import re
# 列表统一加前缀
def list_add_prefix(list_name,pre_str):
    pre_list=list(map(lambda x: pre_str+x, list_name))
    return pre_list

# l = ['abc','def','xyz']
# pre_str='abcd-/'
# lp=list_add_prefix(l,pre_str)
# print(lp)