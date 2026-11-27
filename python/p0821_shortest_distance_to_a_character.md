# 821. Shortest Distance to a Character · Python

[原题](https://leetcode.com/problems/shortest-distance-to-a-character/)。

每个位置最近的目标字符要么在左边要么在右边。正向维护最后看到的目标下标，得到左侧距离；反向维护接下来最近的目标下标，与已有距离取最小。目标位置两趟都产生0。题目保证目标字符出现，哨兵距离大于任何实际合法距离，因此在两趟完成后不会影响答案。

时间O(n)，输出数组O(n)，除输出外额外空间O(1)。输入字符串保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
