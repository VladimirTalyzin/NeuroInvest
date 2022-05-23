from tinkoff.investments import CandleResolution
from enum import Enum

# interval between trading points in seconds
scanInterval = 5 * 60
tinkoffScanInterval = CandleResolution.MIN_5

# scan period from current time in seconds
scanPeriod = 3 * 24 * 60 * 60

# prediction period for training
predictPeriod = 1 * 24 * 60 * 60

# historical scan period for training
# 100 days for beginning
trainingPeriod = 100 * 24 * 60 * 60

# intervals for calculating predictions
predictionIntervals = [1 * 60 * 60, 2 * 60 * 60, 4 * 60 * 60, 8 * 60 * 60]

# TOKENS

# Tinkoff API
tinkoffAPIToken = "t.CaO41bzhmufd8Riay6GGS-jZ9xVwoQ_A23zFOqt_BEamTO6ZMc7gtOtFYpur4l0sEhxwnm65WU79Caf24Mib7w"

# TTinkoff trading pair data
class TinkoffTrade(Enum):
    APPLE       = {"name": "APPLE INC/USD",         "figi": "BBG000B9XRY4"},
    GAZPROM_OIL = {"name": "GAZPROM NEFT PJSC/RUR", "figi": "BBG004S684M6"},