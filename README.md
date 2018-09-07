# reptile
reptile


# 关于python2和python3的编码区别
python2:
    unicode字符串类型:  unicode
    非unicode字符串类型:    str
    python2 中的with open 没有encoding这个属性,如果非要用就导入codecs这个包
    普通写的时候unicode要转换成str的才能写,除非使用codecs

python3:
    unicode字符串类型:  str
    非unicode字符串类型:    bytes
    unicode_str = u'你好'
    type(unicode_str)   打印的是<class 'str'>
    utf8_str = unicode_str.encode('utf-8')
    转成utf8类型 但是python3中非unicode类型都是bytes类型 所以type(utf8_str) 打印为<class 'bytes'>
    with open('text.txt, 'w', encoding='gbk') as f:
        f.write(unicode_str)
        # f.write(unicode_str.encode('gbk')
    这里的写的是unicode_str, unicode_str 为 unicode类型的, 文件格式就是gbk类型  
    上面的encoding是文件格式的类型  下面的encode是文本是什么类型

unicode:
    可以看做一个中间人,可以通过 gbk -> unicode -> utf-8 
    gbk,utf-8这类都可以通过转成unicode类型来转换成别的类型

python解析器编码
    import sys
    sys.getdefaultencoding()    查看编译器的编码
    python2 ascii
    python3 utf-8
    一般都用utf-8,可以改变默认编码
    reload(sys)     重载
    sys.setdefaultencoding('utf-8')     设置
    import sys      重新导入就行了
    一般用python2写的时候,只要在py文件头部写上  #encoding:utf-8就行了
    
