## 数据收集
我们使用Bitcore钱包同步节点数据，下载了648个blk**.dat文件，从2009年1月3日至2016年10月7日共433803块。

## 数据解析
利用BitcoinDatabaseGenerator我们将dat文件中的数据解析到SQL Server,运行了后，我们发现总共涉及次交易，充分感受到了SQL Server的速度。对于每个数据库中我们主要用到两张表，```TransactionInput```和```TransactionOutput```,两张表通过```BitcoinTransactionId```联系起来，由于表中的地址由id替换，无法进行聚类，需要增加```InputAddress、OutputAddress、InputValue、TransactionFee```

经过一夜挣扎，考虑方案如下：
现有数据实在过大，我们的目的是提供更准确的分类方法，方法是对交易数据进行分析，不要求数据一定从创世纪快开始，所以先采用一年的数据。改写解析工具，加入hash映射实现分类。

嗯，看完源码发现。。。 Blockchain.dll是个什么鬼，为什么不解析hash address!

发现了一个新工具，BlockSci,功能很强大，然而安装不上，考虑后序在服务器上安装。

## 目前的解决方案

基于demo利用Blockchain.info提供的接口进行递归查询，需要自行解析。