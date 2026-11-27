# 1186. Maximum Subarray Sum with One Deletion · Python

[原题](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/)。

允许删除至多一个元素，但结果子数组必须非空。keep表示未删除的最优后缀，deleted表示删除恰一次的最优后缀。加入新值时，已删除状态可延长，或从此前keep删除当前值而来；未删除状态则在当前单独起段或继续旧段。deleted初始为负无穷，防止全负数组通过删除唯一元素得到非法空数组0。

时间O(n)，额外空间O(1)，无需实际删除或修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
