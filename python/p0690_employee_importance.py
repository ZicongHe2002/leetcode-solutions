class Solution:
    def getImportance(self, employees, id):
        by_id = {employee.id: employee for employee in employees}
        pending = [id]
        seen = set()
        total = 0
        while pending:
            current = pending.pop()
            if current in seen:
                continue
            seen.add(current)
            employee = by_id[current]
            total += employee.importance
            pending.extend(employee.subordinates)
        return total
