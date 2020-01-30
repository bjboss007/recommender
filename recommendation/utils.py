
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
# maxi = {}
# for i in data:
#     maxi[i] = sum(data[i])
# print(maxi)

# maximum = max(maxi.values())
# print("This is the maximum value in the dictionary")
# print(maximum)


def turner(dictionary:dict):
    for i in dictionary:
        dictionary[i] = sum(dictionary[i])
    maximum = max(dictionary.values())
    return dictionary, maximum

def getKey(dictionary, val):
    for key, value in dictionary.items():
        if val == value:
            return key
        # else:
        #     return "key not found"

maxi, maximum = turner(data)
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