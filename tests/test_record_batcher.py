import unittest

from src.batchr import RecordBatcher


class TestRecordBatcher(unittest.TestCase):
    def test_batcher_defaults(self):
        batcher = RecordBatcher()

        self.assertEqual(batcher.max_record_size, 1e6)
        self.assertEqual(batcher.max_batch_size, 5e6)
        self.assertEqual(batcher.max_records_per_batch, 500)

    def test_execute_creates_correct_batches(self):
        batcher = RecordBatcher(max_record_size=10, max_batch_size=20, max_records_per_batch=2)
        records = ["record1", "record2", "record3-longer-than-max-record", "record4", "record5", "record6", "record7"]

        batches = batcher.execute(records)

        # Check if records are within the specified size limit
        for batch in batches:
            for record in batch:
                record_size = len(record.encode('utf-8'))
                self.assertLessEqual(record_size, batcher.max_record_size)

        # Check if batch size is within the specified limit
        for batch in batches:
            batch_size = sum(len(record.encode('utf-8')) for record in batch)
            self.assertLessEqual(batch_size, batcher.max_batch_size)

        # Check if the number of records in a batch is within the specified limit
        for batch in batches:
            self.assertLessEqual(len(batch), batcher.max_records_per_batch)

    def test_execute_with_all_exceeding_record_limit(self):
        batcher = RecordBatcher(max_record_size=5, max_batch_size=20, max_records_per_batch=5)
        records = [f"record-longer-than-max-record-{i}" for i in range(20)]

        batches = batcher.execute(records)

        self.assertEqual(0, len(batches))


if __name__ == '__main__':
    unittest.main()
