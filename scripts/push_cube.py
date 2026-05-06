import time
import csv
import pybullet as p
import pybullet_data
from pathlib import Path
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
p.resetDebugVisualizerCamera(
   cameraDistance=1.2,
   cameraYaw=45,
   cameraPitch=-35,
   cameraTargetPosition=[0.65,0.0,0.0]
)

plane_id=p.loadURDF("plane.urdf")

cube_size=0.06
cube_half=cube_size/2
cube_collision=p.createCollisionShape(
    shapeType=p.GEOM_BOX,
    halfExtents=[cube_half,cube_half,cube_half]
)
cube_visual=p.createVisualShape(
    shapeType=p.GEOM_BOX,
    halfExtents=[cube_half,cube_half,cube_half],
    rgbaColor=[0,0,1,0.5]
)
cube_id=p.createMultiBody(
    baseMass=0.1,
    baseCollisionShapeIndex=cube_collision,
    baseVisualShapeIndex=cube_visual,
    basePosition=[0.55,0.0,cube_half]
)


pusher_size=[0.04,0.10,0.06]
pusher_half=[
    pusher_size[0]/2,
    pusher_size[1]/2,
    pusher_size[2]/2
]
pusher_collision=p.createCollisionShape(
    shapeType=p.GEOM_BOX,
    halfExtents=pusher_half
)
pusher_visual=p.createVisualShape(
    shapeType=p.GEOM_BOX,
    halfExtents=pusher_half,
    rgbaColor=[0,1,0,1]
)
pusher_id=p.createMultiBody(
    baseMass=0.2,
    baseCollisionShapeIndex=pusher_collision,
    baseVisualShapeIndex=pusher_visual,
    basePosition=[0.42,0.0,pusher_half[2]]
)


target_radius=0.04
target_height=0.0002
target_position = [0.75, 0.0, cube_half]
target_visual=p.createVisualShape(
    shapeType=p.GEOM_CYLINDER,
    radius=target_radius,
    length=target_height,
    rgbaColor=[1,0,0,0.1]
)
target_id=p.createMultiBody(
    baseMass=0,
    baseCollisionShapeIndex=-1,
    baseVisualShapeIndex=target_visual,
    basePosition=[0.75,0.0,target_height/2]
)



log_dir=Path("results/logs")
log_dir.mkdir(parents=True, exist_ok=True)
log_path=log_dir/"push_log.csv"
f=open(log_path,"w",newline="",encoding="utf-8")
writer=csv.writer(f)
writer.writerow([
    "step",
    "cube_x",
    "cube_y",
    "cube_z",
    "target_distance",
    "reward",
    "success"
])


for step in range(10000):
    p.resetBaseVelocity(pusher_id,linearVelocity=[0.4,0,0])
    p.stepSimulation()
    cube_pos,cube_orn=p.getBasePositionAndOrientation(cube_id)
    cube_x=cube_pos[0]
    cube_y=cube_pos[1]
    cube_z=cube_pos[2]
    dx=cube_x-target_position[0]
    dy=cube_y-target_position[1]
    dz=cube_z-target_position[2]
    target_distance=(dx**2+dy**2+dz**2)**0.5
    reward=-target_distance
    success_radius=0.055
    success=target_distance<success_radius

    if success:
        reward+=1
        print("已成功")
        break

    writer.writerow([
        step,
        cube_x,     
        cube_y,     
        cube_z, 
        target_distance,
        reward,
        success]
    )
    if step%50==0:
        print(
            "step:",step,
            "cube_x:",round(cube_x, 4),
            "distance:",round(target_distance, 4),
            "success:",success
        )
   
    time.sleep(1.0/240.0)
f.close()
print("log saved to:",log_path)
p.disconnect()


