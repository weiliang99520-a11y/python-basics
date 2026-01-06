# 功能：输入年龄，最多尝试3次，成年才能进入
count=0
while True:
    age=int(input('请输入你的年龄:'))
    count = count +1
    if age >=18:
        print('验证通过,可以进入')
        break
    else:
        print('未成年,请重新输入')
        if count ==3:
            print('输入次数过多,无法登入')
            break
        