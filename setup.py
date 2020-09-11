from setuptools import setup, find_packages

VERSION = "0.0.1"

tests_require = ["unitest", "sphinx"]

requires = ["numpy", "mathplotlib", "scipy"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="",
    version=VERSION,
    url="",
    license="MIT",
    author="slashformotion",
    author_email="slashformotion@protonmail.com",
    description="",
    packages=[""],
    long_description=long_description,
    long_description_content_type="text/markdown",
    tests_require=tests_require,
    install_requires=requires,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    python_requires='>=3.6',
)