# 1061. Lexicographically Smallest Equivalent String · Python

[原题](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/)。

对应字母相等关系具有传递性，形成并查集等价类。把较大根接到较小根，保持每类代表是其字典序最小字母；后续合并也维持该性质。baseStr每位可独立换成所属类最小代表，逐位最小即整体字典序最小。没有关系的字母仍代表自己，路径压缩不改变代表最小值。

固定26字母下时间O(len(s1)+len(baseStr))，除输出外额外空间O(26)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
