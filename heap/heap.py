#!/usr/bin/env python3

import math

class MaxHeap:

    def __init__(self):
        self.data = []

    def set(self, data):
        for item in data:
            self.data.append(item)
            self._bubble_up(self.heap_size() - 1)

    def insert(self, item):
        self.data.append(item)
        if self.heap_size() == 1:
            return
        self._bubble_up(self.heap_size() - 1)

    def remove_max(self):
        m = self.data[0]
        self.data[0] = self.data.pop()
        self._trickle_down(0)
        return m

    def heap_size(self):
        return len(self.data)

    # Private
    def _idx_left_child(self, idx):
        lidx = 2*idx+1
        if lidx >= self.heap_size():
            return None
        return lidx

    def _idx_right_child(self, idx):
        ridx = 2*idx+2
        if ridx >= self.heap_size():
            return None
        return ridx

    def _idx_parent(self, idx):
        if idx == 0:
            return None
        return math.floor((idx-1)/2)

    def _swap_with_parent(self, idx):
        if idx == 0:
            return
        pidx = self._idx_parent(idx)
        tmp = self.data[pidx]
        self.data[pidx] = self.data[idx]
        self.data[idx] = tmp

    def _bubble_up(self, idx):
        # check if we are root
        if idx == 0:
            return

        # bubble up
        pidx = self._idx_parent(idx)
        if self.data[pidx] < self.data[idx]:
            self._swap_with_parent(idx)
            self._bubble_up(pidx)

    def _trickle_down(self, idx):
        # assume subtrees are max heaps
        lidx = self._idx_left_child(idx)
        ridx = self._idx_right_child(idx)
        largest = idx

        if lidx == None:
            # no left child, (or right) so we're done
            return

        if self.data[lidx] > self.data[idx]:
            largest = lidx
        if ridx != None and self.data[ridx] > self.data[largest]:
            largest = ridx
        if largest != idx:
            self._swap_with_parent(largest)
            self._trickle_down(largest)

def build_max_heap(data):
    maxheap = MaxHeap()
    for item in data:
        maxheap.insert(item)

def is_max_heap(heap):
    if not isinstance(heap, MaxHeap):
        print("We don't know how to test this type: {0}.".format(type(heap)))

    for idx, item in enumerate(heap.data):
        lidx = heap._idx_left_child(idx)
        if lidx != None:
            if heap.data[lidx] > heap.data[idx]:
                return False
        ridx = heap._idx_right_child(idx)
        if ridx != None:
            if heap.data[ridx] > heap.data[idx]:
                return False
    return True



