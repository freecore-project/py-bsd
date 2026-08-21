import errno
import os

from bsd import closefrom


def test_closefrom_preserves_lower_descriptors_and_closes_the_rest():
    pid = os.fork()
    if pid == 0:
        try:
            preserved_fd = os.open('/dev/null', os.O_RDONLY)
            first_closed_fd = os.open('/dev/null', os.O_RDONLY)

            closefrom(first_closed_fd)

            os.fstat(preserved_fd)
            try:
                os.fstat(first_closed_fd)
            except OSError as e:
                if e.errno != errno.EBADF:
                    os._exit(1)
            else:
                os._exit(1)
        except BaseException:
            os._exit(1)

        os._exit(0)

    _, status = os.waitpid(pid, 0)
    assert os.WIFEXITED(status)
    assert os.WEXITSTATUS(status) == 0
