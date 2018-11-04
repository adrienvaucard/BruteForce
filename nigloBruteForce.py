#Niglo BruteForce
import functions
import characters

# #Create a fake password to test script

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





#Start real BruteForce script

print("Enter minChars and maxChars of Passwords")
print("Min Chars: ")
minChars = int(input())
print("Max Chars: ")
maxChars = int(input())

checkPassword = ""

#Create string with minimal length
while len(checkPassword) < minChars:
    checkPassword += "A"


#Increment string length by one until max Chars
while len(checkPassword) < maxChars+1:
    length = 0
    while length < len(checkPassword):
        for char in characters.matchChars:
            tempCheckPassword = checkPassword[0:len(checkPassword)-length]
            tempCheckPassword += str(char)
            print(tempCheckPassword)

        length+= 1
    checkPassword += "A"

