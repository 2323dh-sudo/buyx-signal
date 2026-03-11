#!/usr/bin/env python3
"""
Buyx.ink Signal Fetcher - Using API Native Data
"""

import requests
import re
import json
from datetime import datetime

def fetch_buyx_signals_today():
    """Fetch today's AI recommendation signals from Buyx.ink"""
    url = 'https://buyx.ink/zh-cn/trade/ETH'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    try:
        r = requests.get(url, headers=headers, timeout=15)
        r.encoding = 'utf-8'
        
        match = re.search(r'<script[^>]*id="__NEXT_DATA__"[^>]*>([^<]+)</script>', r.text)
        if not match:
            raise Exception("Cannot find page data")
        
        data = json.loads(match.group(1))
        page_props = data['props']['pageProps']
        rec_data = page_props.get('recommendPageData', {})
        
        # Use API native data
        today_total = rec_data.get('todayTotal', {})
        buy_count = today_total.get('buy', 0)
        sell_count = today_total.get('sell', 0)
        
        max_profit = rec_data.get('maxProfit', 0) * 100
        
        # Update timestamp
        update_at = rec_data.get('updateAt', 0)
        try:
            ts = int(update_at)
            update_time = datetime.fromtimestamp(ts / 1000).strftime('%Y-%m-%d %H:%M:%S')
        except:
            update_time = str(update_at)
        
        # Get recommendation list (deduplicated)
        recommends = rec_data.get('recommends', [])
        today = datetime.now().strftime('%Y-%m-%d')
        today_signals = [r for r in recommends if today in r.get('updatedAt', '') and r.get('direction') == 'buy']
        
        seen = set()
        unique_signals = []
        for s in today_signals:
            if s['symbol'] not in seen:
                seen.add(s['symbol'])
                unique_signals.append(s)
        
        unique_signals.sort(key=lambda x: x.get('maxProfit', 0), reverse=True)
        
        # Format output (matching screenshot format)
        output = []
        output.append(f"【BuyX Signal Push】📅 {datetime.now().strftime('%Y-%m-%d')}")
        output.append("=" * 35)
        output.append(f"Last Update: {update_time}")
        output.append(f"Today's Recommendations: {buy_count + sell_count} coins")
        output.append(f"Buy: {buy_count}")
        output.append(f"Sell: {sell_count}" if sell_count > 0 else f"Sell: -")
        output.append(f"Max Profit: +{max_profit:.2f}%")
        output.append("")
        output.append("Details:")
        
        for i, s in enumerate(unique_signals[:10]):
            profit = s.get('maxProfit', 0) * 100
            direction = "📈Buy"
            output.append(f"{i+1}. {s['symbol']} {direction} +{profit:.2f}%")
        
        result_text = '\n'.join(output)
        print(result_text)
        
        return {
            'status': 'success',
            'last_update': update_time,
            'total': buy_count + sell_count,
            'buy': buy_count,
            'sell': sell_count,
            'max_profit': f"+{max_profit:.2f}%"
        }
        
    except Exception as e:
        print(f"Error: {e}")
        return {'status': 'error', 'error': str(e)}

if __name__ == "__main__":
    fetch_buyx_signals_today()
