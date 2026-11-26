# 395. Longest Substring with At Least K Repeating Characters · Python

[原题](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)。

求最长连续子串，使其中每个出现的字符都至少出现k次，不存在时返回0。原题字符串只含26种小写英文字母，长度1..10000，k在1..100000；不能把子序列当子串。本实现不修改字符串，额外支持空串返回0。

先枚举窗口中目标不同字符数target=1..26。扫描右端，counts记录每个字符的次数，distinct记录正次数种类，satisfied记录次数至少为k的种类。右扩时仅在次数从k-1到k时增加satisfied；左缩时仅在从k降到k-1时减少。不同字符数超过target才移动左端，直到恢复至多target种。

distinct与satisfied都等于target时，每个出现字符都达到k，窗口合法。对于任一最优子串，选它的实际不同字符数作为target；扫描到其右端时，当前窗口左端不会越过该子串左端，因为整个子串本身没有超过target种字符。窗口若还多含左侧同种字符，只会增加频率，仍合法且长度不小于该最优子串，因此枚举覆盖全局最优。

每个target下左右端各移动至多n次，时间O(26n)，额外空间O(26)。没有递归切片或以字符串长度为键的额外缓存。k=1时整个串满足，k大于总长度时没有非空合法串，提前返回。

独立参考枚举每个起终点，对实际切片用Counter重新计数并检查全部次数，不复用生产窗口或饱和状态。a/b/c、长度0..7全部3280个字符串，对k=1..5共16400项查询对照。另测10000字符、全26字母、阈值刚好达到、稀有字母隔断与最大k；空串为扩展。未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
