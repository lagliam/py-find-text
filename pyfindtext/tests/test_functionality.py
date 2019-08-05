import pyfindtext
import os

test_dir = os.path.abspath('pyfindtext/tests/test_files')


def test_functionality_1():
    x = pyfindtext.find(test_dir, 'sbrannigan')
    # expect line number to be 3
    assert x[0][1] == 3
    assert x[0][2].find('sbrannigan')


def test_functionality_2():
    y = pyfindtext.find(test_dir, 'CIRCUMFLEX')
    # expect data returned equals expected result from file
    assert y[0][2].find('CIRCUMFLEX')