"""

=====================================================================

PRIJSCALCULATOR BOUWMATERIALEN

=====================================================================

Berekent de prijs voor bouwmaterialen en houdt een winkelmandje bij.

- Bij Hout wordt gerekend met: meterprijs x meters x aantal
- Prijzen worden beschouwd als inclusief 21% btw; de calculator toont ook excl. btw.

- Bij de rest wordt gerekend met: stukprijs x aantal

-----------------------------------------------------------------

EEN PRIJS AANPASSEN OF EEN NIEUWE MAAT TOEVOEGEN

-----------------------------------------------------------------

Ga naar het blok "PRIJZEN" hieronder en voeg je regel toe op

dezelfde manier als de regels die er al staan, bijvoorbeeld:

   "Vuren": {

       "22x50": {"Ongeschaafd": 1.10, "Geschaafd": 1.45},

       "34x89": {"Ongeschaafd": 2.20},   <-- nieuwe regel

   },

-----------------------------------------------------------------

EEN HELE NIEUWE CATEGORIE TOEVOEGEN (naast Schroeven/Hout/Gips/Platen)

-----------------------------------------------------------------

1. Voeg je prijzen toe aan PRIJZEN. Gebruik dezelfde opbouw als een

   bestaande categorie van hetzelfde "type":

     type "stuk"   (zoals Schroeven)   ->  Soort -> Maat -> prijs (per stuk)

     type "dikte"  (zoals Gips/Platen) ->  Soort -> Maat -> Dikte -> prijs (per plaat, NIET per m²)

     type "meter"  (zoals Hout)        ->  Soort -> Maat -> Afwerking -> prijs (per meter)

2. Voeg een regel toe aan CATEGORIEEN hieronder.

Klaar - de nieuwe categorie staat automatisch in het menu.

=====================================================================

"""

# =====================================================================

# PRIJZEN  (pas hier prijzen aan / voeg regels toe)

# =====================================================================

PRIJZEN = {

    "Schroeven": {

        "Verzinkt": {

           "2.5x16": 0.0175,

           "3.0x16": 0.0175,

           "3.0x20": 0.0175,

           "3.0x30": 0.0175,

           "3.0x35": 0.0175,

           "3.0x40": 0.02,

           "3.5x20": 0.0175,

           "3.5x25": 0.02,

           "3.5x35": 0.0225,

           "3.5x40": 0.025,

           "3.5x50": 0.0275,

           "4.0x20": 0.01875,

           "4.0x30": 0.0225,

           "4.0x40": 0.0275,

           "4.0x50": 0.0325,

           "4.0x60": 0.0375,

           "5.0x40": 0.04,

           "5.0x50": 0.045,

           "5.0x60": 0.0575,

           "5.0x70": 0.0675,

           "5.0x80": 0.075,

           "5.0x90": 0.0925,

           "5.0x100": 0.1,

           "5.0x120": 0.125,

           "6.0x60": 0.07375,

           "6.0x80": 0.1,

           "6.0x100": 0.13,

           "6.0x120": 0.17,

           "6.0x150": 0.225,

           "6.0x200": 0.4,

        },

        "RVS": {

           "3.0x16": 0.019,

           "3.0x20": 0.021,

           "3.0x25": 0.025,

           "3.0x30": 0.0275,

           "3.0x35": 0.0315,

           "3.5x40": 0.042,

           "3.5x45": 0.0415,

           "4.0x25": 0.0345,

           "4.0x30": 0.035,

           "4.0x35": 0.0395,

           "4.0x40": 0.03875,

           "4.0x45": 0.0425,

           "4.0x50": 0.046,

           "4.0x60": 0.06,

           "4.0x70": 0.0675,

           "5.0x40": 0.0625,

           "5.0x50": 0.075,

           "5.0x60": 0.0865,

           "5.0x70": 0.099,

           "5.0x80": 0.12125,

           "5.0x90": 0.1375,

           "5.0x100": 0.15,

           "5.0x120": 0.1875,

           "6.0x60": 0.1275,

           "6.0x80": 0.171,

           "6.0x100": 0.2075,

           "6.0x120": 0.27,

           "6.0x140": 0.4425,

           "6.0x160": 0.52,

        },

        "Boorpuntschroef RVS blanke kop": {

           "4.0x40": 0.075,

           "4.0x50": 0.0875,

           "5.0x40": 0.1,

           "5.0x50": 0.1125,

           "5.0x60": 0.125,

           "5.0x70": 0.1375,

           "5.0x80": 0.15,

           "5.0x100": 0.175,

        },

        "Boorpuntschroef RVS zwarte kop": {

           "4.0x40": 0.0925,

           "4.0x50": 0.1,

           "5.0x40": 0.1125,

           "5.0x50": 0.125,

        },

        "Betonschroef": {

           "6x50": 0.425,

           "6x80": 0.525,

           "6x100": 0.7,

           "8x60": 0.8,

           "8x80": 1,

           "8x100": 1.2,

        },

        "Slagpluggen": {

           "5.0x40": 0.075,

           "5.0x50": 0.08,

           "6.0x40": 0.075,

           "6.0x60": 0.12,

           "6.0x80": 0.14,

           "8.0x60": 0.18,

           "8.0x80": 0.2,

           "8.0x100": 0.24,

           "8.0x120": 0.26,

           "8.0x140": 0.3,

           "10.0x100": 0.46,

           "10.0x120": 0.5,

           "10.0x140": 0.58,

           "10.0x160": 0.8,

        },

        "Slotbouten": {

           "6x25/6x30": 0.065,

           "6x40": 0.08325,

           "6x50": 0.10005,

           "6x60": 0.11385,

           "6x70": 0.1311,

           "6x80": 0.14145,

           "6x100": 0.1863,

           "6x120": 0.2243,

           "8x30": 0.14145,

           "8x40": 0.1573,

           "8x50": 0.1863,

           "8x60": 0.20355,

           "8x70": 0.2277,

           "8x80": 0.2415,

           "8x100": 0.276,

           "8x120": 0.3174,

           "8x140": 0.3726,

           "8x160": 0.414,

           "8x180": 0.5176,

           "8x200": 0.5452,

           "10x80": 0.414,

           "10x100": 0.414,

           "10x120": 0.575,

           "10x140": 0.6072,

           "10x160": 0.6762,

           "10x180": 0.7452,

           "10x200": 0.8556,

           "10x220": 0.9384,

           "10x260": 1.2256,

           "10x280": 1.2972,

        },

        "Moeren en Ringen": {

            "M6": 0.0225,

            "M8": 0.0415,

            "M10": 0.083,

            "M12": 0.18,

            "M16": 0.3,

        },

        "Petschroeven": {

           "6x40": 0.07,

           "6x50": 0.08,

           "6x240": 0.4,

           "8x40": 0.175,

           "8x60": 0.19,

           "8x80": 0.228,

           "8x100": 0.28,

           "8x120": 0.32,

           "8x140": 0.37,

           "8x160": 0.422,

           "8x180": 0.52,

           "8x200": 0.59,

           "8x220": 0.64,

           "8x240": 0.71,

           "8x260": 0.9,

           "8x280": 1.04,

           "8x360": 1.4,

           "8x400": 1.63,

           "10x220": 1.05,

           "10x260": 1.52,

        },

        "Houtdraadbout": {

           "6x40": 0.0325,

           "6x50": 0.0375,

           "6x60": 0.047,

           "6x70": 0.0535,

           "6x80": 0.065,

           "8x40": 0.0625,

           "8x50": 0.07,

           "8x60": 0.08,

           "8x80": 0.1025,

           "8x100": 0.13,

           "8x120": 0.155,

           "8x140": 0.18,

           "8x160": 0.215,

           "10x50": 0.132,

           "10x60": 0.145,

           "10x70": 0.16,

           "10x80": 0.175,

           "10x100": 0.21,

           "10x120": 0.26,

           "10x140": 0.29,

           "10x160": 0.35,

        },

        "Spijkers met platte kop": {

            "1.0x15 300g": 3.75,

        },

        "Spijkers met bolle kop": {

            "1.0x15 300g": 6.75,

        },

        "Schalienagels": {

            "3.0x20 1kg": 7.5,

        },

    },

    "IJzerwaren": {

        "Scharnieren": {

            "scharnieren": {

                "51x39": 2,

                "76x51": 2.75,

                "76x76": 2.75,

                "76x76 RVS": 6.25,

                "76x76 + pen": 3.25,

            },

            "Kogellagerscharnier": {

            },

            "kogellagerscharnier met klauw": {

            },

        },

        "Plankendragers": {

        },

        "Raveeldragers": {

        },

        "hoekijzers": {

        },

    },

    "Kit en Pur": {

        "Kit": {

            "Illbruck Construction kit": 9,

            "Bruislijm": 9,

            "Acrylaat kit wit": 6,

            "Polymax": 10.5,

            "Bitumen kit": 7.5,

            "Constructie kit zwart": 9,

            "Hertalan EPDM": 15,

            "Kozijnenlijm Frencken": 15,

            "Glas kit": 9,

            "High Tech": 9,

            "Hybraseal": 9,

            "Kitspuit economy": 7.5,

            "Kitspuit premium": 20,

            "Siliconen kit": 7.50,

            "siliconen kit antraciet": 12,

        },

        "Pur": { 

            "Pur pistool": 20,

            "pur reiniger": 7,

            "Normale pur/met spriet": 5,

            "Montageschuim pur": 5.6,

            "Flexibele pur": 6.5,

            "elastische pur": 6.5,

            "steenlijm/pur": 8.5,

        },

    },

    "Hout": {

        "Hardhout": {

            "16x145 tuinplank keruing": {"geschaafd": 5.75},

            "22x145 vlonderplank": {"geschaafd": 7.5},

            "25x145 vlonderplank bankirai": {"geschaafd": 8},

            "28x145 vlonderplank": {"geschaafd": 9.5},

            "28x145 tuinplank keruing": {"geschaafd": 8.5},

            "28x190 geschaafd keruing": {"geschaafd": 13.15},

            "0.6x100 hardhoutstrip": {"ruw": 1.75},

            "20x45": {"ruw": 1.4},

            "20x100": {"ruw": 4.25},

            "20x150": {"ruw": 6.5},

            "20x200": {"ruw": 8.5},

            "25x25": {"ruw": 2},

            "25x90": {"geschaafd": 3},

            "28mm damwand": {"ruw": 54.50},

            "28x135 damwand": {"ruw of geschaafd": 7.25},

            "28x150": {"ruw": 8.5},

            "28x185 damwand": {"ruw of geschaafd": 10.75},

            "30x200": {"ruw": 11.5},

            "30x250": {"ruw": 13},

            "39x70": {"geschaafd": 4},

            "40mm damwand": {"ruw of geschaafd": 76.95},

            "40x40": {"ruw": 2.5},

            "45x70": {"geschaafd": 6},

            "45x90": {"geschaafd": 7.6},

            "48x185": {"ruw of geschaafd": 9.35},

            "50x50": {"geschaafd": 2, "ruw": 3},

            "50x150": {"ruw": 12.5},

            "50x200": {"ruw": 20},

            "58x185": {"ruw of geschaafd": 9.65},

            "60x60": {"ruw": 5},

            "65x65": {"geschaafd": 8},

            "68x68": {"geschaafd": 8},

            "70x70": {"ruw": 8},

            "80x80": {"ruw": 10.5},

            "80x150": {"ruw": 20},

            "88x88": {"geschaafd": 15},

            "100x100": {"ruw": 12},

            "100x200": {"ruw": 33.4},

            "120x120": {"ruw": 24},

            "150x150": {"ruw": 30},


        },

        "Douglas": {

            "22x50": {"Ongeschaafd": 1.45, "Geschaafd": 1.85},

            "28x70": {"Ongeschaafd": 2.10},

            "45x145": {"Ongeschaafd": 5.60},

        },

        "Geïmpregneerd": {

            "22x50": {"Ongeschaafd": 1.55, "Geschaafd": 1.95},

            "28x70": {"Ongeschaafd": 2.25},

        },

        "Eiken": {

            "20x100": {"Ongeschaafd": 6.50, "Geschaafd": 7.90},

        },

        "Vuren": {

            "45x95": {"geschaafd": 2.42},

            "45x70": {"geschaafd": 1.78},

            "45x45": {"geschaafd": 1.25},

        },

    },

    # Let op: prijs = prijs per hele plaat (stuk), NIET per m²

    "Gips": {

        "Groen": {

            "2600x600": {"9.5": 13.56, "12.5": 12.85},

            "2600x1200": {"12.5": 25.71},

        },

        "Wit": {

            "2600x1200": {"9.5": 8.95, "12.5": 10.25},

        },

    },

    # Let op: prijs = prijs per hele plaat (stuk), NIET per m²

    "Platen": {

        "Betonplex": {

            "2500x1250": {"18": 42.50, "21": 49.90},

        },

        "Altrifloor underlayment": {

            "2440x1220": {"6": 18.50, "9": 24.90},

        },

        "Sudati underlayment": {

            "2440x1220": {"6": 17.90, "9": 23.50},

        },

        "Meranti multiplex": {

            "2500x1220": {"12": 35.00, "18": 48.50},

        },

        "Berken": {

            "2500x1250": {"12": 39.90, "18": 54.90},

        },

        "Trespa": {

            "2550x1860": {"8": 89.00, "10": 105.00},

        },

        "OSB": {

            "2500x1250": {"12": 15.90, "18": 21.50},

        },

        "Spano": {

            "2440x1220": {"18": 19.90, "22": 23.90},

        },

        "MDF": {

            "2440x1220": {"12": 17.50, "18": 22.90},

        },

        "Tipoply": {

            "2440x1220": {"12": 24.90},

        },

        "Okoume": {

            "2500x1220": {"12": 33.50, "18": 46.90},

        },

    },

    "Isolatie": {
        "Steenwol": {
            "50mm": 7.29,
            "60mm": 8.59,
        },
        "Pir 60x120": {
            "20mm": 8,
        },
        "Glaswol Volcalis": {
            "85mm": 7.2,
        },
    },

    "Verf": {

       "Rubber Seal": {

           "750 ml": 17.50,

           "2,5L": 37.50,

           "Koker": 8.00,

           "Textielband 10cm x 10mtr": 13.50,

           "Reparatiekit": 22.50,

       },

       "Olie": {

          "Bankirai Olie": {

              "Bankirai": {

                  "1L": 12.70,

                  "2,5L": 30.50,

              },

           },

           "Scheepsteer": {

               "Scheepsteer":{

                   "750ML": 12.50,

                   "2,5L": 35.00,

               },

           },

       },

          "Verf": {

             "Aquafiller": {

                 "Betonverf": {

                     "1L": 17.50,

                     "2,5L": 40.00,

                     },

                 },

             },

         "Beits": {

             "Betonverf": {

                 "Betonverf": {

                     "1L": 17.50,

                     "2,5L": 40.00,

                 },

             },

             "Bruinoleum": {

                 "Bruinoleum": {

                     "2,5L": 14.73,

                 },

             },

             "Cronostain": {

                 "Zwart": {

                     "1L": 17.25,

                     "2,5L": 32.00,

                     "10L": 95.00

                 },

             },

             "Tuinbeits": {

                 "Groen": {

                     "1L": 10.00,

                     "2,5L": 25.00,

                 },

             },

             "Remmers": {

                 "Zwart": {

                     "750ML": 20.00,

                     "2,5L": 45.00,

                 },

                 "Lichtgrijs/Donkergrijs": {

                     "750ML": 25.00,

                     "2,5L": 60.00,

                 },

                 "platinagrijs": {

                     "750ML": 25.00,

                     "2,5L": 57.50,

                 },

                 "HK-Lazuur": {

                     "750ML": 20.00,

                     "2,5L": 45.00,

                     "10L": 110.00,

                 },

                 "Long-Life": {

                     "750ML": 27.50,

                     "2,5L": 55.00,

                 },

                 "Wit": {

                     "750ML": 25.00,

                     "2,5L": 60.00,

                 },

             },

             "Pine beits": {

                 "blank": {

                     "1L": 12.19,

                     "2,5L": 28.97,

                 },

             },

             "Steigerhoutbeits": {

                 "Steigerhoutbeits": {

                     "1L": 12.71,

                     "2,5L": 25.41,

                 },

             },

             "Tuinhoutolie": { 

                 "Tuinhoutolie": {

                     "1L": 17.50,

                     "2,5L": 37.50,

                 },

             },

             "Ventilatielak": {

                 "Ventilatielak": {

                     "750ML": 35.00,

                     "2,5L": 85.00,

                 },

             },

         },

     }

}

# =====================================================================

# CATEGORIEËN  (koppelt elke categorie aan zijn "type" vragenlijst)

# =====================================================================

CATEGORIEEN = [

   {"naam": "Schroeven", "sleutel": "Schroeven", "type": "stuk"},

   {"naam": "IJzerwaren", "sleutel": "IJzerwaren", "type": "ijzerwaren"},

   {"naam": "Kit en Pur", "sleutel": "Kit en Pur", "type": "stuk"},

   {"naam": "Hout",      "sleutel": "Hout",      "type": "meter"},

   {"naam": "Gips",      "sleutel": "Gips",      "type": "dikte"},

   {"naam": "Platen",    "sleutel": "Platen",    "type": "dikte"},

   {"naam": "Verf",      "sleutel": "Verf",      "type": "Verf"},
   {"naam": "Isolatie", "sleutel": "Isolatie", "type": "Isolatie"},

]

# =====================================================================

# HULPFUNCTIES

# =====================================================================

BTW_PERCENTAGE = 0.21

# Prijzen in PRIJZEN worden beschouwd als prijzen INCLUSIEF 21% btw.
WINKELMANDJE = []


class GeenOptiesError(Exception):
   """Wordt gebruikt wanneer een categorie nog geen producten bevat."""


class OngeldigePrijsError(Exception):
   """Wordt gebruikt wanneer een prijs 0 of negatief is."""


def kies_uit_lijst(vraag, opties):

   """Laat de gebruiker kiezen uit een genummerde lijst."""

   if not opties:
       print(f"\nFOUT: {vraag} bevat nog geen producten of opties.")
       raise GeenOptiesError

   print(f"\n{vraag}")

   for i, optie in enumerate(opties, start=1):

       print(f"  {i}. {optie}")

   while True:

       keuze = input("Keuze (nummer): ").strip()

       if keuze.isdigit() and 1 <= int(keuze) <= len(opties):

           return opties[int(keuze) - 1]

       print("Ongeldige keuze, probeer opnieuw.")


def vraag_getal(vraag, is_geheel=False):

   """Vraagt een positief getal; accepteert komma of punt als decimaalteken."""

   while True:

       antwoord = input(f"{vraag}: ").strip().replace(",", ".")

       try:

           waarde = int(antwoord) if is_geheel else float(antwoord)

           if waarde > 0:

               return waarde

       except ValueError:

           pass

       print("Vul een geldig getal in (bijv. 3 of 3,5).")


def eur(bedrag):

   """Formatteert een bedrag als Nederlandse euro-notatie, bv. € 1.234,56"""

   tekst = f"{bedrag:,.2f}"

   tekst = tekst.replace(",", "X").replace(".", ",").replace("X", ".")

   return f"€ {tekst}"


def controleer_prijs(prijs, omschrijving="dit product"):

   """Controleert of een prijs groter dan 0 is."""

   if prijs <= 0:

       raise OngeldigePrijsError(
           f"FOUT: voor {omschrijving} is nog geen geldige prijs ingevuld."
       )

   return prijs


def controleer_prijzen(data, pad=None):

   """Zoekt door alle prijsgegevens naar prijzen van 0 of lager."""

   if pad is None:
       pad = []

   fouten = []

   for sleutel, waarde in data.items():

       huidig_pad = pad + [str(sleutel)]

       if isinstance(waarde, dict):

           fouten.extend(controleer_prijzen(waarde, huidig_pad))

       elif isinstance(waarde, (int, float)) and waarde <= 0:

           fouten.append((" -> ".join(huidig_pad), waarde))

   return fouten


def toon_resultaat(naam, regels, totaal, prijs_per_eenheid=None,
                   eenheid="stuk", aantal=None):

   totaal_incl_btw = totaal
   totaal_excl_btw = totaal_incl_btw / (1 + BTW_PERCENTAGE)

   print(f"\n--- Resultaat: {naam} ---")

   for label, waarde in regels:

       print(f"{label + ':':<18}{waarde}")

   print(f"{'TOTAAL incl. btw:':<18}{eur(totaal_incl_btw)}")
   print(f"{'TOTAAL excl. btw:':<18}{eur(totaal_excl_btw)}")

   WINKELMANDJE.append({
       "naam": naam,
       "regels": regels,
       "incl_btw": totaal_incl_btw,
       "excl_btw": totaal_excl_btw,
       "prijs_per_eenheid": prijs_per_eenheid,
       "eenheid": eenheid,
       "aantal": aantal,
   })


def toon_winkelmandje():

   if not WINKELMANDJE:

       print("\nHet winkelmandje is leeg.")

       return

   totaal_incl_btw = sum(item["incl_btw"] for item in WINKELMANDJE)
   totaal_excl_btw = sum(item["excl_btw"] for item in WINKELMANDJE)

   print("\n" + "=" * 65)
   print(" WINKELMANDJE")
   print("=" * 65)

   for nummer, item in enumerate(WINKELMANDJE, start=1):

       print(f"\n{nummer}. {item['naam']}")

       if item["aantal"] is not None:
           print(f"   Aantal: {item['aantal']}")

       if item["prijs_per_eenheid"] is not None:
           print(
               f"   Prijs per {item['eenheid']}: "
               f"{eur(item['prijs_per_eenheid'])} incl. btw"
           )

       print(f"   Totaal incl. btw: {eur(item['incl_btw'])}")
       print(f"   Totaal excl. btw: {eur(item['excl_btw'])}")

   print("-" * 65)
   print(f"{'TOTAAL incl. btw:':<35}{eur(totaal_incl_btw)}")
   print(f"{'TOTAAL excl. btw:':<35}{eur(totaal_excl_btw)}")

# =====================================================================

# REKENFUNCTIES PER TYPE

# =====================================================================

def bereken_stuk(sleutel, naam):

   """Soort -> Maat -> Aantal.  Totaal = stukprijs x aantal."""

   data = PRIJZEN[sleutel]

   soort = kies_uit_lijst(f"Welke soort {naam.lower()}?", list(data.keys()))

   maat = kies_uit_lijst("Welke maat?", list(data[soort].keys()))

   prijs = controleer_prijs(
       data[soort][maat],
       f"{naam} - {soort} - {maat}"
   )

   aantal = vraag_getal("Aantal", is_geheel=True)

   totaal = prijs * aantal

   toon_resultaat(naam, [

       ("Soort", soort),

       ("Maat", maat),

       ("Stukprijs", eur(prijs)),

       ("Aantal", str(aantal)),

   ], totaal, prijs_per_eenheid=prijs, aantal=aantal)

   return totaal

def bereken_dikte(sleutel, naam):

   """Soort -> Maat -> Dikte -> Aantal.  Totaal = stukprijs x aantal."""

   data = PRIJZEN[sleutel]

   soort = kies_uit_lijst(f"Welke soort {naam.lower()}?", list(data.keys()))

   maat = kies_uit_lijst("Welke maat?", list(data[soort].keys()))

   dikten = list(data[soort][maat].keys())

   dikte = kies_uit_lijst("Welke dikte?", [f"{d} mm" for d in dikten])

   dikte_key = dikte.replace(" mm", "")

   prijs = controleer_prijs(
       data[soort][maat][dikte_key],
       f"{naam} - {soort} - {maat} - {dikte_key} mm"
   )

   aantal = vraag_getal("Aantal", is_geheel=True)

   totaal = prijs * aantal

   toon_resultaat(naam, [

       ("Soort", soort),

       ("Maat", maat),

       ("Dikte", f"{dikte_key} mm"),

       ("Stukprijs", eur(prijs)),

       ("Aantal", str(aantal)),

   ], totaal, prijs_per_eenheid=prijs, aantal=aantal)

   return totaal

def bereken_meter(sleutel, naam):

   """Soort -> Maat -> Afwerking -> Aantal -> Meters.  Totaal = meterprijs x meters x aantal."""

   data = PRIJZEN[sleutel]

   soort = kies_uit_lijst(f"Welke soort {naam.lower()}?", list(data.keys()))

   maat = kies_uit_lijst("Welke maat (mm)?", list(data[soort].keys()))

   afwerkingen = list(data[soort][maat].keys())

   # Als er maar één afwerking beschikbaar is, automatisch kiezen
   # en dit als opmerking bewaren.
   if len(afwerkingen) == 1:

       afwerking = afwerkingen[0]

       melding = f"Deze houtsoort is alleen {afwerking}"

       print(f"\\n{melding}")

   else:

       afwerking = kies_uit_lijst(
           "Ongeschaafd of geschaafd?",
           afwerkingen
       )

       melding = None

   meterprijs = controleer_prijs(
       data[soort][maat][afwerking],
       f"{naam} - {soort} - {maat} - {afwerking}"
   )

   aantal = vraag_getal("Aantal stuks", is_geheel=True)

   meters = vraag_getal("Lengte per stuk in meters")

   totaal = meterprijs * meters * aantal

   regels = [

       ("Soort", soort),

       ("Maat", f"{maat} mm"),

       ("Afwerking", afwerking),

   ]

   if melding:

       regels.append(("Opmerking", melding))

   regels.extend([

       ("Meterprijs", eur(meterprijs)),

       ("Lengte", f"{meters} m"),

       ("Aantal", f"{aantal} stuks"),

   ])

   toon_resultaat(
       naam,
       regels,
       totaal,
       prijs_per_eenheid=meterprijs,
       eenheid="meter",
       aantal=f"{aantal} stuks ({meters} m per stuk)"
   )

   return totaal

def bereken_verf(sleutel, naam):

    data = PRIJZEN[sleutel]

    categorie = kies_uit_lijst(

        "Welke soort?",

        list(data.keys())

    )

    # Rubber Seal heeft geen soort/kleur/liter

    if categorie == "Rubber Seal":

        product = kies_uit_lijst(

            "Welke Rubber Seal?",

            list(data[categorie].keys())

        )

        prijs = controleer_prijs(
            data[categorie][product],
            f"{naam} - {categorie} - {product}"
        )

        aantal = vraag_getal("Aantal", is_geheel=True)

        totaal = prijs * aantal

        toon_resultaat(naam, [

            ("Categorie", categorie),

            ("Product", product),

            ("Prijs", eur(prijs)),

            ("Aantal", str(aantal)),

        ], totaal, prijs_per_eenheid=prijs, aantal=aantal)

        return totaal


    # Olie, Verf en Beits

    soort = kies_uit_lijst(

        "Welke soort?",

        list(data[categorie].keys())

    )

    kleur = kies_uit_lijst(

        "Welke kleur?",

        list(data[categorie][soort].keys())

    )

    liter = kies_uit_lijst(

        "Welke inhoud?",

        list(data[categorie][soort][kleur].keys())

    )

    prijs = controleer_prijs(
        data[categorie][soort][kleur][liter],
        f"{naam} - {categorie} - {soort} - {kleur} - {liter}"
    )

    aantal = vraag_getal("Aantal", is_geheel=True)

    totaal = prijs * aantal

    toon_resultaat(naam, [

        ("Categorie", categorie),

        ("Soort", soort),

        ("Kleur", kleur),

        ("Inhoud", liter),

        ("Prijs", eur(prijs)),

        ("Aantal", str(aantal)),

    ], totaal, prijs_per_eenheid=prijs, aantal=aantal)

    return totaal

def bereken_ijzerwaren(sleutel, naam):

    data = PRIJZEN[sleutel]

    soort1 = kies_uit_lijst(

        f"Welke soort {naam.lower()}?",

        list(data.keys())

    )

    soort2 = kies_uit_lijst(

        "Welke uitvoering?",

        list(data[soort1].keys())

    )

    maat = kies_uit_lijst(

        "Welke maat?",

        list(data[soort1][soort2].keys())

    )

    prijs = controleer_prijs(
        data[soort1][soort2][maat],
        f"{naam} - {soort1} - {soort2} - {maat}"
    )

    aantal = vraag_getal("Aantal", is_geheel=True)

    totaal = prijs * aantal

    toon_resultaat(naam, [

        ("Soort", soort1),

        ("Uitvoering", soort2),

        ("Maat", maat),

        ("Stukprijs", eur(prijs)),

        ("Aantal", str(aantal)),

    ], totaal)

    return totaal

def bereken_isolatie(sleutel, naam):

    """Isolatie -> Dikte -> Vierkante meters.
    Totaal = prijs per m² x aantal m².
    """

    data = PRIJZEN[sleutel]

    # Kies soort isolatie
    soort = kies_uit_lijst(
        f"Welke soort {naam.lower()}?",
        list(data.keys())
    )

    # Kies dikte
    dikten = list(data[soort].keys())

    dikte = kies_uit_lijst(
        "Welke dikte?",
        [f"{d} mm" for d in dikten]
    )

    # Haal de echte key zonder " mm" op
    dikte_key = dikte.replace(" mm", "")

    # Prijs per vierkante meter
    prijs = controleer_prijs(
        data[soort][dikte_key],
        f"{naam} - {soort} - {dikte_key} mm"
    )

    # Vraag aantal vierkante meters
    vierkante_meter = vraag_getal(
        "Hoeveel vierkante meter?",
        is_geheel=False
    )

    # Berekening
    totaal = prijs * vierkante_meter

    toon_resultaat(naam, [

        ("Soort", soort),

        ("Dikte", f"{dikte_key} mm"),

        ("Prijs per m²", eur(prijs)),

        ("Oppervlakte", f"{vierkante_meter} m²"),

    ], totaal, prijs_per_eenheid=prijs, eenheid="m²",
    aantal=f"{vierkante_meter} m²")

    return totaal

REKENFUNCTIES = {

   "stuk": bereken_stuk,

   "dikte": bereken_dikte,

   "meter": bereken_meter,

   "Verf": bereken_verf,

   "ijzerwaren": bereken_ijzerwaren,

   "Isolatie": bereken_isolatie,

}

# =====================================================================

# HOOFDMENU

# =====================================================================

def hoofdmenu():

   print("=" * 55)

   print(" PRIJSCALCULATOR BOUWMATERIALEN")

   print("=" * 55)

   ongeldige_prijzen = controleer_prijzen(PRIJZEN)

   if ongeldige_prijzen:

       print("\nWAARSCHUWING: de volgende prijzen zijn 0 of negatief:")

       for pad, prijs in ongeldige_prijzen:

           print(f"  - {pad}: {eur(prijs)}")

       print("Vul deze prijzen aan voordat je deze producten gebruikt.\n")

   while True:

       namen = [c["naam"] for c in CATEGORIEEN]

       keuze = kies_uit_lijst("Wat wil je berekenen?", namen)

       categorie = next(c for c in CATEGORIEEN if c["naam"] == keuze)

       functie = REKENFUNCTIES[categorie["type"]]

       try:

           functie(categorie["sleutel"], categorie["naam"])

       except GeenOptiesError:

           # De foutmelding is al getoond. Ga terug naar het hoofdmenu.

           pass

       except OngeldigePrijsError as fout:

           print(f"\n{fout}")

       opnieuw = input("\nNog een berekening doen? (j/n): ").strip().lower()

       if opnieuw != "j":

           toon_winkelmandje()

           print("\nDoei")

           break

if __name__ == "__main__":

   try:

       hoofdmenu()

   except KeyboardInterrupt:

       print("\n\nAfgebroken.")