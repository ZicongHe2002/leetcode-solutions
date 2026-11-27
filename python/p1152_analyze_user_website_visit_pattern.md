# 1152. Analyze User Website Visit Pattern · Python

[原题](https://leetcode.com/problems/analyze-user-website-visit-pattern/)。

三站模式要求同一用户按严格时间顺序访问，不要求访问连续，也允许站点名称重复。题目时间戳互异，先对全部访问按时间排序，再为每个用户枚举下标递增的三元组合。同一用户多次出现同一模式只计1分，因此先对该用户的模式集合去重。最终优先选覆盖用户数最多的模式，平局取站点三元组字典序最小者，题目保证至少一个用户有三次访问。

记录n条、用户u有m_u次访问，时间O(n log n+sum(m_u^3))，空间O(n+P+max(m_u^3))，P为不同模式数，输入列表保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
