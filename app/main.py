from PasswordGenerator import pwdgen
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

# Root redirects to swagger-ui

@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')

# Generate a password
@app.get("/generate", summary="Generate a random password", tags=['Password Generator'])
async def read_item(pass_length: Optional[int] = "20"):
    """
    Parameters:<br>
    - pass_length: (int) Length of password to be generated.

    Returns:<br>
    - generated_password: (str) Password from the password-generator service.

    """
    if pass_length is None:
        return ("This should not happen") # Cast from str to int to allow for null / empty checking? Currently this does nothing.
    if pass_length == 0:
        return ("Password length cannot be 0")
    elif pass_length < 0:
        return ("Password length cannot be negative")
    elif pass_length < 12:
        return("Minimum password length is 12. Please try again.")

    pwd = pwdgen.generate_password(pwdLength=pass_length)
    response = {"generated_password": pwd}
    return (response)

# Simple health endpoint
@app.get("/health", summary="Check health status", tags=['healthcheck'])
def health_check():
    return {"status": "OK"}