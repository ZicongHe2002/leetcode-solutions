# 1057. Campus Bikes · Python

[原题](https://leetcode.com/problems/campus-bikes/)。

本题规定每次取所有尚可用配对中最小距离，再按工人下标、车下标打破平局，不是最小总费用匹配。按工人再车下标生成所有配对放入距离桶，桶内天然保持所需同距顺序；按距离升序扫描，双方都未分配才接受。已经占用的一方不会重新释放，因此跳过其后配对不会影响其他候选优先级。题目车数不少于工人数。

W工人B车D种距离，时间O(WB+D log D)，空间O(WB+D)，输入坐标保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
