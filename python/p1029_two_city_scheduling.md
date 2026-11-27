# 1029. Two City Scheduling · Python

[原题](https://leetcode.com/problems/two-city-scheduling/)。

先设全部去B，再必须选一半改去A，改变费用恰是A-B。选择最小的一半差值使总费用最小，等价于排序后前半取A费用、后半取B费用。差值而非单边绝对费用体现改派代价，确保两城人数恰各半，负差优先也自然处理。

时间O(n log n)，排序副本空间O(n)，原费用表保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
