# 1013. Partition Array Into Three Parts With Equal Sum · Python

[原题](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/)。

三段同和要求总和能被3整除。扫描累计到目标和就结束一段并清零；最早两个目标段若在最后一个元素前结束，剩下非空后缀的和必是同一目标，不需另搜第三段。负数不影响该前缀等式，目标为0时也必须实际消费元素形成两段并留下非空后缀，不能接受空段。

时间O(n)，额外空间O(1)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
