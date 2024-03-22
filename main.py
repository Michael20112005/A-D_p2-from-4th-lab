import unittest
from taskq import Queue

class TestPriorityTaskQueue(unittest.TestCase):

    def test_get_highest_priority_task(self):
        task_queue = PriorityTaskQueue()
        task_queue.add_task('Task 1', 5)
        task_queue.add_task('Task 2', 10)
        task_queue.add_task('Task 3', 2)

        self.assertEqual(task_queue.get_highest_priority_task(), 'Task 2')

    def test_peek_highest_priority_task(self):
        task_queue = PriorityTaskQueue()
        task_queue.add_task('Task 1', 5)
        task_queue.add_task('Task 2', 10)
        task_queue.add_task('Task 3', 2)

        self.assertEqual(task_queue.peek_highest_priority_task(), 'Task 2')

    def test_get_highest_priority_task_empty_queue(self):
        task_queue = PriorityTaskQueue()

        self.assertIsNone(task_queue.get_highest_priority_task())

if __name__ == '__main__':
    unittest.main()