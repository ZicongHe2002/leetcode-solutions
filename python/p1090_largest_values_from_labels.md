# 1090. Largest Values From Labels · Python

[原题](https://leetcode.com/problems/largest-values-from-labels/)。

输入价值非负，最多选numWanted项，每个标签最多useLimit项。按价值从大到小考察，标签额度已满的项跳过，其余加入直到总额度满。对同标签，任何低价值选择都可被未选的更高价值项替换；跨标签时优先选当前可行的最高价值也不会减少可选总数。因此降序扫描能取得最优总和。标签额度为0时所有项被跳过，numWanted为0时直接停止。

时间O(n log n)，额外空间O(n)，排序的是新建配对列表，不修改原输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
