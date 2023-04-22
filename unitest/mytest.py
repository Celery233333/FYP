import pytest
from chord import predict_chord
from predict_multi import predict

################################ test chord.py #########################################

# non exist file
def test_chord1():
    assert predict_chord('q.csv',30) == ''

# non exist threshold
def test_chord2():
    assert predict_chord('test/test1.csv',666) == ''

# regular data in dataset
def test_chord3():
    assert predict_chord('test/test1.csv',30) == ['Gm7']

# ambiguity data in dataset
def test_chord4():
    assert predict_chord('test/test2.csv',30) == ['Bb,C7,E7,Db7']

# no data in dataset
def test_chord5():
    assert predict_chord('test/test3.csv',30) == '&'

# multiple data in dataset
def test_chord6():
    a = predict_chord('test/test4.csv',30)
    assert a[0] == 'Gm7'
    assert a[1] == 'Gm7'

# error data in dataset
def test_chord7():
    assert predict_chord('test/test5.csv',30) == ''

################################ test predict_multi.py #########################################

# regular image
def test_predict1():
    assert predict('test/test1.png','normal') == 'clef-G2 + keySignature-FM + note-F3 note-Bb3 note-D4 note-A4 '

# non exist image
def test_predict2():
    with pytest.raises(AttributeError) as excinfo:
            predict('qc.png','normal')
    assert excinfo.type == AttributeError
    assert "'NoneType' object has no attribute 'shape'" in str(excinfo.value)

# empty image
def test_predict3():
    assert predict('test/test2.png','normal') == 'clef-G2 '  

# two lines input
def test_predict4():
    assert predict('test/test3.png','normal') == 'clef-G2 + clef-G2 '  

# camera-based mode
def test_predict5():
    assert predict('test/test1.png','tough') == 'clef-G2 + keySignature-FM + note-D3 note-A3 note-D4 note-A4 '

# non exist mode
def test_predict6():
    assert predict('test/test1.png','haha') == 'clef-G2 + keySignature-FM + note-F3 note-Bb3 note-D4 note-A4 '
