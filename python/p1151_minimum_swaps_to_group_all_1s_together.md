# 1151. Minimum Swaps to Group All 1s Together · Python

[原题](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/)。

数组是二进制，允许交换任意两个位置。最终全部1占据一个长度为1总数k的连续窗口。窗口每个0都可与外部一个1交换，且至少需要这么多次，因此代价等于窗口内0数。滑窗找到包含最多1的长度k窗口，返回k减该数量。没有1或仅一个1时不需交换。

时间O(n)，初始化切片使用O(k)额外空间，不实际修改输入或执行交换。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
