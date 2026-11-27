# 1115. Print FooBar Alternately · Python

[原题](https://leetcode.com/problems/print-foobar-alternately/)。

本题接口为FooBar(n)，两个线程分别调用foo与bar。初始只有foo持有可用许可，打印后才把许可交给bar，bar打印后再交回foo，因此每轮严格产生foobar，且任意时刻只有一个线程有打印权。许可可在另一线程开始等待前发出，不会丢失唤醒。两个循环都执行n次，不启动额外工作线程、不使用睡眠估计调用顺序。

共O(n)次同步和回调操作，阻塞时间由线程调度决定，额外空间O(1)。回调按题意正常返回。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
