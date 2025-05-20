
from launch.actions import DeclareLaunchArgument
from launch.conditions import LaunchConfigurationEquals

arg_name = DeclareLaunchArgument('name', default_value='ur5e',)
arg_calibration_type = DeclareLaunchArgument('calibration_type', choices=["eye_in_hand", "eye_on_base"],
                                             description="Type of the calibration", default_value='eye_in_hand')
arg_tracking_base_frame = DeclareLaunchArgument('tracking_base_frame', default_value='FTKCamera')
arg_tracking_marker_frame = DeclareLaunchArgument('tracking_marker_frame', default_value='RobotHand')
arg_robot_base_frame = DeclareLaunchArgument('robot_base_frame', default_value='base')
arg_robot_effector_frame = DeclareLaunchArgument('robot_effector_frame', default_value='tool0')

is_eye_in_hand = LaunchConfigurationEquals('calibration_type', 'eye_in_hand')