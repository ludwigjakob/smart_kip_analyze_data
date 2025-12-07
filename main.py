import pandas as pd
from common.data_connector.temperature_connector import TemperatureConnector
from skopt import gp_minimize

def cost(threshold, df):
    """
    Kostenfunktion für die Optimierung:
    - Energieverbrauch = Summe der Fan-On-Zeiten
    - Penalty = Temperatur > threshold+2 trotz Lüfter
    """
    # Energieverbrauch: tatsächliche Lüfterlaufzeit
    energy = df["fan_status"].sum()

    # Penalty: Temperatur über threshold+2 trotz Lüfter
    penalty = ((df["temperature"] > (threshold + 2)) & (df["fan_status"] == 1)).sum() * 10

    return energy + penalty


def main():
    # Connector initialisieren
    connector = TemperatureConnector()


    # Daten der letzten 7 Tage als DataFrame abrufen
    df = connector.read_trainingdata_7_days_df()


    # Erste Zeilen anzeigen
    print("Erste Werte der letzten 7 Tage:")
    print(df.head())

    # Statistik über die Werte
    print("\nStatistische Übersicht:")
    print(df.describe())

    res = gp_minimize(lambda x: cost(x[0], df), [(10, 30)], n_calls=30)

    print("\nOptimierter Schwellwert:", res.x[0])


if __name__ == "__main__":
    main()
