# 1015. Smallest Integer Divisible by K · Python

[原题](https://leetcode.com/problems/smallest-integer-divisible-by-k/)。

末位恒为1，k含2或5因子就无解。其余情况下只维护当前全1数除k的余数，追加1后变为(10*r+1)%k，第一次0的长度最小。若前k个长度都不为0，非零余数必有重复，两全1数之差是较短全1数乘10的幂；k与10互质意味着该较短全1数已应整除k，矛盾，因此至多k步足够。

时间O(k)，额外空间O(1)，不分配长度不断增长的大整数。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
