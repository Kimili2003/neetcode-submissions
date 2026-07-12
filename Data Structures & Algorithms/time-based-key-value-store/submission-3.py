class TimeMap:

    def __init__(self):
        self.machine = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.machine:
            self.machine[key] = []
        self.machine[key].append([value,timestamp])
    

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        ansList = self.machine.get(key, [])
        print(ansList)
        seen = -1
        
        for item in ansList:
            if item[1] <= timestamp:
                if item[1] >= seen:
                    seen = item[1]
                    ans = item[0]
        

        return ans