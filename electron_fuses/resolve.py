"""
resolve.py: Resolve Electron framework from executable

Primarily intended for macOS where applications' entry point is separate from Electron framework
"""


from pathlib import Path


class ResolveFramework:

    def __init__(self, executable: str) -> None:
        self._executable = Path(executable)


    def _resolve_app(self) -> str:
        """
        Resolve the Electron framework from the application
        """

        path = self._executable / "Contents" / "Frameworks" / "Electron Framework.framework" / "Electron Framework"
        if path.exists():
            return str(path.resolve())

        # Certain embedded apps, for example 'Helper' apps will reference Electron in the same directory
        path = self._executable.parent / "Electron Framework.framework" / "Electron Framework"
        if path.exists():
            return str(path.resolve())

        raise FileNotFoundError("Could not find Electron framework")


    def _resolve_executable(self) -> str:
        """
        Resolve the Electron framework from the executable
        """
        # Check if ELF binary, if so the framework is embedded
        if self._executable.read_bytes()[1:4] == b"ELF":
            return str(self._executable)

        path = self._executable.parent.parent / "Frameworks" / "Electron Framework.framework" / "Electron Framework"
        if path.exists():
            return str(path.resolve())

        raise FileNotFoundError("Could not find Electron framework")


    @property
    def framework(self) -> str:
        """
        Resolve the Electron framework from the executable
        """
        if self._executable.suffix == ".exe":
            return self._executable

        if self._executable.suffix == ".app" and self._executable.is_dir():
            return self._resolve_app()

        return self._resolve_executable()