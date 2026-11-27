# 866. Prime Palindrome · Python

[原题](https://leetcode.com/problems/prime-palindrome/)。

除11外，偶数位十进制回文都能被11整除，不会是质数。先返回2、3、5、7、11中第一个不小于n的值；之后只按前半段递增生成奇位回文，把前半段除最后一位外反向附在末尾。生成顺序随前缀递增，跳过小于n的值，对候选用奇数试除至平方根。首次通过就是所求最小质数回文，不逐个整数筛选。

若访问P个回文候选、返回值上界M，时间上界O(P*(sqrt(M)+log M))，额外空间O(log M)，未声称质数间距有固定保证。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
