from setuptools import setup, find_packages

setup(
    name="zimpy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "stringi",  # if you’re using stringi via rpy2, otherwise remove
    ],
    author="Chris Zimmer",
    author_email="zimmejoc@gmail.com",
    description="Teaching-friendly data cleaning helpers (ventclean + datewizard)",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/doctorzimmy/zimpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
