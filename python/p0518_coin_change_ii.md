# 518. Coin Change II · Python

[原题](https://leetcode.com/problems/coin-change-ii/)。

原题coins含1..300个互异正面值，值在[1,5000]，amount在[0,5000]，每种硬币可使用无限次，返回无序组合数量；相同面值数量相同的一组只计一次，不把不同排列分开。原题保证答案适合32位整数。本实现额外支持空面值列表：目标0为1种空组合，正目标为0；coins顺序与内容保持。

处理一个coin之前，counts只统计此前面值组成的组合。把total从coin向上扫描，counts[total-coin]已允许使用当前coin，因此在旧组合后追加一个coin恰好覆盖使用它至少一次的组合；旧counts[total]保留不使用它的组合。每一组按当前面值的用量分解唯一，候选外循环防止不同排列重复计数。counts[0]=1是空组合。时间O(amount·len(coins))，额外空间O(amount)。

独立oracle枚举每种面值的使用次数向量，按加权和筛选，不复用硬币动态规划。从面值池1..5选非空子集、枚举输入顺序及amount=0..10，共3575次；逐次检查输入保持。边界覆盖amount=5000、300面值、不可达奇数、[1,2]目标5000的2501组独立期望，以及空列表扩展。

A使用OpenAI Codex辅助编写；实际验证见PR与日志，未向LeetCode提交。完整初稿可由B正式review后按最终head普通merge，共同补写为可选，仅按真实内容署名。
