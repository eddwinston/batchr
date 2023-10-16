class RecordBatcher:
    def __init__(self, max_record_size=1e6, max_batch_size=5e6, max_records_per_batch=500):
        self.max_record_size = max_record_size
        self.max_batch_size = max_batch_size
        self.max_records_per_batch = max_records_per_batch

    def execute(self, records):
        current_batch = []
        current_batch_size = 0
        batches = []

        for record in records:
            record_size = len(record.encode('utf-8'))
            
            if record_size > self.max_record_size:
                # Discard records larger than the max_record_size
                continue

            if current_batch_size + record_size > self.max_batch_size \
                    or len(current_batch) >= self.max_records_per_batch:
                # Start a new batch if the current one exceeds size or record limit
                batches.append(current_batch)
                current_batch = []
                current_batch_size = 0

            current_batch.append(record)
            current_batch_size += record_size

        if current_batch:
            batches.append(current_batch)

        return batches
