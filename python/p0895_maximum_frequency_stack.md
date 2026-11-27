# 895. Maximum Frequency Stack · Python

[原题](https://leetcode.com/problems/maximum-frequency-stack/)。

push把该值频次加1，再压入对应频次层。层中保存到达这一频次的时间顺序，因此最高频层末尾正好是频次最高且并列时最近压入的值。pop只移除最高层末尾，并降低该值频次；若该层空，最大频次降1。较低层中的旧记录保留，以表示尚未弹出的更早出现。题目保证pop时栈非空。

每次操作平均O(1)，总空间O(P)，P为累计push次数的上界；没有每次遍历全栈寻找最大值。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
