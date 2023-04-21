
import json

# Add .json file here
link = ""

def set_json(data, new_link):
    with open(new_link,'w') as f:
        json.dump(data, f)


def get_json(link):
    with open(link,'r') as f:
        data = json.load(f)
    return data


new_dict = {}


def write2dict(k, v,):
    try:
        new_dict[v].append(k)
    except:
        new_dict[v] = [k]


def singleTypeChecker(k, v):
    if type(v) == None:
        write2dict(k, "None")
    if type(v) == type(None):
        write2dict(k, "None")
    if type(v) == type(42):
        write2dict(k, v)
    if type(v) == type(42.0):
        write2dict(k, v)
    if type(v) == type("42"):
        write2dict(k, v)
    if type(v) == type(True):
        write2dict(k, v)


def listTypeChecker(k, v):
    if type(v) == type(["1"]):
        for x in range(len(v)):
            if type(v[x]) == type(["1"]):
                listTypeChecker(k + " " + str(x), v[x])
            if type(v[x]) == type({"1":1}):
                dictTypeChecker(k + " " + str(x), v[x])
            else:
                #print("LIST: " + str(v[x]))
                singleTypeChecker(k + " " + str(x), v[x])


def dictTypeChecker(k, v):
    if type(v) == type({"1":1}):
        for k2, v2 in v.items():
            if type(v2) == type({"1":1}):
                k3 = k + " " + k2
                dictTypeChecker(k3, v2)
            if type(v2) == type(["1"]):
                k3 = k + " " + k2
                listTypeChecker(k3, v2)
            else:
                #print("DICT: " + str(k2))
                k3 = k + " " + k2
                singleTypeChecker(k3, v2)


def traverse_json(data):
    for k, v in data.items():
        singleTypeChecker(k, v)
        # check list and dict here
        listTypeChecker(k, v)
        dictTypeChecker(k, v)


####### MAIN LOOP #######################################################

data = get_json(link)

#print(len(data))

traverse_json(data)

set_json(new_dict, "anti-json.json")

# Testing Please Remove (Printing Out New Dictionary Here)
print("")
for k, v in new_dict.items():
    print(str(k) + ": " + str(v))
