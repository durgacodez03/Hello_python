def reverse(data_list):
    length = len(data_list)
    s = length
    var = []
    new_list = [None]*length
    for item in data_list:
        s = s-1
        print(s,"Durga")
        new_list[s] = item
    var.append(new_list)
    print(var)

data_list = ["a","b","c","d"]
reverse(data_list)