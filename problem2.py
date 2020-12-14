


#---------------------------------------------------------------------------------#
#--------------------------------function-----------------------------------------#
#---------------------------------------------------------------------------------#
def checkLength(s):

    if(len(s) < 6):
        print('Not secure: Password must contain at least 6 characters.')
        print('Hint: add ',6-len(s),' characters to the password.\n')
        return False

    if( len(s) > 20):
        print('Password must not exceed 20 characters.')
        print('Hint: consider omitting', len(s)-20,'characters.\n')
        return False

    return True

#---------------------------------------------------------------------------------#
#--------------------------------function-----------------------------------------#
#---------------------------------------------------------------------------------#
def checkCharacters(s):

    lowerCase = False
    upperCase = False
    digit     = False
    
    for i in s:
        if( ord(i) >= 97 and ord(i) <= 122 ):
            lowerCase = True

        if( ord(i) >= 65 and ord(i) <= 90 ):
            upperCase = True

        if( ord(i) >= 48 and ord(i) <= 57 ):
            digit = True

    if(not lowerCase):
        print('Not secure: Password must contain at least one lowercase character.')
        print('Hint: add at least one character from a-z.\n')
    if(not upperCase):
        print('Not secure: Password must contain at least one uppercase character.')
        print('Hint: add at least one character from A-Z.\n')
    if(not digit):
        print('Not secure: Password must contain at least one numeric character.')
        print('Hint: add at least one number from 0-9.\n')

    return lowerCase, upperCase, digit


#---------------------------------------------------------------------------------#
#--------------------------------function-----------------------------------------#
#---------------------------------------------------------------------------------#
def checkPattern(s):

    valid = True
    
    for i in range(len(s)-2):
        if(s[i] == s[i+1] and s[i] == s[i+2]):
            if( valid ):
                print('Not secure: Password must not contain three repeating characters in a row.');
            print('Hint: omit or move one of the', s[i],"'s.")
            valid = False
    return valid

#---------------------------------------------------------------------------------#
#--------------------------------function-----------------------------------------#
#---------------------------------------------------------------------------------#
def strongPasswordChecker ( s ):

    lengthValid = checkLength(s)
    lowercaseValid, uppercaseValid, digitValid = checkCharacters(s)
    repeatValid = checkPattern(s)

    if(lengthValid & lowercaseValid & uppercaseValid & digitValid & repeatValid):
        print('0')

#---------------------------------------------------------------------------------#
#----------------------------------start------------------------------------------#
#---------------------------------------------------------------------------------#

strongPasswordChecker("herrekereechetorichekhabara??")
