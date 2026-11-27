# 771. Jewels and Stones · Python

[原题](https://leetcode.com/problems/jewels-and-stones/)。

原题jewels与stones长度均为1..50，字符为大小写英文字母，jewels内字符互异。每个jewels字符代表一种宝石，统计stones中有多少颗宝石；重复宝石石头每颗都计数，大小写是不同种类。

把jewels转为集合后逐个读取stones，每个字符只作一次准确成员判定，真值加1。集合只去掉种类查找的重复，不会对stones去重，因此同一宝石重复出现也逐颗累计；不做lower转换，所以a和A不会混同。输入字符串不变。

设宝石种类数J、石头数S，哈希集合期望时间O(J+S)，额外空间O(J)。原题字母域52种，集合也受该常数限制。返回sum产生的int，而不是是否至少有一颗宝石的bool。

独立oracle逐颗石头与每个互异宝石字符直接相等比较，不用集合。三字符AaB的全部7个非空宝石子集，以及长度1..6的全部1092石头串，共7644查询；包含大小写与重复计数。另核对官方例、两输入最大50长度、全命中、全不命中和大小写分离。未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
