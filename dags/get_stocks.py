import yfinance as yf
from airflow.decorators import dag, task
from airflow.macros import ds_add
from pathlib import Path
import pendulum

TICKERS = ["AAPL", "MSFT", "GOOG", "TSLA"]

@task()
def get_history(ticker, ds=None, ds_nodash=None):
    file_path = f"/home/ruan/projeto-airflow/stocks/{ticker}/{ticker}_{ds_nodash}.csv"
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    yf.Ticker(ticker).history(
        interval="1h",
        start=ds_add(ds, -1),
        end=ds,
        prepost=True
    ).to_csv(file_path)

@dag(
    schedule_interval="@daily",  
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    end_date=pendulum.datetime(2025, 1, 30, tz="UTC"),
    catchup=True
)
def get_stocks_dag():
    for ticker in TICKERS:
        get_history.override(task_id=ticker)(ticker)

dag = get_stocks_dag()

