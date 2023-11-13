from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt") as g:
    required = g.read().splitlines()

setup(
    name="dsss_homework_2",
    version="1.0",
    description="Homework for University. Can you solve the math quiz?",
    url="https://github.com/luca-stoehr/dsss_homework_2",
    author="Luca Stöhr",
    author_email="luca_stoehr@web.de",
    install_requires=required,
    python_requires=">=3.9",
)
