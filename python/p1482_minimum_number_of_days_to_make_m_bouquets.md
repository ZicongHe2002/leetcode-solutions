# 1482. Minimum Number of Days to Make m Bouquets · Python

[原题](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)。

原题bloomDay长1..100000，每项1..10^9；需要m个花束，每束取连续k朵已开放且未复用的花，m在1..10^6、k在1..len(bloomDay)。求最早可完成的天数，无解为-1。输入保持，数组非空。

若m*k超过花的总数就永远不可能。否则给定日期，扫描每段已开放的连续花，累计到k就完成一束并把当前段计数清零；遇到未开的花也清零。每段长度L最多提供floor(L/k)束，贪心恰好达到这个上界。日期增大只会增加可用花，故在最小到最大开放日期之间二分第一个可行值；最大日期时全部开放，已通过数量检查所以必可行。含上下界初始化的时间为O(n log(maxDay-minDay+2))，额外空间O(1)。

独立oracle枚举日期和m个长度k区间的起点组合，逐一检查互不重叠且区间内所有花已开放，不复用连续段贪心。开放日1/2/3、长度1..6共1092个数组，覆盖全部k及m=1..floor(n/k)+1，共19464次比较。边界覆盖100000朵、10^9日、隔花未开打断相邻性与数量不足，核对int及输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
