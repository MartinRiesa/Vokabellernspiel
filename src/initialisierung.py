# src/initialisierung.py

import os
import pandas as pd
from PIL import Image, ImageTk

# Wir importieren hier Dein poster_loader-Modul unter dem Namen "poster"
import poster_loader as poster

# Pfade zu den CSV-Dateien im assets/data-Verzeichnis
CSV_VOCAB = os.path.join("assets", "data", "Vokabeln alle.csv")
CSV_STATIONS = os.path.join("assets", "data", "Stationenbeschreibung-englisch.csv")

def load_game_data(learn_lang: str, native_lang: str):
    """
    Lädt aus der Vokabel- und Stations-CSV die benötigten Daten.
    Gibt (stations_df, vocab_levels_df) zurück.
    """
    df_vocab = pd.read_csv(CSV_VOCAB, sep=';', encoding='utf-8-sig')
    df_st = pd.read_csv(CSV_STATIONS, sep=';', encoding='utf-8-sig')

    vocab_levels = df_vocab[[learn_lang, native_lang]]
    stations = df_st

    return stations, vocab_levels

def init_game_state(app, stations, vocab_levels):
    """
    Initialisiert den Spielzustand in der App-Instanz.
    """
    try:
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
    Erstellt die Haupt-GUI-Elemente.
    """
    app.root.title("Vokabellernspiel")
    # (Weitere UI-Elemente…)

def load_poster(app, level):
    """
    Wrapper, damit main.py initialisierung.load_poster aufruft.
    """
    return poster.load_poster(app, level)
