# 1021. Remove Outermost Parentheses · Python

[原题](https://leetcode.com/problems/remove-outermost-parentheses/)。

有效括号串中深度从0进入1的左括号，是一个原语最外开括号，跳过；右括号先减深度，回到0时是其最外闭括号，也跳过。其他深度下的括号都保留。每次回到0开始下个原语，无需先拆分字符串或只删除整个串的第一最后字符。

时间O(n)，结果空间O(n)，深度状态O(1)，输入保证有效且保持不变。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
