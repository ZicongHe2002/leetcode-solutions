# 795. Number of Subarrays with Bounded Maximum · Python

[原题](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/)。

原题nums长1..100000，元素与left/right在0..10^9，left<=right。求非空连续子数组的最大值处于闭区间[left,right]的个数，题目另保证最终答案能放入32位整数。输入保持，Python返回int。

固定右端index，last_too_large记录最近一个>right的位置，last_in_range记录最近一个落在[left,right]的位置。合法左端必须在last_too_large之后，排除所有过大元素；还必须不晚于last_in_range，保证至少包含一个>=left的元素。故本右端恰有max(0,last_in_range-last_too_large)个合法子数组，逐右端相加不会重复。遇到过大元素不必重置另一个下标，非正差自动使贡献为0；小于left的元素可延长已有合法区间，却不能独自创造合法最大值。

每项更新两个下标，时间O(n)，额外空间O(1)。闭区间等号、left=0以及两下标初始-1都自然包含，不做left-1算术或存全部区间。

独立oracle枚举每个非空切片，直接求max再检查闭区间。值0..3、长度1..6共5460个数组，各核对10种有序界限，共54600查询。另测官方例、长度100000的隔断数组、10^9、单点与65535个同值产生2147450880答案；没有把答案超过题目32位保证的100000同值全合法情况伪装为合法测试。核对int与输入保持，未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
