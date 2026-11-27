# 1024. Video Stitching · Python

[原题](https://leetcode.com/problems/video-stitching/)。

排序后保持[0,covered]已连续覆盖。下一片起点必须不晚于covered，否则有空隙；在所有这类候选中取最远终点，用同样一片带来最大可达范围，不会限制后续机会。候选都扫描过后若无延伸就无解，否则使用数加1继续，达到或超过time即完成。端点相接允许拼接，片段可剪裁不额外计数。

时间O(n log n)，排序副本空间O(n)，扫描状态O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
