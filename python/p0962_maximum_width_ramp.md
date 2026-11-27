# 962. Maximum Width Ramp · Python

[原题](https://leetcode.com/problems/maximum-width-ramp/)。

若某个左端值不比更早位置更小，它会被更早且值更小或相等的位置支配，因此只保留严格递减前缀最小值下标。右端从最右向左扫描，满足左值<=右值的候选第一次遇到的就是它最远可行终点，计算宽度后弹出。每个候选只入栈出栈一次，等值允许构成坡但更晚等值左端不必保留。

时间O(n)，额外空间O(n)，无正宽候选时返回0，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
