import numpy as np


# -----------------------------
# PARTE 2 - CLASSI OOP
# -----------------------------

class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = int(eta)
        self.peso = float(peso)
        self.analisi_effettuate = list(analisi)

    def scheda_personale(self):
        return (
            "SCHEDA PAZIENTE\n"
            f"Nome: {self.nome} {self.cognome}\n"
            f"CF: {self.codice_fiscale}\n"
            f"Età: {self.eta} anni\n"
            f"Peso: {self.peso:.1f} kg\n"
            f"Analisi: {', '.join(self.analisi_effettuate)}"
        )


class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        print(
            f"Il Dr. {self.nome} {self.cognome} "
            f"({self.specializzazione}) sta visitando {paziente.nome} {paziente.cognome}"
        )


class Analisi:
    def __init__(self, tipo, risultato):
        self.tipo = tipo.lower().strip()
        self.risultato = float(risultato)

    def valuta(self):
        # range inventati ma plausibili
        if self.tipo == "glicemia":
            norma_min, norma_max = 70, 110
        elif self.tipo == "colesterolo":
            norma_min, norma_max = 120, 200
        elif self.tipo == "trigliceridi":
            norma_min, norma_max = 0, 150
        elif self.tipo == "creatinina":
            norma_min, norma_max = 0.6, 1.3
        else:
            norma_min, norma_max = 0, 1000  # default

        if norma_min <= self.risultato <= norma_max:
            return "NORMA"
        if self.risultato < norma_min:
            return "BASSO"
        return "ALTO"


# -----------------------------
# PARTE 4 - INTEGRAZIONE OOP + NUMPY
# -----------------------------

class PazienteNumpy(Paziente):
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi, risultati):
        super().__init__(nome, cognome, codice_fiscale, eta, peso, analisi)
        self.risultati_analisi = np.array(risultati, dtype=float)

    def statistiche_analisi(self):
        if self.risultati_analisi.size == 0:
            return "Statistiche: nessun risultato disponibile"

        media = np.mean(self.risultati_analisi)
        minimo = np.min(self.risultati_analisi)
        massimo = np.max(self.risultati_analisi)
        dev_std = np.std(self.risultati_analisi)

        return (
            f"Statistiche: Media={media:.1f}, "
            f"Min={minimo:.1f}, Max={massimo:.1f}, Std={dev_std:.1f}"
        )


# -----------------------------
# MAIN - PARTE 1 / 3 / 5
# -----------------------------

def main():
    print("PARTE 1 - VARIABILI BASE")
    print("=" * 40)

    # Paziente 1
    nome1 = "Mario"
    cognome1 = "Rossi"
    cod_fisc1 = "RSSMRA45D12L219X"
    eta1 = 45
    peso1 = 78.5
    analisi1 = ["emocromo", "glicemia", "colesterolo"]
    print(f"Paziente 1: {nome1} {cognome1}, {eta1} anni, {peso1}kg")
    print(f"Analisi: {analisi1}")

    # Paziente 2
    nome2 = "Anna"
    cognome2 = "Verdi"
    cod_fisc2 = "VRDNNA78B34H567I"
    eta2 = 52
    peso2 = 65.2
    analisi2 = ["glicemia", "colesterolo", "trigliceridi"]
    print(f"Paziente 2: {nome2} {cognome2}, {eta2} anni, {peso2}kg")
    print(f"Analisi: {analisi2}")

    # Paziente 3
    nome3 = "Luca"
    cognome3 = "Bianchi"
    cod_fisc3 = "BNCLCU32E15F890P"
    eta3 = 38
    peso3 = 82.0
    analisi3 = ["emocromo", "creatinina", "glicemia"]
    print(f"Paziente 3: {nome3} {cognome3}, {eta3} anni, {peso3}kg")
    print(f"Analisi: {analisi3}")

    print("\nPARTE 2 - CLASSI OOP")
    print("=" * 40)

    p1 = Paziente(nome1, cognome1, cod_fisc1, eta1, peso1, analisi1)
    print(p1.scheda_personale())
    print()

    m1 = Medico("Giovanni", "Ferri", "Endocrinologo")
    m1.visita_paziente(p1)
    print()

    a1 = Analisi("glicemia", 95)
    a2 = Analisi("colesterolo", 220)
    print(f"{a1.tipo}: {a1.risultato} -> {a1.valuta()}")
    print(f"{a2.tipo}: {a2.risultato} -> {a2.valuta()}")

    print("\nPARTE 3 - NUMPY ARRAY 10 PAZIENTI")
    print("=" * 40)

    risultati_10paz = np.array([95, 112, 88, 145, 102, 78, 130, 99, 115, 92], dtype=float)
    print("Risultati glicemia 10 pazienti:", risultati_10paz)

    print(f"Media: {np.mean(risultati_10paz):.1f}")
    print(f"Max: {np.max(risultati_10paz):.1f}")
    print(f"Min: {np.min(risultati_10paz):.1f}")
    print(f"Dev Std: {np.std(risultati_10paz):.1f}")

    print("\nPARTE 4 - PAZIENTE CON NUMPY")
    print("=" * 40)

    # (la classe PazienteNumpy è già definita sopra, qui la useremo in Parte 5)

    print("PARTE 5 - PROGRAMMA COMPLETO")
    print("=" * 70)

    medici = [
        Medico("Giovanni", "Ferri", "Endocrinologo"),
        Medico("Laura", "Galli", "Cardiologo"),
        Medico("Marco", "Neri", "Ematologo"),
    ]

    pazienti = [
        PazienteNumpy("Mario", "Rossi", "RSSMRA45D12L219X", 45, 78.5,
                      ["glicemia", "colesterolo", "emocromo"], [95, 180, 4500]),
        PazienteNumpy("Anna", "Verdi", "VRDNNA78B34H567I", 52, 65.2,
                      ["glicemia", "trigliceridi", "creatinina"], [112, 150, 0.9]),
        PazienteNumpy("Luca", "Bianchi", "BNCLCU32E15F890P", 38, 82.0,
                      ["emocromo", "glicemia", "colesterolo"], [4800, 88, 220]),
        PazienteNumpy("Sara", "Gialli", "GLISR45M67N321O", 41, 70.1,
                      ["glicemia", "colesterolo", "emocromo"], [102, 195, 4200]),
        PazienteNumpy("Paolo", "Arancio", "RCNPLO78R90S456Q", 60, 85.3,
                      ["colesterolo", "glicemia", "trigliceridi"], [240, 130, 180]),
    ]

    for p in pazienti:
        print(p.scheda_personale())
        print(p.statistiche_analisi())
        print("-" * 40)

    for i, p in enumerate(pazienti):
        medico = medici[i % len(medici)]
        medico.visita_paziente(p)

    print("\nPROGRAMMA COMPLETATO - Pronto per consegna EPICODE!")


if __name__ == "__main__":
    main()
