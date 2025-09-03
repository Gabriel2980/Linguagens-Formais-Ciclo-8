import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray



class MyNode(Node):
  
  def __init__(self):
    super().__init__('markov_localization')
    self.get_logger().info('Inicializando o nó!')
    self.x = 0
    self.publisher_1 = self.create_publisher(Twist, "/cmd_vel", 10)

    self.robot_front_laser = None
    self.robot_side_laser = None
    self.subscription = self.create_subscription(LaserScan, '/scan', self.subscriber_callback, 10)

  def __del__(self):
    self.get_logger().info('Finalizando o nó!')
  
  def execute(self):
    self.get_logger().info('Executando o nó!')
    self.create_timer(1, self.timer_callback)
    rclpy.spin(self)
  
  def timer_callback(self):
    if self.x%10 < 5:
      twist_data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
      self.talker_publisher_1(twist_data)
    else:
      twist_data = [0.2, 0.0, 0.0, 0.0, 0.0, 0.0]
      self.talker_publisher_1(twist_data)

    self.x = self.x+1

    self.get_logger().info(f'Valor do laser lateral do robô: {self.robot_side_laser}')

    array_data = [1.0, 2.0, 3.0, 4.0]
    self.talker_publisher_2(array_data)
  
  

  def subscriber_callback(self, msg):
      self.robot_front_laser = msg.ranges[0]
      self.robot_side_laser = msg.ranges[90]

  def talker_publisher_1(self, data):
    msg = Twist()
    msg.linear.x = data[0]
    msg.linear.y = data[1]
    msg.linear.z = data[2]
    msg.angular.x = data[3]
    msg.angular.y = data[4]
    msg.angular.z = data[5]
    self.publisher_1.publish(msg)

  def talker_publisher_2(self, data):
    msg = Float64MultiArray()
    msg.data = data
    self.publisher_2.publish(msg)

def main(args=None):
  rclpy.init(args=args)
  my_node = MyNode()
  my_node.execute()

if __name__ == '__main__':
  main()