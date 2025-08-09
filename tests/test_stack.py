# tests/test_stack.py
import pytest
from data_structure.stack import Stack

@pytest.fixture
def s() -> Stack[int]:
    return Stack[int]()

def test_push_pop_basic(s):
    s.push(1); s.push(2)
    assert len(s) == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()

@pytest.mark.parametrize("seq", [[], [1], [1,2,3]])
def test_len_and_empty_invariants(seq):
    st = Stack[int]()
    for x in seq:
        st.push(x)
    assert (len(st) == 0) == st.is_empty()

def test_pop_empty_raises(s):
    with pytest.raises(IndexError):
        s.pop()
