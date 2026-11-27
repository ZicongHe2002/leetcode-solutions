# 1007. Minimum Domino Rotations For Equal Row · Python

[原题](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/)。

若某一行最终全为v，第一张骨牌至少一面必须有v，因此候选只需tops[0]或bottoms[0]。对每个候选，任一骨牌两面都没有它就不可行；否则顶面不等者需翻到顶、底面不等者需翻到底，分别计数取小。双面同值不需翻，两个候选都不可行返回-1，输入不修改。

固定两个候选，时间O(n)，额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
