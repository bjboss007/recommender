
def parseData(score : int):
    if (score <= 15) and (score >=10):
        return "Severe"
    elif (score <=9) and (score >=6):
        return "Moderate"
    elif (score <=5) and (score >=0):
        return "Normal"
    else:
        pass
    

data = {"Hangout" : [4,3,4,5,1,2,3,5], "Relax" : [4,3,4,3,4,4,3,1] ,"Exercise" : [4,3,4,5,3,4,3,5]}

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

maxi, maximum = get_rating(data)
key = getKey(maxi,maximum)
print("This is the lost key : ", key)

print(" THis is the values of the dictionary: ",maxi)
# if __name__ == "__main__":
#     m = parseData(4)
#     print(m)


# data = {"Exercise" : [4,3,4,5,3,5], "Hangout" : [4,3,4,5,1,2,3,5], "Relax" : [4,3,4,3,4,4,3,1] }


# import time
# flag = True

# sink = []
# while flag:
#     for i in range(10):
#         time.sleep(1)
#         sink.append(i)
#         print(sink)
#         if len(sink) == 5:
#             flag = False
#             print('present')
#             break