# 1195. Fizz Buzz Multithreaded · Python

[原题](https://leetcode.com/problems/fizz-buzz-multithreaded/)。

接口为FizzBuzz(n)，四线程分别调用fizz、buzz、fizzbuzz、number。共享current只能在条件锁内检查和推进，四个谓词互斥且覆盖每个整数。不属于自己时wait释放锁并等待，再循环复核，能应对虚假唤醒；打印后推进并notify_all，使下一负责线程有机会执行。最后一次推进也唤醒全部线程，它们发现current>n后退出，不会留下尾部等待者。

共n次回调和O(n)次固定四线程唤醒工作，额外状态O(1)，调度等待时间不计入计算工作。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
