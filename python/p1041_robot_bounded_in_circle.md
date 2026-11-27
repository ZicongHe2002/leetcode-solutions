# 1041. Robot Bounded In Circle · Python

[原题](https://leetcode.com/problems/robot-bounded-in-circle/)。

只模拟一次指令周期。若回到原点，每周期重复同一路线；若最终朝向不是原北向，后续周期位移会旋转，至多四周期总位移抵消，也有界。只有朝向仍北且产生非零位移时，每周期重复同向平移，距离可无限增大。无需猜测重复执行次数或搜索某个半径。

时间O(指令长)，额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
