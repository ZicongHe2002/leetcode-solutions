# 725. Split Linked List in Parts · Python

[原题](https://leetcode.com/problems/split-linked-list-in-parts/)。

原题链表0..1000个节点，值0..1000，k在1..50。把原链按原顺序切成恰k段，长度两两至多相差1，前段不能短于后段，允许空段。本实现使用原有ListNode对象，切断段尾next后返回各段头，不复制节点或改写val。

先扫描得总长度n。写成n=base*k+extra且0<=extra<k，由总数和差至多1可知每段只能长base或base+1，且恰extra段较长。前段不短的规则使前extra段取base+1，余下取base。n<k时前n段各一个节点，后面为空；n=0时全部为空。

第二次遍历中，node始终指向尚未分配后缀的首节点。每次先记录段头；非空段走size-1步到段尾，先保存following，再把next置空，最后从following继续。保存顺序保证不会丢掉余下链。空段只记录None，不解引用。所有非空段长度之和恰n，因此最后一个非空段结束后node为None，每个原节点恰好分到一段。

计数遍历O(n)，切段累计前进O(n)且必须产生k项，故时间O(n+k)。返回列表空间O(k)，除返回值外工作空间O(1)。空链仍有O(k)输出成本。ListNode由LeetCode环境提供，实现不依赖自定义节点构造。

独立oracle对小规模枚举全部弱组成，再按总长度、前段不短和最大最小差至多1的字面条件筛选唯一长度序列，不使用divmod公式。核对值0/1000、长度0..7所有255条链及k=1..6共1530次切分。遍历结果严格检查原节点身份、值、全局无重用/无环、恰k段与段尾断开；另覆盖1000节点的k=1/7/50、空链k=50及官方不足k样例。未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
