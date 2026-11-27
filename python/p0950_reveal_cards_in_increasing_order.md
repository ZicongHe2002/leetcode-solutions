# 950. Reveal Cards In Increasing Order · Python

[原题](https://leetcode.com/problems/reveal-cards-in-increasing-order/)。

实际揭牌与移底只依赖位置，不依赖牌面。先用0..n-1位置队列模拟：队首是下一张被揭牌的原位置，取出后将下一位置移队尾。按牌值升序把最小未分配值填到被揭的位置，便保证未来揭露顺序递增。队列空时不再移底，输入牌组保持。

时间O(n log n)，额外空间O(n)，包括排序副本、位置队列和结果。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
