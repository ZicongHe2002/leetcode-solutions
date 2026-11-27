# 1139. Largest 1-Bordered Square · Python

[原题](https://leetcode.com/problems/largest-1-bordered-square/)。

只要求边框全1，内部允许0。固定右下角，向左和向上连续1长度给出底边与右边的上界；再检查顶部右端的left长度和左下角的up长度，就覆盖另外两条边。从最大候选边长递减，只需尝试超过当前最佳的尺寸，成功后立即停止该角枚举。

时间O(RC min(R,C))，额外空间O(RC)，返回面积而非边长，原矩阵保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
