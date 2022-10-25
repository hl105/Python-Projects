def inputFloat(a):
    print(a)
    return float(input())

def formatHours(hour,label):
    return str(round(hour,2))+' '+label

def indentMessage(message, targetlength):
    len(message)
    indentsize= targetlength - len(message)
    return ' ' * indentsize + message

def createBar(letter, length):
    return round(length) * letter



def timeProfile():
    '''summarizes profile'''
    name = input("What is your name? ")
    work = inputFloat("How many hours do you work each week?")
    sleep = inputFloat("How many hours per day do you sleep on average?") * 7
    classtime = inputFloat("How many classes are you taking this semester?")
    avgclasstime = inputFloat("For one class, what is the average time spent in the classroom per week?")
    ecname = input("What shall we call the 'everything else' category? ")
    echours = inputFloat("How many hours per week do you spend on " +  "'"+ ecname +" '"+ "?")
    coursework = classtime * avgclasstime *3
    print("Weekly time profile for Latanya: ")
    lwork = formatHours(work, "work hours: ") 
    lsleep = formatHours(sleep, "sleep hours: ")
    lclass = formatHours(coursework, "class hours: ")
    lechours = formatHours(echours, ecname + "hours: ")
    freetime = 168-(work+sleep+coursework+echours)
    lfreetime = formatHours((freetime), "free hours: ")
    targetlen = max(len(lwork), len(lsleep), len(lclass), len(lechours), len(lfreetime))
    print(indentMessage(lwork, targetlen)+createBar("W", work))
    print(indentMessage(lsleep, targetlen)+createBar("S", sleep))
    print(indentMessage(lclass, targetlen)+createBar("C", coursework))
    print(indentMessage(lechours, targetlen)+createBar("E", echours))
    print(indentMessage(lfreetime, targetlen)+createBar("F", freetime))
    
timeProfile()