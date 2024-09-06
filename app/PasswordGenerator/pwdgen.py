import os
import string, secrets

class passwordGenerator:

    def __init__(self):
        pass

    @staticmethod

    def generate_password(pwdName: str, pwdLength: int):

    
        # Define a default password length # TODO - check if value is empty or string?
        defaultLength =int(20)

        if pwdLength == 0:
            return ("Password length cannot be 0")
        elif pwdLength < 0:
            return ("Password length cannot be negative")
        elif pwdLength < 12:
            return("Minimum password length is 12. Please try again.")
        
        # Build lists of candidate characters to be used in the password
        s1 = string.ascii_letters
        s2 = string.digits
        s3 = """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""" # OWASP special characters: https://owasp.org/www-community/password-special-characters

        # Create a list of characters to be used in the password
        characterList = s1 + s2 + s3

        while True:

            # Concatenate random characters from the characterList using the secrets module, up to the pwdLength
            # The password should have at least 2 uppercase, lowercase, numbers, and special characters
            password = ''.join(secrets.choice(characterList) for i in range(pwdLength))
            if (sum(char.islower() for char in password) >=2
                    and sum(char.isupper() for char in password) >=2
                    and sum(char.isdigit() for char in password) >=2
                    and sum(char.isalnum() for char in password) >=2):
                break

        print ("Successfully generated password with a length of", pwdLength, "characters!")        
        return (pwdName, password)
























#if __name__ == '__main__':
#    app.config['DEBUG'] = True
#    app.run("0.0.0.0", "5000")