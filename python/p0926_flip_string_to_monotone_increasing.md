# 926. Flip String to Monotone Increasing · Python

[原题](https://leetcode.com/problems/flip-string-to-monotone-increasing/)。

目标形式为若干0后接若干1。已见1时可直接保留，最优成本不增加；遇到0，可以把当前0翻为1并沿用此前最优成本，也可以把此前所有原始1都翻为0，使整个前缀全0，成本为ones。两者取小。ones始终记录原串前缀1数，不因某个候选翻转路径改变，flips概括该前缀全部可行分界的最优值。

时间O(n)，额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
