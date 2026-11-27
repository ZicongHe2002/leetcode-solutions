# 985. Sum of Even Numbers After Queries · Python

[原题](https://leetcode.com/problems/sum-of-even-numbers-after-queries/)。

先求当前偶数和，只有被修改下标的贡献可能变化。旧值是偶数就先扣掉，执行加法后新值若为偶数再加入，覆盖偶转奇、奇转偶及奇偶不变四种情况，负值的奇偶判断同样适用。每次记录更新后的总和，不重新扫描数组。使用nums副本，调用方输入和queries保持。

N项Q次查询，时间O(N+Q)，副本与输出空间O(N+Q)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
