# 1203. Sort Items by Groups Respecting Dependencies · Python

[原题](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/)。

同组项目必须连续，依赖项目必须在当前项之前。每个-1项目各建一个独立组，不能把所有无组项目强制绑定在一起。项目拓扑序保证组内依赖顺序；跨组边去重后拓扑排序保证整组间先后次序。按组序输出对应项目桶，两种约束同时满足。项目图或组图有环都无解，即使项目图无环，组连续性也可能形成额外组环。

时间和空间O(n+m+E)，E为输入依赖条目数，参数m指原始组数，新增组最多n个。输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
