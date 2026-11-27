# 1210. Minimum Moves to Reach Target with Rotations · Python

[原题](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/)。

蛇占相邻两格，状态以尾部的左上坐标及朝向表示，0为水平、1为竖直。水平向右只需检查新增右格，向下或顺时针旋转都需检查下方两格；竖直向下检查新增下格，向右或逆时针旋转检查右侧两格。只检查旋转后的单个蛇头格不够，还必须有完整2x2旋转空间。每种合法操作代价1，因此BFS首次到达右下水平状态即最少步数，无路返回-1。

最多2n^2个状态，时间和额外空间O(n^2)，原网格保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
