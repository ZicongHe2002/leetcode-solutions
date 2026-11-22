# 1011. Capacity To Ship Packages Within D Days · Python

[原题](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)。

原题weights长1..50000，每项1..500，1<=days<=len(weights)。必须按原顺序运送全部包裹，每天的重量不超过固定容量，求能在至多days天完成的最小容量。输入保持；数组必须非空。

给定容量，按顺序让当前天尽量装满，下一件放不下才新开一天。任何合法方案在同一天结束时都不能运走比这个最长前缀更多的包裹，逐天交换可知该贪心使用的天数最少。容量增大不会让可行方案失效，因此在max(weights)..sum(weights)中二分第一个可行容量；下界能装下单件，上界一天完成。每次扫描O(n)，含上下界初始化的总时间为O(n log(sum(weights)-max(weights)+2))，额外空间O(1)。

独立oracle枚举所有恰好days组的连续分割，再取每组和的最大值并最小化，不复用贪心或二分；正重量使至多days组的最优值也能由恰好days组达到。值1/2/3、长度1..6共1092个数组，各测全部合法days，共6015次比较。边界覆盖50000个最大重量、1天、每天一件与必须有一天装两件，核对int及输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
