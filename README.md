# houchangxi.github.ai

## Andrew Hou's Space
# Numpy 学习
重点：

1、Python切记 注意事项
  
  a, 如果b的值设成a的初始化值，可以用 a = b.copy() 对a进行赋值。
  
  b, 浅层复制可以使用  a = b.View()  这种复制用 print(a is b)进行判断为Fasle 说明2个变量!=，并且用shape查看也为不同变量。但是若a中的数据变化则b中数   据也随之变化，故不建议使用这种浅层复制。
  
  注：赋值变量不用 "=" 用 "copy"。 “=” 如 a=b a、b指针相同，修改其中一个都会改变。 

2、常用Numpy 命令
   
   a, numpy.argmax     最大值索引
   
   b, numpy.tile       numpy.tile(data,(3,5)) 赋值data数据成为[3,5]的矩阵
   
   c, numpy.argsort    排序返回索引 （默认从小到大）