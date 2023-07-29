import time


class Search:
    def __init__(self, l, target):
        self.l = l
        self.target = target
    
    def linear_search(self):
        for index, value in enumerate(self.l):
            if value == self.target:
                return index
        
        return -1
    
    def binary_search(self):
        start, end = 0, len(self.l) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if self.l[mid] == self.target:
                return mid
            elif self.l[mid] < self.target:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1


if __name__ == '__main__':
    s = Search(list(range(10000000)), 10000001)
    start_time = time.time()
    
    print(s.linear_search())
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print("Execution time:", execution_time, "seconds")
    
    start_time = time.time()
    
    print(s.binary_search())
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print("Execution time:", execution_time, "seconds")