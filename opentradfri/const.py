ROOT_DEVICES = "15001"
ROOT_GROUPS = "15004"
ROOT_MOODS = "15005"
PATH_GATEWAY_INFO = ["15011", "15012"]

ATTR_APPLICATION_TYPE = "5750"
ATTR_DEVICE_INFO = "3"
ATTR_NAME = "9001"
ATTR_CREATED_AT = "9002"
ATTR_ID = "9003"
ATTR_REACHABLE_STATE = "9019"
ATTR_LAST_SEEN = "9020"
ATTR_LIGHT_CONTROL = "3311"  # array

ATTR_NTP = "9023"
ATTR_FIRMWARE_VERSION = "9029"
ATTR_CURRENT_TIME_UNIX = "9059"
ATTR_CURRENT_TIME_ISO8601 = "9060"
ATTR_FIRST_SETUP = "9069"  # ??? unix epoch value when gateway first setup
ATTR_GATEWAY_ID = "9081"  # ??? id of the gateway

ATTR_LIGHT_STATE = "5850"  # 0 / 1
ATTR_LIGHT_DIMMER = "5851"  # Dimmer, not following spec: 0..255
ATTR_LIGHT_COLOR = "5706"  # string representing a value in some color space
ATTR_LIGHT_COLOR_X = "5709"
ATTR_LIGHT_COLOR_Y = "5710"
