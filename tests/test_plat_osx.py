import os
import sys
from getpass import getuser
from os import path as op
from shutil import rmtree
from tempfile import NamedTemporaryFile
from tempfile import mkdtemp

import pytest

from send2trash import send2trash as s2t


def clean_from_trash(name):
    cwd = os.getcwd()
    os.chdir('/Users/{}/.Trash/'.format(getuser()))
    if op.isfile(name):
        remove = os.remove
    else:
        remove = rmtree
    remove(name)
    os.chdir(cwd)


@pytest.fixture
def temp_file_path():
    with NamedTemporaryFile('w+', delete=False) as f:
        assert os.path.exists(f.name)
        yield f.name

        clean_from_trash(os.path.basename(f.name))


@pytest.fixture
def temp_dir_path():
    d = mkdtemp()
    assert op.exists(d)
    yield d
    clean_from_trash(os.path.basename(d))


@pytest.mark.skipif(sys.platform != 'darwin', reason='Not OSX')
def test_trash_file(temp_file_path):
    s2t(temp_file_path)
    assert not op.exists(temp_file_path)


@pytest.mark.skipif(sys.platform != 'darwin', reason='Not OSX')
def test_trash_folder(temp_dir_path):
    s2t(temp_dir_path)
    assert not op.exists(temp_dir_path)


@pytest.mark.skipif(sys.platform != 'darwin', reason='Not OSX')
def test_trash_file_put_back(self):
    pass


@pytest.mark.skipif(sys.platform != 'darwin', reason='Not OSX')
def test_file_located_in_trash(self):
    pass
