import sqlite3
from pathlib import Path
DB=Path("analytics.db")
def initialize(db=DB):
    with sqlite3.connect(db) as con:
        con.execute("CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY, region TEXT, business_unit TEXT, product TEXT, revenue REAL, status TEXT)")
        count=con.execute("SELECT COUNT(*) FROM sales").fetchone()[0]
        if not count: con.executemany("INSERT INTO sales(region,business_unit,product,revenue,status) VALUES(?,?,?,?,?)",[("South","Retail","Laptop",1200,"closed"),("North","Retail","Phone",800,"closed"),("South","Enterprise","Cloud",3000,"open"),("West","Retail","Tablet",500,"closed"),("North","Enterprise","Cloud",2500,"open")])
def run_query(question:str,business_unit:str|None=None,db=DB):
    q=question.lower()
    if "revenue" in q and "region" in q:
        sql="SELECT region, SUM(revenue) AS revenue FROM sales WHERE (? IS NULL OR business_unit=?) GROUP BY region ORDER BY revenue DESC"
        intent="revenue_by_region"
    elif "orders" in q or "sales" in q:
        sql="SELECT status, COUNT(*) AS count, SUM(revenue) AS revenue FROM sales WHERE (? IS NULL OR business_unit=?) GROUP BY status ORDER BY count DESC"
        intent="sales_by_status"
    else: raise ValueError("Supported questions: 'revenue by region' or 'orders by status'")
    with sqlite3.connect(db) as con:
        con.row_factory=sqlite3.Row
        rows=[dict(r) for r in con.execute(sql,(business_unit,business_unit)).fetchall()]
    return {"intent":intent,"business_unit_scope":business_unit,"rows":rows,"row_count":len(rows)}
