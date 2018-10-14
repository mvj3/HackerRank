from nose.tools import assert_equal, assert_raises

class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.store = [[] for i in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        index = self._hash_function(key)
        table = self.store[index]
        for item in table:
            if item.key == key:
                item.value = value
                return
        table.append(Item(key, value))

    def get(self, key):
        index = self._hash_function(key)
        table = self.store[index]
        for item in table:
            if item.key == key:
                return item.value
        raise KeyError(key)

    def remove(self, key):
        index = self._hash_function(key)
        table = self.store[index]
        for idx, item in enumerate(table):
            if item.key == key:
                del table[idx]
                return
        raise KeyError(key)


class TestHashMap(object):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        hash_table = HashTable(10)

        print("Test: get on an empty hash table index")
        assert_raises(KeyError, hash_table.get, 0)

        print("Test: set on an empty hash table index")
        hash_table.set(0, 'foo')
        assert_equal(hash_table.get(0), 'foo')
        hash_table.set(1, 'bar')
        assert_equal(hash_table.get(1), 'bar')

        print("Test: set on a non empty hash table index")
        hash_table.set(10, 'foo2')
        assert_equal(hash_table.get(0), 'foo')
        assert_equal(hash_table.get(10), 'foo2')

        print("Test: set on a key that already exists")
        hash_table.set(10, 'foo3')
        assert_equal(hash_table.get(0), 'foo')
        assert_equal(hash_table.get(10), 'foo3')

        print("Test: remove on a key that already exists")
        hash_table.remove(10)
        assert_equal(hash_table.get(0), 'foo')
        assert_raises(KeyError, hash_table.get, 10)

        print("Test: remove on a key that doesn't exist")
        assert_raises(KeyError, hash_table.remove, -1)

        print('Success: test_end_to_end')


def main():
    test = TestHashMap()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
