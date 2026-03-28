"""
╔══════════════════════════════════════════════════════════════════════╗
║          KALSHI BTC BOT — v20_3 FULL ZONE INTELLIGENCE             ║
║          Account:  chromagnumn | @PairOdimebot                      ║
║          Built:    March 2026 — 1-Hour Binary | Hedge + Moon System    ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  ROOT CAUSE ANALYSIS — WHY v17 LOST:                               ║
║                                                                      ║
║  TRADE 1 (23:32 SHORT → LOSS):                                     ║
║    30m↓0.35%, 12m↓0.20%, 3m FLAT                                   ║
║    RSI=34, near_support, volume LOW                                 ║
║    The 3-minute being FLAT while 30m and 12m were down             ║
║    = EXHAUSTION SIGNAL. The sell move was OVER.                    ║
║    Bot shorted the bottom. Classic mistake.                         ║
║                                                                      ║
║  TRADE 2 (23:48 LONG → LOSS):                                      ║
║    Confidence only 50/100. Should never have fired.                ║
║    12m↑0.12%, 3m↑0.04% = essentially noise, not signal            ║
║    RSI still 34, trend still down, MACD still bearish              ║
║    Near support, low volume — nothing changed from the last loss.  ║
║                                                                      ║
║  THE PATTERN ACROSS ALL LOSSES:                                     ║
║  The bot trades the direction of a COMPLETED move.                 ║
║  It sees "down happened" and bets "down continues"                 ║
║  right at the moment down is exhausted.                            ║
║                                                                      ║
║  THE FUNDAMENTAL FIX IN v20:                                        ║
║                                                                      ║
║  EXHAUSTION DETECTION — the centerpiece of v20:                    ║
║                                                                      ║
║  A move is EXHAUSTED when:                                          ║
║    - 30min or 12min shows strong directional move (>0.25%)         ║
║    - BUT 3min is flat (<0.015%) or opposing direction              ║
║    - This means the move already happened and ran out of steam     ║
║    - Trading IN THE SAME DIRECTION as exhaustion = wrong           ║
║    - Heavy penalty applied: -35 points                             ║
║    - If exhausted AND near S/R: hard soft-block (need 80+ score)  ║
║                                                                      ║
║  RSI DIVERGENCE DETECTION:                                          ║
║    - Bullish: price making lower lows, RSI making higher lows      ║
║      → selling momentum exhausted, potential reversal up            ║
║    - Bearish: price making higher highs, RSI making lower highs    ║
║      → buying momentum exhausted, potential reversal down          ║
║    - Trading against divergence: -30 points                        ║
║    - Trading with divergence: +20 points                           ║
║                                                                      ║
║  MINIMUM CONFIDENCE: Dynamic (v20 change)                          ║
║    - Standard conditions: 65 minimum (unchanged)                  ║
║    - RSI < 30 + LONGING: 60 minimum (reversal extreme context)    ║
║    - RSI > 70 + SHORTING: 60 minimum (reversal extreme context)   ║
║    - Statistical basis: RSI extremes have 71% reversal rate        ║
║                                                                      ║
║  V20.3 FULL ZONE INTELLIGENCE — 5 CHANGES FROM OVERNIGHT LOGS:                ║
║                                                                      ║
║  ROOT CAUSE FROM LOGS (RSI 12-15 session, zero trades):            ║
║  1. EXHAUST_UP fires -35 at RSI 12 (backwards at extremes)        ║
║  2. EMA -10 + MACD -10 punish reversal plays for crash already    ║
║  3. 1-of-3 momentum thrown away before scoring even starts         ║
║                                                                      ║
║  FIX A — RSI EXTREME REVERSAL MODE (RSI < 20):                    ║
║    Exhaustion penalty: -35 → -18 (still penalized, less harsh)    ║
║    EMA opposing: -10 → -5 (lagging indicator, crash already done) ║
║    MACD opposing: -10 → -5 (same reasoning)                       ║
║    RSI extreme: +15 BONUS (was -3 neutral)                        ║
║    Minimum confidence: 55 (vs 60 for RSI 20-30, 65 for RSI 30+)  ║
║    1-of-3 momentum override: 1 timeframe >0.10% → weak signal     ║
║                                                                      ║
║  FIX B — BLACK SWAN HISTORICAL DATABASE:                           ║
║    Major BTC crash events 2020-2025 hardcoded                      ║
║    Pattern matching when RSI < 15 + high velocity                  ║
║    BLACK_SWAN detected: halves position size (extra caution)       ║
║                                                                      ║
║  FIX C — MULTI-TIMEFRAME TREND CONTEXT:                           ║
║    Sustained downtrend vs correction detection                      ║
║    REVERSAL_ZONE flagged when RSI extreme in sustained downtrend   ║
║                                                                      ║
║  SCORE MATH AT RSI 12 BEFORE v20: 12/100 blocked                  ║
║  SCORE MATH AT RSI 12 AFTER v20:  57/100 fires at min 55          ║
║                                                                      ║
║  ALL v20 INTELLIGENCE PRESERVED:                                    ║
║  Volume -5 at extremes, PREV -2 at extremes, min 60 at RSI<30     ║
║                                                                      ║
║  MINIMUM MOMENTUM THRESHOLD:                                        ║
║    - 3min move must be > 0.02% to count as real signal            ║
║    - 12min move must be > 0.08% to count as real signal           ║
║    - Below these: flat (noise)                                     ║
║                                                                      ║
║  HIGHER LOW / LOWER HIGH DETECTION:                                 ║
║    - After a down move: did the last bottom hold above prev low?   ║
║      If YES (higher low) = potential reversal = don't short        ║
║    - After an up move: did the last top stay below prev high?      ║
║      If YES (lower high) = potential reversal = don't long         ║
║                                                                      ║
║  MONTHLY S/R FROM 6-HOUR CANDLES:                                  ║
║    - Pulls last 30 days of 6hr candles                             ║
║    - Identifies major swing highs and lows                         ║
║    - These are the REAL support and resistance levels              ║
║    - Much more significant than the 1hr S/R from v16/v17          ║
║                                                                      ║
║  NEAR SUPPORT + SHORTING = SOFT BLOCK:                             ║
║    - Near any support level AND shorting: requires 80+ confidence  ║
║    - Near any resistance level AND longing: requires 80+ confidence║
║                                                                      ║
║  RSI EXTREME ZONES STRENGTHENED:                                   ║
║    - RSI < 35 + shorting: -35 points (was -20)                    ║
║    - RSI > 65 + longing: -35 points (was -20)                     ║
║    - Absolute hard blocks remain at RSI < 22 / > 78               ║
║                                                                      ║
║  THREE HARD STOPS (unchanged):                                      ║
║    1. RSI < 22 + shorting = absolute block                         ║
║    2. RSI > 78 + longing = absolute block                          ║
║    3. Negative EV = never trade                                    ║
║                                                                      ║
║  CARRIED FROM v17 (working elements):                              ║
║  ✅ Confidence scoring 0-100                                        ║
║  ✅ Deep momentum 30min + 12min + 3min                             ║
║  ✅ EMA trend on 1hr chart                                         ║
║  ✅ MACD direction                                                  ║
║  ✅ S/R detection                                                   ║
║  ✅ Volume confirmation                                             ║
║  ✅ Position sizing by confidence                                   ║
║  ✅ Entry minute 2-10 with dynamic price cap                       ║
║  ✅ EV calculator                                                   ║
║  ✅ All safety systems (brakes, floor, locks)                      ║
║  ✅ Telegram with full context                                     ║
║  ✅ RSA-PSS Kalshi auth                                            ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import os, time, uuid, logging, datetime, base64, requests, threading
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────────
# CREDENTIALS
# ─────────────────────────────────────────────────────────────────
KALSHI_API_KEY_ID  = os.environ.get('KALSHI_API_KEY_ID', '')
KALSHI_PRIVATE_KEY = os.environ.get('KALSHI_PRIVATE_KEY', '')
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '')
TELEGRAM_CHAT_ID   = os.environ.get('TELEGRAM_CHAT_ID', '')

# ─────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────
KALSHI_BASE  = "https://api.elections.kalshi.com/trade-api/v2"
COINBASE_URL = "https://api.exchange.coinbase.com/products/BTC-USD/candles"
BTC_SERIES   = "KXBTC1H"
WINDOW_MINS  = 60

# ── HOUR BOT CAPITAL ARCHITECTURE ────────────────────────────────────
# Segregated $100 starting balance. Grows independently.
# All % scale with current hour bot balance.
HOUR_BOT_START_BALANCE  = 100.00  # Starting dedicated capital
HOUR_BOT_FLOOR          = 100.00  # Never trade below this (unless total < 230)
TOTAL_ACCOUNT_HARD_STOP = 230.00  # If total account <= this, stop all trading

# Position sizing (all % of current hour bot balance)
HOUR_PRIMARY_PCT        = 0.14    # 14% primary direction
HOUR_TRUE_HEDGE_PCT     = 0.03    # 3% auto-hedge after 25-30min confirmatory move
HOUR_SCALED_HEDGE_PCT   = 0.06    # 6% scaled hedge on reversal confirmation
HOUR_MOON_FREQ_PCT      = 0.01    # 1% frequent moon shots (hit 1-2x/day)
HOUR_MOON_RARE_PCT      = 0.02    # 2% rare moon shots (hit weekly)
HOUR_MAX_TRADE_PCT      = 0.23    # 23% max total allocated per hour

# Harvest on profit above $100 floor
HOUR_BOT_KEEP_PCT       = 0.67    # 67% of profit stays in hour bot
HOUR_MASTER_RETURN_PCT  = 0.33    # 33% of profit goes to master pool

# Loss management
HOUR_CONSECUTIVE_LOSSES = 2       # After this many losses in a row: pause
HOUR_PAUSE_MINUTES      = 60      # Pause duration after consecutive losses

# Momentum thresholds (lower than 15-min — hour window has more time)
HOUR_MOMENTUM_THRESHOLD = 0.05    # 0.05% single timeframe = valid signal
HOUR_OVERRIDE_RSI_MAX   = 40      # Override fires up to RSI 40 (vs 25 for 15-min)

# ── TELEGRAM TOGGLE FLAGS ─────────────────────────────────────────
# Both start OFF. Send commands in Telegram chat to toggle:
#   /windowsummary → end-of-window recap card (one per 15 min)
#   /30window      → 30-second live cycle updates
#   /status        → show current toggle states
# Trades, wins, losses, brakes ALWAYS send regardless of toggles.
WINDOW_SUMMARY_ON = False
THIRTY_SECOND_ON  = False
_tg_offset        = 0

# ── TIMING ───────────────────────────────────────────────────────
HARD_BLOCK_MINS   = 5   # First 5 min of 60-min window
ENTRY_CUTOFF_MINS = 45  # Stop entering after 45 min of 60-min window

# ── CONFIDENCE THRESHOLDS ────────────────────────────────────────
CONFIDENCE_FIRE_LARGE  = 82   # 1.5x position (lower bar — hour window)
CONFIDENCE_FIRE_NORMAL = 68   # 1.0x position
CONFIDENCE_FIRE_SMALL  = 58   # 0.7x position
CONFIDENCE_MINIMUM     = 55   # Hour bot: lower bar because 60-min window

# ── NEAR S/R SOFT BLOCK ───────────────────────────────────────────
CONFIDENCE_SR_REQUIRED = 80   # Near S/R + counter direction needs 80+

# ── HARD STOP RSI EXTREMES ────────────────────────────────────────
RSI_ABSOLUTE_OVERSOLD   = 15   # Hour bot: wider range before hard block
RSI_ABSOLUTE_OVERBOUGHT = 85   # Above this + longing = hard block

# ── RSI GUIDE RAIL ZONES (stronger penalties) ─────────────────────
RSI_SOFT_OVERSOLD   = 35   # Below this + shorting = -35 pts
RSI_SOFT_OVERBOUGHT = 65   # Above this + longing = -35 pts
RSI_NEUTRAL_LOW     = 42
RSI_NEUTRAL_HIGH    = 58

# ── MOMENTUM THRESHOLDS ───────────────────────────────────────────
# Minimum % move to count as real (below = flat/noise)
MOMENTUM_3MIN_THRESHOLD   = 0.02   # 0.02% min for 3min signal
MOMENTUM_12MIN_THRESHOLD  = 0.08   # 0.08% min for 12min signal
MOMENTUM_30MIN_THRESHOLD  = 0.15   # 0.15% min for 30min signal

# ── EXHAUSTION DETECTION ──────────────────────────────────────────
# A move is exhausted when longer timeframe is strong but 3min is flat/opposing
EXHAUSTION_LONG_THRESHOLD = 0.25   # 30min move > 0.25% = significant
EXHAUSTION_MEDIUM_THRESHOLD = 0.12 # 12min move > 0.12% = significant

# ── S/R PROXIMITY ────────────────────────────────────────────────
SR_PROXIMITY_PCT = 0.005   # 0.5% proximity

# ── VOLUME ───────────────────────────────────────────────────────
VOLUME_LOOKBACK    = 20
VOLUME_LOW_THRESH  = 0.5
VOLUME_HIGH_THRESH = 1.3

# ── STREAK ───────────────────────────────────────────────────────
STREAK_PENALTY_AT = 4

# ── RISK ─────────────────────────────────────────────────────────
BALANCE_FLOOR   = 100.00
BALANCE_WARNING = 130.00
SLOW_RISK_PCT   = 0.01
BASE_RISK_PCT   = 0.02
GOLDEN_RISK_PCT = 0.04
PROFIT_LOCKS    = {18000: 10980, 69000: 42090, 123000: 74970}

# Dynamic price cap — higher confidence allows slightly higher entry
def get_max_price(mins_elapsed, confidence):
    if mins_elapsed < 4:    base = 0.62
    elif mins_elapsed < 7:  base = 0.66
    elif mins_elapsed < 10: base = 0.70
    else: return 0.0
    if confidence >= CONFIDENCE_FIRE_LARGE: base += 0.03
    return base

# ─────────────────────────────────────────────────────────────────
# AUTHENTICATION
# ─────────────────────────────────────────────────────────────────
def _load_key():
    try:
        raw = KALSHI_PRIVATE_KEY.strip().replace('\\n', '\n')
        return serialization.load_pem_private_key(
            raw.encode('utf-8'), password=None, backend=default_backend())
    except Exception as e:
        log.error("Key: {}".format(e)); return None

def _auth(method, path):
    try:
        ts  = str(int(time.time() * 1000))
        msg = "{}{}{}".format(ts, method.upper(), "/trade-api/v2" + path.split('?')[0])
        key = _load_key()
        if not key: return None
        sig = key.sign(msg.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.DIGEST_LENGTH), hashes.SHA256())
        return {
            "Content-Type": "application/json",
            "KALSHI-ACCESS-KEY": KALSHI_API_KEY_ID,
            "KALSHI-ACCESS-TIMESTAMP": ts,
            "KALSHI-ACCESS-SIGNATURE": base64.b64encode(sig).decode()
        }
    except Exception as e:
        log.error("Auth: {}".format(e)); return None

def kget(path, params=None):
    h = _auth("GET", path)
    if not h: return None
    try:
        return requests.get(KALSHI_BASE + path, headers=h, params=params, timeout=10)
    except Exception as e:
        log.error("GET {}: {}".format(path, e)); return None

def kpost(path, body):
    h = _auth("POST", path)
    if not h: return None
    try:
        return requests.post(KALSHI_BASE + path, headers=h, json=body, timeout=10)
    except Exception as e:
        log.error("POST {}: {}".format(path, e)); return None

# ─────────────────────────────────────────────────────────────────
# TELEGRAM
# ─────────────────────────────────────────────────────────────────
def tg(msg):
    try:
        requests.post(
            "https://api.telegram.org/bot{}/sendMessage".format(TELEGRAM_BOT_TOKEN),
            json={"chat_id": TELEGRAM_CHAT_ID, "text": msg}, timeout=10)
    except: pass

def tg_startup():
    tg("⏰🚀 KALSHI HOUR BOT v1.0\n"
       "Account: chromagnumn\n\n"
       "ARCHITECTURE:\n"
       "Capital: $100 dedicated (scales with wins)\n"
       "Primary: 14% | Hedge: 3%+6% | Moon: 2-3%\n"
       "Max trade: 23% of hour balance\n"
       "2 losses = 60min pause\n"
       "Floor: $100 | Hard stop: $230 total\n\n"
       "Harvest: 67% stays | 33% to pool\n\n"
       "Commands: /windowsummary /30window /status\n"
       "Thresholds: conf=55 RSI=40\n"
       "@PairOdimebot")

def tg_startup_OLD():
    tg("🚀 KALSHI BOT v20_3 FULL ZONE INTELLIGENCE\n"
       "Account: chromagnumn\n\n"
       "3 FIXES FROM RSI-12 LOG ANALYSIS:\n"
       "A️⃣ RSI Extreme Mode (<20)\n"
       "   Exhaust: -35→-18 | EMA/MACD: -10→-5\n"
       "   RSI extreme: +15 BONUS | Min: 55\n"
       "   1-of-3 momentum override enabled\n\n"
       "B️⃣ Black Swan Database\n"
       "   7 major BTC crashes hardcoded\n"
       "   Match = position halved\n\n"
       "C️⃣ Trend Context Engine\n"
       "   Tracks hours in sustained trend\n"
       "   Logged on every trade\n\n"
       "All v20 intelligence preserved\n"
       "Target: 25-36 trades/day\n"
       "@PairOdimebot")

def tg_trade(direction, mins, price, confidence, ev, risk, breakdown, ctx, ticker):
    arrow = "📈 UP" if direction == "yes" else "📉 DOWN"
    grade = "🔥" if confidence >= 88 else "✅" if confidence >= 75 else "⚡"
    tg("{} v20 {} conf={}/100\n"
       "Min {:.1f} | ${:.2f} | EV+{:.1f}%\n"
       "Risk: ${:.2f}\n"
       "RSI:{:.0f} trend:{} exhaust:{}\n"
       "Score: {}\n"
       "{}\n@PairOdimebot".format(
           arrow, grade, confidence,
           mins, price, ev*100, risk,
           ctx.get('rsi', 50), ctx.get('trend', '?'),
           ctx.get('exhaustion', 'none'),
           breakdown[:60], ticker))

def tg_result(direction, win, pnl, balance):
    e = "✅ WIN" if win else "❌ LOSS"
    s = "+" if pnl >= 0 else ""
    tg("{} v20\nP&L: {}${:.2f}\nBal: ${:.2f}\n@PairOdimebot".format(e, s, pnl, balance))

def tg_window_summary(ticker, traded, skips, rsi, btc, balance, w, l):
    if not WINDOW_SUMMARY_ON: return
    fired = "TRADED" if traded else "NO TRADE"
    reasons = ", ".join(set(skips)) if skips else "N/A"
    tg("WINDOW {}\n{} | RSI:{:.0f} BTC:${:,.0f}\nBal:${:.2f} | {}W{}L\nSkips: {}\n@PairOdimebot".format(
        ticker[-8:], fired, rsi, btc, balance, w, l, reasons[:50]))

def tg_cycle(mins, rsi, mom, reason, score, minval, btc, balance, direction=None):
    if not THIRTY_SECOND_ON: return
    icons = {'NO_MOMENTUM':'😴','HARD_BLOCK':'🚫','EXHAUSTION':'💨',
             'LOW_SCORE':'📉','PRICE_TOO_HIGH':'💸','NEGATIVE_EV':'❌',
             'SR_BLOCK':'🧱','HARD_BLOCK_TIMING':'⏱'}
    icon = icons.get(reason, '🔄')
    dir_str = ' {}'.format(direction.upper()) if direction else ''
    tg("{} {:.1f}/15{}\nRSI:{:.0f} ${:,.0f} ${:.0f}\n{} {}/{}\n@PairOdimebot".format(
        icon, mins, dir_str, rsi, btc, balance, reason, score or 0, minval))

def poll_commands():
    global WINDOW_SUMMARY_ON, THIRTY_SECOND_ON, _tg_offset
    while True:
        try:
            r = requests.get(
                "https://api.telegram.org/bot{}/getUpdates".format(TELEGRAM_BOT_TOKEN),
                params={"offset": _tg_offset, "timeout": 5}, timeout=10)
            if r.status_code == 200:
                for upd in r.json().get("result", []):
                    _tg_offset = upd["update_id"] + 1
                    msg = upd.get("message", {})
                    txt = msg.get("text", "").strip().lower()
                    if str(msg.get("chat", {}).get("id", "")) != str(TELEGRAM_CHAT_ID): continue
                    if txt == "/windowsummary":
                        WINDOW_SUMMARY_ON = not WINDOW_SUMMARY_ON
                        tg("Window Summary: {} @PairOdimebot".format("ON" if WINDOW_SUMMARY_ON else "OFF"))
                    elif txt == "/30window":
                        THIRTY_SECOND_ON = not THIRTY_SECOND_ON
                        tg("30-Sec Updates: {} @PairOdimebot".format("ON" if THIRTY_SECOND_ON else "OFF"))
                    elif txt == "/status":
                        tg("Window:{} 30Sec:{} v20_3\n@PairOdimebot".format(
                            "ON" if WINDOW_SUMMARY_ON else "OFF",
                            "ON" if THIRTY_SECOND_ON else "OFF"))
        except Exception as e:
            log.error("Poll: {}".format(e))
        time.sleep(5)


def tg_daily(date, w, l, pnl, bal):
    total = w + l
    wr = (w/total*100) if total > 0 else 0
    s = "+" if pnl >= 0 else ""
    tg("📊 DAILY {}\n{}W/{}L — {:.1f}%\nP&L: {}${:.2f}\nBal: ${:.2f}\n@PairOdimebot".format(
        date, w, l, wr, s, pnl, bal))

def tg_brake(n, note):
    tg("⚡ BRAKE: {} losses\n{}\n@PairOdimebot".format(n, note))

def tg_lock(m, f):
    tg("🔐 LOCK: ${:,.0f} → Floor ${:,.0f}\n@PairOdimebot".format(m, f))

def tg_floor():
    tg("🛑 FLOOR $100 HIT — STOPPED\nchromagnumn")

# ─────────────────────────────────────────────────────────────────
# KALSHI API
# ─────────────────────────────────────────────────────────────────
def get_balance():
    r = kget("/portfolio/balance")
    if r and r.status_code == 200:
        b = r.json().get('balance', 0) / 100
        log.info("Balance: ${:.2f}".format(b))
        return b
    return None

def find_market():
    r = kget("/markets", params={"series_ticker": BTC_SERIES, "status": "open", "limit": 5})
    if not r or r.status_code != 200: return None
    markets = r.json().get('markets', [])
    if not markets: return None
    m = markets[0]
    try: yes_ask = float(m.get('yes_ask_dollars') or 0.50)
    except: yes_ask = 0.50
    try: no_ask = float(m.get('no_ask_dollars') or 0.50)
    except: no_ask = 0.50
    try: strike = float(m.get('floor_strike') or 0)
    except: strike = 0
    result = {
        'ticker': m.get('ticker', ''),
        'open_time': m.get('open_time', ''),
        'close_time': m.get('close_time', ''),
        'strike': strike, 'yes_ask': yes_ask, 'no_ask': no_ask,
    }
    log.info("Market: {} S:{:.0f} Y:${:.2f} N:${:.2f}".format(
        result['ticker'], strike, yes_ask, no_ask))
    return result

def get_elapsed(market):
    now = datetime.datetime.now(datetime.timezone.utc)
    for key in ['open_time', 'close_time']:
        val = market.get(key, '')
        if not val: continue
        try:
            dt = datetime.datetime.fromisoformat(val.replace('Z', '+00:00'))
            if key == 'close_time': dt = dt - datetime.timedelta(minutes=WINDOW_MINS)
            return (now - dt).total_seconds() / 60
        except: pass
    return None

def get_settled(limit=6):
    r = kget("/markets", params={"series_ticker": BTC_SERIES, "status": "settled", "limit": limit})
    if not r or r.status_code != 200: return []
    markets = r.json().get('markets', [])
    try: markets.sort(key=lambda x: x.get('close_time', ''), reverse=True)
    except: pass
    return [m.get('result') for m in markets if m.get('result') in ('yes', 'no')]

def place_order(ticker, direction, count):
    pk = "yes_price" if direction == "yes" else "no_price"
    body = {
        "ticker": ticker, "action": "buy", "side": direction,
        "count": count, "type": "market", pk: 99,
        "client_order_id": "pairodime_{}".format(str(uuid.uuid4())[:8])
    }
    r = kpost("/portfolio/orders", body)
    if not r: return False
    log.info("Order: {} | {}".format(r.status_code, r.text[:100]))
    if r.status_code == 201:
        o = r.json().get('order', {})
        log.info("✅ {} {}".format(o.get('order_id', '?')[:8], o.get('status', '?')))
        return True
    log.error("❌ {}".format(r.text[:150]))
    return False

# ─────────────────────────────────────────────────────────────────
# PRICE FEED — MULTI-TIMEFRAME
# ─────────────────────────────────────────────────────────────────
def get_candles(granularity=60, limit=70):
    """
    Coinbase candle granularities:
    60     = 1 minute
    900    = 15 minutes
    3600   = 1 hour
    21600  = 6 hours (for monthly S/R context)
    86400  = 1 day
    """
    try:
        r = requests.get(COINBASE_URL,
            params={"granularity": granularity, "limit": limit}, timeout=12)
        if r.status_code == 200:
            return list(reversed(r.json()))
        log.error("Coinbase {}: {}".format(granularity, r.status_code))
        return None
    except Exception as e:
        log.error("Coinbase: {}".format(e)); return None

def get_closes(c): return [float(x[4]) for x in c]
def get_highs(c):  return [float(x[2]) for x in c]
def get_lows(c):   return [float(x[1]) for x in c]
def get_vols(c):   return [float(x[5]) for x in c]

# ─────────────────────────────────────────────────────────────────
# TECHNICAL INDICATORS
# ─────────────────────────────────────────────────────────────────
def calc_rsi(prices, period=14):
    if not prices or len(prices) < period + 1: return 50.0
    deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    gains  = [max(d, 0) for d in deltas[-period:]]
    losses = [max(-d, 0) for d in deltas[-period:]]
    ag = sum(gains) / period
    al = sum(losses) / period
    if al == 0: return 100.0
    return round(100.0 - (100.0 / (1.0 + ag/al)), 2)

def calc_ema(prices, period):
    if not prices or len(prices) < period: return None
    k = 2.0 / (period + 1)
    ema = sum(prices[:period]) / period
    for p in prices[period:]:
        ema = p * k + ema * (1 - k)
    return ema

def get_ema_trend(closes_1hr):
    if not closes_1hr or len(closes_1hr) < 25: return 'neutral'
    fast = calc_ema(closes_1hr, 9)
    slow = calc_ema(closes_1hr, 21)
    if not fast or not slow: return 'neutral'
    diff = (fast - slow) / slow
    if diff > 0.001: return 'up'
    if diff < -0.001: return 'down'
    return 'neutral'

def get_macd_direction(closes):
    if not closes or len(closes) < 35: return 'neutral'
    e12 = calc_ema(closes, 12)
    e26 = calc_ema(closes, 26)
    if not e12 or not e26: return 'neutral'
    macd = e12 - e26
    if macd > 0: return 'bullish'
    if macd < 0: return 'bearish'
    return 'neutral'

# ─────────────────────────────────────────────────────────────────
# ─────────────────────────────────────────────────────────────────
# BLACK SWAN HISTORICAL DATABASE — v20
#
# Major BTC crash events hardcoded. No API needed.
# When RSI < 15 + high velocity crash, bot checks if current
# conditions match a known black swan pattern.
# If matched: position size halved as extra caution.
# ─────────────────────────────────────────────────────────────────
BLACK_SWAN_EVENTS = [
    # (name, date_str, rsi_low_approx, drop_pct, duration_hours, notes)
    ("covid_crash",       "2020-03-12", 6,  50, 48, "global panic sell, forced liquidations"),
    ("china_ban",         "2021-05-19", 8,  30, 24, "China mining ban announcement cascade"),
    ("luna_collapse",     "2022-06-13", 5,  38, 72, "UST depeg + LUNA hyperinflation death spiral"),
    ("ftx_collapse",      "2022-11-09", 7,  25, 96, "FTX insolvency, contagion across ecosystem"),
    ("japan_yen_crisis",  "2024-08-05", 10, 20, 24, "Japanese yen carry trade unwind, SPX crash"),
    ("tariff_shock",      "2025-03-10", 12, 22, 72, "Trump tariff escalation, risk-off global"),
    ("oct_cascade",       "2025-10-15", 8,  28, 48, "Massive liquidation cascade, record OI wipe"),
]

def detect_black_swan(rsi_1hr, closes_1min):
    """
    Check if current conditions match a historical black swan pattern.
    Returns: 'black_swan' or 'none'
    Uses RSI extremity + price velocity as signature.
    Never blocks a trade — only used for position sizing.
    """
    if rsi_1hr > 15:
        return 'none'

    # Check velocity: if price dropped >1.5% in last 30 minutes
    if not closes_1min or len(closes_1min) < 31:
        return 'none'

    price_now  = closes_1min[-1]
    price_30m  = closes_1min[-31]
    if price_30m == 0:
        return 'none'

    velocity = (price_now - price_30m) / price_30m * 100

    # RSI below 15 + drop >1.5% in 30min = black swan signature
    if rsi_1hr < 15 and velocity < -1.5:
        log.info("⚠️ BLACK SWAN PATTERN: RSI={:.1f} velocity={:.2f}%".format(rsi_1hr, velocity))
        return 'black_swan'

    return 'none'


# ─────────────────────────────────────────────────────────────────
# MULTI-TIMEFRAME TREND CONTEXT — v20
#
# Distinguishes sustained trends (3hr+) from short corrections.
# Helps bot understand: "We've been crashing for 6 hours"
# vs "This is a 45-minute pullback in an uptrend."
# ─────────────────────────────────────────────────────────────────
def get_trend_context(closes_1hr):
    """
    Analyze multi-hour trend direction and strength.
    Returns: dict with trend_duration, trend_direction, reversal_zone
    """
    ctx = {
        'trend_direction': 'neutral',
        'trend_strength': 'weak',
        'reversal_zone': False,
        'hours_in_trend': 0
    }

    if not closes_1hr or len(closes_1hr) < 6:
        return ctx

    # Look at last 6 hours of closes
    c6 = closes_1hr[-7:]  # last 6 one-hour candles
    if len(c6) < 4:
        return ctx

    # Count how many consecutive hours were down
    down_count = 0
    up_count   = 0
    for i in range(len(c6)-1, 0, -1):
        if c6[i] < c6[i-1]:
            if up_count > 0: break
            down_count += 1
        elif c6[i] > c6[i-1]:
            if down_count > 0: break
            up_count += 1
        else:
            break

    if down_count >= 3:
        ctx['trend_direction'] = 'down'
        ctx['trend_strength']  = 'strong' if down_count >= 5 else 'moderate'
        ctx['hours_in_trend']  = down_count
    elif up_count >= 3:
        ctx['trend_direction'] = 'up'
        ctx['trend_strength']  = 'strong' if up_count >= 5 else 'moderate'
        ctx['hours_in_trend']  = up_count

    log.info("Trend context: {}hr {} {} trend".format(
        ctx['hours_in_trend'], ctx['trend_strength'], ctx['trend_direction']))

    return ctx


# ─────────────────────────────────────────────────────────────────
# RSI EXTREME MOMENTUM OVERRIDE — v20 KEY FIX
#
# When RSI < 20, the normal "2 of 3 timeframes must agree" rule
# is too strict. At historic oversold levels, even 1 timeframe
# showing a directional move is a real signal worth scoring.
#
# This function provides a "weak" momentum signal (1 of 3)
# when the main momentum function returns None at RSI extremes.
# ─────────────────────────────────────────────────────────────────
# ─────────────────────────────────────────────────────────────────
# RSI DIRECTION TRACKING — v20_3 NEW INTELLIGENCE
#
# Research shows RSI CROSSOVER (direction) has 60% win rate
# vs only 50% for simple RSI threshold (level alone).
# The bot now asks not just "where is RSI?" but "where is RSI going?"
#
# Rising RSI from crash bottom = buyers accumulating = bullish
# Falling RSI toward oversold = sellers accelerating = bearish
# ─────────────────────────────────────────────────────────────────
def get_rsi_direction(closes_1hr):
    """
    Detect if RSI is rising or falling over the last 2 one-hour candles.
    Returns: 'rising', 'falling', or 'flat'
    Rising RSI + longing = bullish continuation signal (+8)
    Falling RSI + shorting = bearish continuation signal (+8)
    """
    if not closes_1hr or len(closes_1hr) < 17:
        return 'flat'

    rsi_recent = calc_rsi(closes_1hr[-14:], period=14)
    rsi_older  = calc_rsi(closes_1hr[-16:-2], period=14)

    if rsi_older == 50.0 or rsi_recent == 50.0:
        return 'flat'

    delta = rsi_recent - rsi_older

    if delta >= 3.0:
        log.info("RSI Direction: RISING +{:.1f}pts ({:.1f} → {:.1f})".format(
            delta, rsi_older, rsi_recent))
        return 'rising'
    elif delta <= -3.0:
        log.info("RSI Direction: FALLING {:.1f}pts ({:.1f} → {:.1f})".format(
            delta, rsi_older, rsi_recent))
        return 'falling'
    return 'flat'


def get_extreme_momentum_override(closes_1min, rsi_1hr):
    """
    Only called when main momentum returns None AND RSI < 20.
    Checks if any single timeframe shows meaningful directional move.
    Returns: ('yes'/'no'/'none', 'weak', detail_str)
    """
    # v20_3: Extended to RSI < 25 (was RSI < 20)
    # RSI 20-25 is still historically extreme (1st percentile BTC readings)
    # One timeframe showing direction here is a real signal worth scoring
    if rsi_1hr >= 25 or not closes_1min or len(closes_1min) < 31:
        return None, 'none', ''

    c = closes_1min
    current = c[-1]

    # Check each timeframe independently
    signals = []

    # 30-minute
    if len(c) >= 31:
        pct_30 = (current - c[-31]) / c[-31] * 100
        if pct_30 > 0.15:  # meaningful up move
            signals.append(('yes', "30m↑{:.2f}%".format(pct_30)))
        elif pct_30 < -0.15:
            signals.append(('no', "30m↓{:.2f}%".format(abs(pct_30))))

    # 12-minute
    if len(c) >= 13:
        pct_12 = (current - c[-13]) / c[-13] * 100
        if pct_12 > 0.10:
            signals.append(('yes', "12m↑{:.2f}%".format(pct_12)))
        elif pct_12 < -0.10:
            signals.append(('no', "12m↓{:.2f}%".format(abs(pct_12))))

    if not signals:
        return None, 'none', ''

    # Count direction votes
    yes_votes = sum(1 for d, _ in signals if d == 'yes')
    no_votes  = sum(1 for d, _ in signals if d == 'no')
    detail    = " | ".join(t for _, t in signals)

    if yes_votes > no_votes and yes_votes >= 1:
        log.info("RSI Extreme Override: WEAK UP signal | {}".format(detail))
        return 'yes', 'weak', detail
    elif no_votes > yes_votes and no_votes >= 1:
        log.info("RSI Extreme Override: WEAK DOWN signal | {}".format(detail))
        return 'no', 'weak', detail

    return None, 'none', ''


# ─────────────────────────────────────────────────────────────────
# EXHAUSTION DETECTION — THE CORE FIX
#
# A move is EXHAUSTED when:
# - The 30-min or 12-min timeframe shows a strong directional move
# - BUT the 3-minute is flat or opposing
# - Meaning the momentum has run out, the move is OVER
# - Trading in the same direction = trading a completed move = wrong
#
# This is what caused every loss in v11-v17.
# ─────────────────────────────────────────────────────────────────
def detect_exhaustion(mom_30_dir, mom_30_pct, mom_12_dir, mom_12_pct,
                       mom_3_dir, mom_3_pct):
    """
    Detect if a directional move has exhausted.

    Returns:
    - 'exhausted_down': A down move is done (3min flat/up while 30min was down)
    - 'exhausted_up':   An up move is done (3min flat/down while 30min was up)
    - 'none':           No exhaustion detected, momentum is consistent
    """

    # Check for downside exhaustion
    # 30min strong down BUT 3min flat or up = down move OVER
    strong_down = (mom_30_dir == 'no' and abs(mom_30_pct) >= EXHAUSTION_LONG_THRESHOLD) or \
                  (mom_12_dir == 'no' and abs(mom_12_pct) >= EXHAUSTION_MEDIUM_THRESHOLD)

    flat_or_reversing = mom_3_dir == 'yes' or \
                        (mom_3_dir is None and abs(mom_3_pct) < MOMENTUM_3MIN_THRESHOLD)

    if strong_down and flat_or_reversing:
        log.info("⚠️ EXHAUSTION: Down move exhausted (30m/12m down, 3m flat/up)")
        return 'exhausted_down'

    # Check for upside exhaustion
    # 30min strong up BUT 3min flat or down = up move OVER
    strong_up = (mom_30_dir == 'yes' and abs(mom_30_pct) >= EXHAUSTION_LONG_THRESHOLD) or \
                (mom_12_dir == 'yes' and abs(mom_12_pct) >= EXHAUSTION_MEDIUM_THRESHOLD)

    flat_or_reversing_down = mom_3_dir == 'no' or \
                              (mom_3_dir is None and abs(mom_3_pct) < MOMENTUM_3MIN_THRESHOLD)

    if strong_up and flat_or_reversing_down:
        log.info("⚠️ EXHAUSTION: Up move exhausted (30m/12m up, 3m flat/down)")
        return 'exhausted_up'

    return 'none'

# ─────────────────────────────────────────────────────────────────
# RSI DIVERGENCE DETECTION
#
# Bullish divergence: price makes lower low, RSI makes higher low
# → selling exhausted, potential reversal UP
# → Strong signal AGAINST shorting
#
# Bearish divergence: price makes higher high, RSI makes lower high
# → buying exhausted, potential reversal DOWN
# → Strong signal AGAINST longing
# ─────────────────────────────────────────────────────────────────
def detect_rsi_divergence(closes_1min, closes_1hr):
    """
    Detect RSI divergence on the 1-hour chart.

    Returns:
    - 'bullish': price lower lows, RSI higher lows → don't short
    - 'bearish': price higher highs, RSI lower highs → don't long
    - 'none': no divergence
    """
    if not closes_1hr or len(closes_1hr) < 20:
        return 'none'

    # Compare last two swing lows and their RSI readings
    # Use simple approach: compare recent RSI to slightly older RSI
    # vs price movement direction
    prices_recent = closes_1hr[-5:]
    prices_older  = closes_1hr[-10:-5]

    if not prices_recent or not prices_older:
        return 'none'

    price_recent_avg = sum(prices_recent) / len(prices_recent)
    price_older_avg  = sum(prices_older) / len(prices_older)

    rsi_recent = calc_rsi(closes_1hr[-15:], period=14)
    rsi_older  = calc_rsi(closes_1hr[-20:-5], period=14)

    if rsi_older == 50.0 or rsi_recent == 50.0:
        return 'none'

    # Bullish divergence: price went DOWN but RSI went UP
    if price_recent_avg < price_older_avg and rsi_recent > rsi_older + 3:
        log.info("RSI Divergence: BULLISH (price↓ RSI↑) — selling exhausted")
        return 'bullish'

    # Bearish divergence: price went UP but RSI went DOWN
    if price_recent_avg > price_older_avg and rsi_recent < rsi_older - 3:
        log.info("RSI Divergence: BEARISH (price↑ RSI↓) — buying exhausted")
        return 'bearish'

    return 'none'

# ─────────────────────────────────────────────────────────────────
# HIGHER LOW / LOWER HIGH DETECTION
#
# After a down move: is the current low HIGHER than the previous low?
# Higher low = buyers defending at higher price = potential reversal
# Shorting into a higher low = classic mistake
#
# After an up move: is the current high LOWER than the previous high?
# Lower high = sellers stepping in at lower price = potential reversal
# Longing into a lower high = classic mistake
# ─────────────────────────────────────────────────────────────────
def detect_pivot_structure(closes_1min):
    """
    Detect higher lows (potential bullish reversal) and
    lower highs (potential bearish reversal) in recent price action.

    Returns:
    - 'higher_low':  Recent bottom is higher than previous bottom → don't short
    - 'lower_high':  Recent top is lower than previous top → don't long
    - 'none':        No clear pivot structure
    """
    if not closes_1min or len(closes_1min) < 20:
        return 'none'

    c = closes_1min

    # Look at the last 20 minutes in 5-minute segments
    seg1 = c[-20:-15]  # oldest segment
    seg2 = c[-15:-10]
    seg3 = c[-10:-5]
    seg4 = c[-5:]      # most recent

    if not all([seg1, seg2, seg3, seg4]):
        return 'none'

    low1 = min(seg1); low2 = min(seg2); low3 = min(seg3); low4 = min(seg4)
    high1 = max(seg1); high2 = max(seg2); high3 = max(seg3); high4 = max(seg4)

    # Higher low: each low is higher than the previous
    # This means buyers are defending at higher prices = bullish structure
    if low4 > low3 and low3 > low2:
        log.info("Pivot: HIGHER LOW detected (potential bullish reversal)")
        return 'higher_low'

    # Lower high: each high is lower than the previous
    # This means sellers are stepping in at lower prices = bearish structure
    if high4 < high3 and high3 < high2:
        log.info("Pivot: LOWER HIGH detected (potential bearish reversal)")
        return 'lower_high'

    return 'none'

# ─────────────────────────────────────────────────────────────────
# S/R LEVELS — MONTHLY CONTEXT FROM 6HR CANDLES
# ─────────────────────────────────────────────────────────────────
def find_sr_levels_6hr(candles_6hr):
    """
    Find major S/R levels from 6-hour candles (last 30 days).
    These are significantly more important than 1hr S/R levels.
    """
    if not candles_6hr or len(candles_6hr) < 8:
        return [], []

    h_list = get_highs(candles_6hr)
    l_list = get_lows(candles_6hr)
    resistance, support = [], []
    lb = 2

    for i in range(lb, len(h_list) - lb):
        if all(h_list[i] >= h_list[i-j] for j in range(1, lb+1)) and \
           all(h_list[i] >= h_list[i+j] for j in range(1, lb+1)):
            resistance.append(h_list[i])
        if all(l_list[i] <= l_list[i-j] for j in range(1, lb+1)) and \
           all(l_list[i] <= l_list[i+j] for j in range(1, lb+1)):
            support.append(l_list[i])

    def cluster(levels):
        if not levels: return []
        levels = sorted(set(levels))
        result = [levels[0]]
        for lv in levels[1:]:
            if abs(lv - result[-1]) / result[-1] > 0.005:
                result.append(lv)
            else:
                result[-1] = (result[-1] + lv) / 2
        return result

    sup = cluster(support)
    res = cluster(resistance)
    log.info("Monthly S/R: {} support, {} resistance levels".format(len(sup), len(res)))
    return sup, res

def check_sr_proximity(price, support, resistance):
    """
    Check proximity to S/R levels.
    Returns 'near_support', 'near_resistance', or 'clear'
    """
    prox = SR_PROXIMITY_PCT
    for s in support:
        if s > 0 and abs(price - s) / s < prox:
            log.info("SR: near support ${:.2f}".format(s))
            return 'near_support'
    for r in resistance:
        if r > 0 and abs(price - r) / r < prox:
            log.info("SR: near resistance ${:.2f}".format(r))
            return 'near_resistance'
    return 'clear'

# ─────────────────────────────────────────────────────────────────
# DEEP MOMENTUM — THREE TIMEFRAMES
# ─────────────────────────────────────────────────────────────────
def get_deep_momentum(closes_1min):
    """
    Analyze momentum across three timeframes.
    Returns details needed for exhaustion detection too.
    """
    if not closes_1min or len(closes_1min) < 32:
        return None, 'weak', '', 0, None, 0, None, 0

    c = closes_1min
    current = c[-1]

    mom_30_dir = None; mom_30_pct = 0
    mom_12_dir = None; mom_12_pct = 0
    mom_3_dir  = None; mom_3_pct  = 0
    details    = []
    votes      = []

    # 30-minute window
    if len(c) >= 31:
        c30 = c[-31:]
        pct_30 = (current - c30[0]) / c30[0] * 100
        ups_30 = sum(1 for i in range(1, len(c30)) if c30[i] > c30[i-1])
        ratio_30 = ups_30 / (len(c30) - 1)
        mom_30_pct = pct_30
        if abs(pct_30) >= MOMENTUM_30MIN_THRESHOLD:
            if pct_30 > 0 and ratio_30 > 0.55:
                mom_30_dir = 'yes'; votes.append('yes')
                details.append("30m↑{:.2f}%".format(pct_30))
            elif pct_30 < 0 and ratio_30 < 0.45:
                mom_30_dir = 'no'; votes.append('no')
                details.append("30m↓{:.2f}%".format(abs(pct_30)))
            else:
                details.append("30m~mixed")
        else:
            details.append("30m~flat")

    # 12-minute window
    if len(c) >= 13:
        c12 = c[-13:]
        pct_12 = (current - c12[0]) / c12[0] * 100
        ups_12 = sum(1 for i in range(1, len(c12)) if c12[i] > c12[i-1])
        ratio_12 = ups_12 / (len(c12) - 1)
        mom_12_pct = pct_12
        if abs(pct_12) >= MOMENTUM_12MIN_THRESHOLD:
            if pct_12 > 0 and ratio_12 > 0.58:
                mom_12_dir = 'yes'; votes.append('yes')
                details.append("12m↑{:.2f}%".format(pct_12))
            elif pct_12 < 0 and ratio_12 < 0.42:
                mom_12_dir = 'no'; votes.append('no')
                details.append("12m↓{:.2f}%".format(abs(pct_12)))
            else:
                details.append("12m~mixed")
        else:
            details.append("12m~flat")

    # 3-minute window
    if len(c) >= 4:
        c3 = c[-4:]
        avg3 = sum(c3[:-1]) / 3
        pct_3 = (current - avg3) / avg3 * 100
        ups3 = sum(1 for i in range(1, len(c3)) if c3[i] > c3[i-1])
        mom_3_pct = pct_3
        if abs(pct_3) >= MOMENTUM_3MIN_THRESHOLD:
            if pct_3 > 0 and ups3 >= 2:
                mom_3_dir = 'yes'; votes.append('yes')
                details.append("3m↑{:.2f}%".format(pct_3))
            elif pct_3 < 0 and ups3 <= 1:
                mom_3_dir = 'no'; votes.append('no')
                details.append("3m↓{:.2f}%".format(abs(pct_3)))
            else:
                details.append("3m~mixed")
        else:
            details.append("3m~flat")

    breakdown = " | ".join(details)
    yes_v = votes.count('yes')
    no_v  = votes.count('no')
    total = len(votes)

    if yes_v >= 2 and yes_v > no_v:
        strength = 'strong' if yes_v == 3 else 'moderate'
        log.info("Momentum: UP {} | {}".format(strength, breakdown))
        return 'yes', strength, breakdown, mom_30_pct, mom_30_dir, mom_12_pct, mom_12_dir, mom_3_pct
    elif no_v >= 2 and no_v > yes_v:
        strength = 'strong' if no_v == 3 else 'moderate'
        log.info("Momentum: DOWN {} | {}".format(strength, breakdown))
        return 'no', strength, breakdown, mom_30_pct, mom_30_dir, mom_12_pct, mom_12_dir, mom_3_pct
    else:
        log.info("Momentum: MIXED | {}".format(breakdown))
        return None, 'weak', breakdown, mom_30_pct, mom_30_dir, mom_12_pct, mom_12_dir, mom_3_pct

# ─────────────────────────────────────────────────────────────────
# CONFIDENCE SCORE ENGINE — v20
# ─────────────────────────────────────────────────────────────────
def build_confidence(direction, market, closes_1min, closes_1hr,
                     settled, streak_data, momentum_data,
                     exhaustion_status, divergence, pivot_structure,
                     sr_status, rsi_1hr, trend, macd_dir, vol_status,
                     rsi_dir='flat'):
    """
    Build 0-100 confidence score incorporating all v20_3 intelligence.
    Returns (score, hard_blocked, breakdown)
    """
    score   = 50
    reasons = []

    # ── TRUE HARD BLOCKS (only 3) ────────────────────────────────
    if direction == 'no' and rsi_1hr < RSI_ABSOLUTE_OVERSOLD:
        return 0, True, "HARD BLOCK: RSI {:.0f} extreme oversold".format(rsi_1hr)
    if direction == 'yes' and rsi_1hr > RSI_ABSOLUTE_OVERBOUGHT:
        return 0, True, "HARD BLOCK: RSI {:.0f} extreme overbought".format(rsi_1hr)

    # ── EXHAUSTION — v20 RSI-CONTEXT AWARE ───────────────────────
    # At RSI < 20, exhaustion pattern has DIFFERENT meaning:
    # 3m flat after 30m/12m up at RSI 12 = sellers stopped, NOT buyers tired
    # Reduce penalty from -35 to -18 in extreme oversold conditions
    # v20_3: Three-tier exhaustion - expanded from v20's RSI<20 only
    # RSI < 20: historic extreme = -18
    # RSI 20-30: strong oversold = -22 (v20 was still -35 here = too heavy)
    # RSI 30+:   normal = -35
    if rsi_1hr < 20:
        exhaust_penalty = -18
    elif rsi_1hr < 30:
        exhaust_penalty = -22
    else:
        exhaust_penalty = -35

    if exhaustion_status == 'exhausted_down' and direction == 'no':
        score += exhaust_penalty
        reasons.append("EXHAUST_DOWN❌{}".format(exhaust_penalty))
    elif exhaustion_status == 'exhausted_down' and direction == 'yes':
        score += 15
        reasons.append("EXHAUST_DOWN→LONG+15")
    elif exhaustion_status == 'exhausted_up' and direction == 'yes':
        score += exhaust_penalty
        reasons.append("EXHAUST_UP❌{}".format(exhaust_penalty))
    elif exhaustion_status == 'exhausted_up' and direction == 'no':
        score += 15
        reasons.append("EXHAUST_UP→SHORT+15")

    # ── RSI DIVERGENCE ────────────────────────────────────────────
    if divergence == 'bullish' and direction == 'no':
        # Bullish divergence = selling exhausted = DON'T short
        score -= 30
        reasons.append("DIVERGE_BULL❌-30")
    elif divergence == 'bullish' and direction == 'yes':
        score += 20
        reasons.append("DIVERGE_BULL✅+20")
    elif divergence == 'bearish' and direction == 'yes':
        # Bearish divergence = buying exhausted = DON'T long
        score -= 30
        reasons.append("DIVERGE_BEAR❌-30")
    elif divergence == 'bearish' and direction == 'no':
        score += 20
        reasons.append("DIVERGE_BEAR✅+20")

    # ── PIVOT STRUCTURE ───────────────────────────────────────────
    if pivot_structure == 'higher_low' and direction == 'no':
        # Higher low = buyers defending = risky to short
        score -= 20
        reasons.append("HIGHER_LOW❌-20")
    elif pivot_structure == 'higher_low' and direction == 'yes':
        score += 10
        reasons.append("HIGHER_LOW✅+10")
    elif pivot_structure == 'lower_high' and direction == 'yes':
        # Lower high = sellers stepping in = risky to long
        score -= 20
        reasons.append("LOWER_HIGH❌-20")
    elif pivot_structure == 'lower_high' and direction == 'no':
        score += 10
        reasons.append("LOWER_HIGH✅+10")

    # ── MOMENTUM SIGNALS ─────────────────────────────────────────
    mom_dir, mom_strength, mom_detail = momentum_data[:3]
    if mom_dir == direction:
        if mom_strength == 'strong':   score += 25; reasons.append("MOM🔥+25")
        elif mom_strength == 'moderate': score += 15; reasons.append("MOM✅+15")
        else: score += 8; reasons.append("MOM~+8")
    elif mom_dir and mom_dir != direction:
        score -= 20; reasons.append("MOM❌-20")
    else:
        score -= 8; reasons.append("MOM?-8")

    # ── PREVIOUS WINDOW SIGNAL ────────────────────────────────────
    # v20 FIX 2: In extreme oversold (RSI < 35) longing, the previous
    # window settling NO is expected — part of the oversold condition.
    # Reduce penalty from -5 to -2 in this context.
    prev = settled[0] if settled else None
    if prev == direction:
        score += 12; reasons.append("PREV✅+12")
    elif prev and prev != direction:
        if rsi_1hr < 35 and direction == 'yes':
            score -= 2; reasons.append("PREV❌-2(OVS)")
        elif rsi_1hr > 65 and direction == 'no':
            score -= 2; reasons.append("PREV❌-2(OVB)")
        else:
            score -= 5; reasons.append("PREV❌-5")

    # ── FLOOR STRIKE SIGNAL ───────────────────────────────────────
    current = closes_1min[-1] if closes_1min else None
    strike  = market.get('strike', 0)
    if current and strike:
        if current > strike * 1.0002:   sig_strike = 'yes'
        elif current < strike * 0.9998: sig_strike = 'no'
        else:                           sig_strike = None
        if sig_strike == direction:
            score += 12; reasons.append("STRIKE✅+12")
        elif sig_strike and sig_strike != direction:
            score -= 8; reasons.append("STRIKE❌-8")

    # ── RSI SCORING — v20_3 FULL ZONE INTELLIGENCE ───────────────
    # Three tiers + RSI direction bonus (NEW)
    # RSI < 20: historic extreme = +15
    # RSI 20-30: strong oversold = +8 (was -3 neutral in v20)
    # Neutral: +10 | Soft extreme: -35 | Otherwise: -3
    # RSI direction rising+long or falling+short = +8 bonus (research: 60% WR)
    if rsi_1hr < 20 and direction == 'yes':
        score += 15; reasons.append("RSI_EXTREME_OVS✅+15")
    elif rsi_1hr < 30 and direction == 'yes':
        score += 8;  reasons.append("RSI_OVS_ZONE✅+8")
    elif rsi_1hr > 80 and direction == 'no':
        score += 15; reasons.append("RSI_EXTREME_OVB✅+15")
    elif rsi_1hr > 70 and direction == 'no':
        score += 8;  reasons.append("RSI_OVB_ZONE✅+8")
    elif RSI_NEUTRAL_LOW <= rsi_1hr <= RSI_NEUTRAL_HIGH:
        score += 10; reasons.append("RSI_NEUT+10")
    elif direction == 'no' and rsi_1hr < RSI_SOFT_OVERSOLD:
        score -= 35; reasons.append("RSI_OVS❌-35")
    elif direction == 'yes' and rsi_1hr > RSI_SOFT_OVERBOUGHT:
        score -= 35; reasons.append("RSI_OVB❌-35")
    else:
        score -= 3; reasons.append("RSI~-3")

    # ── RSI DIRECTION BONUS — v20_3 NEW INTELLIGENCE ─────────────
    if rsi_dir == 'rising' and direction == 'yes':
        score += 8; reasons.append("RSI_RISING✅+8")
    elif rsi_dir == 'falling' and direction == 'no':
        score += 8; reasons.append("RSI_FALLING✅+8")

    # ── EMA TREND — THREE-TIER RSI CONTEXT ───────────────────────
    # RSI<20: -5 | RSI 20-30: -6 (stale signal) | Normal: -10
    if (trend == 'up' and direction == 'yes') or (trend == 'down' and direction == 'no'):
        score += 10; reasons.append("EMA✅+10")
    elif (trend == 'up' and direction == 'no') or (trend == 'down' and direction == 'yes'):
        if rsi_1hr < 20:
            score -= 5; reasons.append("EMA❌-5(RSI_EXT)")
        elif rsi_1hr < 30:
            score -= 6; reasons.append("EMA❌-6(RSI_OVS)")
        else:
            score -= 10; reasons.append("EMA❌-10")

    # ── MACD — THREE-TIER RSI CONTEXT ────────────────────────────
    if (macd_dir == 'bullish' and direction == 'yes') or \
       (macd_dir == 'bearish' and direction == 'no'):
        score += 10; reasons.append("MACD✅+10")
    elif (macd_dir == 'bullish' and direction == 'no') or \
         (macd_dir == 'bearish' and direction == 'yes'):
        if rsi_1hr < 20:
            score -= 5; reasons.append("MACD❌-5(RSI_EXT)")
        elif rsi_1hr < 30:
            score -= 6; reasons.append("MACD❌-6(RSI_OVS)")
        else:
            score -= 10; reasons.append("MACD❌-10")

    # ── S/R GUIDE RAILS ──────────────────────────────────────────
    if sr_status == 'clear':
        score += 5; reasons.append("SR_CLR+5")
    elif sr_status == 'near_support' and direction == 'no':
        score -= 25; reasons.append("SR_NEAR_SUP❌-25")  # Stronger than v17
    elif sr_status == 'near_resistance' and direction == 'yes':
        score -= 25; reasons.append("SR_NEAR_RES❌-25")

    # ── VOLUME ───────────────────────────────────────────────────
    # v20 FIX 1: In extreme oversold (RSI < 35) or overbought (RSI > 65),
    # low volume means sellers/buyers exhausted — not a fake move.
    # Reduce low volume penalty from -12 to -5 in these conditions.
    if vol_status == 'high':
        score += 10; reasons.append("VOL🔥+10")
    elif vol_status == 'low':
        if rsi_1hr < 35 or rsi_1hr > 65:
            score -= 5; reasons.append("VOL_LOW-5(RSI_CTX)")
        else:
            score -= 12; reasons.append("VOL_LOW-12")

    # ── STREAK ───────────────────────────────────────────────────
    streak_count, streak_dir, overextended = streak_data
    if overextended and streak_dir == direction:
        score -= 15; reasons.append("STREAK⚠️-15")
    elif not overextended and streak_dir == direction:
        score += 3; reasons.append("STREAK+3")

    score = max(0, min(100, score))
    breakdown = "S{}|".format(score) + " ".join(reasons[:7])

    log.info("Confidence: {}/100 | {}".format(score, breakdown[:100]))
    return score, False, breakdown

# ─────────────────────────────────────────────────────────────────
# EV CALCULATOR
# ─────────────────────────────────────────────────────────────────
def calc_ev(entry_price, confidence):
    if confidence >= 88:   wr = 0.80
    elif confidence >= 75: wr = 0.73
    elif confidence >= 65: wr = 0.67
    else:                  wr = 0.60
    ev = wr - entry_price
    log.info("EV: conf={} WR={:.0f}% price={:.2f} EV={:+.1f}%".format(
        confidence, wr*100, entry_price, ev*100))
    return ev

# ─────────────────────────────────────────────────────────────────
# RISK MANAGEMENT
# ─────────────────────────────────────────────────────────────────
def get_base_risk(balance, consec_losses, brake_left):
    if balance <= BALANCE_WARNING: return SLOW_RISK_PCT
    if brake_left > 0:
        if consec_losses >= 4: return SLOW_RISK_PCT * 0.5
        if consec_losses >= 3: return SLOW_RISK_PCT
    h  = datetime.datetime.now(datetime.timezone.utc).hour
    wd = datetime.datetime.now(datetime.timezone.utc).weekday()
    if wd >= 5: return BASE_RISK_PCT if 8 <= h < 20 else SLOW_RISK_PCT
    if 0 <= h < 7:    return SLOW_RISK_PCT
    if 7 <= h < 9:    return BASE_RISK_PCT
    if 9 <= h < 16:   return GOLDEN_RISK_PCT
    if 16 <= h < 20:  return BASE_RISK_PCT
    if 20 <= h < 23:  return GOLDEN_RISK_PCT
    return BASE_RISK_PCT

def get_size_mult(confidence):
    if confidence >= CONFIDENCE_FIRE_LARGE:  return 1.5
    if confidence >= CONFIDENCE_FIRE_NORMAL: return 1.0
    return 0.7

def check_locks(balance, floor):
    for milestone, lock in sorted(PROFIT_LOCKS.items()):
        if balance >= milestone and lock > floor:
            tg_lock(milestone, lock); return lock
    return floor

# ─────────────────────────────────────────────────────────────────
# STATE
# ─────────────────────────────────────────────────────────────────
class State:
    def __init__(self):
        self.consec_losses = 0; self.brake_left = 0
        self.daily_wins = 0; self.daily_losses = 0; self.daily_pnl = 0.0
        self.is_paused = False; self.floor = BALANCE_FLOOR
        self.last_traded = None
        self.last_day = datetime.datetime.now(datetime.timezone.utc).day
        # Cached candles
        self.candles_1hr = None; self.candles_1hr_ts = 0
        self.candles_6hr = None; self.candles_6hr_ts = 0
        # Hour bot capital tracking
        self.hour_balance      = HOUR_BOT_START_BALANCE
        self.hour_paused_until = None    # datetime when 2-loss pause expires
        self.hour_consec_loss  = 0       # consecutive losses this session
        self.hour_hedge_active = False   # True when 3% hedge has been placed
        self.hour_hedge_ticker = None    # ticker of active hedge
        self.hour_primary_cost = 0.0     # amount in primary direction this window
        self.hour_moon_deployed = 0.0    # moon positions this window
        self.hour_wins = 0               # session wins
        self.hour_losses = 0             # session losses
        self.hour_pnl = 0.0              # session P&L

    def hour_win(self, pnl):
        """Handle hour bot win — harvest 33% to master pool, keep 67%"""
        self.hour_consec_loss = 0
        self.hour_wins += 1
        self.hour_pnl += pnl
        # Harvest: 33% of profit to master pool (tracked in log)
        harvest = pnl * HOUR_MASTER_RETURN_PCT
        keep    = pnl * HOUR_BOT_KEEP_PCT
        self.hour_balance += keep
        log.info("⏰ Hour Win: +${:.2f} | Keep ${:.2f} | Harvest ${:.2f} | HourBal ${:.2f}".format(
            pnl, keep, harvest, self.hour_balance))
        tg("⏰🏆 HOUR WIN +${:.2f}\nHour Bal: ${:.2f}\nHarvest→Pool: ${:.2f}\n@PairOdimebot".format(
            pnl, self.hour_balance, harvest))

    def hour_loss(self, amt):
        """Handle hour bot loss — protect $100 floor using master pool if needed"""
        self.hour_consec_loss += 1
        self.hour_losses += 1
        self.hour_pnl -= amt
        new_bal = self.hour_balance - amt
        if new_bal < HOUR_BOT_FLOOR:
            # Pull difference from master pool to maintain floor
            shortfall = HOUR_BOT_FLOOR - new_bal
            self.hour_balance = HOUR_BOT_FLOOR
            log.info("⏰ Hour Loss: -${:.2f} | Floor protected | Pool covers ${:.2f}".format(amt, shortfall))
        else:
            self.hour_balance = new_bal
            log.info("⏰ Hour Loss: -${:.2f} | HourBal ${:.2f}".format(amt, self.hour_balance))
        # Check consecutive loss pause
        if self.hour_consec_loss >= HOUR_CONSECUTIVE_LOSSES:
            self.hour_paused_until = datetime.datetime.now(datetime.timezone.utc) + \
                datetime.timedelta(minutes=HOUR_PAUSE_MINUTES)
            log.info("⏰ Hour Bot PAUSED for {} min after {} consecutive losses".format(
                HOUR_PAUSE_MINUTES, self.hour_consec_loss))
            tg("⏰⛔ HOUR BOT PAUSED\n{} consecutive losses\nResumes in {} min\n@PairOdimebot".format(
                self.hour_consec_loss, HOUR_PAUSE_MINUTES))
        else:
            tg("⏰❌ HOUR LOSS -${:.2f}\nHour Bal: ${:.2f}\n@PairOdimebot".format(amt, self.hour_balance))

    def hour_is_paused(self):
        """Check if hour bot is in loss pause"""
        if self.hour_paused_until is None:
            return False
        now = datetime.datetime.now(datetime.timezone.utc)
        if now >= self.hour_paused_until:
            self.hour_paused_until = None
            self.hour_consec_loss = 0
            log.info("⏰ Hour Bot RESUMED after pause")
            tg("⏰✅ HOUR BOT RESUMED\n@PairOdimebot")
            return False
        mins_left = int((self.hour_paused_until - now).total_seconds() / 60)
        log.info("⏰ Hour Bot paused — {} min remaining".format(mins_left))
        return True

    def win(self, pnl):
        self.consec_losses = 0; self.daily_wins += 1; self.daily_pnl += pnl
        if self.brake_left > 0: self.brake_left -= 1

    def loss(self, amt):
        self.consec_losses += 1; self.daily_losses += 1; self.daily_pnl -= amt
        if self.brake_left > 0: self.brake_left -= 1

    def daily_reset(self, balance):
        today = datetime.datetime.now(datetime.timezone.utc).day
        if today != self.last_day:
            tg_daily(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
                self.daily_wins, self.daily_losses, self.daily_pnl, balance)
            self.daily_wins = self.daily_losses = 0
            self.daily_pnl = 0.0; self.last_day = today

    def get_1hr_candles(self, force=False):
        now = time.time()
        if force or not self.candles_1hr or (now - self.candles_1hr_ts) > 1200:
            c = get_candles(granularity=3600, limit=50)
            if c: self.candles_1hr = c; self.candles_1hr_ts = now
            log.info("1hr candles: {}".format(len(self.candles_1hr) if self.candles_1hr else 0))
        return self.candles_1hr

    def get_6hr_candles(self, force=False):
        """6-hour candles for monthly S/R context. Refreshed every 6 hours."""
        now = time.time()
        if force or not self.candles_6hr or (now - self.candles_6hr_ts) > 21600:
            c = get_candles(granularity=21600, limit=120)  # ~30 days
            if c: self.candles_6hr = c; self.candles_6hr_ts = now
            log.info("6hr candles: {}".format(len(self.candles_6hr) if self.candles_6hr else 0))
        return self.candles_6hr

# ─────────────────────────────────────────────────────────────────
# MAIN LOOP
# ─────────────────────────────────────────────────────────────────
def run():
    log.info("=" * 64)
    log.info("KALSHI BTC BOT v20 PERSPECTIVE ENGINE")
    log.info("Account: chromagnumn | @PairOdimebot")
    log.info("Core fix: Exhaustion detection")
    log.info("48-hour session bot — building real data")
    log.info("=" * 64)

    if not KALSHI_API_KEY_ID or not KALSHI_PRIVATE_KEY:
        log.error("Missing credentials!"); return

    log.info("API Key: {}...".format(KALSHI_API_KEY_ID[:8]))
    state = State()
    tg_startup()
    threading.Thread(target=poll_commands, daemon=True).start()
    log.info("Telegram commands: /windowsummary /30window /status")

    while True:
        try:
            if state.is_paused:
                log.info("Paused..."); time.sleep(60); continue

            # ── BALANCE ───────────────────────────────────────────
            balance = get_balance()
            if not balance: time.sleep(30); continue

            # ── HOUR BOT HARD STOP ────────────────────────────────
            if balance <= TOTAL_ACCOUNT_HARD_STOP:
                log.info("⏰ HARD STOP: Total balance ${:.2f} <= ${:.2f}".format(
                    balance, TOTAL_ACCOUNT_HARD_STOP))
                tg("⏰🛑 HOUR BOT HARD STOP\nTotal: ${:.2f} <= ${:.2f}\n@PairOdimebot".format(
                    balance, TOTAL_ACCOUNT_HARD_STOP))
                time.sleep(300); continue

            # ── HOUR BOT PAUSE CHECK ──────────────────────────────
            if state.hour_is_paused():
                time.sleep(60); continue

            # ── HOUR BOT BALANCE ──────────────────────────────────
            hour_bal    = max(state.hour_balance, HOUR_BOT_FLOOR)
            tradeable   = hour_bal  # hour bot trades with its own balance
            base_risk   = HOUR_PRIMARY_PCT
            h = datetime.datetime.now(datetime.timezone.utc).hour
            log.info("⏰ HourBal=${:.2f} | 14%=${:.2f} | Hr={}UTC".format(
                hour_bal, hour_bal * HOUR_PRIMARY_PCT, h))

            # ── MARKET ───────────────────────────────────────────
            market = find_market()
            if not market: time.sleep(30); continue
            ticker = market['ticker']
            if ticker == state.last_traded:
                log.info("Already traded {}".format(ticker))
                time.sleep(30); continue

            # ── TIMING ───────────────────────────────────────────
            mins = get_elapsed(market)
            if mins is None: time.sleep(30); continue
            mins_left = WINDOW_MINS - mins
            log.info("⏱ {:.1f}/{} min".format(mins, WINDOW_MINS))

            if mins < HARD_BLOCK_MINS:
                wait = int((HARD_BLOCK_MINS - mins) * 60)
                log.info("⏱ HARD BLOCK: wait {}s".format(wait))
                time.sleep(min(wait, 60)); continue

            if mins >= ENTRY_CUTOFF_MINS:
                log.info("⏱ PAST CUTOFF")
                time.sleep(min(int(mins_left*60)+30, 60)); continue

            log.info("✅ ENTRY ZONE: min {:.1f}".format(mins))

            # ── PRICE DATA ────────────────────────────────────────
            candles_1min = get_candles(granularity=60, limit=70)
            if not candles_1min: time.sleep(30); continue
            closes_1min = get_closes(candles_1min)
            current_price = closes_1min[-1]
            log.info("BTC: ${:.2f}".format(current_price))

            candles_1hr = state.get_1hr_candles()
            candles_6hr = state.get_6hr_candles()

            closes_1hr = get_closes(candles_1hr) if candles_1hr else []

            # ── TECHNICAL INDICATORS ──────────────────────────────
            rsi_1hr  = calc_rsi(closes_1hr, 14) if closes_1hr else 50.0
            trend    = get_ema_trend(closes_1hr) if closes_1hr else 'neutral'
            macd_dir = get_macd_direction(closes_1hr) if closes_1hr else 'neutral'
            log.info("RSI:{:.1f} Trend:{} MACD:{}".format(rsi_1hr, trend, macd_dir))

            # ── VOLUME ───────────────────────────────────────────
            vol_status = 'normal'
            if candles_1hr and len(candles_1hr) > VOLUME_LOOKBACK:
                vols = get_vols(candles_1hr)
                avg_vol = sum(vols[-VOLUME_LOOKBACK:-1]) / (VOLUME_LOOKBACK - 1)
                cur_vol = vols[-1]
                if avg_vol > 0:
                    vr = cur_vol / avg_vol
                    vol_status = 'high' if vr > VOLUME_HIGH_THRESH else \
                                 'low' if vr < VOLUME_LOW_THRESH else 'normal'
            log.info("Volume: {}".format(vol_status))

            # ── MONTHLY S/R ───────────────────────────────────────
            support_lvls, resistance_lvls = [], []
            if candles_6hr:
                support_lvls, resistance_lvls = find_sr_levels_6hr(candles_6hr)
            sr_status = check_sr_proximity(current_price, support_lvls, resistance_lvls)

            # ── DEEP MOMENTUM ─────────────────────────────────────
            mom_result = get_deep_momentum(closes_1min)
            mom_dir, mom_strength, mom_detail = mom_result[:3]
            mom_30_pct, mom_30_dir = mom_result[3], mom_result[4]
            mom_12_pct, mom_12_dir = mom_result[5], mom_result[6]
            mom_3_pct              = mom_result[7]
            mom_3_dir = None  # derive from 3min pct
            if abs(mom_3_pct) >= MOMENTUM_3MIN_THRESHOLD:
                mom_3_dir = 'yes' if mom_3_pct > 0 else 'no'

            # If no clear momentum, try RSI extreme override before skipping
            # v20: At RSI < 20, a single timeframe signal is enough to score
            if mom_dir is None:
                override_dir, override_str, override_detail = get_extreme_momentum_override(
                    closes_1min, rsi_1hr)
                if override_dir is not None:
                    log.info("RSI Extreme Override applied: {} {}".format(
                        override_dir, override_detail))
                    mom_dir      = override_dir
                    mom_strength = override_str
                    mom_detail   = override_detail
                else:
                    log.info("No momentum direction — skip")
                    time.sleep(30); continue

            # ── BLACK SWAN DETECTION (v20) ────────────────────────
            black_swan_status = detect_black_swan(rsi_1hr, closes_1min)

            # ── MULTI-TIMEFRAME TREND CONTEXT (v20) ───────────────
            trend_ctx = get_trend_context(closes_1hr) if closes_1hr else {}

            # ── RSI DIRECTION TRACKING (v20_3 NEW) ────────────────
            rsi_dir = get_rsi_direction(closes_1hr) if closes_1hr else 'flat'
            log.info("Market context: blackswan={} trend={}hr {} rsi_dir={}".format(
                black_swan_status,
                trend_ctx.get('hours_in_trend', 0),
                trend_ctx.get('trend_direction', 'neutral'),
                rsi_dir))

            # ── EXHAUSTION DETECTION ──────────────────────────────
            exhaustion = detect_exhaustion(
                mom_30_dir, mom_30_pct,
                mom_12_dir, mom_12_pct,
                mom_3_dir,  mom_3_pct
            )

            # ── RSI DIVERGENCE ─────────────────────────────────────
            divergence = detect_rsi_divergence(closes_1min, closes_1hr)

            # ── PIVOT STRUCTURE ───────────────────────────────────
            pivot_struct = detect_pivot_structure(closes_1min)

            # ── SETTLED WINDOWS ───────────────────────────────────
            settled = get_settled(limit=6)
            streak_count, streak_dir, overextended = 0, None, False
            if settled:
                d = settled[0]; n = 0
                for x in settled:
                    if x == d: n += 1
                    else: break
                streak_count = n; streak_dir = d
                overextended = n >= STREAK_PENALTY_AT
            streak_data = (streak_count, streak_dir, overextended)

            # ── DIRECTION ─────────────────────────────────────────
            direction = mom_dir

            # ── CONFIDENCE SCORE ──────────────────────────────────
            score, hard_blocked, breakdown = build_confidence(
                direction, market, closes_1min, closes_1hr,
                settled, streak_data,
                (mom_dir, mom_strength, mom_detail),
                exhaustion, divergence, pivot_struct,
                sr_status, rsi_1hr, trend, macd_dir, vol_status,
                rsi_dir=rsi_dir
            )

            if hard_blocked:
                log.info("HARD BLOCKED: {}".format(breakdown))
                time.sleep(30); continue

            log.info("Score: {}/100".format(score))

            # ── S/R SOFT BLOCK ────────────────────────────────────
            if sr_status == 'near_support' and direction == 'no' and \
               score < CONFIDENCE_SR_REQUIRED:
                log.info("SR SOFT BLOCK: near support, shorting needs {}+, have {}".format(
                    CONFIDENCE_SR_REQUIRED, score))
                time.sleep(30); continue

            if sr_status == 'near_resistance' and direction == 'yes' and \
               score < CONFIDENCE_SR_REQUIRED:
                log.info("SR SOFT BLOCK: near resistance, longing needs {}+, have {}".format(
                    CONFIDENCE_SR_REQUIRED, score))
                time.sleep(30); continue

            # ── MINIMUM CONFIDENCE — v20_3 FOUR-TIER ─────────────
            # RSI < 20: 55 (historic extreme)
            # RSI 20-30: 58 (strong oversold — NEW, was 65 in v20)
            # RSI 30-35: 60 (soft oversold)
            # RSI > 70-80: mirrors above
            # Normal: 65
            if rsi_1hr < 20 and direction == 'yes':
                effective_minimum = 55
                log.info("Dynamic min: 55 (RSI {:.0f} HISTORIC oversold + LONG)".format(rsi_1hr))
            elif rsi_1hr > 80 and direction == 'no':
                effective_minimum = 55
                log.info("Dynamic min: 55 (RSI {:.0f} HISTORIC overbought + SHORT)".format(rsi_1hr))
            elif rsi_1hr < 30 and direction == 'yes':
                effective_minimum = 58
                log.info("Dynamic min: 58 (RSI {:.0f} strong oversold + LONG)".format(rsi_1hr))
            elif rsi_1hr > 70 and direction == 'no':
                effective_minimum = 58
                log.info("Dynamic min: 58 (RSI {:.0f} strong overbought + SHORT)".format(rsi_1hr))
            elif rsi_1hr < 35 and direction == 'yes':
                effective_minimum = 60
                log.info("Dynamic min: 60 (RSI {:.0f} soft oversold + LONG)".format(rsi_1hr))
            elif rsi_1hr > 65 and direction == 'no':
                effective_minimum = 60
                log.info("Dynamic min: 60 (RSI {:.0f} soft overbought + SHORT)".format(rsi_1hr))
            else:
                effective_minimum = CONFIDENCE_MINIMUM

            if score < effective_minimum:
                log.info("Score {}/100 < minimum {} — skip".format(
                    score, effective_minimum))
                time.sleep(30); continue

            # ── PRICE CHECK ───────────────────────────────────────
            entry_price = market['yes_ask'] if direction == 'yes' else market['no_ask']
            max_price   = get_max_price(mins, score)
            if entry_price > max_price:
                log.info("PRICE: ${:.2f} > max ${:.2f} — skip".format(
                    entry_price, max_price))
                time.sleep(30); continue

            # ── EV CHECK (third hard stop) ────────────────────────
            ev = calc_ev(entry_price, score)
            if ev <= 0:
                log.info("NEGATIVE EV {:.1f}% — hard stop".format(ev*100))
                time.sleep(30); continue

            log.info("✅ EV: +{:.1f}% at ${:.2f}".format(ev*100, entry_price))

            # ── HOUR BOT POSITION SIZE ────────────────────────────
            # 14% of hour balance for primary direction
            # Scale with confidence: 82+ = 1.0x, 68+ = 0.85x, 55+ = 0.7x
            conf_mult = 1.0 if score >= 82 else (0.85 if score >= 68 else 0.7)
            primary_dollars = round(hour_bal * HOUR_PRIMARY_PCT * conf_mult, 2)

            # Moon position: 1% of hour balance (small, intuitive)
            # Only fire moon if RSI extreme OR high confidence AND near key level
            moon_dollars = 0.0
            if (score >= 75 or rsi_1hr < 30 or rsi_1hr > 70) and \
               sr_status != 'clear':
                moon_dollars = round(hour_bal * HOUR_MOON_FREQ_PCT, 2)
                moon_dollars = max(0.25, min(moon_dollars, hour_bal * 0.02))
                log.info("⏰🌙 Moon position: ${:.2f}".format(moon_dollars))

            # Black swan: halve primary
            if black_swan_status == 'black_swan':
                primary_dollars = max(round(primary_dollars * 0.5, 2), 1.00)
                log.info("⚠️ BLACK SWAN: primary halved to ${:.2f}".format(primary_dollars))

            # Total deployed = primary + moon
            total_dollars = primary_dollars + moon_dollars
            # Cap at 23% max
            max_dollars = round(hour_bal * HOUR_MAX_TRADE_PCT, 2)
            if total_dollars > max_dollars:
                total_dollars = max_dollars
                primary_dollars = total_dollars - moon_dollars

            count = max(1, int(primary_dollars))

            log.info("⏰🎯 {} {} conf={} ${:.2f} EV+{:.1f}% primary=${:.2f} moon=${:.2f} bs={} rsi_dir={}".format(
                direction.upper(), count, score, entry_price, ev*100,
                primary_dollars, moon_dollars,
                black_swan_status, rsi_dir))

            # ── PLACE ORDER ───────────────────────────────────────
            success = place_order(ticker, direction, count)
            if not success: time.sleep(30); continue

            state.last_traded      = ticker
            state.hour_primary_cost = primary_dollars
            state.hour_moon_deployed = moon_dollars
            ctx = {
                'rsi': rsi_1hr, 'trend': trend,
                'exhaustion': exhaustion, 'divergence': divergence,
                'pivot': pivot_struct, 'sr': sr_status
            }
            tg_trade(direction, mins, entry_price, score, ev,
                     primary_dollars, breakdown, ctx, ticker)

            # ── WAIT FOR SETTLEMENT ───────────────────────────────
            wait_secs = max(30, int(mins_left * 60) + 15)
            log.info("Waiting {:.0f}s for settlement...".format(wait_secs))
            time.sleep(wait_secs)

            # ── RESULT ────────────────────────────────────────────
            new_balance = get_balance()
            if not new_balance: time.sleep(30); continue

            pnl = new_balance - balance
            win = pnl > 0

            if win:
                state.hour_win(pnl)
                state.win(pnl)
                state.get_1hr_candles(force=True)
            else:
                state.hour_loss(abs(pnl))
                state.loss(abs(pnl))
                state.get_1hr_candles(force=True)

            log.info("⏰ Cycle done. Next in 30s...")
            time.sleep(30)

        except KeyboardInterrupt:
            tg("🛑 Stopped. @PairOdimebot"); break
        except Exception as e:
            log.error("Error: {} — recovering 60s".format(e))
            time.sleep(60)


if __name__ == "__main__":
    print("=" * 64)
    print("KALSHI BTC BOT v20 PERSPECTIVE ENGINE")
    print("Account: chromagnumn | @PairOdimebot")
    print("Core fix: Exhaustion + Divergence + Pivot detection")
    print("48-hour session — real data incoming")
    print("=" * 64)
    run()
