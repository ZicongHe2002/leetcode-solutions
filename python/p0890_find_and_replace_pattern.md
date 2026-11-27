# 890. Find and Replace Pattern · Python

[原题](https://leetcode.com/problems/find-and-replace-pattern/)。

按字符首次出现次序分配0、1、2等编号，同字符再次出现沿用原编号。两个字符串编码相同，当且仅当相同位置具有相同的相等关系，从而存在字符到字符的双射；不仅约束同一源字符不能映成两种，还约束不同源字符不能合并。编码元组长度也保证词长匹配。

总词长度L、模式长P，期望时间O(L+P)，除输出外额外空间O(P+最长词长度)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
