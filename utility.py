# constants
DARKFLOW_PATH = '/var/www/html/claimit_backend/darkflow/'
MODEL_CFG_PATH = '/var/www/html/claimit_backend/darkflow/cfg/yolov2-tiny-voc-7c.cfg'
PROTOBUF_PATH = '/var/www/html/claimit_backend/darkflow/built_graph/tiny-yolo-voc-7c.pb'
META_FILE_PATH = '/var/www/html/claimit_backend/darkflow/built_graph/tiny-yolo-voc-7c.meta'
DEFAULT_THRESHOLD = 0.09
LABEL = 'label'
LABEL_X = 'x'
LABEL_Y = 'y'
LABEL_TOP_LEFT = 'topleft'
LABEL_BOTTOM_RIGHT = 'bottomright'
BOX_OFFSET = 10
DOMAIN_NAME = '' # YOUR HTTPS DOMAIN NAME HERE
WEB_DIR_PATH = '/var/www/html'
IMG_UPLOADS_DIRECTORY = '/var/www/html/claimit_backend/darkflow/uploads/'
IMG_UPLOADS_DISPLAY_URL = DOMAIN_NAME + '/claimit_backend/darkflow/uploads/'
DEFAULT_FILE_TYPE = '.png'