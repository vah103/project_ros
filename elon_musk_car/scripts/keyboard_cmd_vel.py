#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

def main():
    rospy.init_node('keyboard_cmd_vel_node')
    pub_cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    pub_truc1 = rospy.Publisher('/truc1_jt_position_controller/command', Float64, queue_size=10)
    pub_truc2 = rospy.Publisher('/truc2_jt_position_controller/command', Float64, queue_size=10)

    print("Nhập lệnh điều khiển robot:")
    print("w: tiến | s: lùi | a: quay trái | d: quay phải | x: dừng | q: thoát")
    print("+: tăng tốc độ | -: giảm tốc độ")
    print("u: nhập vị trí cho tay máy")

    current_linear = 0.5  
    current_angular = 0.0
    current_truc1 = 0.0  
    current_truc2 = 0.0 

    while not rospy.is_shutdown():
        key = input(">> Nhập lệnh (w/s/a/d/x/q/+/-/u): ")

        if key == 'w':
            current_linear = 0.5
            current_angular = 0.0  
        elif key == 's':
            current_linear = -0.5
            current_angular = 0.0  
        elif key == 'a':
            current_angular = 1.0
        elif key == 'd':
            current_angular = -1.0
        elif key == 'x':
            current_linear = 0.0
            current_angular = 0.0
        elif key == 'q':
            print("Thoát node.")
            break
        elif key == '+':
            current_linear += 0.1
            if current_linear > 2.0: 
                current_linear = 2.0
            print(f"Tốc độ tiến/lùi hiện tại: {current_linear} m/s")
        elif key == '-':
            current_linear -= 0.1
            if current_linear < 0.0: 
                current_linear = 0.0
            print(f"Tốc độ tiến/lùi hiện tại: {current_linear} m/s")
        
        
        elif key == 'u':  
            try:
                current_truc1, current_truc2 = map(float, input("Nhập vị trí tay máy (trục 1, trục 2) cách nhau bằng dấu cách: ").split())
                print(f"Vị trí tay máy 1 (truc1): {current_truc1}, Vị trí tay máy 2 (truc2): {current_truc2}")
            except ValueError:
                print("Lỗi nhập liệu! Vui lòng nhập hai giá trị số cách nhau bằng dấu cách.")
                continue
        else:
            print("Lệnh không hợp lệ.")
            continue

        twist = Twist()
        twist.linear.x = current_linear
        twist.angular.z = current_angular
        pub_cmd_vel.publish(twist)

        pub_truc1.publish(current_truc1)
        pub_truc2.publish(current_truc2)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
