# 953. Verifying an Alien Dictionary · Python

[原题](https://leetcode.com/problems/verifying-an-alien-dictionary/)。

建立自定义字符排名，字典序由首个不同字符决定；比较出顺序后不再看后面字符。若公共长度内全相同，则较短词必须在前，防止长词排在其前缀之前。全部相邻词有序就由字典序传递性保证整个列表有序。原始字母ASCII顺序不参与比较。

总词长度L，时间O(L+26)，排名表额外空间O(26)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
