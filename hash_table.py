"""A simple hash table implementation in Python."""
class HashTable:
    """Class representing a hash table data structure."""
    def __init__(self):
        self.collection = {}

    # 3, 4, 5
    def hash(self, key):
        """Return the sum of Unicode values of each character in the string."""
        return sum(ord(char) for char in key)

    # 6, 7
    def add(self, key, value):
        """Add a key-value pair to the hash table."""
        hashed = self.hash(key)

        if hashed not in self.collection:
            self.collection[hashed] = {}

        self.collection[hashed][key] = value

    # 8, 9, 10, 11, 17
    def remove(self, key):
        """Remove a key-value pair if it exists; do nothing otherwise."""
        hashed = self.hash(key)

        if hashed in self.collection and key in self.collection[hashed]:
            del self.collection[hashed][key]

            # Optional: if bucket becomes empty, you can either keep or delete it.
            if not self.collection[hashed]:
                del self.collection[hashed]

    # 12, 13, 18, 19
    def lookup(self, key):
        """Return the value for the given key, or None if not found."""
        hashed = self.hash(key)

        if hashed in self.collection and key in self.collection[hashed]:
            return self.collection[hashed][key]

        return None


my_hash_table = HashTable()
print(my_hash_table.hash('golf'))
print(my_hash_table.add('golf', 'sport'))
print(my_hash_table.add('dear', 'friend'))
print(my_hash_table.add('read', 'book'))
print(my_hash_table.lookup('golf'))
print(my_hash_table.add('rose', 'flower'))
print(my_hash_table.collection)
