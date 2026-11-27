# 1032. Stream of Characters · Python

[原题](https://leetcode.com/problems/stream-of-characters/)。

匹配的是当前整个字符流的某个后缀，所以把词倒序放字典树，查询从最新字符反向检查。走到终止标记即已有一个词作后缀，不必消费更早全部历史；缺边则不存在任何候选。最长词长M以内的后缀之外永远不会参与答案，用有界deque只保留这部分字符，词和查询都仅含小写字母，#只作内部终止标记。

总词长L，初始化O(L)，单次query最坏O(M)，总空间O(L+M)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
