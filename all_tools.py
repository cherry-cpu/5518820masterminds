'''
https://expert-space-cod-j9xqw7r6v7v25wpr.github.dev/

https://github.com/cherry-cpu/5518820masterminds
'''
from threading import Thread
import requests as r
import sqlite3
from datetime import datetime
import pandas as pd
#stocks=["ADANIENT","ADANIPORTS","APOLLOHOSP","ASIANPAINT","AXISBANK","BAJAJ-AUTO","BAJFINANCE","BAJAJFINSV","BEL","BPCL","BHARTIARTL","BRITANNIA","CIPLA","COALINDIA","DRREDDY","EICHERMOT","GRASIM","HCLTECH","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDUNILVR","ICICIBANK","ITC","INDUSINDBK","INFY","JSWSTEEL","KOTAKBANK","LT","M&M","MARUTI","NTPC","NESTLEIND","ONGC","POWERGRID","RELIANCE","SBILIFE","SHRIRAMFIN","SBIN","SUNPHARMA","TCS","TATACONSUM","TATAMOTORS","TATASTEEL","TECHM","TITAN","TRENT","ULTRACEMCO","WIPRO"]

def stocks_thread(stocks):
	stock_prices={}
	rs=r.Session()
	rs.get('https://www.nseindia.com',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36','Accept-Encoding': 'gzip, deflate','Accept': '*/*','Connection': 'keep-alive'})
	def last_price(stock_name):
		res=rs.get(f'https://www.nseindia.com/api/quote-equity?symbol={stock_name}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36','Accept-Encoding': 'gzip, deflate','Accept': '*/*','Connection': 'keep-alive'})
		stock_prices[stock_name]=res.json()['priceInfo']['lastPrice']
		return res.json()['priceInfo']['lastPrice']

	thread_list=[]
	for i in set(stocks):
		thread_list.append(Thread(target=last_price, args=(i,)))
	for j in thread_list:
		j.start()
	for k in thread_list:
		k.join()
	return stock_prices

con=sqlite3.connect('all_data.db', check_same_thread=False)
cur=con.cursor()
try:
	cur.execute('''
CREATE TABLE "users" (
	"username"	TEXT,
	"user_id"	INTEGER UNIQUE
);
		''')
	con.commit()
except:
	print('Table exist')


def validate_user(username, user_id):
	cmd=f'''select * from users where username='{username}' and user_id={user_id} '''
	if cur.execute(cmd).fetchall()!=[]:
		return True
	else:
		return False

def validate_table(table_name):
	try:
		con.execute(f"select * from {table_name}").fetchall()
		return True
	except:
		return False

def create_tables_for_user(username,user_id):
	if validate_user(username,user_id):
		buy_table_name=username+'_'+str(user_id)+'_'+'holdings'
		if not validate_table(buy_table_name):
			cmd=f'''
CREATE TABLE "{username}_{user_id}_holdings" (
	"user_id"	TEXT,
	"buy_id"	TEXT UNIQUE,
	"time"	TEXT,
	"stock"	TEXT,
	"buy_price"	REAL,
	"no_of_shares"	INTEGER,
	"total_buy_price"	REAL,
	"holdings"	INTEGER,
	"soldout"	INTEGER
);
'''
			cur.execute(cmd)
			con.commit()

		sell_table_name=username+'_'+str(user_id)+'_'+'soldout'
		if not validate_table(sell_table_name):
			cmd=f'''
CREATE TABLE "{username}_{user_id}_soldout" (
	"user_id"	TEXT,
	"buy_id"	TEXT,
	"time"	INTEGER,
	"stock"	TEXT,
	"buy_price"	REAL,
	"sell_price"	INTEGER,
	"no_of_shares"	INTEGER,
	"P&L" INTEGER,
	"tax"	REAL
);
'''
			cur.execute(cmd)
			con.commit()
	else:
		print("user invalid")

def create_user(username, user_id):
	try:
		cmd=f'''insert into users values('{username}',{user_id})'''
		cur.execute(cmd)
		create_tables_for_user(username,user_id)
		con.commit()
		return True
	except:
		return False

def timestamp_to_id(timestamp, stock_name, nos):
    return '_'.join(timestamp.replace('-','_').split(':')).split('.')[0]+'_'+'_'.join(timestamp.replace('-','_').split(':')).split('.')[1][:2]+'_'+stock_name+'_'+f'{nos}'

def buy_action(username, user_id,stock_name, buy_price,no_of_shares, current_holdings, soldout_shares):
	time=datetime.now().__str__()
	buy_id=timestamp_to_id(time, stock_name, no_of_shares)
	total_price=buy_price*no_of_shares
	table_name=f'{username}_{user_id}_holdings'
	cmd=f"insert into {table_name} values({user_id},'{buy_id}','{time.split('.')[0]+'.'+time.split('.')[1][:2]}','{stock_name}',{buy_price},{no_of_shares},{total_price},{current_holdings},{soldout_shares})"
	cur.execute(cmd)
	con.commit()

def sell_action(username, user_id,buy_id,time,stock_name, buy_price,sell_price, no_of_shares_selling, pl,tax):
	table_name=f'{username}_{user_id}_soldout'	
	cmd=f"insert into {table_name} values({user_id},'{buy_id}','{time}','{stock_name}',{buy_price},{sell_price},{no_of_shares_selling},{pl},{tax})"
	if validate_sell(username, user_id, buy_id,no_of_shares_selling):
		cur.execute(cmd)
		con.commit()
		return "Sell Action Successful"
	else:
		return "No of shares, Invalid sell request"

def validate_sell(username, user_id, buy_id, no_of_shares_selling):
	table_name=f'{username}_{user_id}_holdings'
	sell_data=cur.execute(f"select holdings from {table_name} where buy_id='{buy_id}'").fetchone()[0]
	if no_of_shares_selling<=sell_data:
		return True
	else:
		return False

def update_sell_action(username, user_id, buy_id, no_of_shares_selling):
	table_name=f'{username}_{user_id}_holdings'
	sell_data=cur.execute(f'''select * from {table_name} where buy_id="{buy_id}" ''').fetchone()
	if validate_sell(username, user_id, buy_id, no_of_shares_selling):
		print(sell_data)
		update_cmd=f'''update {table_name}
	set soldout={sell_data[-1]+no_of_shares_selling},holdings={sell_data[-2]-no_of_shares_selling}
	where buy_id='{buy_id}'
		'''
		cur.execute(update_cmd)
		con.commit()
		return sell_data
	else:
		print("Invalid Sell Action, No Of Shares Not Available")

# returns-> total_charges, net_profit
def upstox_tax(company_name, no_of_shares, buy_at, sell_at):
	# Input From User
	company=str(company_name)
	no_of_shares=int(no_of_shares)

	buy = float(buy_at)
	sell= float(sell_at)

	net_buy=no_of_shares*buy
	net_sell=no_of_shares*sell

	profit = sell-buy
	net_profit = net_sell-net_buy

	# Charges
	# Brokerage	     - 40.00 per net investment>40,000, If Investment>40,000 varies
	if net_buy>=40000:
		brokerage=40
	else:
		brokerage=20

	# STT/CTT 	     - 0.025 % of investment + 0.025% of profit
	stt_ctt = (0.00025)*(net_sell)


	# Transaction Charges  - 2*(0.00345 % of investment)+ (0.00345 % of profit)
	transaction_charges=2*((0.0000345)*net_buy)+((0.0000345*profit))

	# GST  		     -  18% on (brokerage + transaction charges)
	gst=(0.18)*(brokerage+transaction_charges)

	# Stamp Duty           - 0.003% on buy side
	stamp_duty=(0.00003)*net_buy

	dp_charges= "No DP Charges for Intraday (Demate Transaction Charges)"


	# SEBI charges         - 0.0002% of Buy Price + 0.0001% of Profit
	sebi_charges=((0.000002)*net_buy)+((0.000001)*profit)

	total_charges=brokerage+stt_ctt+gst+stamp_duty+transaction_charges+sebi_charges

	data=f'''
	Hello There,

	Buy  At = {buy} 
	Sell At = {sell}

	Net Buy={net_buy}
	Net Sell={net_sell}
	Profit={profit}

	Total Charges={total_charges}

		Brokerage Charges------ {brokerage}
		
		STT/CTT---------------- {stt_ctt}
		GST-------------------- {gst}
		Stamp Duty------------- {stamp_duty}
		
		Transaction Charges---- {transaction_charges} 
		
		DP Charges------------- No DP Charges for Intraday
		
		SEBI charges----------- {sebi_charges}
		
	Net Profit = Profit - Total Charges = {net_profit-total_charges}

	Overall Net Profit={net_profit-total_charges-20}
		'''
	return total_charges, net_profit-total_charges, data



def final_sell_action(username, user_id,buy_id,stock_name, no_of_shares_selling):
	time=datetime.now().__str__()
	table_name=f'{username}_{user_id}_holdings'
	buy_price=cur.execute(f''' select buy_price from {table_name} where buy_id='{buy_id}' ''').fetchone()[0]
	sell_price=stocks_thread([stock_name])[stock_name]
	pl=(sell_price-buy_price)*no_of_shares_selling
	tax=upstox_tax(stock_name, no_of_shares_selling, buy_price, sell_price)
	print(buy_price,'  ', sell_price,'  ', pl, tax)
	sell_action(username, user_id,buy_id,time,stock_name, buy_price,sell_price, no_of_shares_selling, pl,tax)
	print('asd')
	update_sell_action(username, user_id, buy_id, no_of_shares_selling)


def view(table_name):
	cmd=f''' select * from {table_name} '''
	d=cur.execute(cmd).fetchall()
	return pd.DataFrame(d)

def get_holdings_data(username, user_id):
	cmd=f'''select buy_id, time, stock,buy_price, no_of_shares,total_buy_price from {username}_{user_id}_holdings '''
	return cur.execute(cmd).fetchall()
