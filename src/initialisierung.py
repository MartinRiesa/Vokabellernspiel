# src/initialisierung.py

import os
import pandas as pd
from PIL import Image, ImageTk

# Pfade zu den CSV-Dateien im assets/data-Verzeichnis
CSV_VOCAB = os.path.join("assets", "data", "Vokabeln alle.csv")
CSV_STATIONS = os.path.join("assets", "data", "Stationenbeschreibung-englisch.csv")

def load_game_data(learn_lang: str, native_lang: str):
    """
    Lädt aus der Vokabel- und Stations-CSV die benötigten Daten.
    Gibt (stations_df, vocab_levels_df) zurück.
    """
    # Vokabeln
    df_vocab = pd.read_csv(CSV_VOCAB, sep=';', encoding='utf-8-sig')
    # Stationsbeschreibungen
    df_st = pd.read_csv(CSV_STATIONS, sep=';', encoding='utf-8-sig')

    # Filtern nach Sprachen
    vocab_levels = df_vocab[[learn_lang, native_lang]]
    stations = df_st

    return stations, vocab_levels

def init_game_state(app, stations, vocab_levels):
    """
    Initialisiert den Spielzustand in der App-Instanz:
    - app.level, app.questions, app.current_question etc.
    """
    try:
        # Beispiel: Level starten bei 1, Fragen aus dem vocab_levels
        app.level = 1
        app.questions = vocab_levels.values.tolist()
        app.current_question = 0
        return True
    except Exception as e:
        from tkinter import messagebox
        messagebox.showerror("Fehler", f"Spiel konnte nicht initialisiert werden:\n{e}")
        return False

def build_ui(app):
    """
    Erstellt die Haupt-GUI: Canvas, Buttons, Labels etc.
    Verwendet PIL für Bild-Laden falls notwendig.
    """
    # Beispielhafter Aufbau
    app.root.title("Vokabellernspiel")
    # ... weitere UI-Elemente hier anlegen ...
