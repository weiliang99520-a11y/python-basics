for login_count in range(1,6):
    if login_count  >=3:
        print(login_count,'次登录，需要验证码')
    else:
        print(login_count,'次登录，直接进入')
