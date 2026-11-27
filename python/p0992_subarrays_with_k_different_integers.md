# 992. Subarrays with K Different Integers · Python

[原题](https://leetcode.com/problems/subarrays-with-k-different-integers/)。

恰好k种等于至多k种减至多k-1种。至多窗口加入右端后，若种类超限就移出左端并删除归零频次，直到合法；此时以当前右端结束、从left到right任一位置开始都合法，共right-left+1个。每个数组位置对应各自子数组，不去重重复内容。limit0会缩到空窗口，贡献自然为0。

两趟期望时间O(n)，窗口频次空间O(min(n,k+1))，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
