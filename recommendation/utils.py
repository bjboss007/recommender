
def parseData(score : int):
    if (score <= 15) and (score >=12):
        return "Severe"
    elif (score <=11) and (score >=9):
        return "Moderate"
    elif (score <=8) and (score >=5):
        return "Mild"
    elif (score <=4) and (score >=0):
        return "Normal"
    else:
        pass
    
def get_rating(dictionary:dict):
    for i in dictionary:
        length = len(dictionary[i])
        total_score = sum(dictionary[i])
        rating_score = total_score/length
        dictionary[i] = rating_score
    maximum = max(dictionary.values())
    return dictionary, maximum

def getKey(dictionary, val):
    for key, value in dictionary.items():
        if val == value:
            return key
