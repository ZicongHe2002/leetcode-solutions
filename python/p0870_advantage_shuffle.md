# 870. Advantage Shuffle · Python

[原题](https://leetcode.com/problems/advantage-shuffle/)。

保留nums2原下标并按值排序，递增处理nums1。当前最小可用值若能赢最小剩余对手，就把这场胜利固定；若连最小对手也赢不了，它无法对任何剩余对手获胜，牺牲给最大对手，把较易赢的对手留给后面较大的值。这样不浪费可用胜场，按保存的下标写回答案，胜利使用严格大于。

时间O(n log n)，额外空间O(n)，输入不修改，返回nums1的一个排列。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
