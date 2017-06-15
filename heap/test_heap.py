import pytest
from heap import *

class TestMaxHeap:

    def test_trickle_down(self):
        maxheap = MaxHeap([3,5,6,1,4,2])
        maxheap._trickle_down(0)
        assert(maxheap.data == [6,5,3,1,4,2])

    def test_bubble_up(self):
        maxheap = MaxHeap([6,5,3,1,12,2])
        maxheap._bubble_up(4)
        assert(maxheap.data == [12,6,3,1,5,2])

    def test_is_max_heap(self):
        maxheap = MaxHeap([6,5,3,1,12,2])
        assert(not is_max_heap(maxheap))
        maxheap = MaxHeap([12,6,3,1,5,2])
        assert(is_max_heap(maxheap))
        maxheap = MaxHeap([1,1,1,1,1,1])
        assert(is_max_heap(maxheap))
        maxheap = MaxHeap([0,1,1,1,1,1])
        assert(not is_max_heap(maxheap))
        maxheap = MaxHeap([2,2,1,2,2,1,1])
        assert(is_max_heap(maxheap))

    def test_remove_max(self):
        maxheap = MaxHeap([12,6,3,1,5,2])
        maxheap.remove_max()
        assert(maxheap == [6,5,3,1,2])

    def test_build_max_heap(self):
        assert(is_max_heap(build_max_heap([1,2,3,9,8,7,6,5])))
