class TimeMap(object):

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])


    def get(self, key, timestamp):
        values = self.store.get(key, [])
        result = ""
        left, right = 0, len(values) - 1

        # FIX 1: Change to <= so single-element lists are checked
        while left <= right: 
            mid = left + ((right - left) // 2)
            
            # FIX 2: Change to <= to include exact timestamp matches
            if values[mid][1] <= timestamp: 
                result = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        # FIX 3: Return the final tracking result
        return result