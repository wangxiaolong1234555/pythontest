name = input('请输入用户名字:')

password = input('请输入密码')

if name == 'root' and password == '123':
    print('root login success')
else:
    print('用户名或密码错误')
""" if 条件:
        满足条件时要做的事情1
        满足条件时要做的事情2
        满足条件时要做的事情3
        ...(省略)...
    else:
        不满足条件时要做的事情1
        不满足条件时要做的事情2
        不满足条件时要做的事情3
        ...(省略)... """