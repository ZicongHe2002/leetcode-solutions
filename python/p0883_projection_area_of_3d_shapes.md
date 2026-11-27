# 883. Projection Area of 3D Shapes · Python

[原题](https://leetcode.com/problems/projection-area-of-3d-shapes/)。

每格是从地面连续堆起的单位立方体。俯视投影中非空格贡献1，零高度格不贡献；沿一行观看时较矮堆被最高堆覆盖，面积就是该行最大高度，列方向同理。三种投影面积独立求出后相加，不计算表面积或重复暴露面。

边长n，时间O(n^2)，除生成器外不存新矩阵，额外空间O(n)，包含zip生成的一列元组，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
