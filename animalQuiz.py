def boolFromResponse(response):
    '''true if response starts with y alphabet'''
    return response.lower().startswith("y")

def boolFromUser(prompt):
    '''finds y/n by input to boolFromResponse'''
    userresponse = input(prompt)
    return boolFromResponse(userresponse)
    
def chooseAnimal(meat, cold, fuzzy):
    '''finds the animal depending on the res from boolFromUser'''
    if meat and cold and fuzzy:
        return "polar bear"
    elif meat and cold and not(fuzzy):
        return "orca"
    elif meat and not(cold) and fuzzy:
        return "tiger"
    elif meat and not(cold) and not(fuzzy):
        return "komodo dragon"
    elif not(meat) and cold and fuzzy:
        return "yak"
    elif not(meat) and cold and not(fuzzy):
        return "clam"
    elif not(meat) and not(cold) and fuzzy:
        return "bunny"
    elif not(meat) and not(cold) and not(fuzzy):
        return "tortoise"

def animalQuiz():
    ''' animal quiz'''
    print("what animal are you? Let's find out!")
    print("Your animal is the " + chooseAnimal(boolFromUser("Do you like to eat meat?"),boolFromUser("Do you like cold weather?"),boolFromUser("Do you like fuzzy things?")))

 
animalQuiz()


    