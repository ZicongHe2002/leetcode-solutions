# 820. Short Encoding of Words · Python

[原题](https://leetcode.com/problems/short-encoding-of-words/)。

参考串以#结束每个独立词，某词若是另一个词的后缀，就可以把下标指向较长词内部而共享同一个#。先按整词去重，再从候选集合删除每个词的所有真后缀。剩下的词相互不是真后缀，每个都需要独立的终止#；把它们各自加#连接即可覆盖全部原词，因此总长度为各词长度加1之和。

Python切片构造后缀需要复制字符，时间O(sum(len(word)^2))，额外空间O(sum(len(word)))，不把切片视为常数时间。输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
