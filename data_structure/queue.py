# queue.py
from __future__ import annotations
from typing import Generic, TypeVar, Iterable, Optional, List

T = TypeVar("T")


class TwoStackQueue(Generic[T]):
    """
    두 개의 스택을 이용해 큐(FIFO)를 구현하는 클래스.

    핵심 아이디어:
    - in_stack(_in): 새로 들어오는 원소를 push
    - out_stack(_out): 나갈 원소를 pop
    - dequeue/peek 시 out_stack이 비어 있으면 in_stack에서 옮겨 채움 (_shift)
    """

    __slots__ = ("_in", "_out")

    def __init__(self, data: Optional[Iterable[T]] = None) -> None:
        self._in: List[T] = []
        self._out: List[T] = []
        if data:
            # TODO: 초기 데이터가 있다면 순서대로 enqueue
            for x in data:
                self.enqueue(x)
            pass

    def _shift(self) -> None:
        """out_stack이 비었을 때 in_stack의 모든 원소를 out_stack으로 이동"""
        # TODO:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        pass

    def enqueue(self, item: T) -> None:
        """큐의 맨 뒤에 원소 추가"""
        
        self._in.append(item)
        pass

    def dequeue(self) -> T:
        """큐의 맨 앞 원소를 제거하고 반환. 비었으면 IndexError."""
        self._shift()
        if not self._out:
            raise IndexError("dequeue from empty queue")
        return self._out.pop()
        
    def peek(self) -> T:
        """큐의 맨 앞 원소를 조회 (제거 없음). 비었으면 IndexError."""
        self._shift()
        if not self._out:
            raise IndexError("peek from empty queue")
        return self._out[-1]

    def is_empty(self) -> bool:
        """큐가 비었는지 여부."""
        return not self._in and not self._out

    def __len__(self) -> int:
        """큐의 길이"""
        return len(self._in) + len(self._out)

    def __repr__(self) -> str:
        """큐의 내용을 front->back 순으로 보기 좋게 출력"""
        logical = list(self._out)
        logical.reverse()
        logical += self._in
        return f"TwoStackQueue(front->back={logical})"