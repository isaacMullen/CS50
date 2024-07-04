from twttr import shorten

def test_argument():
    assert shorten("aeiouggg") == "ggg"