# def fib(max):
#     n,a,b=0,0,1
#     while n <max:
#         # print(b)
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return "---done---"
# f=fib(10)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# g=fib(6)
# print("---------------------------")
# while True:
#     try:
#         x=next(g)
#         print("g:",x)
#     except StopIteration as e:
#         print("generator return value:",e.value)
#         break
# def fib(max):
#     n,a,b=0,0,1
#     while n <max:
#         # print(b)
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return "---done---"
# f = fib(10)
# print(type(f))
# print(f.__next__())
# print("你可以随时插入你的语句")
# print(f.__next__())
# print("生成器会记住之前的位置继续循环")
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print("打了那么多就是要超出限制")
# print(f.__next__())
# print(f.__next__())
import time
def customer(name):
    print("%s开始吃包子啦"%name)
    while True:
        baozi = yield
        print("%s吃了%s的包子"%(name,baozi))
def product(name):
    c=customer("A")
    c2=customer("B")
    c.__next__()
    c2.__next__()
    print("开始做包子啦")
    for i in range(10):
        print("做了两个包子")
        time.sleep(1)
        c.send("韭菜馅")
        c2.send("香菇馅")
product("C")