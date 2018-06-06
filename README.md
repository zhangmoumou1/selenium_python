# python-selenium(ui自动化)
#### 一、实现步骤参考
1、理解框架各个模块和调用流程（如不理解可参考readme文件下的xmind流程图）<br>
<br>
2、以页面为单位编写自动化测试用例<br>
<br>
3、封装公共模块（webdriver定位方法、截图、日志、登录、数据读写等）<br>
<br>
4、可以先单独写脚本对元素定位和操作进行调试，成功后再引入框架<br>
<br>
5、使用PageObject模式来编写测试脚本，实现页面操作、定位、用例、测试数据的分离，提高代码维护性<br>
<br>
6、最后可通过Jenkins+tomcat+git持续集成平台，实现脚本的维护、构建控制并输出测试报告<br>

#### 二、框架目录讲解<br>
![no view](https://github.com/zhangmoumou1/selenium-python/blob/master/readme/%E6%A1%86%E6%9E%B6%E7%9B%AE%E5%BD%95.jpg)<br>
1、config文件夹：config.ini 配置项目的路径；globalparam.py 封装所有需要获取或者保存的路径，如日志、截图、测试报告、上传文件、测试数据;<br>
<br>
2、data文件夹：dataread.py读取excel数据，把字典存储在列表中；datas.xlsx存储测试数据;<br>
<br>
3、public文件夹：公共方法的封装，如webdriver操作、logging、读取excel数据、截图、日志、读取配置文件、发送报告;<br>
<br>
4、report文件夹：用例失败截图、用例成功截图、存放日志和测试报告;<br>
<br>
![no view](https://github.com/zhangmoumou1/selenium-python/blob/master/readme/%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A.jpg)<br>
![no view](https://github.com/zhangmoumou1/selenium-python/blob/master/readme/%E6%97%A5%E5%BF%97.jpg)<br>
<br>
5、test_case文件夹：page_obj下主要写元素定位和动作流程；*sta.py根据page页面写测试用例;<br>
<br>
6、up_files文件夹：根据autoit工具保存上传文件.exe文件;<br>
<br>
7、run_ai_test.py：测试用例执行文件并生成测试报告。<br>
