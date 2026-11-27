# 991. Broken Calculator · Python

[原题](https://leetcode.com/problems/broken-calculator/)。

正向操作是乘2或减1，反向是偶数除2或加1。目标仍比起点大时，奇数只能先加1才能利用除2，偶数直接除2优于多次加1后再除。目标已不大于起点时，正向从起点连续减1即可，所需差值直接累计。逆向避免从小数向大量过大状态搜索。

时间O(log target)，额外空间O(1)，按整数运算计。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
