# 1109. Corporate Flight Bookings · Python

[原题](https://leetcode.com/problems/corporate-flight-bookings/)。

输入航班编号从1开始，预订包含闭区间[first,last]。转换到0起始下标后，在first-1处增加座位，在last处撤销，使前缀和恰好覆盖原区间。差分数组多保留一个元素，因此last=n的撤销也能直接写入，输出时只遍历前n项。重叠预订通过加法叠加，无预订航班自然为0。

预订m项、航班n个，时间O(m+n)，额外空间O(n)，输入预订列表不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
