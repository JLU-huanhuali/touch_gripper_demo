# PyBullet Basic Grammar 
## Day two
### PyBullet 里物体的位置通常指物体中心点的位置
### ctrl+鼠标左键转视角
## visual shape
    p.createVisualShape(...)
    >创建视觉几何体
    shapeType   
    rgbaColor=[R,G,B,A]  0~1, A:alpha 透明度 1为不透明

#### GEOM_X
>GEOM: geometry

    CYLINDER  #圆柱
## collision shape
## `p.createMultiBody()`
>真正创建物体

    baseMass
    baseCollisionShapeIndex  指定碰撞形状
    baseVisualShapeIndex
    basePosition

## `from pathlib import Path`
>Path: Python 用来处理文件路径 / 文件夹路径

>pathlib:面向对象的文件系统路径工具

### 创建路径对象
    log_dir=Path("results/logs")

### 创建文件夹
    log_dir.mkdir(parents=True,exist_ok=True)

### `orientation = [x, y, z, w]`
>**四元数 quaternion**
>** 用来表示物体姿态 / 旋转**

### `round(x,num)`
>保留num位小数+四舍五入