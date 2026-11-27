# 908. Smallest Range I · Python

[原题](https://leetcode.com/problems/smallest-range-i/)。

每项可独立增加[-k,k]内任意整数。原最大和最小两项调整后仍至少相差原极差减2k，这是下界；其余中间值都可调入这两个端点限定的共同范围。若原极差不超过2k，所有允许区间有公共点，能全部调为同值，极差0。故返回max(0,max-min-2k)。

时间O(n)，额外空间O(1)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
