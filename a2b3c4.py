def expand(input):
    result=""
    i=0
    while i<len(input):
        char=input[i]
        i+=1
        num_str=""
        while i<len(input) and input[i].isdigit():
            num_str+=input[i]
            i+=1
        num=int(num_str)
        result+=char*num
    return result
print(expand("a4b103c7"))