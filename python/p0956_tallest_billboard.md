# 956. Tallest Billboard · Python

[原题](https://leetcode.com/problems/tallest-billboard/)。

两侧支架不区分左右，只记非负高度差d，以及在此差下最大的较矮高度h；同差下更大h让两侧都更高，完全支配更小h。新杆不选时保留原状态；加高侧使差为d+rod、矮高仍h；加矮侧后差为abs(d-rod)，新矮高为h+min(d,rod)。每杆从旧表转到新表，保证仅用一次。最后差0的最大矮高就是等高广告牌答案。

杆数N、总长度S，时间O(NS)，滚动状态空间O(S)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
