

# Test.assert_equals(will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]), True)
# Test.assert_equals(will_fit(["L", "L", "M"], [56, 62, 84, 90]), True)
# Test.assert_equals(will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70 , 80, 90, 200]), False)
# Test.assert_equals(will_fit(["S", "L"], [73 , 87, 95, 229]), False)
# Test.assert_equals(will_fit(["L", "L", "L", "L"], [54, 54, 200, 200, 200]), True, "54 and 54 can fit in one hold.")


def encode_morse(message,test):
    sum_message = ''
    char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'}
    for x in message.upper():
        sum_message +=char_to_dots[x] + ' '
    sum_message = sum_message[0:-1]
    # print(sum_message)
    # print(test)
    # print(len(sum_message), len(test))
    # print ('True' if (sum_message == test) else 'False')
    return sum_message

def main():
    print("hello world")
    print("morse code")



    test1  = ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
    encode_morse("EDABBIT CHALLENGE",test1)
    test1  = ".... . .-.. .--.   -- .   -.-.--"
    encode_morse("HELP ME !",test1)

    test1  = "-.-. .... .- .-.. .-.. . -. --. ."
    encode_morse("CHALLENGE",test1)

    test1  = ".----   .- .--. .--. .-.. .   .- -. -..   .....   -.-. .... . .-. .-. -.-- --..--   --...   ... .- -. -.. .-- .. -.-. .... . ... --..--   ..---   - .- -... .-.. . ... --..--   ----.   .. -. ...- .. - . -..   --. ..- -.-- ...   -.-.--   - .... .- - .----. ...   ... ---   -.-. --- --- .-.. .-.-.- .-.-.- .-.-.-"
    encode_morse("1 APPLE AND 5 CHERRY, 7 SANDWICHES, 2 TABLES, 9 INVITED GUYS ! THAT'S SO COOL...",test1)

    

    test1  = "-.. .. -..   -.-- --- ..-   --. --- -   -- -.--   -- .- .. .-..   ..--.."
    encode_morse("did you got my mail ?",test1)

    test1  = "- .-- ---   - .... .. -. --. ...   - ---   -.- -. --- .--   ---...   ..   ..-. --- .-. --. . -   - .... . --   ---... -.-."
    encode_morse("TWO THInGS TO KNOW : i FORGeT THeM :C",test1)



    
    
# Test.assert_equals(encode_morse("HELP ME !"), ".... . .-.. .--.   -- .   -.-.--", "Test 2")
# Test.assert_equals(encode_morse("CHALLENGE"), "-.-. .... .- .-.. .-.. . -. --. .", "Test 3")
# Test.assert_equals(encode_morse("1 APPLE AND 5 CHERRY, 7 SANDWICHES, 2 TABLES, 9 INVITED GUYS ! THAT'S SO COOL..."), ".----   .- .--. .--. .-.. .   .- -. -..   .....   -.-. .... . .-. .-. -.-- --..--   --...   ... .- -. -.. .-- .. -.-. .... . ... --..--   ..---   - .- -... .-.. . ... --..--   ----.   .. -. ...- .. - . -..   --. ..- -.-- ...   -.-.--   - .... .- - .----. ...   ... ---   -.-. --- --- .-.. .-.-.- .-.-.- .-.-.-", "Test 4")
# Test.assert_equals(encode_morse("did you got my mail ?"), "-.. .. -..   -.-- --- ..-   --. --- -   -- -.--   -- .- .. .-..   ..--..", "Test 5")
# Test.assert_equals(encode_morse("TWO THInGS TO KNOW : i FORGeT THeM :C"), "- .-- ---   - .... .. -. --. ...   - ---   -.- -. --- .--   ---...   ..   ..-. --- .-. --. . -   - .... . --   ---... -.-.", "Test 6")

    

    # choice = int(input("Enter Selection\n"))
    # choice = 1




if __name__ == "__main__":
    main()