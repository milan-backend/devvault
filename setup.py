from setuptools import setup, find_packages

setup(
    name="devvault",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "typer",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "devvault=cli.devvault_cli:app"
        ]
    },
)