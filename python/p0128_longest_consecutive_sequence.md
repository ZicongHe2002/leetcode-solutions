# 128. Longest Consecutive Sequence · Python

[原题](https://leetcode.com/problems/longest-consecutive-sequence/)。

输入长度0..100000，整数在[-10^9,10^9]；求不同连续整数段的最大长度，而非原数组连续子段长度。先去重，仅在start-1不存在时扫描该段。每个非空连续段有唯一最小值；段内其他值均跳过，因此每个不同值只参与一次段扫描。空集合best=0，重复项不延长段。

集合操作取平均常数时间，总时间O(n)，额外空间O(n)。Python整数的start-1和start+length不会发生固定宽度溢出。测试oracle先排序，再扫描去重后的相邻差，未使用生产段首集合遍历；五值集合上长度0..6全部19531个数组。边界含100000项连续段、100000个重复值和两个相隔很远的值域端点。原列表保持。

A使用OpenAI Codex辅助编写；实际验证结果见PR，未向LeetCode提交。B只有实际补写内容后才记录共同署名，正式review与创作分别记录。
