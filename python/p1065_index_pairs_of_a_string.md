# 1065. Index Pairs of a String · Python

[原题](https://leetcode.com/problems/index-pairs-of-a-string/)。

把词典放入前缀树，从文本每个起点沿后续字符匹配，缺边则该起点再延长也不可能成词，可停止。到达终止标记就输出[start,end]，继续匹配以支持一个词是另一个词前缀的情况；每个起点都搜索，允许重叠出现。起点递增、同起点终点递增，结果天然满足所需排序。

词总长L、文本长N、最长词M，时间O(L+NM)，空间O(L+输出数)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
