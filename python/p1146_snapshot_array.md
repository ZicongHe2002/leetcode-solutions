# 1146. Snapshot Array · Python

[原题](https://leetcode.com/problems/snapshot-array/)。

接口为SnapshotArray，不使用Solution。所有元素初值0，以(-1,0)作历史哨兵。set记录在下一个快照编号下，同一快照内重复set只保留最后值；snap只推进编号，无需复制整个数组。get对指定下标的有序历史二分，取编号不大于snap_id的最后记录，未发生新set的快照自然继承旧值。题目保证查询已产生的快照及合法下标。

初始化O(length)，set和snap均O(1)，get为O(log h)，h为该下标记录数；总额外空间O(length+S)，S为实际保留的set记录数。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
