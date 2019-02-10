from setuptools import setup
import os

exec(open("trio_typing/_version.py", encoding="utf-8").read())

LONG_DESC = open("README.rst", encoding="utf-8").read()

stub_packages = [
    "async_generator-stubs", "outcome-stubs", "trio-stubs"
]

setup(
    name="trio-typing",
    version=__version__,
    description="Static type checking support for Trio and related projects",
    url="https://github.com/oremanj/trio-typing",
    long_description=LONG_DESC,
    long_description_content_type="text/x-rst",
    author="Joshua Oreman",
    author_email="oremanj@gmail.com",
    license="MIT -or- Apache License 2.0",
    packages=[
        "async_generator-stubs",
        "outcome-stubs",
        "trio-stubs",
        "trio_typing",
    ],
    include_package_data=True,
    install_requires=[
        "trio >= 0.11.0",
        "mypy >= 0.660",
        "typing_extensions >= 3.7.2",
        "mypy_extensions >= 0.4.1",
    ],
    keywords=[
        "async", "trio", "mypy"
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: Apache Software License",
        "Framework :: Trio",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: BSD",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
    ],
)
