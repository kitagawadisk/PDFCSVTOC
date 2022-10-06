# 「ロボットプログラミングROS2入門」（科学情報出版）

<img src="https://images-na.ssl-images-amazon.com/images/I/41bqnfH8P7L._SX373_BO1,204,203,200_.jpg" alt="エビフライトライアングル" title="サンプル">

## お知らせ
2020.10.22 Windows10にDockerをインストールためのガイドを書きました (https://note.com/hiroyuki_okada/n/n0f25f0d94466?fbclid=IwAR1aq2TMPXSlgpShlNo6NRerrbd3bVbL9KMyOfg437AArm_2g7FgNR7FsTY)

2020.9.16 販売開始されました

2020.9.16 出版予定

2020.9.1  予約開始
[アマゾン](https://amazon.co.jp/dp/4904774906)

2020.4.19 まもなく脱稿

## リポジトリ一覧
### Docker Hub
*  本書を通して使うDockerイメージ
[https://hub.docker.com/repository/docker/okdhryk/ros2docker](https://hub.docker.com/repository/docker/okdhryk/ros2docker)

*  4章の演習で使うDockerイメージ
[https://hub.docker.com/repository/docker/okdhryk/py3](https://hub.docker.com/repository/docker/okdhryk/py3)


## 正誤表（第一刷）
| **場所** |**誤** |**正** | **訂正日**|
| ------ | ------ |------|------|
| p.74| ros2 rviz2 rviz2 |ros2 **run** rviz2 rviz2|2020/9/1|
| p.112,p.113| ros2 topic **info** /turtle1/cmd_vel |ros2 topic **echo** /turtle1/cmd_vel|2020/9/1|
| p.116 6行目 |オプションとして **-rate** 1 を追加します。|オプションとして **--rate** 1 を追加します。|2020/9/1|
|p.122|ros2 service call /spawn turtlesim/srv/Spawn “{x: 2,y: 2,theta: 0.2,name: ’ ‘}”|ros2 service call /spawn turtlesim/srv/Spawn “{x: 2,y: 2,theta: 0.2,name: ’‘}|2020/9/1|
|p.132|ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute {‘theta: -1.57’} **-feedback**|ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute {‘theta: -1.57’} **--feedback**|2020/9/1|
|p.152 図8-2, p.157 8-3-2, p,158 図8-4, p.164上から2行目, p.164 図8-6, p.167 8-5-2, p.168 図8-7|move = **my**_turtle_pkg.moveTurtle:main ,<br>spawn = **my**_turtle_pkg.spawnTurtle:main,<br>bg_color = **my**_turtle_pkg.bg_paramTurtle:main,<br>rotate = **my**_turtle_pkg.rotateTurtle:main,|move = **your**_turtle_pkg.moveTurtle:main,<br>spawn = **your**_turtle_pkg.spawnTurtle:main,<br>bg_color = **your**_turtle_pkg.bg_paramTurtle:main,<br>rotate = **your**_turtle_pkg.rotateTurtle:main,|2020/9/1|
|p.177|export TURTLEBOT3_MODEL = waffle|export TURTLEBOT3_MODEL=waffle|2020/9/1|


Copyright [Hiroyuki Okada] The Apache Software Foundation
This product includes software developed at
The Apache Software Foundation (http://www.apache.org/).

# PDFCSVTOC
