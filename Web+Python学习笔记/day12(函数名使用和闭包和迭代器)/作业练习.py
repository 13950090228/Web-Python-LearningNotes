n=int(input('请输入要几行：'))
for i in range(1,n+1):
    for j in range(2*n-2*i):
        print('',end=' ')
    for k in range(2*i-1):
        print('*',end=' ')
    print('')
