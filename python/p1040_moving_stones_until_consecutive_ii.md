# 1040. Moving Stones Until Consecutive II · Python

[原题](https://leetcode.com/problems/moving-stones-until-consecutive-ii/)。

排序后最终需占据n个连续位置，滑窗统计跨度不超过n的区间内已有多少石，通常移入其余n-present块即可。特殊情况是n-1块已完全连续、另一块远在端点；直接填相邻空位会让移动石仍是端点而违法，需两步周转，不能按缺1块计一步。

最大步数取两种首次舍弃外端后剩余区间空位数的较大者，即[rightmost-second]-n+2或[secondlast-leftmost]-n+2；后续逐空位推进可达到，且不能创造更多可用间隙。本题移动后必须不再是端点，区别于1033条件。

时间O(n log n)，排序副本空间O(n)，滑窗O(1)额外状态，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
