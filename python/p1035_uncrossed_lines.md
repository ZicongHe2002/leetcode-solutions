# 1035. Uncrossed Lines · Python

[原题](https://leetcode.com/problems/uncrossed-lines/)。

连相等值且不交叉，等价于匹配项在两数组都保持相同下标先后，所以答案为最长公共子序列。相等末项可接旧左上状态加1，不同则跳过任一边取较大。滚动时best[column]尚是上一行，best[column-1]已是当前行，用diagonal保存覆盖前旧左上值，防止读错状态。

长度N、M，时间O(NM)，额外空间O(M)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
