# 984. String Without AAA or BBB · Python

[原题](https://leetcode.com/problems/string-without-aaa-or-bbb/)。

若末尾两字相同，下一位必须使用另一字符；否则优先消耗剩余更多的字符，避免最后积压过多同字符。题目保证a、b存在合法构造，这种选择在不触发三连时尽量平衡剩余数量。每步恰消耗一个对应计数，最后得到所需a个a与b个b，无aaa或bbb，允许任意合法答案。

时间O(a+b)，结果空间O(a+b)，输出外计数状态O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
