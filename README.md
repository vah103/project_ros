Mặc định trong RViz không có sẵn display type cho IMU nên chạy lệnh sau để cài gói hỗ trợ: sudo apt install ros-noetic-rviz-imu-plugin ( Anh nhớ có cài cái này nhé )
Anh chạy file gazebo.launch là bật cả gazebo và rviz ạ
Em có file node python điều khiển cả dành cho xe chạy và điều khiển tay máy : rosrun elon_musk_car keyboard_cmd_vel.py ( giới hạn tay máy cho trục 1 và trục 2 là từ -1.5 đến 1 anh nhé )
