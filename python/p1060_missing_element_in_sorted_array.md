# 1060. Missing Element in Sorted Array · Python

[原题](https://leetcode.com/problems/missing-element-in-sorted-array/)。

缺失从首元素开始算，不是从1开始。到nums[i]之间本应有nums[i]-nums[0]+1个整数，实际i+1个，所以缺失数为nums[i]-nums[0]-i，随i单调。二分首个缺失数至少k的下标left；目标之前共有left个原有元素且k个缺失数，因此值为nums[0]+k+left-1。若所有数组内缺失数仍不足，left等于长度，同一公式自然延伸到末尾之后。

时间O(log n)，额外空间O(1)，输入保证严格递增且不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
