class Solution:
    def calPoints(self, operations: List[str]) -> int:
        newlist = []
        record = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                newlist.append(int(newlist[len(newlist)-1]) + newlist[len(newlist)-2])
            elif operations[i] == "D":
                newlist.append(int(newlist[len(newlist)-1]) * 2)
            elif operations[i] == "C":
                newlist.pop()
            else:
                newlist.append(int(operations[i]))
        for n in newlist:
            record += n
        
        return record