# 1116. Print Zero Even Odd · Python

[原题](https://leetcode.com/problems/print-zero-even-odd/)。

本题接口是ZeroEvenOdd(n)，三个方法由三个线程调用，目标为010203...0n。初始仅zero有许可；它每次打印0后只唤醒下一数字所属的奇数或偶数线程，数字线程打印后把许可还给zero。两类数字分别单调遍历自己的序列，因此zero的轮数与打印出的数字一一对应，不会多打印最后一个0。

共O(n)次同步和打印操作，额外空间O(1)，阻塞等待由运行时调度。回调正常返回的约定同原题，不自行创建线程。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
