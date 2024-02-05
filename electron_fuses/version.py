"""
version.py: Electron version detection
"""

import bs4
import requests

from pathlib import Path
from functools import cached_property


class ElectronVersion:

    def __init__(self, file: str) -> None:
        self._file = file


    @cached_property
    def electron_version(self) -> str:
        """
        Fetch the Electron version from the binary
        """
        return self._fetch_generic_version("Electron/")


    @cached_property
    def chromium_version(self) -> str:
        """
        Fetch the Chromium version from the binary
        """
        if Path(self._file).name in ["nwjs Framework", "node-webkit Framework"]:
            return self._nwjs_version_detection()
        return self._fetch_generic_version("Chrome/")


    def _fetch_generic_version(self, string: str) -> str:
        """
        Fetch the version from the binary
        """
        version = ""

        binary_contents = open(self._file, "rb").read()
        if string.encode("utf-8") not in binary_contents:
            return "N/A"

        # If the value is '%', then ignore and search past it
        position = binary_contents.find(string.encode("utf-8"))
        while True:
            if chr(binary_contents[position + len(string)]) in "0123456789":
                break
            # Search for null byte before continuing
            while binary_contents[position] != 0:
                position += 1
            position = binary_contents.find(string.encode("utf-8"), position)

        position += len(string)
        while binary_contents[position] != 0:
            version += chr(binary_contents[position])
            position += 1

        if version == "":
            return "N/A"

        return version.strip()


    def _nwjs_version_detection(self) -> str:
        """
        Fetch the NW.js version
        Can be resolved from path:
        - ../nwjs Framework.framework/Versions/92.0.4515.107/nwjs Framework
        """
        return Path(self._file).resolve().parent.name


    @cached_property
    def electron_release_date(self) -> str:
        """
        Fetch the release date for the Electron version
        """
        return self._electron_release_date(self.electron_version)


    def _electron_release_date(self, version: str) -> str:
        """
        Resolve the release for the given Electron version

        Parses GitHub directly to avoid API rate limits
        """
        try:
            release = requests.get(f"https://github.com/electron/electron/releases/v{version}").text
        except requests.exceptions.RequestException:
            return "N/A"

        soup = bs4.BeautifulSoup(release, "html.parser")
        for tag in soup.find_all("relative-time"):
            if "datetime" in tag.attrs:
                return tag.attrs["datetime"]
        return "N/A"

