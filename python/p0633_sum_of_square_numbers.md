# 633. Sum of Square Numbers · Python

[原题](https://leetcode.com/problems/sum-of-square-numbers/)。

原题0<=c<=2^31-1，判断是否存在整数a、b使a²+b²=c，返回bool。平方抹去符号，因此只需考虑0<=a<=b<=floor(sqrt(c))；0也合法，c=0应返回True。使用math.isqrt求准确整数平方根，不经过浮点取整。

左右指针初始为0与isqrt(c)，尚未排除的候选位于left<=a<=b<=right。若left²+right²<c，那么固定a=left时，即使采用当前最大的b也不足，故可排除这个a并增加left。若和大于c，固定b=right时，即使采用当前最小的a也过大，故可排除这个b并减少right。等于时立即成功；left>right表明候选全部排除，返回False。循环必须允许left==right，否则会漏掉2a²；不能从1开始，否则漏掉完全平方数与0。

两指针合计最多移动O(sqrt(c)+1)次，额外空间O(1)，运算均为整数；在本题32位非负输入范围，平方与平方和的整数长度有界。独立小输入oracle直接构造a²+b²不超过20000的集合，完整核对0..20000的20001个输入，不使用双指针。大输入oracle按平方和定理检查素因子分解：每个模4余3的素因子指数必须为偶数；单独处理0，用试除获得指数，不复用生产状态。200个固定种子的十亿至32位上界样本及上界、近上界平方、相等两平方、0/1/2/3/4等边界均核对bool结果。未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
