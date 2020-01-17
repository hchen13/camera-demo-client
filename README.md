# camera-demo-client
Security camera VIP recognition demo with TechForce (client)

# 环境配置

配置好Python 3环境后，在该环境下运行命令`pip install -r requirements.txt`安装必要的package。

# 运行

运行命令：

``python app.py``

# 参数说明

## 1. 实时显示

在文件[app.py](/app.py)中修改变量`feed`的值来控制是否在屏幕上实时显示。

## 2. 服务器地址

在文件[app.py](/app.py)中配置变量`host`来指向正确服务器地址。

## 3. 运动检测

在文件[app.py](/app.py)中配置构造方法`MotionDetector`的参数`sensitivity`来控制运动检测的灵敏度。

~~~python
...

if __name__ == '__main__':
    feed = True
    host = '47.108.136.249'

    con = Connector(host)
    motion = MotionDetector(sensitivity=.5)

    vs = VideoStream().start()
    sleep(2.)

...
~~~