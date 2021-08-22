#!/usr/bin/python3
import rospy
import rosbag
import rospkg


rp = rospkg.RosPack()
package_path = rp.get_path('gnss_navigation')

relative_path = '/bag_data/data.bag'

final_path = package_path+relative_path
# from std_msgs.msg import Int32, String

# bag = rosbag.Bag('test.bag', 'w')

# try:
#     s = String()
#     s.data = 'foo'

#     i = Int32()
#     i.data = 42

#     bag.write('chatter', s)
#     bag.write('numbers', i)
# finally:
#     bag.close()
#print(package_path)
bag = rosbag.Bag(final_path)
msg1=None
msg2=None

for topic, msg, t in bag.read_messages(topics=['/sensors/gnss/odom']):
    msg1=msg

for topic, msg, t in bag.read_messages(topics=['/sensors/odom']):
    msg2=msg

print(msg1)
print(msg2)
bag.close()