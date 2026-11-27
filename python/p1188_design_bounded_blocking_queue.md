# 1188. Design Bounded Blocking Queue · Python

[原题](https://leetcode.com/problems/design-bounded-blocking-queue/)。

接口为BoundedBlockingQueue，capacity为正。生产者先等待空位，在锁内加入队尾后发布一个元素许可；消费者先等待元素，在锁内取队头后发布一个空位许可。阻塞发生在持有互斥锁之前，所以满队列不会锁住消费者，空队列也不会锁住生产者。size同样取锁读取实际已入队元素数，不用信号量的内部计数冒充队列大小。

除调度等待外，各操作O(1)，队列空间O(capacity)，不使用sleep或忙等。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
