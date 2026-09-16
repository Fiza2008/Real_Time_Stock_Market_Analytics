-- 1. Latest price for each stock
SELECT symbol, timestamp, close
FROM stock_prices
WHERE (symbol, timestamp) IN (
    SELECT symbol, MAX(timestamp)
    FROM stock_prices
    GROUP BY symbol
);

-- 2. Average closing price by stock
SELECT
    symbol,
    ROUND(AVG(close), 2) AS average_close
FROM stock_prices
GROUP BY symbol
ORDER BY average_close DESC;

-- 3. Maximum and minimum price
SELECT
    symbol,
    ROUND(MAX(high), 2) AS highest_price,
    ROUND(MIN(low), 2) AS lowest_price
FROM stock_prices
GROUP BY symbol;

-- 4. Average trading volume
SELECT
    symbol,
    ROUND(AVG(volume), 0) AS average_volume
FROM stock_prices
GROUP BY symbol
ORDER BY average_volume DESC;

-- 5. Number of records collected
SELECT
    symbol,
    COUNT(*) AS records
FROM stock_prices
GROUP BY symbol
ORDER BY records DESC;
