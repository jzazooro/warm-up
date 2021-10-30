def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value=bitcoin_amount*bitcoin_value_euros
    if (euros_value<30000):
        print("Alerta, tus bitcoins valen menos de 30000 euros actualmente")
    return euros_value








bitcoinToEuros(1,25000)