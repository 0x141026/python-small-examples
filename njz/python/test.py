#定义一个数组接受用户的输入 
n=input("请输入要排序多少个数字：")
n=int(n)
arr1 = [0 for i in range(n)]

print("请输入要比较的数：")
for j in range(n):
    print('请输入%d个数' % int(j+1) ,end = '')
    arr1[j]=input("")
    arr1[j]=int(arr1[j])
print("输出输入的所有数字：", end = '')
for k in arr1:
    print(k, end = '  ')
    
def bubbleSort(shuzu):
    length = len(arr1)
    for i in range(0,length-1):
        for j in range(0,length-1-i):
            if shuzu[j] > shuzu[j+1]:
                temp = shuzu[j]
                shuzu[j] = shuzu[j+1]
                shuzu[j+1] = temp
    print("\n排序之后的序列是：",end = '')  
    for k in range(n):
        print(arr1[k],end = ' ')
bubbleSort(arr1)



