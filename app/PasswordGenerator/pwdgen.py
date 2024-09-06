import os
import string, secrets

def generate_password(pwdLength: int):


    # Define a default password length # TODO - check if value is empty or string?
    defaultLength =int(20)

    # Raise an exception if length is <= 0
    if pwdLength <= 0:
        raise ("Password length cannot be less than or equal to 0")
    
    # Build lists of candidate characters to be used in the password
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""" # OWASP special characters: https://owasp.org/www-community/password-special-characters

    # Create a list of characters to be used in the password
    characterList = s1 + s2 + s3

    while True: # We could get rid of the while loop by building a list and then randomizing it

        # Concatenate random characters from the characterList using the secrets module, up to the pwdLength
        # The password should have at least 2 uppercase, lowercase, numbers, and special characters
        password = ''.join(secrets.choice(characterList) for i in range(pwdLength))
        if (sum(char.islower() for char in password) >=2
                and sum(char.isupper() for char in password) >=2
                and sum(char.isdigit() for char in password) >=2
                and sum(char.isalnum() for char in password) >=2):
            break

    print ("Successfully generated password with a length of", pwdLength, "characters!")        
    return (password)
























#if __name__ == '__main__':
#    app.config['DEBUG'] = True
#    app.run("0.0.0.0", "5000")