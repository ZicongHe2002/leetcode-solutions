# 923. 3Sum With Multiplicity · Python

[原题](https://leetcode.com/problems/3sum-with-multiplicity/)。

先统计值频次，只枚举first<=second<=third，third由目标和唯一确定，每种值多重集只计一次。三个值全同用C(freq,3)，恰两同用C(freq,2)乘另一频次，全不同用三频次乘积。每组被选下标按升序唯一对应i<j<k，因此无需额外乘排列数。second递增使third递减，一旦third<second可停止内层。

N个元素、U种值，时间O(N+U^2)，额外空间O(U)，输入保持，最终按10^9+7取模。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
