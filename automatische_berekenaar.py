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

        "(dop)/(oog)Moeren en Ringen": {

            "M6 Moeren en Ringen": 0.0225,
            "M6 Dopmoeren": 0.25,
            "M6 Oogmoeren": 1,
            "M8 Moeren en Ringen": 0.0415,
            "M8 Dopmoeren": 0.30,
            "M8 Oogmoeren": 1,
            "M10 Moeren en Ringen": 0.083,
            "M10 Dopmoeren": 0.63,
            "M10 Oogmoeren": 1.5,
            "M12 Moeren en Ringen": 0.18,
            "M12 Dopmoeren": 0.78,
            "M12 Oogmoeren": 1.5,
            "M14 Oogmoeren": 2,
            "M16 Moeren en Ringen": 0.3,
            "M16 Oogmoeren": 2.25,

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

        "Spijkers met platte kop per doos": {

            "1.0x15 300g": 3.75,
            "1.2x20 400g": 3.75,
            "1.5x25 425g": 3.75,
            "1.8x30 470g": 3.75,
            "2.0x35 600g": 3.75,
            "2.0x40 700g": 3.75,
            "2.7x50 725g": 3.75,
            "2.7x60 750g": 3.75,
            "3.5x80 750g": 3.75,
            "4.0x100 750g": 3.75,
            "boomspijkers 2,5kg": 10,
        },

        "Spijkers met bolle kop per doos": {

            "1.0x15 300g": 6.75,
            "1.2x20 400g": 6.75,
            "1.5x25 425g": 6.75,
            "1.8x30 470g": 6.75,
            "2.0x35 550g": 6.75,
            "2.0x40 600g": 6.75,
            "2.2x45 650g": 6.75,
            "2.7x50 700g": 6.75,
            "2.7x55 700g": 7.5,
            "2.7x60 725g": 7.5,
            "RVS 2.4x50 1kg": 35,
        },

        "Schalienagels per doos": {
            "3.0x20 270g": 4,
            "3.0x20 1kg": 7.5,

        },

        "Blauw geharde Staalspijkers per doos": {
            "2.0x20 200g": 4.5,
            "2.4x30 200g": 4.5,
            "3.0x40 375g": 4.5,
            "3.0x50 375g": 4.5,

        },

        "Krammen per doos": {
            "1.8x15 200g": 4.75,
            "2.0x20 260g": 3.75,
            "2.7x25 325g": 3.75,
            "3.0x30 350g": 4,
            "3.5x35 350g": 4.75,
            "1.8x15 1kg": 12.75,
            "2.0x20 1kg": 12,
            "2.7x25 1kg": 10,
            "3.0x30 1kg": 9.75,
            "4.0x40 1kg": 9.75,
            "schroefnagel 3.8x32 200st": 8,
            "schroefnagel 3.8x40 1000st": 20,
        },

        "Schietspijkers/nagels per doos": {
            "Goldlook 30mm": 35,
            "Goldlook 40mm": 42.5,
            "Goldlook 50mm": 30,
            "Afwerknagel 20mm": 11,
            "Afwerknagel 40mm": 14.5,
            "Afwerknagel 50mm": 17.5,
        },

        "Overige spijkers per doos": {
            "draadnagels 5kg": 17.78,
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

        "Rolmaten, mesjes, hamers etc": {
            "Rolmaten en duimstokken": { 
                "Cosmos 3m": 8.25,
                "Cosmos 5m": 11.25,
                "Cosmos 8m": 14.5,
                "Stanley 5m": 17.8,
                "Stanley 8m": 25,
                "Duimstok kunstof": 7.5,
                "Duimstok hout": 14,
               
            },
            "hamers en bijlen": {
                "Hamer cosmos": 12.5,
                "Hamer 4tecx": 15,
            },
            "zagen, mesjes, bits en potloden": {
                "Handzaag Bahco": 12.5,
                "Mesjes": 5,
                "alle bits": 1,
                "bitset klein": 15,
                "bitset groot": 20,
                "potlood": 1.5,
            },
            "Waterpas": {
                "400mm": 16.5,
                "600mm": 18.5,
                "1000mm": 27.5,
                "1800mm": 55,
            },
            "Lijmtang": {
                "500x120mm staal": 55,
                "600x120mm staal": 57.5,
                "600x120mm gegoten kop": 42.5,
            },

        },
        "Boren": {
            "SDS boor": {
                "6mm": 4.5,
                "6x260mm": 6,
                "8mm": 4.5,
                "10mm": 5.6,
                "10x260mm": 6.5,
                "12mm": 6.6,
                "14mm": 8.65,
                "14x300mm": 9,
                "16x150": 9,
                "18x200": 15,
                "18x400": 15,
                "40mm verlengd": 30,
            },
            "vlinderboor": {
                "6, 8, 10, 12 of 13mm": 2.55,
                "14, 16, 17, 18, 19 of 20mm": 2.8,
                "22, 24 of 25mm": 3.3,
                "28, 30 of 32mm": 3.55,
                "35, 38 of 40mm": 4.3,
                "6x400mm verlengd": 4.5,
                "8/10/12x400mm verlengd": 5,
                "18x400mm verlengd": 6,
            },
            "HSS boor blank": {
                "1mm": 1,
                "1,5mm": 1,
                "2mm": 1.5,
                "2,5mm": 1.5,
                "3mm": 2.5,
                "3,5mm": 2.8,
                "4mm": 2.8,
                "4,5mm": 3.05,
                "5mm": 3.05,
                "5,5mm": 3.55,
                "6mm": 3.55,
                "6,5mm": 3.55,
                "7mm": 3.55,
                "7,5mm": 6.1,
                "8mm": 6.1,
                "8mm lang": 9.15,
                "9mm": 6.1,
                "9,5mm": 6.1,
                "10mm": 6.6,
                "10mm lang 175mm": 9.5,
                "HSS boorset": 27.5,
                "Gatenboorset": 25,
            },
            "HSS bekistingsboor": {
                "6x400mm": 10,
                "8x400mm": 12.5,
                "8x600mm": 15,
                "10x400mm": 15,
                "10x600mm": 18,
                "12x400mm": 20,
                "12x600mm": 22.5,
                "14x400mm": 25,
                "14x600mm": 27.5,
                "16x400mm": 27.5,
                "16x600mm": 30,
                "6x460mm zeskant opname": 10,
                "8x460mm zeskant opname": 12.5,
            },
            "Slangenboor": {
                "6x235mm": 10,
                "8x235mm": 10,
                "8x450mm": 14.5,
                "10x235mm": 13,
                "10x450mm": 20,
                "12x235mm": 15,
                "12x450mm": 20,
                "14x235mm": 15,
                "14x450mm": 22.5,
                "16x235mm": 20,

            },
            "Overige boren": {
                "speedboor set 6 tot 25mm 14st": 30,
                "verzinkboor 3/4/5mm": 7.1,
                "verzinkboor 13mm": 10,
                "verzinkboor 16mm": 15,
                "trespaboor": 3.5,

            },
        }, 
        "Wielen": {
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
            "22x45": {"geschaafd": 0.6},

            "45x45": {"geschaafd": 1.25},

            "45x70": {"geschaafd": 1.78},

            "45x95": {"geschaafd": 2.42},

        },

    },

    # Let op: prijs = prijs per hele plaat (stuk), NIET per m²

    "Gips": {

        "Groen": {

            "2600x600": {"9.5": 13.56, "12.5": 12.85},

            "2600x1200": {"12.5": 25.71},

        },

        "Wit": {
            "60x200": {"9,5": 5.47},
            "60x260": {"9,5": 7.11, "12.5": 7.92},
            "60x300": {"9,5": 8.21, "12,5": 9.14},
            "60x360": {"9,5": 9.85, "12,5": 10.97},
            "60x420": {"9,5": 11.49},
            "120x260": {"12,5": 14.04},
            "120x300": {"12,5": 16.2},

        },

    },

    # Let op: prijs = prijs per hele plaat (stuk), NIET per m²

    "Platen": {

        "Betonplex": {
            "125x250 zwart": {"4": 21.85, "6": 24.5, "10": 52.5, "10 as": 57.5, "12": 62.5, "12 as": 72.5, "15": 85, "15 as": 90, "18 B-Keus": 45, "18": 90, "18 as": 95, "21 as": 110},
            "125x250 lichtbruin": {"7": 40, "9": 86.5, "12": 98.8, "15": 111.2, "18": 117.65},
            "150x300 lichtbruin": {"12": 162.95, "15": 173.35, "18": 197.55},
            "215x385 lichtbruin": {"18 as": 356},
            "215x400 lichtbruin": {"18 as": 395},
        },

        "underlayment": {
            "61x244": {"18 Altrifloor": 29},
            "122x244": {"9": 17.5, "18 sudati": 35, "18  Altrifloor": 45},
        },
        "Meranti": {
           "122x244": {"3.6": 15, "5.5": 17.5, "8": 17.5, "9": 27.5, "12": 36.5, "15": 45.5, "18": 50, "22": 88.6, "25": 108.5},
        },

        "Berken": {
            "95x215 gegrond": {"40": 179},
            "122x250 gegrond": {"9": 58, "18": 89},
            "125x250 blank": {"6": 38, "9": 48.3, "12": 58.8, "15": 70.35, "18": 87.5, "40": 243.2},
            "153x305 gegrond": {"6": 100},
        },

        "Trespa": {
            "130x305": {"6": 35.57, "6 gekleurd": 45},

        },

        "OSB": {
            "61x244": {"9": 8.5, "12": 11.2, "18": 15.05},
            "122x244": {"9": 16.85, "18": 31.15},
        },

        "Spano": {
            "61x244": {"12": 11.25, "18": 14},
            "91x244": {"18": 22},
            "122x244": {"18": 28},
        },

        "MDF": {
            "122x244 blank": {"6": 13, "9": 17.25, "12": 20.5, "15": 24.5, "18": 34.5, "22": 40.5, "25": 45, "28": 55, "38": 75},
            "122x244 gegrond": {"9": 33, "12": 33.9, "15": 41, "18": 44.65, "22": 63, "25": 74},
            "122x244 Groen": {"6": 18, "9": 25.15, "12": 27.2, "12 wit": 47.85, "15": 42.5, "18": 55.5, "18 wit": 60, "22": 75, "22 wit": 80, "25": 90},
            "122x305 blank": {"12": 27, "18": 41},
            "122x305 groen/wit/blank": {"9 wit": 37.5, "12 blank": 27, "12 wit": 47, "12 groen": 47.5, "12 groen/wit": 47.8, "18 groen": 65, "18 blank": 41, "18 wit": 67, "18 groen/wit": 67,},
        },
        "Tipoply": {
            "122x244 wit": {"9": 48.7, "12": 55.55, "15": 63.55, "18": 69.75, "22": 86.25},
            "122x244 blank": {"9": 27.5, "12": 35, "15": 40, "18": 52.5},

        },

        "Okoume": {
            "95x215": {"40": 122.5, "40 wit": 150},
            "100x215": {"40": 132.5, "40 wit": 156},
            "105x235": {"40": 147, "40 wit": 155},
            "122x250 blank": {"4": 25.41, "6": 34.57, "8": 38.13, "10": 47.5, "12": 53.75, "15": 61, "18": 91.75, "40": 180.65},
            "122x250 wit": {"8": 50.82, "10": 58.46, "12": 70.25, "15": 81.35, "18": 101.1, "40": 210.5},
            "153x305 blank": {"40": 395},
            "153x310 wit": {"10": 126.2, "12": 140.34, "15": 159.75, "18": 172.43},
        },

    },

    "Isolatie": {
        "Steenwol doorzichtig": {
            "50mm": 7.29,
            "60mm": 8.59,
            "70mm": 10.13,
            "90mm": 13.13,
            "100mm": 14.589,
            "120mm": 16.89,
        },
        "Pir 60x120": {
            "20mm": 8,
            "30mm": 9.95,
            "40mm": 11.65,
            "50mm": 13.85,
            "60mm": 15.8,
            "70mm": 17.75,
            "80mm": 19.75,
            "90mm": 22.21875,
            "100mm": 23.85,
            "120mm": 27.8,
            "140mm": 28.85,
        },
        "Glaswol Volcalis": {
            "85mm": 7.2,
        },
    },
   
   "overig spul in winkel": {
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
   {"naam": "Overig spul in winkel", "sleutel": "Overig spul in winkel", "type": "ijzerwaren"},

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