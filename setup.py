import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitandpipins",
    version="0.0.3",
    author="Forker",
    author_email="and.capuano@gmail.com",
    description="It's pip... with git.",
    long_description=long_description,
    url="https://github.com/arocketman/git-and-pip",
    packages=setuptools.find_packages(include=["gitandpip", "gitandpip2", "gitandpip2.*"]),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
