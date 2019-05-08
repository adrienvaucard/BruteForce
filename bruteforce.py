#Niglo BruteForce
import functions
import characters
import time

#Create a fake password to test script

# print("Password to crack")
# password = input()
# print("Your password is " + password)


# #Ask which hash algorithm you want to use
# print("What Hash function Do you want to use ?")
# print("MD5 ?")
# print("SHA256 ?")
# hashChoice = input()


# #Test to know which hash apply to password
# if hashChoice == "MD5":
#     hashedPassword = functions.getMD5Hash(password)
# elif hashChoice == "SHA256":
#     hashedPassword = functions.getSHA256Hash(password)
# else:  
#     print('Error, please enter a correct hash algorithm')
#     exit

# print("Your hashed password is" + hashedPassword)


hashpassw = functions.getMD5Hash('azer')


#Start real BruteForce script

print("Enter minChars and maxChars of Passwords")
print("Min Chars: ")
minChars = int(input())

checkPassword = ""

#Create string with minimal length
while len(checkPassword) < minChars:
    checkPassword += characters.matchChars[0]

isCracked = False

#Main Function
def bruteloop(checkString, level):

    #Define isCracked as Global to use it in function
    global isCracked

    #Loop until cracked
    for i in range(len(characters.matchChars)):
        if not isCracked:
            #Convert String to List to manipulate it
            checkString = list(checkString)
            checkString[level] = characters.matchChars[i]
            checkString = "".join(checkString)

            #Hash test
            if functions.getMD5Hash(checkString) == hashpassw:
                print('Password = ' + checkString)
                isCracked = not isCracked
            else:
                print(checkString)

            #Recursivity of function
            if level < (len(checkString) - 1):
                bruteloop(checkString, level + 1)

        

if __name__ == "__main__": 
      
    print("First Test") 
    bruteloop(checkPassword, 0)