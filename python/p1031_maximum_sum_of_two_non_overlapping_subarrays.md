# 1031. Maximum Sum of Two Non-Overlapping Subarrays · Python

[原题](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/)。

两个窗口要么firstLen在左，要么secondLen在左，两种都计算。固定右窗口的右开端，split是其左端；用前缀和更新所有结束于split或更早的最佳左窗口，再与当前右窗口相加。左窗口可更早结束，允许两窗口有空隙，但永不相交。原题值非负，初始最佳0合法，长度和不超过数组长。

时间O(n)，前缀和空间O(n)，两趟扫描额外状态O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
