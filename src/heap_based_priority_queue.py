class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityTaskQueue:
    def __init__(self):
        self.task_heap = []

    def add_task(self, task):
        self.task_heap.append(task)
        self._reorder_up(len(self.task_heap) - 1)

    def add_new_task(self, value, priority):
        self.add_task(Node(value, priority))

    def get_highest_priority_task(self):
        if not self.task_heap:
            return None

        highest_priority_task = self.task_heap[0]
        self.task_heap[0] = self.task_heap[-1]
        self.task_heap.pop()
        self._reorder_down(0)

        return highest_priority_task.value

    def peek_highest_priority_task(self):
        return self.task_heap[0].value if self.task_heap else None

    def _reorder_up(self, index):
        parent_index = (index - 1) // 2
        while (index > 0) and (self.task_heap[index].priority > self.task_heap[parent_index].priority):
            self.task_heap[index], self.task_heap[parent_index] = self.task_heap[parent_index], self.task_heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _reorder_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if left_child_index < len(self.task_heap) and \
                    self.task_heap[left_child_index].priority > self.task_heap[largest].priority:
                largest = left_child_index

            if right_child_index < len(self.task_heap) and \
                    self.task_heap[right_child_index].priority > self.task_heap[largest].priority:
                largest = right_child_index

            if largest != index:
                self.task_heap[index], self.task_heap[largest] = self.task_heap[largest], self.task_heap[index]
                index = largest
            else:
                break
