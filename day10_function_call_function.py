def is_lw(age):       
    return age>=20
def is_fwl(age):
    return is_lw(age)    #只能函数里面只能写一个规则，is_lw是引用的规则
print(is_lw(20))
print(is_fwl(19))      #函数调用加括号，函数名不加括号和符号