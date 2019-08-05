import pyfindtext
import os

test_dir = os.path.abspath('pyfindtext/tests/test_files')


def test_functionality_1():
    x = pyfindtext.find(test_dir, 'sbrannigan')
    # expect line number to be 3
    assert x[0][1] == 3
    assert x[0][2] == 'Steve,Brannigan,sbrannigan,changeme,sbrannigan@kanab.' \
                   'org,123-456-7890,3,1,1041,Teacher,328 Innovation,Suite ' \
                   '# 200 ,state college,PA,16803\r\n'


def test_functionality_2():
    y = pyfindtext.find(test_dir, 'CIRCUMFLEX')
    # expect data returned equals expected result from file
    assert y[0][2] == '5E  CIRCUMFLEX ACCENT           ' \
                   'DE  CAPITAL LETTER THORN (Icelandic)\n'