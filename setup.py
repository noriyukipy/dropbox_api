import setuptools


setuptools.setup(
    name="dropbox_api",
    packages=setuptools.find_packages(),
    install_requires=[
        "dropbox~=10.10.0",
        "fire~=0.3.0"
    ],
    version="0.1.0",
    author="Noriyuki Abe",
)
