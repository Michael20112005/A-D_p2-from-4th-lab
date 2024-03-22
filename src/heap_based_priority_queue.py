class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class PriorityTaskQueue:
    def __init__(self):
        self.task_heap = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.task_heap.append(task)
        self._reorder_up(len(self.task_heap) - 1)

    def get_highest_priority_task(self):
        if not self.task_heap:
            return None

        highest_priority_task = self.task_heap[0]
        self.task_heap[0] = self.task_heap[-1]
        self.task_heap.pop()
        self._reorder_down(0)

        return highest_priority_task.description

    def peek_highest_priority_task(self):
        if self.task_heap:
            return self.task_heap[0].description
        return None

    def _reorder_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.task_heap[index].priority > self.task_heap[parent_index].priority:
            self.task_heap[index], self.task_heap[parent_index] = self.task_heap[parent_index], self.task_heap[index]
            self._reorder_up(parent_index)

    def _reorder_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.task_heap) and self.task_heap[left_child_index].priority > self.task_heap[index].priority:
            largest = left_child_index
        if right_child_index < len(self.task_heap) and self.task_heap[right_child_index].priority > self.task_heap[largest].priority:
            largest = right_child_index

        if largest != index:
            self.task_heap[index], self.task_heap[largest] = self.task_heap[largest], self.task_heap[index]
            self._reorder_down(largest)

# Usage example
task_queue = PriorityTaskQueue()
task_queue.add_task('to tear out a mannequin_s caddy', 56)
task_queue.add_task('sink a toy boat', 666)
task_queue.add_task('throw an apple', 4)


print(task_queue.get_highest_priority_task())
print(task_queue.get_highest_priority_task())
print(task_queue.get_highest_priority_task())