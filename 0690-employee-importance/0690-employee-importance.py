"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = [0]
        
        emp_list = {emp.id: emp for emp in employees}
        
        def dfs(importance, eid):
            importance[0] += emp_list[eid].importance
            
            for subordinate in emp_list[eid].subordinates:
                dfs(importance, subordinate)
        
        dfs(importance, id)
        return importance[0]