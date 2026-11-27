# 1207. Unique Number of Occurrences · Python

[原题](https://leetcode.com/problems/unique-number-of-occurrences/)。

先按数值计数，再把频次放入集合。若两种数值频次相同，频次集合会比键集合小；两者大小相等当且仅当所有出现次数互异。负数值与正数值使用同样的计数逻辑，不能误检查原数组数值是否重复。

期望时间O(n)，额外空间O(D)，D为不同输入值数，不修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
