# instruction type length in bytes
INSTRUCTION_TYPE_LENGTH = 1

# special VALUES
ALREADY_EXISTS = -1
OK = 1
NULL_ADDRESS = 0

# Index config
DEFAULT_INDEX_FILENAME = "index.bin"
DEFAULT_DATA_FILENAME = "data.bin"

# record config
VOLTAGE_ID = 0
CURRENT_ID = 1
RECORD_SIZE = 16 # two double precision floating point numbers (8*2)
KEY_SIZE = 4 # one 32-bit integer
PAIR_SIZE = 20 # pair of two above
DATA_BLOCKING_FACTOR = 10