#print('test')
def fun_name():
    return

def printSum(a,b): #形式参数：意义上的一种参数，定义时不占内存地址
    '''
    prinf sum, 鼠标放function上就能看到我
    '''
    print('%d+%d=%d' %(a,b,a+b))
    pass

def printSum1(a=10, b=20):  #默认参数
    print('%d+%d=%d' %(a,b,a+b))
    pass

printSum(1, 2)
printSum1(50)

def printSum2(*args): #可变参数：当参数个数不确定的时候
    sum = 0
    for item in args:
        sum+=item
    print('sum=%d' %sum)
    pass
printSum2(1,2,3,4,5)


'''
参数分类:
必选参数，默认参数，可选参数，关键字参数

'''
'''
关键字key可变参数
**来定义
参数关键字所以一个字典类型 key是string
'''
def keyFunc(**kwargs):
    print(kwargs)
    pass
dictA = {"name": "a", "age": 2}
keyFunc(**dictA)  #if pass a dict, **is required; or keyFunc(name="a", age=2)
keyFunc(name='a', age=2)

def complexFunc(*args, **kwargs):
    '''
    **kwargs need to be in front of *args
    '''
    print(args)
    print(kwargs)
    pass
complexFunc(1, 2, 3, 4, name='b')

def calSum(num):
    li = []
    result = 0
    i = 1
    while i <= num:
        result+=1
        i += 1
        pass
    return result
    
print(calSum(5))

#接收n个数字，求参数数字和
#找出传入的列表或元组的基数位对应的元素，并返回一个新列表
#检查传入字典的每一个value的长度，如果大于2，仅保留前两个长度的内容， 并将新内容返回字典

def sumN(*args):
    '''
    接收n个数字，求参数数字和
    '''
    sum = 0
    for idx in args:
        sum += idx
        pass
    print("sum=%s" %sum)
    pass

def findIdx(aList):
    '''
    找出传入的列表或元组的基数位对应的元素，并返回一个新列表
    '''
    li = []
    for position in range(len(aList)):
        if ((position+1) % 2 != 0):
            li.append(aList[position])
            pass
        pass   
    return li
    pass

def fomatDict(aDict):
    '''
    检查传入字典的每一个value的长度，如果大于2，仅保留前两个长度的内容， 并将新内容返回新的字典
    '''
    result = {}
    for key, value in aDict.items():
        if len(value) > 2:
            result[key] = value[:2]
            pass
        pass
    return result
    pass

sumN(1, 2, 3, 4, 5)
num = [1, 2, 3, 4, 'a', 'c']
dictA = {"name":"apple","color":"green","size":"small"}
print(num)
print(findIdx(num))
print(dictA)
print(fomatDict(dictA))

'''
build-in function
'''
print(abs(-1))
li=[2,4,53,45,4]
print(max(li))  #dict will work as well
a,b,c=1,2,3
print('动态执行函数={}'.format(eval('a+b+c')))  #执行表达式, 可以执行函数eval('test()')
print(chr(65))

#sort只能用于list， sorted可以是任何迭代对象
#sort直接改变原list，sorted会创建一个新的
li.sort()
print(li)

finList = sorted(li, reverse=True)
print(finList)
print(li)

#zip() zip to tuple
li1 = [1, 2, 3]
li2 = ['a', 'b', 'c']
print(list(zip(li1, li2)))  #[(1, 'a'), (2, 'b'), (3, 'c')]

#三元运算
result = 5 if 3 > 2 else 6
print(result)
