

# hash table data structure
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # Initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

if __name__ == '__main__':
    # Main program to create a couple of HashTable objects, showing how
    # the 'capacity' constructor argument works.
    ht1 = ChainingHashTable()
    print('ht1:', ht1.table)

    ht2 = ChainingHashTable(5)
    print('ht2:', ht2.table)