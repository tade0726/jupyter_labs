
# Table of Contents
 <p><div class="lev2 toc-item"><a href="#什么是NoSQL?" data-toc-modified-id="什么是NoSQL?-01"><span class="toc-item-num">0.1&nbsp;&nbsp;</span>什么是NoSQL?</a></div><div class="lev2 toc-item"><a href="#为什么使用NoSQL-?" data-toc-modified-id="为什么使用NoSQL-?-02"><span class="toc-item-num">0.2&nbsp;&nbsp;</span>为什么使用NoSQL ?</a></div><div class="lev2 toc-item"><a href="#RDBMS-vs-NoSQL" data-toc-modified-id="RDBMS-vs-NoSQL-03"><span class="toc-item-num">0.3&nbsp;&nbsp;</span>RDBMS vs NoSQL</a></div><div class="lev1 toc-item"><a href="#Mongodb-安装" data-toc-modified-id="Mongodb-安装-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Mongodb 安装</a></div><div class="lev3 toc-item"><a href="#下载" data-toc-modified-id="下载-101"><span class="toc-item-num">1.0.1&nbsp;&nbsp;</span>下载</a></div><div class="lev3 toc-item"><a href="#解压" data-toc-modified-id="解压-102"><span class="toc-item-num">1.0.2&nbsp;&nbsp;</span>解压</a></div><div class="lev3 toc-item"><a href="#将解压文件放到一个合适地方，" data-toc-modified-id="将解压文件放到一个合适地方，-103"><span class="toc-item-num">1.0.3&nbsp;&nbsp;</span>将解压文件放到一个合适地方，</a></div><div class="lev3 toc-item"><a href="#设置环境变量" data-toc-modified-id="设置环境变量-104"><span class="toc-item-num">1.0.4&nbsp;&nbsp;</span>设置环境变量</a></div><div class="lev3 toc-item"><a href="#创建数据存放文件夹（注意权限)" data-toc-modified-id="创建数据存放文件夹（注意权限)-105"><span class="toc-item-num">1.0.5&nbsp;&nbsp;</span>创建数据存放文件夹（注意权限)</a></div><div class="lev3 toc-item"><a href="#启动mongodb-服务器" data-toc-modified-id="启动mongodb-服务器-106"><span class="toc-item-num">1.0.6&nbsp;&nbsp;</span>启动mongodb 服务器</a></div><div class="lev1 toc-item"><a href="#使用" data-toc-modified-id="使用-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>使用</a></div><div class="lev1 toc-item"><a href="#MongoDB-概念解析" data-toc-modified-id="MongoDB-概念解析-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>MongoDB 概念解析</a></div><div class="lev2 toc-item"><a href="#数据库" data-toc-modified-id="数据库-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>数据库</a></div><div class="lev2 toc-item"><a href="#文档" data-toc-modified-id="文档-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>文档</a></div><div class="lev2 toc-item"><a href="#集合" data-toc-modified-id="集合-33"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>集合</a></div><div class="lev2 toc-item"><a href="#元数据" data-toc-modified-id="元数据-34"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>元数据</a></div><div class="lev1 toc-item"><a href="#MongoDB-数据类型" data-toc-modified-id="MongoDB-数据类型-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>MongoDB 数据类型</a></div><div class="lev1 toc-item"><a href="#参考-http://www.runoob.com/mongodb/mongodb-databases-documents-collections.html" data-toc-modified-id="参考-http://www.runoob.com/mongodb/mongodb-databases-documents-collections.html-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>参考 <a href="http://www.runoob.com/mongodb/mongodb-databases-documents-collections.html" target="_blank">http://www.runoob.com/mongodb/mongodb-databases-documents-collections.html</a></a></div>

## 什么是NoSQL?
NoSQL，指的是非关系型的数据库。NoSQL有时也称作Not Only SQL的缩写，是对不同于传统的关系型数据库的数据库管理系统的统称。
NoSQL用于超大规模数据的存储。（例如谷歌或Facebook每天为他们的用户收集万亿比特的数据）。这些类型的数据存储不需要固定的模式，无需多余操作就可以横向扩展。
## 为什么使用NoSQL ?
今天我们可以通过第三方平台（如：Google,Facebook等）可以很容易的访问和抓取数据。用户的个人信息，社交网络，地理位置，用户生成的数据和用户操作日志已经成倍的增加。我们如果要对这些用户数据进行挖掘，那SQL数据库已经不适合这些应用了, NoSQL数据库的发展也却能很好的处理这些大的数据。
## RDBMS vs NoSQL
RDBMS 
- 高度组织化结构化数据 
- 结构化查询语言（SQL） (SQL) 
- 数据和关系都存储在单独的表中。 
- 数据操纵语言，数据定义语言 
- 严格的一致性
- 基础事务
NoSQL 
- 代表着不仅仅是SQL
- 没有声明性查询语言
- 没有预定义的模式
-键 - 值对存储，列存储，文档存储，图形数据库
- 最终一致性，而非ACID属性
- 非结构化和不可预知的数据
- CAP定理 
- 高性能，高可用性和可伸缩性

# Mongodb 安装

### 下载
* https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-3.4.2.tgz
* 其他版本： https://www.mongodb.com/download-center?jmp=homepage#community

### 解压
tar -zxvf mongodb-linux-x86_64-ubuntu1604-3.4.2.tgz

### 将解压文件放到一个合适地方，
mkdir -p mongodb
cp -R -n mongodb-linux-x86_64-3.4.2/ mongodb
Note：注意要有正确的读写权限
### 设置环境变量
为了是mongodb命令能在任意文件夹下执行
add the following line to your shell’s rc file (e.g. ~/.bashrc)

export PATH=<mongodb-install-directory>/bin:$PATH
source ~/.bashrc
### 创建数据存放文件夹（注意权限)
mkdir -p /data/db
### 启动mongodb 服务器 
可以添加子命令，如IP,端口，数据文件位置
mongod
# 使用
可以添加子命令，如IP,端口，数据文件位置

mongo

# MongoDB 概念解析

<table>

<tbody><tr>
<th>SQL术语/概念</th>
<th>MongoDB术语/概念</th>
<th>解释/说明</th>
</tr>
<tr>
<td>database</td>
<td>database</td>
<td>数据库</td>
</tr>
<tr>
<td>table</td>
<td>collection</td>
<td>数据库表/集合</td>
</tr>
<tr>
<td>row</td>
<td>document</td>
<td>数据记录行/文档</td>
</tr>
<tr>
<td>column</td>
<td>field</td>
<td>数据字段/域</td>
</tr>
<tr>
<td>index</td>
<td>index</td>
<td>索引</td>
</tr>
<tr>
<td>table joins</td>
<td>&nbsp;</td>
<td>表连接,MongoDB不支持</td>
</tr>
<tr>
<td>primary key</td>
<td>primary key</td>
<td>主键,MongoDB自动将_id字段设置为主键</td>
</tr>
</tbody>
</table>


<img src="http://www.runoob.com/wp-content/uploads/2013/10/Figure-1-Mapping-Table-to-Collection-1.png">

## 数据库
一个mongodb中可以建立多个数据库。
MongoDB的默认数据库为"db"，该数据库存储在data目录中。
MongoDB的单个实例可以容纳多个独立的数据库，每一个都有自己的集合和权限，不同的数据库也放置在不同的文件中。
"show dbs" 命令可以显示所有数据的列表。

## 文档
文档是一个键值(key-value)对(即BSON)。MongoDB 的文档不需要设置相同的字段，并且相同的字段不需要相同的数据类型，这与关系型数据库有很大的区别，也是 MongoDB 非常突出的特点。
一个简单的文档例子如下：
RDBMS 与 MongoDB 对应的术语：
<table class="reference">
<tbody><tr>
<th style="width:50%;">RDBMS</th>
<th>MongoDB</th>
</tr>
<tr>
<td>数据库</td>
<td>数据库</td>
</tr>
<tr>
<td>表格</td>
<td>集合</td>
</tr>
<tr>
<td>行</td>
<td>文档</td>
</tr>
<tr>
<td>列</td>
<td>字段</td>
</tr>
<tr>
<td>表联合</td>
<td>嵌入文档</td>
</tr>
<tr>
<td>主键</td>
<td>主键 (MongoDB 提供了 key  为 _id )</td>
</tr>
<tr>
<th colspan="2" style="text-align:center;">数据库服务和客户端</th>
</tr>
<tr>
<td>Mysqld/Oracle</td>
<td>mongod</td>
</tr>
<tr>
<td>mysql/sqlplus</td>
<td>mongo</td>
</tr>
</tbody></table>

需要注意的是：
1. 文档中的键/值对是有序的。
文档中的值不仅可以是在双引号里面的字符串，还可以是其他几种数据类型（甚至可以是整个嵌入的文档)。
2. MongoDB区分类型和大小写。
3. MongoDB的文档不能有重复的键。
4. 文档的键是字符串。除了少数例外情况，键可以使用任意UTF-8字符。

## 集合
集合就是 MongoDB 文档组，类似于 RDBMS （关系数据库管理系统：Relational Database Management System)中的表格。
集合存在于数据库中，集合没有固定的结构，这意味着你在对集合可以插入不同格式和类型的数据，但通常情况下我们插入集合的数据都会有一定的关联性。
比如，我们可以将以下不同数据结构的文档插入到集合中：


```python
{"site":"www.baidu.com"}
{"site":"www.google.com","name":"Google"}
{"site":"www.runoob.com","name":"菜鸟教程","num":5}
```




    {'name': '菜鸟教程', 'num': 5, 'site': 'www.runoob.com'}



## 元数据
数据库的信息是存储在集合中。它们使用了系统的命名空间：

<table>

<tbody>
<tr>
<th>集合命名空间</th>
<th>描述</th>
</tr>
<tr>
<td>dbname.system.namespaces</td>
<td>列出所有名字空间。</td>
</tr>
<tr>
<td>dbname.system.indexes</td>
<td>列出所有索引。</td>
</tr>
<tr>
<td>dbname.system.profile</td>
<td>包含数据库概要(profile)信息。</td>
</tr>
<tr>
<td>dbname.system.users</td>
<td>列出所有可访问数据库的用户。</td>
</tr>
<tr>
<td>dbname.local.sources</td>
<td>包含复制对端（slave）的服务器信息和状态。</td>
</tr>
</tbody>
</table>


# MongoDB 数据类型
下表为MongoDB中常用的几种数据类型。

<table>
<tbody><tr>
<th>数据类型</th>
<th>描述</th>
</tr>
<tr><td>String</td><td>字符串。存储数据常用的数据类型。在 MongoDB 中，UTF-8 编码的字符串才是合法的。   </td></tr>
<tr><td>Integer</td><td>整型数值。用于存储数值。根据你所采用的服务器，可分为 32 位或 64 位。  </td></tr>
<tr><td>Boolean</td><td>布尔值。用于存储布尔值（真/假）。  </td></tr>
<tr><td>Double</td><td>双精度浮点值。用于存储浮点值。  </td></tr>
<tr><td>Min/Max keys</td><td>将一个值与 BSON（二进制的 JSON）元素的最低值和最高值相对比。  </td></tr>
<tr><td>Arrays</td><td>用于将数组或列表或多个值存储为一个键。  </td></tr>
<tr><td>Timestamp</td><td>时间戳。记录文档修改或添加的具体时间。  </td></tr>
<tr><td>Object</td><td>用于内嵌文档。  </td></tr>
<tr><td>Null</td><td>用于创建空值。  </td></tr>
<tr><td>Symbol</td><td>符号。该数据类型基本上等同于字符串类型，但不同的是，它一般用于采用特殊符号类型的语言。</td></tr>
<tr><td>Date</td><td>日期时间。用 UNIX 时间格式来存储当前日期或时间。你可以指定自己的日期时间：创建 Date 对象，传入年月日信息。  </td></tr>
<tr><td>Object ID</td><td>对象 ID。用于创建文档的 ID。  </td></tr>
<tr><td>Binary Data</td><td>二进制数据。用于存储二进制数据。</td></tr>
<tr><td>Code</td><td>代码类型。用于在文档中存储 JavaScript 代码。</td></tr>
<tr><td>Regular expression</td><td>正则表达式类型。用于存储正则表达式。</td></tr>
</tbody>
</table>


# 参考 http://www.runoob.com/mongodb/mongodb-databases-documents-collections.html


```python

```
