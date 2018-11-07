#!/usr/bin/python3
#-*- coding: utf-8 -*-

__version__ ="1.0.0" ## Works until they stop allowing me to do this.
__author__ = "0x41_0x48" ## Twitter

## Imports
import json
import requests
import time

global a_string
a_string = []

class cxData():
  """cryptoExchange data"""
  def get_url(self):
    ## Connects to coinmarketcap and collects json.
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=0"
    api_json = requests.get(url=api_url)
    data = api_json.json()
    data_count = len(data)
    self.search(data, data_count)



  def search(self, data, data_count):
    ## Parse json, search for symbols.
    with open('symbols.txt', 'r') as symbol_file:
      sym_ara = symbol_file.readlines()
      ## Search through json for each symbol
      for x in range(0, len(sym_ara)):
        for y in range(0, data_count - 1):
          ## Check against json.
          if sym_ara[x].rstrip() == data[y]['symbol']:
            self.print_data(data[y], x)
            break



  def print_data(self, sym_data, x):
    a_name = sym_data['name']
    a_symbol = sym_data['symbol']
    a_usd = sym_data['price_usd']
    a_btc = sym_data['price_btc']
    a_1h = sym_data['percent_change_1h']
    a_1d = sym_data['percent_change_24h']
    a_7d = sym_data['percent_change_7d']
    a_upd = sym_data['last_updated']
    a_upd = time.ctime(int(a_upd))
    ## Form one string.
    a_string.append('[{} ({})] - ${} [1h:{}% | 1d:{}% | 7d:{}% | {} BTC | last update: {}\n'.format(a_name, a_symbol, a_usd, a_1h, a_1d, a_7d, a_btc, a_upd))



  def clear(self):
    import os
    os.system('printf \033c"')
    os.system('clear')



if __name__ == '__main__':
  cxdata = cxData()
  #cxdata.clear() ## Clear screen obv. lol
  cxdata.get_url()
  for line in a_string:
    print(line)
