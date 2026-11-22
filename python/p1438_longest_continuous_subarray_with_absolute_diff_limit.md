# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit · Python

[原题](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)。

原题nums长1..100000，每项1..10^9，limit在0..10^9，求任意两项绝对差都不超过limit的最长连续子数组。窗口内这一条件等价于最大值减最小值不超过limit。输入保持，实现额外定义空数组返回0。

maxima按值不增、minima按值不减保存下标，新值会从各自队尾淘汰更差且更早过期的候选。相等值保留各自下标，左端移出时只删除下标等于left的队首，避免误删仍在窗口中的重复值。队首给出真实极值；超出limit就逐步缩左端，恢复合法后更新best。limit非负保证单元素窗口合法，收缩不会越过右端。每个下标在每条队列中最多进出一次，时间O(n)，额外空间O(n)。

独立oracle枚举全部连续切片，直接计算max-min检查范围，不复用单调队列。值1/2/3、长度0..7共3280个数组，各测5个合法limit，共16400次；空数组为扩展。边界覆盖100000同值、交替极值、严格递增和两长段重复值，检查重复下标过期、limit=0与10^9，核对int及输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
