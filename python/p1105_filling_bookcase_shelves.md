# 1105. Filling Bookcase Shelves · Python

[原题](https://leetcode.com/problems/filling-bookcase-shelves/)。

每本书的宽度不超过shelfWidth，摆放必须保持原顺序。令best[i]表示前i本书的最小总高度，枚举最后一层从哪本书开始，向左累计宽度与本层最大高度，只要宽度可行就用best[start]+height转移。宽度首次超限后，更靠左的区间也不可行，立即停止。不能贪心地把每层装到最满，因为把高书移到相邻层可能减少两层高度之和。

时间O(n^2)，额外空间O(n)，原书本数组不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
