# 1180. Count Substrings with Only One Distinct Letter · Python

[原题](https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/)。

合法子串非空且全部字符相同。若当前结尾相同字符连续长度为r，恰有r个合法子串以此处结尾，分别取长度1..r，加入总数即可。遇到新字符将r重置为1，避免跨段计数。例如aaaba的各段贡献6、1、1，总计8。

时间O(n)，额外空间O(1)，按位置计数，不去重子串内容。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
