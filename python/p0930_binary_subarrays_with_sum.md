# 930. Binary Subarrays With Sum · Python

[原题](https://leetcode.com/problems/binary-subarrays-with-sum/)。

原题nums为长度1..30000的二进制数组，0<=goal<=len(nums)，统计和恰为goal的非空连续子数组数。0产生的多个不同起点必须分别计数。输入保持，额外定义空数组且goal=0返回0。

和为整数，所以恰为goal的数量等于和至多goal减去和至多goal-1的数量。at_most对非负预算维护和不超预算的窗口，每次加入右端后缩左端直到合法；因数组非负，合法起点恰为left..right，贡献right-left+1。负预算没有合法非空区间，直接返回0，这也覆盖goal=0。两个线性扫描均只前进边界，时间O(n)，额外空间O(1)；这一滑动窗口推理不适用于有负数的数组。

独立oracle枚举全部非空切片并直接sum，不复用两个至多窗口。长度0..10的2047个二进制数组各测全部合法goal，共20481次查询；空数组为扩展。边界覆盖30000长度、全0计数450015000、全1、goal=0与10000，以及交替数组goal=1的边界起终点，核对int和输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
