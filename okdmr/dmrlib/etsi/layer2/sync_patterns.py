import enum


@enum.unique
class SyncPattern(enum.Enum):
    BsSourcedVoice = 0x755FD7DF75F7
    BsSourcedData = 0xDFF57D75DF5D
    MsSourcedVoice = 0x7F7D5DD57DFD
    MsSourcedData = 0xD5D7F77FD757
    MsSourcedRcSync = 0x77D55F7DFD77
    Tdma1Voice = 0x5D577F7757FF
    Tdma1Data = 0xF7FDD5DDFD55
    Tdma2Voice = 0x7DFFD5F55D5F
    Tdma2Data = 0xD7557F5FF7F5
    Reserved = 0xDD7FF5D757DD
    EmbeddedSignalling = -1

    @staticmethod
    def resolve_bytes(payload: bytes):
        assert (
            len(payload) == 6
        ), "SYNC or embedded signalling must be 6 bytes (48 bits)"
        return SyncPattern(int.from_bytes(payload, byteorder="big"))

    @classmethod
    def _missing_(cls, value):
        return SyncPattern.EmbeddedSignalling
