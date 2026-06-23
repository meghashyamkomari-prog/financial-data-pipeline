with staged as (
    select * from {{ ref('stg_stock_prices') }}
),

returns as (
    select
        symbol,
        trade_date,
        close,
        lag(close) over (partition by symbol order by trade_date) as prev_close,
        round(
            ((close - lag(close) over (partition by symbol order by trade_date)) 
            / lag(close) over (partition by symbol order by trade_date) * 100)::numeric, 2
        ) as daily_return_pct
    from staged
)

select * from returns
where prev_close is not null
