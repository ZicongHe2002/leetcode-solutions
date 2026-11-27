# 526. Beautiful Arrangement · Python

[原题](https://leetcode.com/problems/beautiful-arrangement/)。

用1..n各一次排列，要求每个1基位置position上的value满足value能整除position或position能整除value，求全部合法排列数量。原题1<=n<=15，返回精确整数，不取模。两种整除关系是或，不能误写成且，也不能用0基位置做除数。

预先为每个位置建立allowed位掩码，第value-1位表示该值在此位置可用。counts[mask]记录已填完前popcount(mask)个位置、恰好使用mask中值的合法前缀排列数量；空前缀有一种，所以counts[0]=1。下一个位置自然是popcount(mask)+1，无需额外保存位置维度。

候选为allowed[position]与未用位的交集。每次取最低有效bit，把它加入mask并把全部counts[mask]条前缀计数累加到新状态。同一mask可能来自多个不同前缀顺序，不能只保存可达布尔值；未来可用值和当前位置只依赖mask，所以聚合计数不会丢失必要信息。新增位让mask数值严格增加，按整数mask升序就是合法拓扑顺序。

每条完整排列对应唯一的逐位置选值路径；反过来每次转移都满足整除且没有重复值，满掩码恰好是合法完整排列。因此counts[-1]既不会漏计也不会重复计算。Python的~mask虽有无限符号扩展，但与有限allowed掩码相与后只保留1..n的合法位，不会产生范围外的值。

预处理O(n^2)，最多2^n状态各尝试n个候选，时间上界O(n^2+n*2^n)，辅助空间O(2^n+n)。原题掩码至多15位，位运算与bit_count按机器整数操作计；不用递归或枚举全部n!排列来计算生产结果。

独立小参考对n=1..8直接枚举全部排列，逐位置验证定义；n=9..15用从最后位置向前填的普通回溯与布尔使用表枚举，没有位掩码DP或缓存合并。全部15个合法输入分别对照，其中n=15为24679；检查int。原题输入范围完整覆盖，未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
