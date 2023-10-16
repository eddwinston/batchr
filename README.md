### Description
A record batcher library that splits array of records into batches that meets specific size requirements

Defaults:

- Maximum record size is 1 MB
- Maximum batch size is 5 MB
- Maximum number of records per batch is 500

### Usage
Using batcher
```commandline
from batchr import RecordBatcher

records = [f"record{i}" for i in range(250)]

batcher = RecordBatcher()
batches = batcher.execute(records)
```



#### Running test
From the root of the project

```commandline
python3 -m unittest discover -s tests
```
