class Solution:
    def killProcess(self, pid, ppid, kill):
        children = {}
        for process, parent in zip(pid, ppid):
            children.setdefault(parent, []).append(process)
        pending = [kill]
        killed = []
        while pending:
            process = pending.pop()
            killed.append(process)
            pending.extend(children.get(process, ()))
        return killed
