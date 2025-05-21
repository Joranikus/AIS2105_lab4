# AIS2105_lab4

```bash
v4l2-ctl --list-devices
```

## Terminal 1 (Kamera)

```bash
source ~/lab4_ws/install/setup.bash
ros2 run usb_cam usb_cam_node_exe --ros-args -p video_device:=/dev/video4
```

## Terminal 2 (Filter)
```bash
source ~/lab4_ws/install/setup.bash
ros2 launch camera_pipeline pipeline.launch.py
```

## Terminal 3 (rqt)
```bash
source ~/lab4_ws/install/setup.bash
rqt
```
