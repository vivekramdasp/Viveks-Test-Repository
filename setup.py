# Copyright (C) 2021-2022 Archingen, PLC DBA PermitZIP.

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="UPDATE THIS",
    version="0.0.1",
    author="Archingen, PLC",
    author_email="kshultz@permitzip.com",
    short_description="UPDATE THIS.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["click", "requests", "click-help-colors"],
    include_package_data=True,
    entry_points={"console_scripts": ["UPDATE_THIS = cli.cli:UPDATE_THIS"]},
    url="UPDATE_THIS",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Office/Business",
    ],
)
