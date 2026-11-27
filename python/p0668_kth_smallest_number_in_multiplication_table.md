# 668. Kth Smallest Number in Multiplication Table · Python

[原题](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/)。

原题1<=m,n<=30000，乘法表位置(i,j)的值为i*j，下标从1开始，求按所有单元格值排序后的第k项，1<=k<=m*n。相同数值来自不同格时必须重复计数，不能对表值去重；返回值是整数。

对候选x，第i行中不超过x的项数恰为min(n,floor(x/i))，逐行相加得到排名计数。i>x时整行贡献0，可以不访问。交换m、n不会改变单元格多重集，先让m较小，减少每次计数行数；累计已经达到k时也可停止，因为只需判断是否至少k个。

计数随x不减，答案是最小的满足count(x)>=k的整数。以[1,m*n]为闭范围二分：计数足够就保留middle作为上界，不足则下界变middle+1，最终两界相等。重复值会让计数跳过某些k，必须用>=而不是寻找count恰好等于k；最小边界仍正是第k个单元格值。

时间O(min(m,n)*log(m*n+1))，额外空间O(1)，log中的+1也涵盖1x1表。没有构造m*n个值，原题最大900000000格仍只按较小边扫描。

独立小输入oracle真实生成并排序所有i*j，完整核对m,n=1..20的400张表、每张全部排名，共44100次查询，保留重复项。最大30000x30000另查首尾及倒数第二项，单行/单列，以及三个大规模中间排名；中间排名用bisect在每行虚拟range上搜索，不使用生产的整除计数，核对count(answer-1)<k<=count(answer)。未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
