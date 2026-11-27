# 970. Powerful Integers · Python

[原题](https://leetcode.com/problems/powerful-integers/)。

指数允许0，所以两边都从幂值1开始。基数大于1时逐次乘基数直到超过界；基数1的所有指数同为1，只生成一次。枚举两个幂表的所有和，保留不超过bound的值并用集合去重，多个指数表示同一整数也只输出一次。bound小于2时自然没有可行和。

幂表长度P、Q，时间O(P+Q+PQ)，额外空间O(P+Q+PQ)，输出顺序任意。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
