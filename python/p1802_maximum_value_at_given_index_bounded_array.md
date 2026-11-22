# 1802. Maximum Value at a Given Index in a Bounded Array · Python

[原题](https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/)。

原题1<=n<=maxSum<=10^9，0<=index<n。构造长度n的正整数数组，邻项差的绝对值至多1、总和至多maxSum，最大化index处的值。函数返回最大值而不构造数组，输入均为整数标量。

峰值为peak时，距离d的位置至少为max(1,peak-d)；按这个下界填充两侧又确实满足邻项约束，所以得到该峰值所需的最小总和。长度length的一侧先有descending=min(length,peak-1)个递减项，等差和为descending*(2*peak-descending-1)//2，其余位置补1。最小总和随peak增大而增大，在1..maxSum-n+1上二分最后一个可行峰值；上中点保证区间严格缩小。每次用整数公式O(1)，总时间O(log(maxSum-n+2))，额外空间O(1)。

独立oracle枚举所有总和不超过小预算的正整数分拆数组，直接筛选邻项差，不复用峰值两侧公式或二分。n=1..6、预算n..12、每个合法index共182次查询全部核对。大边界覆盖n=maxSum=10^9、单元素10^9预算、两元素与两侧递减后补1，核对int。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
