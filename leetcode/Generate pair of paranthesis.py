def generateParanthesis(openB,closeB,n,s=[]):

    if (closeB==n):
        print(''.join(s))
        return

    else:
        if (openB<closeB):
            s.append(')')
            generateParanthesis(openB,closeB+1,n,s)
            s.pop()
        if (openB<n):
            s.append('(')
            generateParanthesis(openB+1,closeB,n,s)
            s.pop()

    return generateParanthesis()

generateParanthesis(1,1,1)