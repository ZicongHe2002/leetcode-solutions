# 925. Long Pressed Name · Python

[原题](https://leetcode.com/problems/long-pressed-name/)。

原题name和typed分别长1..1000，仅小写英文字母。name每个字符可被输入一次或多次，不能删除、重排或引入另一种字符。返回typed是否可能由长按生成。

matched是已经由typed覆盖的name前缀长。当前字符等于下一个待匹配字符时优先消费该字符；否则只能作为紧邻上次输入字符的重复，首字符或与前一typed字符不同则失败。优先匹配不会妨碍合法方案：连续相同字符先满足name原有次数，剩余次数再作为长按。typed结束后必须已消费整个name，不能只验证每个已输入字符合法。

一次遍历typed，每步常数操作，时间O(|typed|)，额外空间O(1)。提前失败也只读输入，不构造分组或递归。

独立oracle用groupby提取两串的字符游程，要求组字符逐组相同且typed各组长度不少于name。name的abc长度1..4共120串与typed长度1..5共363串，共43560对。另测1000长度、末尾合法重复、末尾新字符、漏输重复字符、name比typed长和固定示例，核对bool。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
