# 918. Maximum Sum Circular Subarray · Python

[原题](https://leetcode.com/problems/maximum-sum-circular-subarray/)。

最优非空段要么不跨数组边界，用最大Kadane直接求；要么跨边界，其未选部分是普通连续段，最大环绕和为总和减最小Kadane段。全负时最小段可能是整个数组，差为0对应非法空选择，必须返回普通最大值。其他情况对两种候选取大，单元素与零值也自然覆盖。

时间O(n)，额外空间O(1)，不复制切片、不修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
