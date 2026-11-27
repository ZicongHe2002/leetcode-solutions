# 1114. Print in Order · Python

[原题](https://leetcode.com/problems/print-in-order/)。

LeetCode本题接口是Foo类，三个方法由三个线程各调用一次，传入的回调负责打印，不使用Solution或自行启动线程。first完成打印才设置first_done；second等待该事件后打印，再设置second_done；third等待第二个事件后打印。Event会保留已完成状态，因此线程先开始等待或事件先完成两种调度都正确，无需忙等或sleep。

除阻塞等待调度外，每个方法只执行常数次同步操作，额外空间O(1)。按题目约定打印回调正常返回，不提供可复用多轮协议。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
