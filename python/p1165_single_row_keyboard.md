# 1165. Single-Row Keyboard · Python

[原题](https://leetcode.com/problems/single-row-keyboard/)。

keyboard是26个小写字母的排列，手指初始位于下标0。每输入一个字母，移动时间为其位置与当前位置之差的绝对值，再更新当前位置。连续相同字母增加0时间；初始位置不是字母a的位置，不能默认从a开始。

时间O(len(keyboard)+len(word))，固定键盘额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
