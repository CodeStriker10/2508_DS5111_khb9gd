"""Smoke tests to verify pytest, Python version, OS, and module imports."""

import sys
import os
import platform

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import bin.normalize as nm 


def test_of_pytest():
    """Ensure pytest is running and this test always passes."""
    assert True


def test_python_version():
    """Check that Python version is either 3.12 or 3.13."""
    assert sys.version_info[:2] in [(3, 12), (3, 13)]


def test_os():
    """Check that the operating system is Linux (posix)."""
    assert os.name == "posix"
    assert platform.system().lower() == "linux"


def test_import_module():
    """Verify that normalize_yahoo and normalize_wsj exist in bin.normalize."""
    assert hasattr(nm, "normalize_yahoo")
    assert hasattr(nm, "normalize_wsj")


