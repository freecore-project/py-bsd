from bsd import MountFlags


def test_gjournal_mount_flag_matches_freebsd_abi():
    assert MountFlags.GJOURNAL.value == 0x0000000002000000
    assert MountFlags(0x0000000002000000) is MountFlags.GJOURNAL
