API_KEY = ''
API_SECRET = ''


SYMBOL = 'ETHUSDT'
LEVERAGE = 10

# Entorno
PAPER_MODE = False   # Simulación: no llama endpoints privados ni coloca órdenes reales
USE_TESTNET = False # Para operar en testnet cuando PAPER_MODE=False y tengas claves de testnet

# Grid settings
GRID_RANGE_MIN = 0.0033   # 6%
GRID_RANGE_MAX = 0.0160   # 15%
MIN_GRID_SPACING = 0.0011   # 0.3%
MAX_GRID_SPACING = 0.0039  # 0.75%
ORDER_USDT_SIZE = 10    # Capital por orden (se multiplica por leverage implícitamente)
REBALANCE_SECONDS = 180

# Take profit
MIN_PROFIT_THRESHOLD = 0.0027  # 0.30% target p
TP_OFFSET_LOW = (0.0001, 0.0002)   # 0.03% y 0.03%
TP_OFFSET_MID = (0.00015, 0.0003)
TP_OFFSET_HIGH = (0.0002, 0.0003)

STOP_LOSS_PERCENTAGE = 0.039

MAKER_FEE_RATE = 0.0002

SAFE_SPREAD = 0.001  # 0.1%: spread mínimo para que la orden de compra realmente mejore el promedio de entrada

STATE_FILE = "state.json"
