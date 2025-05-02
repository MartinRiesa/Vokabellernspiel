# src/initialisierung.py

import os
import pandas as pd
from PIL import Image, ImageTk

# Importiere poster_loader und nenne es poster
import poster_loader as poster

# Pfade zu den CSV-Dateien
CSV_VOCAB = os.path.join("assets", "data", "Vokabeln alle.csv")
CSV_STATIONS = os.path.join("assets", "data", "Stationenbeschreibung-englisch.csv")


def load_game_data(learn_lang: str, native_lang: str):
    """
    Lädt Vokabel- und Stationsdaten aus den CSV-Dateien und
    filtert die Vokabeln nach den gewählten Sprachen.
    """
    df_vocab = pd.read_csv(CSV_VOCAB, sep=';', encoding='utf-8-sig')
    df_st = pd.read_csv(CSV_STATIONS, sep=';', encoding='utf-8-sig')

    vocab_levels = df_vocab[[learn_lang, native_lang]]
    stations = df_st

    return stations, vocab_levels


def init_game_state(app, stations, vocab_levels):
    """
    Initialisiert den Spielzustand in der App-Instanz:
    level, questions, current_question etc.
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
    Erstellt die GUI-Grundlage: Fenster-Titel, Canvas, Buttons etc.
    """
    app.root.title("Vokabellernspiel")
    # Hier kannst Du weitere UI-Elemente anlegen, z.B. Canvas:
    # app.canvas = tk.Canvas(app.root, width=800, height=600)
    # app.canvas.pack()


def load_poster(app, level):
    """
    Wrapper-Funktion, die das korrekte Poster lädt und anzeigt.
    Verwendet poster.display_poster aus poster_loader.py.
    """
    # Erzeuge den Pfad zur Poster-Datei (falls Du Poster-Dateien nach Level benennst)
    # Beispiel: poster_datei = f"assets/data/poster_level_{level}.png"
    # Für jetzt übernimmst Du, was poster_loader selbst erwartet:
    return poster.display_poster(app, poster.load_poster_image, level)
