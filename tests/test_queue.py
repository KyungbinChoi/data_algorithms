# tests/test_queue.py
import pytest
from data_structure.queue import TwoStackQueue

def test_interleaved_ops():
    q = TwoStackQueue[int]()
    q.enqueue(1); q.enqueue(2)
    assert q.dequeue() == 1
    q.enqueue(3)
    assert q.peek() == 2
    assert [q.dequeue(), q.dequeue()] == [2, 3]
    assert q.is_empty()

@pytest.mark.parametrize("values", [[10], [10,20,30]])
def test_order(values):
    q = TwoStackQueue[int]()
    for v in values: q.enqueue(v)
    for v in values: assert q.dequeue() == v
