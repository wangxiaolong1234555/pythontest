"""if xxx1:
    事情1
elif xxx2:
    事情2
elif xxx3:
    事情3"""

score = 77
if 90 <= score <= 100:
    print('本次考试，等级为A')
if 80 <= score <= 90:
    print('本次考试，等级为B')
if 70 <= score <= 80:
    print('本次考试，等级为C')
if 60 <= score <= 70:
    print('本次考试， 等级为D')
if 0 <= score <= 60:
    print('本次考试，等级为E')
""" 当xxx1满足时，执行事情1，然后整个if结束
    当xxx1不满足时，那么判断xxx2，如果xxx2满足，则执行事情2，然后整个if结束
    当xxx1不满足时，xxx2也不满足，如果xxx3满足，则执行事情3，然后整个if结束 """