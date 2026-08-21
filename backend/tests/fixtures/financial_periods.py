from datetime import date
from decimal import Decimal

NORMAL_PERIOD = {
    "ticker": "DEMO",
    "period_end": date(2025, 12, 31),
    "revenue": Decimal(1000),
    "net_income": Decimal(100),
    "beginning_assets": Decimal(400),
    "ending_assets": Decimal(600),
    "beginning_equity": Decimal(200),
    "ending_equity": Decimal(300),
}

EXPECTED_NORMAL_RESULT = {
    "average_assets": Decimal(500),
    "average_equity": Decimal(250),
    "net_profit_margin": Decimal("0.1"),
    "asset_turnover": Decimal(2),
    "equity_multiplier": Decimal(2),
    "roe": Decimal("0.4"),
}

ZERO_REVENUE_PERIOD = {
    **NORMAL_PERIOD,
    "revenue": Decimal(0),
}

ZERO_AVERAGE_ASSETS_PERIOD = {
    **NORMAL_PERIOD,
    "beginning_assets": Decimal(0),
    "ending_assets": Decimal(0),
}

ZERO_AVERAGE_EQUITY_PERIOD = {
    **NORMAL_PERIOD,
    "beginning_equity": Decimal(0),
    "ending_equity": Decimal(0),
}

NEGATIVE_EQUITY_PERIOD = {
    **NORMAL_PERIOD,
    "beginning_equity": Decimal(-200),
    "ending_equity": Decimal(-300),
}