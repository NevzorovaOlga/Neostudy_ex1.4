CREATE OR REPLACE FUNCTION get_credit_debit_info(
    input_date date
) 
RETURNS TABLE (
    oper_date date,
    max_credit_amount float8,
    min_credit_amount float8,
    max_debit_amount float8,
    min_debit_amount float8
)
AS $$
BEGIN
    RETURN QUERY
    SELECT
        oper_date,
        MAX(credit_amount) AS max_credit_amount,
        MIN(credit_amount) AS min_credit_amount,
        MAX(debet_amount) AS max_debit_amount,
        MIN(debet_amount) AS min_debit_amount
    FROM
        ds.ft_posting_f
    WHERE
        oper_date = input_date
    GROUP BY
        oper_date;
END
$$ LANGUAGE plpgsql;