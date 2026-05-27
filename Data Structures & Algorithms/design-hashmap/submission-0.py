class MyHashMap:

    def __init__(self):
        self.mapping = {}

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.mapping[key] = (value)
        else:
            self.mapping[key] = value

    def get(self, key: int) -> int:
        if key in self.mapping:
            return self.mapping[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.mapping:
            del self.mapping[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)