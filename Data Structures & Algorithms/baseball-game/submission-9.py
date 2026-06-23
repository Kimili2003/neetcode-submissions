class Solution:
    def calPoints(self, operations: List[str]) -> int:
        newlist = []
        record = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                record += newlist[len(newlist)-1] + newlist[len(newlist)-2]
                newlist.append(int(newlist[len(newlist)-1]) + newlist[len(newlist)-2])
            elif operations[i] == "D":
                record += int(newlist[len(newlist)-1]) * 2
                newlist.append(int(newlist[len(newlist)-1]) * 2)
            elif operations[i] == "C":
                record -= newlist.pop()
            else:
                record += int(operations[i])
                newlist.append(int(operations[i]))
        
        return record