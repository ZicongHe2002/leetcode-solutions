# 744. Find Smallest Letter Greater Than Target · Python

[原题](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)。

原题letters长度2..10000，已按非递减顺序排列的小写字母，至少两种不同字符。返回严格大于target的最小字母；若不存在，回到letters[0]。相等字符不能成为答案，输入顺序保持。

bisect_right返回把target放在所有相等元素之后的插入位置，也就是首个严格大于target的下标。若它小于数组长度，该位置按有序性就是所需最小字母；若等于长度，说明没有更大字母，取模把它变为0，恰好实现回绕。位置只在0..n之间，取模不会产生其他非预期映射。

重复字母会被bisect_right整体跳过，不需要去重，也不能改用bisect_left而取到相等元素。非空数组由合同保证，模除和首元素读取都有定义。

二分时间O(log n)，额外空间O(1)，没有复制、排序或线性扫描输入数组。字符比较在小写单字母合同下为常数。

独立oracle从原数组左到右寻找第一个大于target的字符，找不到就选首项，不使用二分。枚举a/c/z组成、长度2..8且至少两种不同字母的140个合法有序多重集合，分别查询全部26个目标，共3640次；另核对官方例、10000元素重复块、等于端点和首尾回绕及输入保持。未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
