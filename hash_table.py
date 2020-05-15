class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        idx = self.calculate_hash_value(string)
        self.table[idx] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        key = self.calculate_hash_value(string)
        if self.table[key] != None:
            return key
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return ord(string[0]) * 100 + ord(string[1])
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('HELLO')

# Test lookup edge case
# Should be -1
print hash_table.lookup('HELLO')

# Test store
hash_table.store('HELLO')
# Should be 8568
print hash_table.lookup('HELLO')

