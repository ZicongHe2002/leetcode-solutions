# 1078. Occurrences After Bigram · Python

[原题](https://leetcode.com/problems/occurrences-after-bigram/)。

按空白分词，逐个第三词下标检查其紧前两词是否分别为first和second，命中就保留该词。匹配必须连续，不能跨词跳跃，重叠的二元组和重复后继都按实际出现次数保留，输出顺序等于原文本顺序。接口名称按题目为findOcurrences，保留其拼写。

文本总长L，时间和额外空间O(L)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
