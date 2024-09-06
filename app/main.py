from PasswordGenerator import pwdgen
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/password", summary="Generate a random password", tags=['Password Generator'])
async def read_item(pass_length: Optional[int] = "20",
                    pass_name: Optional[str] = "Password"):
    """
    Parameters:<br>
    - pass_length: (int) Length of password to be generated.
    - pass_name: (str) Name of password to be generated.

    Returns:<br>
    - name of randomly generated password
    - randomly generated password

    """

    generator = pwdgen.passwordGenerator
    pwd = generator.generate_password(pwdLength=pass_length, pwdName=pass_name)
    response = {"generated_password": pwd}
    return (response)

    ## TODO - add a UI or redirect to swagger from root