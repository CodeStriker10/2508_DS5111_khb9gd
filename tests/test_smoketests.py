import sys
import os
sys.path.append('.')

import bin.normalize as nm


def test_of_pytest():
    assert True


def test_python_version():
    assert sys.version_info >= (3, 8)


def test_os():
    assert os.name in ["posix", "nt"]


def test_import_module():
    assert hasattr(nm, "normalize_yahoo")
    assert hasattr(nm, "normalize_wsj")
