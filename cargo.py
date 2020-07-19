

# Test.assert_equals(will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]), True)
# Test.assert_equals(will_fit(["L", "L", "M"], [56, 62, 84, 90]), True)
# Test.assert_equals(will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70 , 80, 90, 200]), False)
# Test.assert_equals(will_fit(["S", "L"], [73 , 87, 95, 229]), False)
# Test.assert_equals(will_fit(["L", "L", "L", "L"], [54, 54, 200, 200, 200]), True, "54 and 54 can fit in one hold.")


def will_fit(holds, cargo):
    
    holds_sum = 0
    cargo_sum = 0
    bool_verdict = False
    thisdict = {
  "S": 50,
  "M": 100,
  "L": 200 }

    for x in holds :
      holds_sum += thisdict[x]
    # return sum 

    for x in cargo :
        cargo_sum += x

    if (holds_sum >= cargo_sum):
        bool_verdict = True

    return True if holds_sum > cargo_sum else False
    # print(holds_sum,cargo_sum,bool_verdict)
    # return holds_sum,cargo_sum, bool_verdict

    

def main():
    print("hello world")
    print("cargo hold")
    # print(will_fit(["M", "L", "L", "M"], [56, 62, 84, 90])) # will be 600 true
    # will_fit(["L", "L", "M"], [56, 62, 84, 90]) #true
    # will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70 , 80, 90, 200]) #false
    will_fit(["S", "L"], [73 , 87, 95, 229]) #false 
    # will_fit(["L", "L", "L", "L"], [54, 54, 200, 200, 200]) # true

    

    # choice = int(input("Enter Selection\n"))
    # choice = 1




if __name__ == "__main__":
    main()