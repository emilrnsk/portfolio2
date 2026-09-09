import math
import statistics

print("Willkommen beim ultimativen Taschenrechner!")
print("Geben Sie 'exit' ein, um das Programm jederzeit zu beenden.")

while True:
    print("-" * 40)
    print("Modi: [1] Mathe  [2] Statistik  [3] Umrechner")
    modus = input("Wählen Sie einen Modus (1, 2, 3 oder 'exit'): ")
    
    if modus.lower() == 'exit':
        print("Auf Wiedersehen!")
        break

    # MODUS 1: Grundlegende und fortgeschrittene Mathematik
    if modus == '1':
        num1_str = input("Geben Sie die erste Zahl ein: ")
        if num1_str.lower() == 'exit': break
        
        try:
            num1 = float(num1_str)
        except ValueError:
            print("Fehler! Bitte geben Sie eine gültige Zahl ein.")
            continue

        operator = input("Operator (+, -, *, /, ^, %, sqrt, sin, cos, tan, ln, log, !): ")

        if operator in ['sqrt', 'sin', 'cos', 'tan', 'ln', '!']:
            if operator == 'sqrt':
                result = math.sqrt(num1) if num1 >= 0 else "Fehler! Quadratwurzel aus negativer Zahl."
            elif operator == 'sin':
                result = math.sin(math.radians(num1))
            elif operator == 'cos':
                result = math.cos(math.radians(num1))
            elif operator == 'tan':
                result = math.tan(math.radians(num1))
            elif operator == 'ln':
                result = math.log(num1) if num1 > 0 else "Fehler! Logarithmus aus nicht-positiver Zahl."
            elif operator == '!':
                result = math.factorial(int(num1)) if num1 >= 0 and num1.is_integer() else "Fehler! Fakultät nur für nicht-negative ganze Zahlen."
            else:
                result = "Unbekannter Operator"
        else:
            num2_str = input("Geben Sie die zweite Zahl ein: ")
            if num2_str.lower() == 'exit': break
            try:
                num2 = float(num2_str)
            except ValueError:
                print("Fehler! Bitte geben Sie eine gültige Zahl ein.")
                continue

            if operator == '+': result = num1 + num2
            elif operator == '-': result = num1 - num2
            elif operator == '*': result = num1 * num2
            elif operator == '/': result = num1 / num2 if num2 != 0 else "Fehler! Division durch Null."
            elif operator == '^': result = num1 ** num2
            elif operator == '%': result = num1 % num2 if num2 != 0 else "Fehler! Division durch Null."
            elif operator == 'log':
                if num1 > 0 and num2 > 0 and num2 != 1:
                    result = math.log(num1, num2)
                else:
                    result = "Fehler! Ungültige Werte für Logarithmus."
            else:
                result = "Unbekannter Operator"

        print("Ergebnis:", result)

    # MODUS 2: Statistik
    elif modus == '2':
        zahlen_str = input("Geben Sie die Zahlen durch Leerzeichen getrennt ein (z.B. 5 10 15 20): ")
        if zahlen_str.lower() == 'exit': break
        
        try:
            # Die eingegebene Zeile in eine Liste von Zahlen umwandeln
            zahlen = [float(x) for x in zahlen_str.split()]
            if not zahlen:
                print("Fehler! Keine Zahlen eingegeben.")
                continue
            
            stat_op = input("Operation (mean, median, stdev): ")
            if stat_op == 'mean':
                print("Ergebnis (Mittelwert / Durchschnitt):", statistics.mean(zahlen))
            elif stat_op == 'median':
                print("Ergebnis (Median):", statistics.median(zahlen))
            elif stat_op == 'stdev':
                if len(zahlen) > 1:
                    print("Ergebnis (Standardabweichung):", statistics.stdev(zahlen))
                else:
                    print("Fehler! Für die Standardabweichung werden mindestens zwei Zahlen benötigt.")
            else:
                print("Fehler! Unbekannte Operation.")
        except ValueError:
            print("Fehler! Bitte geben Sie nur gültige Zahlen ein (verwenden Sie Punkte statt Kommas für Dezimalzahlen).")

    # MODUS 3: Umrechner
    elif modus == '3':
        print("Verfügbare Umrechnungen: km_to_m, m_to_cm, kg_to_g, c_to_f (Celsius zu Fahrenheit)")
        umrechner_op = input("Wählen Sie die Umrechnung: ")
        if umrechner_op.lower() == 'exit': break
        
        wert_str = input("Geben Sie den Wert ein: ")
        if wert_str.lower() == 'exit': break
        
        try:
            wert = float(wert_str)
            if umrechner_op == 'km_to_m': print("Ergebnis:", wert * 1000, "m")
            elif umrechner_op == 'm_to_cm': print("Ergebnis:", wert * 100, "cm")
            elif umrechner_op == 'kg_to_g': print("Ergebnis:", wert * 1000, "g")
            elif umrechner_op == 'c_to_f': print("Ergebnis:", (wert * 9/5) + 32, "°F")
            else: print("Fehler! Unbekannte Umrechnung.")
        except ValueError:
            print("Fehler! Bitte geben Sie eine gültige Zahl ein.")
    
    else:
        print("Fehler! Unbekannter Modus. Bitte 1, 2 oder 3 wählen.")