# 832. Flipping an Image · Python

[原题](https://leetcode.com/problems/flipping-an-image/)。

水平翻转只反转每行像素顺序，二值反色把0变1、1变0，即1-value。按逆序遍历每行时直接执行反色，两项操作合并为一次结果构造，原图像保持。

方形边长n，时间O(n^2)，输出空间O(n^2)，临时行切片额外占O(n)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
