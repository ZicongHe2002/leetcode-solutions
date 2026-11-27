# 986. Interval List Intersections · Python

[原题](https://leetcode.com/problems/interval-list-intersections/)。

两表各自升序且内部不重叠。当前两闭区间的交集左端取大、右端取小，左<=右时记录，端点相接也有单点交集。右端更早的一侧不可能与另一侧更后区间相交，所以推进它；右端相同推进任一侧也不会漏掉合法交集。每步至少一个游标前进，结果天然有序，空表自然返回空结果。

长度N、M，时间O(N+M)，除输出外额外空间O(1)，不修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
