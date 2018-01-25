import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

# Gazebo
# ----------------------------------------

# Catvehicle envs
register(
    id='GazeboCatvehicleLidar-v0',
    entry_point='gym_vehicle.envs.catvehicle:GazeboCatvehicleLidarEnv',
    # More arguments here
)
