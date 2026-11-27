# 939. Minimum Area Rectangle · Python

[原题](https://leetcode.com/problems/minimum-area-rectangle/)。

轴对齐矩形由两列中同一对纵坐标构成。横坐标递增扫描，每列枚举两个y作为纵边，若相同y对曾出现，就得到一个矩形。固定高度与当前右列时，最近的旧左列给最小宽度，所以每个y对只需保存最近横坐标。输入点互异，纵边高度和两列间距都为正，无候选返回0。

N个点，时间上界O(N^2+N log N)，纵边键存储最坏O(N^2)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
