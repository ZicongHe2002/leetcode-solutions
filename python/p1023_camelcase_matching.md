# 1023. Camelcase Matching · Python

[原题](https://leetcode.com/problems/camelcase-matching/)。

查询必须能由pattern仅插入小写字母得到。逐查询维护下一个待匹配模式字符，当前字符相同就消费模式位；否则小写可跳过，大写不能由允许的插入产生，立即失败。结束还必须消费完整模式，既不能少字母也不能有额外大写，不把普通大小写无关匹配当作驼峰规则。

全部查询总字符数L，时间O(L)，除输出外额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
