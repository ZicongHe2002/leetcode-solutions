# 1190. Reverse Substrings Between Each Pair of Parentheses · Python

[原题](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)。

输入括号合法且正确嵌套。先用栈记录每对括号的位置。第二遍遇到括号就跳到匹配端并反转行走方向，相当于从另一端反向遍历内部，离开该层括号时再次反向恢复外层方向。只把普通字母加入结果，所有括号被省略。该过程直接访问最终顺序，不会为每层嵌套重复反转长子串。

时间O(n)，额外空间O(n)，无需递归，原字符串保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
