class Solution:
    x = 121
    def isPalindrome(x: int) -> bool:
        int_string = str(x)
        int_string.split()
        
        single_char = []

        print(int_string)

        for char in range(len(int_string)):
            print(char)
            single_char.append(int_string[char])

        print(single_char)
        single_char_rev = [single_char.reverse()]

        for i in range(len(single_char)):
            if single_char[i] == single_char_rev[i]:
                print("True")
                print(single_char, single_char_rev)
                
                return True
            else:
                print("False")
                print(single_char, single_char_rev)
                return False
    
    isPalindrome(x)

