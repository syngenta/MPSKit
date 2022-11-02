import pymps


def test_version():
    version = pymps.__version__
    print(version)
    assert version is not None


if __name__ == '__main__':
    test_version()
