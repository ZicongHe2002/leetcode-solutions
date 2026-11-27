# 715. Range Module · Python

[原题](https://leetcode.com/problems/range-module/)。

原题维护实数轴上的半开区间[left,right)，1<=left<right<=10^9，三个API合计最多10000次。addRange是并集，removeRange是差集，queryRange要求整个区间的每个实数都被覆盖；不能只查询两个端点或把右端也删除。接口为RangeModule/addRange/queryRange/removeRange。

boundaries保存严格递增的覆盖切换点，成对表示互不重叠、也不相邻的已覆盖区间[start,end)。从左侧未覆盖状态出发，每经过一个边界就切换一次，所以边界前后覆盖状态由下标奇偶决定。相邻区间应合并，否则会留下无意义的零间隔切换。

修改时用bisect_left(left)与bisect_right(right)定位包含相等端点的旧边界段。添加区间时删除其中所有旧切换点；若left外侧原来未覆盖（start为偶数），保留新left起点，若right外侧原来未覆盖（end为偶数），保留新right终点。删除区间时反过来：原来覆盖延伸到left外侧（start为奇数）就用left结束它，原来覆盖延伸到right外侧（end为奇数）就用right重新开始。区间外的旧边界保持。

查询用bisect_right(left)把恰在left的起点算作已进入覆盖，用bisect_left(right)把恰在right的终点留在查询外。只有两个插入位置相同、且奇数个边界已越过时，整个查询都在同一个已覆盖段内；存在内部断点或left未覆盖都会返回False。相等端点的左右bisect选择直接对应半开语义。

设当前边界数M、累计调用数Q。查询O(log(M+2))时间、O(1)空间，+2包含空表的常数工作；添加/删除虽然只做二分，但Python列表切片搬移最坏O(M+1)时间与临时空间，不能声称整体修改O(log M)。总存储O(Q+1)，不按10^9坐标分配数组。

独立oracle保存各单位宽实数小格的布尔覆盖；API端点都是整数，所以每个[x,x+1)内覆盖恒定，逐格检查等价于完整实数区间检查。四个短区间的添加/删除/查询构成12种操作，长度1..4共22620个程序，每步后核对1..5端点的全部10个查询；每实例最多44次API。另覆盖恰10000调用、5000个不相邻区间、10^9边界、相邻合并、移除空区与中间挖洞。未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
