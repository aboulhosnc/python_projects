


def jazzify(lst):
    new_list = [i.replace(i,i+'7')  if not i.endswith('7') else i.replace(i,i) for i in lst]
    # for i in lst:
    #     if not i.endswith('7'):
    #         # print('did not end with 7')
    #         # print(i)
    #         i = i + '7'
    #         print(i)
    print(new_list)
    return new_list
	

def main():
    print("hello world")
    print("jazzify")
    jazzify(["G", "F", "C"])
    jazzify(["Dm", "G", "E", "A"])
    jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"])
    jazzify([])


jazzify(["G", "F", "C"]) #➞ ["G7", "F7", "C7"]

# jazzify(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]

# jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]

# jazzify([]) ➞ []




if __name__ == "__main__":
    main()