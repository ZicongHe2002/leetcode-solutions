# 1187. Make Array Strictly Increasing · Python

[原题](https://leetcode.com/problems/make-array-strictly-increasing/)。

arr2的元素可用于替换arr1任意位置，题目不要求消耗替换值，但最终必须严格递增。best[last]保存已处理前缀结尾为last的最少操作数。原值大于last时可零成本保留；需要替换时只考虑arr2中严格大于last的最小值，其他更大替换同样花一次却限制未来更多，不会更优。同一结尾仅保留最少操作数，每轮没有可行状态则返回-1。

arr1长n、arr2不同值m，状态数至多m+1，时间O(m log m+n(m+1)log(m+1))，额外空间O(m)，两输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
