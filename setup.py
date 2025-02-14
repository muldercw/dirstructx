from setuptools import setup, find_packages

setup(
    name="dirstructx",
    version="0.1.0",
    author="Chris Mulder",
    author_email="muldercw@gmail.com",
    description="A tool to generate structured representations of directories",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/muldercw/dirstructx",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "dirstructx=dirstructx.__main__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)