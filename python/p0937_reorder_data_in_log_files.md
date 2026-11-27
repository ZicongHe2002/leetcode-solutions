# 937. Reorder Data in Log Files · Python

[原题](https://leetcode.com/problems/reorder-data-in-log-files/)。

在第一个空格处分出标识符和完整内容，根据内容首字符判断类型。字母日志按完整内容字典序，再按标识符打破内容平局；数字日志不排序，按读取顺序追加。最终字母在前、数字在后，返回原日志文本，避免重新拼接改变格式，输入不修改。

N条日志、最长长度L，排序时间上界O(NL log N)，解析与存储包含全部文本总长度，额外空间O(NL)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
