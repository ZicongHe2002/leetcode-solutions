# 945. Minimum Increment to Make Array Unique · Python

[原题](https://leetcode.com/problems/minimum-increment-to-make-array-unique/)。

原题值非负且只能增加。排序后，当前项至少是原值，也必须大于前面已分配值，故给它max(原值,下个可用值)是最小合法选择；把它抬得更高只会增加当前成本并限制后面，不可能更优。逐项累计新旧差值，分配后把下个可用值设为新值加1。

时间O(n log n)，排序副本空间O(n)，扫描额外空间O(1)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
