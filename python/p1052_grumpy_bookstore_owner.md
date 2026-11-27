# 1052. Grumpy Bookstore Owner · Python

[原题](https://leetcode.com/problems/grumpy-bookstore-owner/)。

老板不生气时的顾客必满意，先记入base，不能在技巧窗口再重复加。滑窗只累加grumpy为1的顾客，窗口长恰minutes，离开窗口就扣对应可挽回人数，取最大额外值加base。题目minutes在1..总时长内，覆盖全时段也自然成立，customers非负。

时间O(n)，额外空间O(1)，两个输入数组保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
