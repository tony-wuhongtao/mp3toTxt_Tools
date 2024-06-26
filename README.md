# 音频（视频）转写txt工具集
参考相关文档，Tony自制工具集
mp4文件，直接修改后缀为mp3，需要转写的音频直接放在同一个目录下即可进行操作
含多线程版本转写为txt输出
含txt写入excel文件工具
具体用法见文件说明

# 文件说明

## main.py -- 调用讯飞语音转写API
### 用法： python main.py 待转写音频文件所在目录
### 输出： 待转写音频文件所在目录下的txt文件对应音频文件名
### 说明： 英文文件名，不含有特殊字符

## mThreads.py -- 多线程调用讯飞语音转写API版本
### 用法：python mThreads.py 待转写音频文件所在目录
### 说明： 程序内写死4个线程 max_threads = 4，可根据需要修改

## buildcsv.py -- 生成txt文件转写结果写入excel文件
### 用法：python buildcsv.py ，运行后会提示输入含有txt文件的目录
### 输出： 生成一个output.csv，表头默认为'num', 'name', 'grade', 'sub', 'teacher', 'school', 'script'，信息来自txt文件名，script为txt文件内容
### 说明： 程序内写死表头，可根据需要修改，txt文件名需要用_分割,具体分割原理见代码。不直接生成excel文件，主要是考虑到长文本内容，excel文件打开会自动截断，而csv文件不会。
```
同上一堂课_2022春季_小学重难点名师优讲_五年级语文08_《给写作插上想象的翅膀》_朱杰_史家教育集团_20220708-new_crf28.mp3

0          1       2                3                4                  5   6            7
```
## csv2excel.py -- 将csv文件转写结果写入excel文件
### 用法：python csv2excel.py ，运行后会提示输入含有csv文件的目录
### 输出： 生成一个同名的excel文件



#### 注意事项：
>1. 讯飞secret_id和secret_key需要自行申请，并修改代码中对应位置,代码中的key已经被修改，不可直接用，使用时请修改