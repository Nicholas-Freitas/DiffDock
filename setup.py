from setuptools import setup, find_packages

# Load the README.md for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="diffdock",
    version="0.1.0",
    author="Gabriele Corso",
    author_email="gcorso@mit.edu",
    description="DiffDock: Diffusion Steps, Twists, and Turns for Molecular Docking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gcorso/DiffDock",
    packages=find_packages(exclude=["tests", "scripts"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
