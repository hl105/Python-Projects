def makeSofter(channel):
    '''makes the sound softer'''
    result=[num*0.1 for num in channel]
    return result

def chipmunk(channel):
    '''high pithced & fast'''
    result=[channel[i] for i in range(len(channel)) if i%2==0]
    return result

def removeVocals(left,right):
    '''removes the vocals'''
    result=[]
    final=[]
    for i in range(len(left)):
        result.append(left[i]-right[i])
        final.append(result[i]/2)
    return final

def reverse(channel):
    '''reverses the sound'''
    result=[]
    for num in channel:
        result.insert(0,num)
    return result

def twoSampleDelay(channel, twoSampleBack, oneSampleBack):
    '''delays the music'''
    result=channel[:]
    final=[]
    result.insert(0, oneSampleBack)
    result.insert(0, twoSampleBack)
    for i in range(len(result[0:len(result)-2])):
        calc=(result[i]+channel[i])/2
        final.append(calc)
    return final

