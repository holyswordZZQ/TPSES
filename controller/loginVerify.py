from model.readAdminAccount import readAdminAccount

def loginVerify(textname,textpassword):
    for (i, j) in readAdminAccount().items():  # 匹配账户密码，如果与问家中一致，即登陆成功
        if (textname, textpassword) == (i, j):
            return 0
        elif textname == i and textpassword != j:  # 密码出现错误
            return 1
        else:
            return 2
#状态码0表示正确 1表示密码错误 2表示账号错误