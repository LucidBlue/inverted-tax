from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open("requirements.txt") as f:
    requirements = [l.strip() for l in f]

setup(
    name="Inverted Tax Plan",
    version="0.0.1",
    description="Code for computing a realistic inverted tax plan.",
    long_description=readme,
    packages=find_packages(exclude=["data"]),
    install_requires=requirements,
    author="Brad Sheneman",
    author_email="bradsheneman@gmail.com",
    url="https://github.com/lucidblue/inverted-tax",
    license=license,
)

