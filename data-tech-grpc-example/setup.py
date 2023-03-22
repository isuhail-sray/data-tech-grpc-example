import os
from typing import List
from setuptools import find_packages, setup


def read_file(file_name) -> str:
    """Read the contents of a file"""
    file_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        file_name,
    )

    try:
        with open(file_path, "r") as f:
            return f.read()
    except:
        raise RuntimeError("Error while getting the package version.")

def get_version() -> str:
    return read_file("VERSION").strip()

def get_requirements() -> List[str]:
    return read_file("requirements.txt").splitlines()

setup(
    name="data-tech-grpc-example",
    version=get_version(),
    author="Data Technology Team",
    description="This is a sample repo showing an example of a gRPC service ",
    maintainer="Data Technology Team",
    maintainer_email="data_technology@esgbook.com",
    project_urls={
        "Source Code": "https://github.com/arabesque-sray/data-tech-grpc-example"
    },
    license="ESG Book",
    python_requires=">=3.11",
    packages=find_packages(),
    install_requires=get_requirements()
)
