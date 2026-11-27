# 1156. Swap For Longest Repeated Character Substring · Python

[原题](https://leetcode.com/problems/swap-for-longest-repeated-character-substring/)。

最多交换两个位置一次。某种字符的最佳连续区间，要么来自一段再换入一个相同字符，要么来自中间只隔一个其他字符的两段，把中间字符换走。若没有外部同字符，不能凭空增加总数，所以每个候选都以该字符全串频次为上限。两段之间隔两个以上异字符时一次交换无法填满，不构成额外候选。

时间O(n)，分组列表额外空间O(n)，原字符串保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
