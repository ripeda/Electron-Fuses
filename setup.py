"""
setup.py: Setup script
"""

from setuptools import setup, find_packages


MODULE_NAME: str = "electron_fuses"


def fetch_property(property: str) -> str:
    """
    Fetch a property from the main Nekrosis class.

    Parameters:
        property (str): The name of the property to fetch.

    Returns:
        The value of the property.
    """
    for line in open(f"{MODULE_NAME}/__init__.py", "r").readlines():
        if not line.startswith(property):
            continue
        return line.split("=")[1].strip().strip('"')
    raise ValueError(f"Property {property} not found.")


setup(
    name=MODULE_NAME,
    version=fetch_property("__version__:"),
    description="Python-implementation of Electron's fuses module.",
    long_description_content_type="text/markdown",
    long_description=open("README.md", "r").read(),
    author=fetch_property("__author__:"),
    author_email=fetch_property("__author_email__:"),
    license=fetch_property("__license__:"),
    url="https://github.com/ripeda/Electron-Fuses",
    python_requires=">=3.6",
    packages=find_packages(include=[MODULE_NAME]),
    package_data={
        MODULE_NAME: ["*"],
    },
    py_modules=[MODULE_NAME],
    include_package_data=True,
)