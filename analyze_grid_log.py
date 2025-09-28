import pandas as pd
import ast
import matplotlib.pyplot as plt

# Cambia por el path real de tu log
CSV_PATH = "log_historico.csv"

def parse_signal(signal):
    if pd.isna(signal) or signal == '':
        return None
    try:
        return ast.literal_eval(signal)
    except Exception:
        return signal

def parse_orders(order_str):
    if pd.isna(order_str) or order_str == '':
        return []
    try:
        return ast.literal_eval(order_str.replace('""', '"'))
    except Exception:
        return []

def parse_tp(tp_str):
    if pd.isna(tp_str) or tp_str == '':
        return []
    try:
        return ast.literal_eval(tp_str.replace('""', '"'))
    except Exception:
        return []

def parse_sl(sl_str):
    if pd.isna(sl_str) or sl_str == '':
        return []
    try:
        return ast.literal_eval(sl_str.replace('""', '"'))
    except Exception:
        return []

def main():
    df = pd.read_csv(CSV_PATH)

    # Parse signals and orders
    df['signal_parsed'] = df['signal'].apply(parse_signal)
    df['open_orders_parsed'] = df['open_orders'].apply(parse_orders)
    df['take_profits_parsed'] = df['take_profits'].apply(parse_tp)
    df['stop_loss_parsed'] = df['stop_loss'].apply(parse_sl)

    # Basic info
    print("\n--- Info General ---")
    print(df.info())
    print("\n--- Primeras filas ---")
    print(df.head(10))

    # Estadísticas de precios y posición
    print("\n--- Estadísticas de precios ---")
    print(df['last_price'].describe())
    print("\n--- Estadísticas de posición_qty ---")
    print(df['position_qty'].describe())
    print("\n--- Estadísticas de position_avg ---")
    print(df['position_avg'].describe())
    print("\n--- Estadísticas de fees ---")
    print(df['fees'].describe())

    # Número de órdenes abiertas por ciclo
    df['num_open_orders'] = df['open_orders_parsed'].apply(lambda x: len(x))
    print("\n--- Órdenes abiertas por ciclo ---")
    print(df['num_open_orders'].describe())
    print("Máximos:", df['num_open_orders'].max(), "Mínimos:", df['num_open_orders'].min())

    # Ratio TP/SL por ciclo
    df['num_tp'] = df['take_profits_parsed'].apply(lambda x: len(x))
    df['num_sl'] = df['stop_loss_parsed'].apply(lambda x: len(x))
    print("\n--- Ratio Take Profit / Stop Loss ---")
    print("TP totales:", df['num_tp'].sum())
    print("SL totales:", df['num_sl'].sum())
    print("TP/SL ratio:", df['num_tp'].sum() / max(1, df['num_sl'].sum()))

    # Señales utilizadas
    print("\n--- Tipos de señales ---")
    print(df['signal'].value_counts())

    # Evolución de posición y precio
    plt.figure(figsize=(12,4))
    plt.plot(df['timestamp'], df['last_price'], label='Precio')
    plt.plot(df['timestamp'], df['position_avg'], label='Promedio Entrada', alpha=0.7)
    plt.legend()
    plt.xticks(rotation=45)
    plt.title('Evolución Precio y Promedio Entrada')
    plt.tight_layout()
    plt.show()

    # Evolución de cantidad de posición
    plt.figure(figsize=(12,4))
    plt.plot(df['timestamp'], df['position_qty'], label='Cantidad Posición')
    plt.xticks(rotation=45)
    plt.title('Evolución Cantidad de Posición')
    plt.tight_layout()
    plt.show()

    # Evolución de órdenes abiertas
    plt.figure(figsize=(12,4))
    plt.plot(df['timestamp'], df['num_open_orders'], label='Órdenes Abiertas')
    plt.xticks(rotation=45)
    plt.title('Órdenes Abiertas a lo largo del tiempo')
    plt.tight_layout()
    plt.show()

    # Histograma de fees
    plt.figure()
    df['fees'].hist(bins=30)
    plt.title('Distribución de Fees')
    plt.xlabel('Fee')
    plt.ylabel('Frecuencia')
    plt.show()

    # Profit estimado (simple, puedes mejorar)
    # Si tienes la lógica para TP/SL, puedes sumar los profits según fills
    print("\n--- Profit estimado (sólo muestra las fees acumuladas) ---")
    print("Fees totales:", df['fees'].sum())

    # Si tienes fills, podrías sumar el PNL por TP/SL (mejorable si agregas fills al log)

    # Más análisis: añadir drawdown, PNL por sesión, ratio de rebalanceos, etc.
    # Puedes agregar lo que quieras con pandas, por ejemplo:
    # - Agrupar por día y ver profit diario
    # - Ver cuántos ciclos hay entre cada TP/SL
    # - Analizar la relación entre spacing y profit

if __name__ == "__main__":
    main()