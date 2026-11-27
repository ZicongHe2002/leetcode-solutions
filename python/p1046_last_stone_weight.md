# 1046. Last Stone Weight · Python

[原题](https://leetcode.com/problems/last-stone-weight/)。

规则强制每次碰撞最重两块，负数最小堆能直接取出它们。等重不放回，异重只放回正差的负数表示，继续直到至多一块。堆中始终恰是当前未消失石头的重量，不把原数组每次重新排序，也不改变原stones。

时间O(n log n)，堆空间O(n)，无剩余石头返回0。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
