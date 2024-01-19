# Electron Fuses

Python-implementation of Electron's [fuses module](https://github.com/electron/fuses), intended for querying fuse states of an Electron binary.


## Installation

```bash
python3 -m pip install electron-fuses
```


## Usage

```py
>>> from electron_fuses import Fuses
>>> fuses = Fuses("path/to/electron")

>>> print(fuses)

   RUN_AS_NODE: DISABLE
   ENABLE_COOKIE_ENCRYPTION: DISABLE
   ENABLE_NODE_OPTIONS_ENVIRONMENT_VARIABLE: DISABLE
   ENABLE_NODE_CLI_INSPECT_ARGUMENTS: DISABLE
   ENABLE_EMBEDDED_ASAR_INTEGRITY_VALIDATION: ENABLE
   ONLY_LOAD_APP_FROM_ASAR: ENABLE
   LOAD_BROWSER_PROCESS_SPECIFIC_V8_SNAPSHOT: DISABLE

>>> from electron_fuses import FuseConfig
>>> print(fuses.config[FuseV1Options.RUN_AS_NODE])

   FuseState.DISABLE
```

If searching a macOS executable, the .app or entry point (under `Contents/MacOS`) can be provided to `electron_fuses.ResolveFramework()` to determine the path to the Electron Framework for fuse parsing:

```py
>>> from electron_fuses import ResolveFramework
>>> framework_path = ResolveFramework("1Password.app").framework_path()
>>> print(framework_path)
"1Password.app/Contents/Frameworks/Electron Framework.framework/Versions/A/Electron Framework"
```

