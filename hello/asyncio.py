# 异步IO
# 当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理。
# 异步IO模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程
# 当遇到IO操作时，代码只负责发出IO请求，不等待IO结果，然后直接结束本轮消息处理，进入下一轮消息处理过程。当IO操作完成后，将收到一条“IO完成”的消息，
# 处理该消息时就可以直接获取IO操作结果。在“发出IO请求”到收到“IO完成”的这段时间里，同步IO模型下，主线程只能挂起，但异步IO模型下，主线程并没有休息，
# 而是在消息循环中继续处理其他消息。这样，在异步IO模型下，一个线程就可以同时处理多个IO请求，并且没有切换线程的操作。
# 对于大多数IO密集型的应用程序，使用异步IO将大大提升系统的多任务处理能力。

# 老张爱喝茶，煮开水。
# 出场人物：老张，水壶两把（普通水壶，简称水壶；会响的水壶，简称响水壶）。
# 1 老张把水壶放到火上，立等水开。（同步阻塞）
# 老张觉得自己有点傻
# 2 老张把水壶放到火上，去客厅看电视，时不时去厨房看看水开没有。（同步非阻塞）
# 老张还是觉得自己有点傻，于是变高端了，买了把会响笛的那种水壶。水开之后，能大声发出嘀~~~~的噪音。
# 3 老张把响水壶放到火上，立等水开。（异步阻塞）
# 老张觉得这样傻等意义不大
# 4 老张把响水壶放到火上，去客厅看电视，水壶响之前不再去看它了，响了再去拿壶。（异步非阻塞）
# 老张觉得自己聪明了。

# 所谓同步异步，只是对于水壶而言。
# 普通水壶，同步；响水壶，异步。
# 虽然都能干活，但响水壶可以在自己完工之后，提示老张水开了。这是普通水壶所不能及的。
# 同步只能让调用者去轮询自己（情况2中），造成老张效率的低下。

# 所谓阻塞非阻塞，仅仅对于老张而言。
# 立等的老张，阻塞；看电视的老张，非阻塞。
# 情况1和情况3中老张就是阻塞的，媳妇喊他都不知道。虽然3中响水壶是异步的，可对于立等的老张没有太大的意义。所以一般异步是配合非阻塞使用的，这样才能发挥异步的效用。

# 协程，又称微线程，纤程。英文名Coroutine。
# 所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
# 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
# Python对协程的支持是通过generator实现的。在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
# 但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
