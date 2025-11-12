class Bucket:
    def __init__(self, depth, size):
        self.depth = depth        # local depth
        self.size = size
        self.data = {}            # key -> value

class ExtendibleHash:
    def __init__(self, bucket_size=2):
        self.global_depth = 1
        self.bucket_size = bucket_size
        self.directory = [Bucket(1, bucket_size) for _ in range(2)]

    def _index(self, key):
        return hash(key) & ((1 << self.global_depth) - 1)

    def insert(self, key, value):
        idx = self._index(key)
        bucket = self.directory[idx]

        # update if exists
        if key in bucket.data:
            bucket.data[key] = value
            return

        # simple insert if space
        if len(bucket.data) < bucket.size:
            bucket.data[key] = value
            return

        # need to split and then retry insert
        self._split_bucket(idx)
        self.insert(key, value)   # retry after split

    def _split_bucket(self, idx):
        bucket = self.directory[idx]
        # if local depth == global depth, double the directory first
        if bucket.depth == self.global_depth:
            self.directory = self.directory + self.directory[:]   # duplicate refs
            self.global_depth += 1

        # create new bucket and increase local depth of old bucket
        new_bucket = Bucket(bucket.depth + 1, bucket.size)
        bucket.depth += 1

        # redistribute existing keys between bucket and new_bucket
        items = list(bucket.data.items())
        bucket.data.clear()
        for k, v in items:
            new_idx = hash(k) & ((1 << self.global_depth) - 1)
            # check the bit at position (bucket.depth - 1)
            if (new_idx >> (bucket.depth - 1)) & 1:
                new_bucket.data[k] = v
            else:
                bucket.data[k] = v

        # update directory pointers: any directory entry that pointed to old bucket
        # should point to new_bucket if its index has 1 in that bit
        dir_len = len(self.directory)
        for i in range(dir_len):
            if self.directory[i] is bucket:
                if (i >> (bucket.depth - 1)) & 1:
                    self.directory[i] = new_bucket

    def search(self, key):
        idx = self._index(key)
        return self.directory[idx].data.get(key, None)

    def delete(self, key):
        idx = self._index(key)
        bucket = self.directory[idx]
        if key in bucket.data:
            del bucket.data[key]
            return True
        return False

    def display(self):
        print("Global depth:", self.global_depth)
        print("Directory:")
        seen = set()
        for i, b in enumerate(self.directory):
            # print bucket only once (show index -> keys)
            print(f"{i:0{self.global_depth}b}: depth={b.depth}, keys={list(b.data.keys())}")

# ---- demo ----
if __name__ == "__main__":
    ht = ExtendibleHash(bucket_size=2)
    ht.insert(5, "A")
    ht.insert(7, "B")
    ht.insert(15, "C")
    ht.insert(8, "D")
    ht.display()
    print("\nSearch(7):", ht.search(7))
    print("Delete 15 ->", "Success" if ht.delete(15) else "Not found")
    ht.display()