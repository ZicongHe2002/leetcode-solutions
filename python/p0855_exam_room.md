# 855. Exam Room · Python

[原题](https://leetcode.com/problems/exam-room/)。

用有序列表保存已占座号。空考场选0；否则候选是最左空段首座、每对已占座之间靠左中点，以及最右空段末座。按从小座号到大座号扫描，只有最近距离严格更大才替换候选，从而同距取最小座号。插入保持有序，leave删除题目保证已占用的座号。seat调用保证考场未满。

若当前有m个已占座，seat扫描和列表插入O(m)，leave列表删除O(m)，空间O(m)。该实现使用线性间隔扫描，未声称每次操作为对数复杂度。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
