import typer
import requests

app = typer.Typer()

API_URL = "https://devvault-api-vhy3.onrender.com"


@app.command()
def login(email: str, password: str):

    response = requests.post(
        f"{API_URL}/auth/login",
        data={
            "username": email,
            "password": password
        }
    )

    if response.status_code != 200:
        print("Login failed:", response.text)
        raise typer.Exit()

    data = response.json()

    token = data.get("access_token")

    if not token:
        print("Login failed: No token received")
        raise typer.Exit()

    with open(".devvault_token", "w") as f:
        f.write(token)

    print("Login successful")


@app.command()
def pull(project_name: str):

    try:
        with open(".devvault_token") as f:
            token = f.read().strip()
    except FileNotFoundError:
        print("Please login first.")
        raise typer.Exit()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Get projects
    response = requests.get(
        f"{API_URL}/projects",
        headers=headers
    )

    if response.status_code != 200:
        print("Failed to fetch projects:", response.text)
        raise typer.Exit()

    projects = response.json()

    project_id = None

    for project in projects:
        if project["name"] == project_name:
            project_id = project["id"]
            break

    if project_id is None:
        print("Project not found")
        raise typer.Exit()

    # Fetch env secrets
    response = requests.get(
        f"{API_URL}/secrets/projects/{project_id}/env",
        headers=headers
    )

    if response.status_code != 200:
        print("Failed to fetch secrets:", response.text)
        raise typer.Exit()

    data = response.json()

    with open(".env", "w") as env_file:
        for key, value in data.items():
            env_file.write(f"{key}={value}\n")

    print(".env file generated successfully")

if __name__ == "__main__":
    app()

def main():
    app()