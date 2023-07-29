import sys

from tello_msgs.srv import TelloAction
import rclpy
from rclpy.node import Node


class TestClient(Node):

    def __init__(self):
        super().__init__('test_client')
        self.cli = self.create_client(TelloAction, '/drone1/tello_action')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = TelloAction.Request()

    def send_request(self, cmd):
        self.req.cmd = cmd
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        try:
            # Get the response from the server
            response = self.future.result()
            if response.rc == TelloAction.Response.OK:
                self.get_logger().info('Command sent successfully.')
            else:
                self.get_logger().info(f'Command failed. Response code: {response.rc}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')


def main(args=None):
    rclpy.init(args=args)

    minimal_client = TestClient()
    minimal_client.send_request("takeoff")
    # minimal_client.get_logger().info(
    #     'Result of test client: for %d' %
    #     (response))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()