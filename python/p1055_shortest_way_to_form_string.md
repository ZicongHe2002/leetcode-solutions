# 1055. Shortest Way to Form String · Python

[原题](https://leetcode.com/problems/shortest-way-to-form-string/)。

每轮形成source的一个子序列，按target顺序总是使用本轮最早可用的源位置，给后面保留最多空间。二分字符出现位置表找严格大于此前位置的项；没有后继但源中存在该字符时，当前轮已无法继续，只能开启新轮从其首次出现继续。源根本无该字符则无解。只有必要时换轮，得到最少子序列数。

源长S目标长T，时间O(S+T log(S+1))，位置表空间O(S)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
