"""
version.py: Electron version detection
"""

import bs4
import requests
import packaging.version

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

        binary_contents = open(self._file, "rb").read()

        position = binary_contents.find(string.encode("utf-8"))
        if position == -1:
            return "N/A"

        while True:
            if chr(binary_contents[position + len(string)]) in "123456789":
                # Avoid overwriting position if found to be invalid
                version_position = position + len(string)
                version = ""

                # Checking for integers or period will cause false positives
                while binary_contents[version_position] not in [0, 32]:
                    version += chr(binary_contents[version_position])
                    version_position += 1

                version = version.strip()

                try:
                    packaging.version.parse(version)
                    return version
                except packaging.version.InvalidVersion:
                    pass

            # Search for null byte/space before continuing
            while binary_contents[position] not in [0, 32]:
                position += 1
            position = binary_contents.find(string.encode("utf-8"), position)
            if position == -1:
                return "N/A"


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

