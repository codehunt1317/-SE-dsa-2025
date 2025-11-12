class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return key % self.size

    def insert(self, roll, name):
        h = self._hash(roll)
        while self.table[h] and self.table[h][0] != roll:
            h = (h + 1) % self.size
        self.table[h] = (roll, name)

    def search(self, roll):
        h = self._hash(roll)
        for _ in range(self.size):
            if not self.table[h]:
                return None
            if self.table[h][0] == roll:
                return self.table[h][1]
            h = (h + 1) % self.size
        return None

    def delete(self, roll):
        h = self._hash(roll)
        for _ in range(self.size):
            if not self.table[h]:
                print("Record not found"); return
            if self.table[h][0] == roll:
                self.table[h] = None
                print("Record deleted"); return
            h = (h + 1) % self.size

    def display(self):
        print("\nStudent Records (Hash Table):")
        for i, v in enumerate(self.table):
            print(i, ":", v)

# -------- MAIN PROGRAM --------
h = HashTable()
h.insert(101, "riya")
h.insert(112, "Rahul")
h.insert(105, "Sneha")

h.display()
print("\nSearch Roll 105:", h.search(105))
h.delete(112)
h.display()