# hello-world
my first git project

这个工程用来控制树莓派作为声音控制系统，当接收到udp消息后，根据消息内容播放对应的音频。
这里播放使用的是aplay，他能够实现立刻播放，没有延迟。
同时，为了能够多通道同时播放，我用python调用命令行工具，在多任务中调用aplay，通过不同的通道，播放不同的音频文件。

这里是我查看了我的音频设备信息
pi@raspberrypi:~ $aplay -l
card 0: Device [USB Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 0/1
  Subdevice #0: subdevice #0
card 1: ALSA [bcm2835 ALSA], device 0: bcm2835 ALSA [bcm2835 ALSA]
  Subdevices: 8/8
  Subdevice #0: subdevice #0
  Subdevice #1: subdevice #1
  Subdevice #2: subdevice #2
  Subdevice #3: subdevice #3
  Subdevice #4: subdevice #4
  Subdevice #5: subdevice #5
  Subdevice #6: subdevice #6
  Subdevice #7: subdevice #7
card 1: ALSA [bcm2835 ALSA], device 1: bcm2835 ALSA [bcm2835 IEC958/HDMI]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
  
  配置方法：
  新环境布置步骤及相关命令：
一：ssh
sudo raspi-config->5->ps2


二：aplay
sudo apt-get install alsa-utils

三：布置工程文件：

1.下载工程
sudo wget https://github.com/biabianm/hello-world/archive/master.zip 

2.解压
sudo unzip master.zip

3.找到目录
cd hello-world-master/raspberry

4.移动到home目录
sudo mv * /home

5.回到home
cd /home

6.移除多余的文件
sudo rm -R hello-world-master master.zip

7.拷贝开机启动配置文件
sudo cp -f /home/rc.local /etc

8.查看进程
ps aux|grep python3

9.查看ip地址
ifconfig

最后根据实际需要修改main.py里面的创建UDP的ip地址

