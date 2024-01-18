from enum import IntEnum, unique


@unique
class shortcut_key_modifier(IntEnum):
    """shortcut key modifier

    Examples:
        >>> cadwork.shortcut_key_modifier.no_modifier
        no_modifier

    Args:
        ctrl = 2
        shift = 1
        alt = 3

    """
    ctrl = 2
    shift = 1
    alt = 3

    def __int__(self) -> int:
        return self.value
