# 1087. Brace Expansion · Python

[原题](https://leetcode.com/problems/brace-expansion/)。

本题语法的花括号不嵌套，括号内为逗号分隔的不同小写字母。普通字母构成单选组，花括号构成多选组。从空前缀开始，每处理一组，给所有已有前缀分别追加该组的每个选项，因此既不漏掉组合，也不把同一组的多个字母同时追加。最后排序满足字典序要求。例如a{b,c}展开为ab、ac。此实现不用于嵌套表达式的Brace Expansion II。

输入长N，输出P个长度L的字符串，构造时间O(N+PL^2)，排序最坏O(PL log P)，结果及中间字符串空间O(PL+N)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
