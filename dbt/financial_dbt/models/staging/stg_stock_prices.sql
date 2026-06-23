with source as (
    select * from raw_stock_prices
),

staged as (
    select
        symbol,
        date::date as trade_date,
        open,
        high,
        low,
        close,
        volume,
        ingested_at
    from source
    where close is not null
)

select * from staged
