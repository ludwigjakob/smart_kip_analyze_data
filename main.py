import pandas as pd
from common.data_connector.temperature_connector import TemperatureConnector
from skopt import gp_minimize
from common.utils.debug import Debugger

debug = Debugger()

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
    debug.log("Erste Werte der letzten 7 Tage:", label="Analysis App")
    debug.log(df.head(), label="Analysis App")

    # Statistik über die Werte
    debug.log("\nStatistische Übersicht:", label="Analysis App")
    debug.log(df.describe(), label="Analysis App")

    res = gp_minimize(lambda x: cost(x[0], df), [(10, 30)], n_calls=30)

    debug.log(f"\nOptimierter Schwellwert:{res.x[0]}", label="Analysis App")


if __name__ == "__main__":
    main()
