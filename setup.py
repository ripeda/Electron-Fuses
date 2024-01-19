"""
setup.py: Setup script
"""

from setuptools import setup, find_packages


def fetch_property(property: str) -> str:
    """
    Fetch a property from the main Nekrosis class.

    Parameters:
        property (str): The name of the property to fetch.

    Returns:
        The value of the property.
    """
    for line in open("electron_fuses/__init__.py", "r").readlines():
        if not line.startswith(property):
            continue
        return line.split("=")[1].strip().strip('"')
    raise ValueError(f"Property {property} not found.")


setup(
    name="electron_fuses",
    version=fetch_property("__version__:"),
    description="Python-implementation of Electron's fuses module.",
    long_description_content_type="text/markdown",
    long_description=open("README.md", "r").read(),
    author=fetch_property("__author__:"),
    author_email="",
    license=fetch_property("__license__:"),
    url="",
    python_requires=">=3.6",
    packages=find_packages(include=["electron_fuses"]),
    package_data={
        "electron_fuses": ["*"],
    },
    py_modules=["electron_fuses"],
    include_package_data=True,
    install_requires=open("requirements.txt", "r").readlines(),
)