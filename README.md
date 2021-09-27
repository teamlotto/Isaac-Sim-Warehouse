# Isaac-Sim-Warehouse
Develop for Controlling Robot in the Warehouse

# Functions

## 1. Move Goods Zone
![move_zone3](https://user-images.githubusercontent.com/69780812/134845081-dd31feb5-75cc-4130-b854-2db6fc269621.gif)

## 2. Recognization
### Recognizing Goods 
![recognition](https://user-images.githubusercontent.com/69780812/134845295-2a4f372a-e6f3-4f5b-bfd5-1767c1931d67.gif)

## 3. Load Goods
- ***Priority Product : Red, Green, Blue Product***
- ***Priority Direction : Closer Side to Load Zone***
### Turning to Target Goods (Convert to Left or Right Cam)
![turtt1](https://user-images.githubusercontent.com/69780812/134846452-e8fcd74e-0a13-443b-b873-cfc0ee38cfff.gif)
### Matching To Target Goods's Rolltainer and Move to it
![move_target_](https://user-images.githubusercontent.com/69780812/134846608-22bc5383-d1d1-4e30-8812-1feca285aca7.gif)
### Pose Setting, Turning to Target Goods (Convert to Front Cam) 
![tttt2](https://user-images.githubusercontent.com/69780812/134846500-49703114-d4ac-42e7-9a03-05f3b924607d.gif)
### Move to Target Goods as traking target Rolltainer with CAM (Darknet_ROS)
![asdfasdf111!!](https://user-images.githubusercontent.com/69780812/134847356-76aa92a9-a739-43ac-9f66-f7d568c70079.gif)

### Entering to Rolltainer with Lidar (Pose Fine Tuning)
![lidar](https://user-images.githubusercontent.com/69780812/134851911-3aa10103-282d-4709-86fa-9fa4ad6746fe.gif)

### Lifting Up Target Goods
![lifting](https://user-images.githubusercontent.com/69780812/134853100-e15a0f5f-9b3f-42b4-a2fb-6141181fca87.gif)


### Move to Target's Load Zone and Lifting Down, Escaping Target Goods
![redzone](https://user-images.githubusercontent.com/69780812/134853591-55e8d022-5323-425a-b5f0-a0c2589832df.gif)
![escape](https://user-images.githubusercontent.com/69780812/134853618-a9da8883-1a18-4919-8fbc-65d9f807a78e.gif)

## 4. Move Wait Zone
![waitzone](https://user-images.githubusercontent.com/69780812/134853881-ab8d8799-3db4-43f3-bfe5-6b50619f199e.gif)

# Test
```shell
sh start_project_container.sh
```
- start docker container
```shell
roslaucnh lotti_nav move_base.launch
roslaucnh lotti_nav rviz.launch
roslaucnh lotti_nav lotti_operate.launch
```
- launch 3 files (Warning : Start Order)
