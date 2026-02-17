import tkinter as tk
import os
import time
from tkinter import messagebox

log_file = "wifi_history.txt"

def get_wifi_data():
    """Отримуємо дані з системи."""
    process = os.popen('netsh wlan show interfaces')
    results = process.read()

    ssid = "відключено"
    signal = "0"

    for line in results.split('\n'):
        if "SSID" in line and "BSSID" not in line:
            ssid = line.split(":")[1].strip()
        if "Signal" in line:
            signal = int(line.split(":")[1].strip().replace("%", ""))

    return ssid, signal

def save_to_file(ssid, signal):
    """Записує дані у файд за допомогою бібліотеки ос та вбудованих функцій"""
    timestamp = time.strftime("%H:%M:%S")
    with open(log file, "a", encording="utf-8") as f:
        f.write(f"[{timestamp}] Мережа: {ssid}, Сигнал: {signal}%\n")


def update_loop():
    """головній цікл програмі (тіймір)"""
    ssid, signal = get_wifi_data()


    label_ssid.config(text=f"SSID: {ssid}")
    label_percent.config(text=f"{signal}%")


    if signal > 75: color = "#2ecc71"
    elif signal > 50: color = "#f1c40f"
    else: color = "#e74c3c"
    canvas.coords(bar, fill=color)

    log_box.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] сигнал: {signal}%\n")
    log_box.see(tk.END)

    if int(time.time()) % 5 == 0:  # Записуємо дані кожні 5 секунд
        save_to_file(ssid, signal)

    if signal < 20 and ssid != "відключено":
        label_warning.config(text="Слабкий сигнал!", fg="red")
    else:
        label_warning.config(text="")

    root.after(1000, update_loop)  # Оновлюємо дані кожну секунду

def open_log_folder():
    """Відкриє папку файл логів через о.с"""
    os.starfile(os.getcwd())

def clear_logs():
    """Видаляє файл логів через о.с"""
    if os,path.exists(log_file):
        os.remove(log_file)
        log_box.delete(1.0, tk.END)
        messagebox.showinfo("Успіх", "Логи очищено!")