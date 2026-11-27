# 677. Map Sum Pairs · Python

[原题](https://leetcode.com/problems/map-sum-pairs/)。

原题insert把小写key映射到val，同key重插是覆盖；sum返回所有以prefix开头的当前键值之和。key/prefix长度1..50，val在1..1000，每实例insert与sum合计最多50次。接口为MapSum/insert/sum，不是Solution。

values保存每个完整key最近的值，前缀树节点total保存经过该前缀的所有完整key当前值之和。insert先求delta=新值-旧值（新key旧值为0），只把delta加到根及key路径的每个节点。若值变小，delta为负，正好撤销被覆盖掉的多余部分；若新旧相同则总和不变。不能每次都把新值直接累加，否则重复插入会多计。

沿prefix走树即可找到该前缀的total；中途缺边代表不存在匹配键，返回0。完整key也可为另一个key的前缀，路径总和自然同时包含两者，不需要把终点和中间节点混为只存一个词的值。查询不创建新节点。

设key长度K、prefix长度P。平均哈希操作下insert为O(K)，sum为O(P)；前缀节点数不超过不同键总字符数加1，连同当前完整键值表空间O(S)，S为当前不同键的总字符数。新节点只在路径缺边时构建，不通过setdefault提前构建无用对象。

独立oracle只维护普通字典，sum时遍历全部键并使用startswith求和。三种短key与三种合法值构成9种insert，枚举全部3次插入程序，共729个对象；每次插入后核对6个前缀，共13122次sum，每对象21次API调用，包含相同key降值与重复插入。边界对象恰50次API调用，核对50字符键/前缀、最大val与缺前缀；另用短独立对象检查空映射和apple/app覆盖。未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
