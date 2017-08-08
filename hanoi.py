def hanoi(n,x,y,z):
    if n==1:
        print(x,'---->',z)
        return
    else:
        hanoi(n-1,x,z,y)  #将上面的n-1个先移到y上
        hanoi(1,x,y,z)    #将最下面的一个从x移到z上
        hanoi(n-1,y,x,z)  #将上面的n-1个从y上移到上

hanoi(3,'x','y','z')
