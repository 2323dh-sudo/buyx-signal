#!/usr/bin/env python3
"""
Buyx.ink Signal Fetcher - 使用API原生数据
"""

import requests
import re
import json
from datetime import datetime

def fetch_buyx_signals_today():
    """从Buyx.ink获取今日AI推荐信号"""
    url = 'https://buyx.ink/zh-cn/trade/ETH'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    try:
        r = requests.get(url, headers=headers, timeout=15)
        r.encoding = 'utf-8'
        
        match = re.search(r'<script[^>]*id="__NEXT_DATA__"[^>]*>([^<]+)</script>', r.text)
        if not match:
            raise Exception("无法找到页面数据")
        
        data = json.loads(match.group(1))
        page_props = data['props']['pageProps']
        rec_data = page_props.get('recommendPageData', {})
        
        # 使用API原生数据（这就是截图显示的数据）
        today_total = rec_data.get('todayTotal', {})
        buy_count = today_total.get('buy', 0)
        sell_count = today_total.get('sell', 0)
        
        max_profit = rec_data.get('maxProfit', 0) * 100
        
        # 更新时间戳
        update_at = rec_data.get('updateAt', 0)
        try:
            ts = int(update_at)
            update_time = datetime.fromtimestamp(ts / 1000).strftime('%Y-%m-%d %H:%M:%S')
        except:
            update_time = str(update_at)
        
        # 获取买入信号列表（只显示todayTotal中的买入）
        recommends = rec_data.get('recommends', [])
        today = datetime.now().strftime('%Y-%m-%d')
        today_signals = [r for r in recommends if today in r.get('updatedAt', '') and r.get('direction') == 'buy']
        
        # 去重并排序
        seen = set()
        unique_signals = []
        for s in today_signals:
            if s['symbol'] not in seen:
                seen.add(s['symbol'])
                unique_signals.append(s)
        
        unique_signals.sort(key=lambda x: x.get('maxProfit', 0), reverse=True)
        
        # 格式输出（按截图格式）
        output = []
        output.append(f"【BuyX信号推送】📅 {datetime.now().strftime('%Y-%m-%d')}")
        output.append("=" * 30)
        output.append(f"最近更新: {update_time}")
        output.append(f"今日推荐: {buy_count + sell_count} 个加密货币")
        output.append(f"买入: {buy_count}")
        output.append(f"卖出: {sell_count}" if sell_count > 0 else f"卖出: -")
        output.append(f"最大盈利: +{max_profit:.2f}%")
        output.append("")
        output.append("详细列表:")
        
        for i, s in enumerate(unique_signals[:10]):
            profit = s.get('maxProfit', 0) * 100
            direction = "📈买入"
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
