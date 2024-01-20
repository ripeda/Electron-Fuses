"""
config.py: Fuse configuration
"""


from .resources import SENTINEL, FuseState, FuseV1Options, SentinelNotFound


class FuseConfig:

    def __init__(self, file: str) -> None:
        self.raw_config = self._fetch_fuse_state(file)
        self.config = self._fuse_config()


    def __repr__(self) -> str:
        value = "\n".join([f"{k.name}: {v.name}" for k, v in self.config.items()])
        return f"{value}"


    def _fetch_fuse_state(self, binary: str) -> dict:
        """
        Fetch configured fuses from electron binary
        """
        binary_contents = open(binary, "rb").read()

        fuse_wire_position = binary_contents.find(SENTINEL.encode("utf-8")) + len(SENTINEL)
        if fuse_wire_position - len(SENTINEL) == -1:
            raise SentinelNotFound("Could not find sentinel")

        fuse_wire_length = binary_contents[fuse_wire_position + 1]

        fuse_config = {}
        for i in range(fuse_wire_length):
            idx = fuse_wire_position + 2 + i
            current_state = binary_contents[idx]
            fuse_config[i] = current_state

        return fuse_config


    def _get_fuse_state(self, fuse: FuseV1Options) -> FuseState:
        """
        Get the state of a fuse
        """
        return FuseState(self.raw_config[fuse.value])


    def _fuse_config(self) -> dict:
        """
        Get the fuse configuration
        """
        return {FuseV1Options(k): FuseState(v) for k, v in self.raw_config.items()}
