# password-generator

This is a simple password generater written in Python and served via FastAPI.

# Usage:

### Docker Build:

1. CD into the root directory of the project
2. Build the image: `docker build -t pwdgen .`
3. Run the container: `docker run --name pwdgen -p 8000:8000 pwdgen`
4. Navigate to `http://127.0.0.1:8000` to view the swagger UI. You can replace `127.0.0.1` with `localhost` if you like.

This assumes you want to use port 8000 to access the application.

### Docker Hub:

1. Run `docker run --name pwdgen -p 8000:8000 darianhuotari/password-generator:latest`

Todo:

Add container to registry 

Add instructions for deploying in k3s

Add test coverage
