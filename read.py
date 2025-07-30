def getFileContent():
    """Here, We are retrieving information from the txt file and storing it in a dictionary.."""

    file = open("Lands.txt","r")
    data = file.readlines()
    
    dic = {}
    for each in data:
        each = each.replace("\n", "")
        var = each.split(",")
        key = var[0]
        values = var[1:]
        dic[key]=values
    return dic

