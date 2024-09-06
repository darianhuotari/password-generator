from PasswordGenerator import pwdgen
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/password", summary="Generate a random password", tags=['Password Generator'])
async def read_item(pass_length: Optional[int] = "20"):
    """
    Parameters:<br>
    - pass_length: (int) Length of password to be generated.

    Returns:<br>
    - randomly generated password

    """
    if pass_length is None:
        return ("This should not happen")
    if pass_length == 0:
        return ("Password length cannot be 0")
    elif pass_length < 0:
        return ("Password length cannot be negative")
    elif pass_length < 12:
        return("Minimum password length is 12. Please try again.")

    pwd = pwdgen.generate_password(pwdLength=pass_length)
    response = {"generated_password": pwd}
    return (response)

    ## TODO - add a UI or redirect to swagger from root