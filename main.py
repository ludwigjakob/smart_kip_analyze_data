import pandas as pd
from common.data_connector.temperature_connector import TemperatureConnector

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

if __name__ == "__main__":
    main()
