"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employee_dict = {emp.id: emp for emp in employees}

        stack = [id]
        total_importance = 0
        while stack:
            emp_id = stack.pop()
            emp = employee_dict[emp_id]
            total_importance += emp.importance
            stack.extend(emp.subordinates)

        return total_importance