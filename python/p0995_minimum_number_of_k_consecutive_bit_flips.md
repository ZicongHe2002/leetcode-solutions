# 995. Minimum Number of K Consecutive Bit Flips · Python

[原题](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/)。

从左向右，已处理位不能再被未来起点影响，所以当前有效位若为0，从当前开始翻k位是唯一必须的选择；若不足k个剩余位就无解。parity保存所有覆盖当前处的翻转奇偶，用到期差分在index+k撤销该翻转的影响，不真正遍历更新整段。当前位为1时不额外翻转，故每一步都由前缀要求强制，操作数最少。

时间O(n)，差分额外空间O(n)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
