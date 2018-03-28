# content of test_sample.py

import utils.version as version

def inc(x):
    return x + 1

def test_answer():
    assert inc(4) == 5

def test_version():
    assert version.__version__=="0.0.1"