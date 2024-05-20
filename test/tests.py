from heap_based_priority_queue import PriorityTaskQueue
import unittest


class TestPriorityTaskQueue(unittest.TestCase):
    def test_good_case(self):
        task_queue = PriorityTaskQueue()
        task_queue.add_new_task('to tear out a mannequin_s caddy', 56)
        task_queue.add_new_task('sink a toy boat', 666)

        self.assertEqual(task_queue.get_highest_priority_task(), 'sink a toy boat')

    def test_bad_case(self):
        task_queue = PriorityTaskQueue()
        task_queue.add_new_task('task 1', 10)
        task_queue.add_new_task('task 2', 10)

        self.assertEqual(task_queue.get_highest_priority_task(), 'task 1')

    def test_empty_case(self):
        task_queue = PriorityTaskQueue()

        self.assertIsNone(task_queue.get_highest_priority_task())


if __name__ == '__main__':
    unittest.main()
