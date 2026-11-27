# 1138. Alphabet Board Path · Python

[原题](https://leetcode.com/problems/alphabet-board-path/)。

棋盘前五行各五个字母，最后一行只有z在第0列。固定先U、L再D、R：进入z之前必先左移到第0列，离开z之前必先上移到完整行，因此不经过不存在的格子。每个目标字母完成最短曼哈顿移动后追加!，连续相同字母只需追加!。

棋盘尺寸固定，每字符移动数有常数上界，时间和输出空间O(n)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
