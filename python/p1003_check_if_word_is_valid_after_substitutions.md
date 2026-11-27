# 1003. Check If Word Is Valid After Substitutions · Python

[原题](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/)。

正向操作在任意位置插入abc，逆向就是删除连续abc。栈保存已读前缀尚未归约的字符，追加新字符后若末三位为abc就立刻删除。删除可能让两侧此前被插入内容隔开的字符重新相邻，后续压栈继续处理，覆盖嵌套与串接的插入结构。所有字符都归约为空才合法，不只比较三字母计数。

每字符进出栈至多一次，三位后缀检查为常数，时间O(n)，空间O(n)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
