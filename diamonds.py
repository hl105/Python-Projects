zero  = '     '
one   = '  1  '
two   = ' 2 2 '
three = '3 3 3'
empty = ''


'''shape of first pattern line'''
def dshape():
    return(
        print((one+zero)*4),
        print((two+zero)*4),
        print((three+zero)*4),
        print((two+zero)*4),
        print((one+zero)*4)
        )

''' shape of second pattern line'''
def twodshape():
    return(
        print((zero+one)*4),
        print((zero+two)*4),
        print((zero+three)*4),
        print((zero+two)*4),
        print((zero+one)*4)
        )

'''brings two patterns together'''
def addtogether():
    return (dshape()+twodshape())


'''final pattern'''

def diamondPattern():
    addtogether(),
    addtogether(),
    addtogether(),
    addtogether()


diamondPattern()


