# def get_hash(key):
#     h=0
#     for char in key:
#         h+=ord(char)
#     return h%100

# print(get_hash('march 22'))

class HashTable:
    def __init__(self):
        self.Max=100
        self.arr=[None for x in range(self.Max)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.Max

    def __setitem__(self,key,value):
        n=self.get_hash(key)
        self.arr[n]=value

    def __getitem__(self,key):
        k=self.get_hash(key)
        return self.arr[k]
    
    def __delitem__(self,key):
        d=self.get_hash(key)
        self.arr[d]=None

    # def add(self,key,value):
    #     n=self.get_hash(key)
    #     self.arr[n]=value

    # def get(self,key):
    #     k=self.get_hash(key)
    #     return self.arr[k]

hash=HashTable()
# print(hash.get_hash('march 6'))
# hash.add('march 7',9)
# hash.add('march 6',130)
# print(hash.get('march 6'))

hash['march 6']=9
hash['march6']=120

print(hash['march6'])

print (hash.arr)
print("\n")
del hash['march 6']


print(hash.arr)