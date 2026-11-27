# 911. Online Election · Python

[原题](https://leetcode.com/problems/online-election/)。

按严格递增投票时间处理，每票更新对应人数；新计数达到当前最大值就把本次投票者设为领先者，等号实现平票时最近投票优先。保存每次事件后的领先者。查询t用bisect_right找最后一个不晚于t的事件下标，所以恰好等于投票时刻时该票已计入。题目保证查询不早于首次投票。

初始化O(n)，每次查询O(log n)，额外空间O(n)，输入数组保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
