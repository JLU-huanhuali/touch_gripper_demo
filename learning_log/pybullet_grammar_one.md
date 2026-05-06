# PyBullet Basic Grammar 
## Day one 

## 1. `p.setAdditionalSearchPath(pybullet_data.getDataPath())`

>加载模型时，除了当前文件夹，也去 PyBullet 自带资源库里找。

## 2. `p.setGravity(x, y, z)`

>设置仿真世界中的重力方向和大小。

## 3. `plane_id = p.loadURDF("plane.urdf")`

### `loadURDF` 补充解释

|  | |
|---|---|
| URDF | Unified Robot Description Format，统一机器人描述格式 |
| 本质 | **XML 格式的模型说明文件** |
| plane.urdf | **地面模型文件** |
## 4.仿真步进 + 时间同步
`p.stepSimulation()`

`time.sleep(1.0/240.0)`
>执行一次前向动力学仿真；默认时间步长是 1/240 秒