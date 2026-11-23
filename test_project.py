import project
from project import get_rounds
from project import check_round
from project import get_sample
import pytest

# Now, since our function get_rounds does not take any parameter, but simply asks for a number and checks if it is a valid number of rounds,
# we use monkeypatch, which is a tool to simulate the entry of data. 
def test_get_rounds(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "7") # This sets the built in value that we would input via keyboad with a constant 
    # function that returns "7" no matter what.
    assert get_rounds() == 7

    inputs = iter(["cat", "-2", "-4", "4"]) # Here iter is a standard python object which is essentially a list that gives one value at the time
    # in order, when we call next.
    monkeypatch.setattr("builtins.input", lambda _: next(inputs)) # Here we simulate that the input given via keyboard is given by
    # "cat", then "-2" then "0" and then finally "4". 
    assert get_rounds() == 4

    inputs = iter(["dog", "&*^*&*", "qicdb", "1"]) # Here iter is a standard python object which is essentially a list that gives one value at the time
    # in order, when we call next.
    monkeypatch.setattr("builtins.input", lambda _: next(inputs)) 
    assert get_rounds() == 1


def test_check_round(): 
    # We write here two of our entries of the dataset, so that we can test them locally
    entry1 =   {
    "language": ["Montenegrin", "Serbian", "Bosnian", "Croatian", "Albanian"],
    "country": ["Montenegro"],
    "city": [
      "Podgorica", "Nikšić", "Herceg Novi", "Pljevlja", "Bijelo Polje",
      "Bar", "Berane", "Cetinje", "Ulcinj", "Budva",
      "Tivat", "Kotor", "Rožaje", "Danilovgrad", "Plužine",
      "Žabljak", "Mojkovac", "Andrijevica", "Šavnik", "Petnjica",
      "Gusinje", "Tuzi", "Kolašin", "Šavnik", "Risan",
      "Sutomore", "Bečići", "Perast", "Igalo", "Petrovac",
      "Dobrota", "Stari Bar", "Virpazar", "Donja Gorica", "Golubovci",
      "Orahovac", "Lastva", "Grbalj", "Kaluđerski Laz", "Velika",
      "Vranjina", "Crkvice", "Murino", "Božaj", "Komani",
      "Spuž", "Plav", "Mataguži", "Đenovići", "Lepetane",
      "Zelenika", "Baošići", "Njeguši", "Đurđevića Tara", "Krnjača",
      "Gornja Lastva", "Bać", "Donji Kokoti", "Vrmci", "Godičelj",
      "Orahovac", "Pavlova Strana", "Donji Morinj", "Babino Polje", "Vidrovan",
      "Grbalj", "Radovan", "Slatina", "Ravna Rijeka", "Donji Stoliv"
    ],
    "alphabet": "A B C Č Ć D Dž Đ E F G H I J K L Lj M N Nj O P R S Š T U V Z Ž"
    }
    
    entry2 = {
      "language": ["Italian"],
      "country": ["Italy"],
      "city": [
        "Roma", "Milano", "Napoli", "Torino", "Palermo",
        "Genova", "Bologna", "Firenze", "Bari", "Catania",
        "Venezia", "Verona", "Messina", "Padova", "Trieste",
        "Taranto", "Brescia", "Parma", "Modena", "Reggio Calabria",
        "Perugia", "Livorno", "Ravenna", "Cagliari", "Foggia",
        "Trento", "Siracusa", "Latina", "Monza", "Bergamo",
        "Pescara", "Forlì", "Vicenza", "Terni", "Novara",
        "Piacenza", "Ancona", "Arezzo", "Udine", "Bolzano",
        "La Spezia", "Pistoia", "Alessandria", "Cesena", "Pesaro",
        "Lucca", "Como", "Treviso", "Rimini", "Ferrara",
        "Lecce", "Salerno", "Grosseto", "Cremona", "Cosenza",
        "Potenza", "Siena", "Crotone", "Pisa", "Mantova",
        "Viterbo", "Asti", "Savona", "L'Aquila", "Matera",
        "Ragusa", "Trapani", "Vibo Valentia", "Brindisi", "Benevento",
        "Avellino", "Caserta", "Isernia", "Campobasso", "Aosta"
      ],
      "alphabet": "A B C D E F G H I L M N O P Q R S T U V Z"
        }

    assert check_round(entry1, "montenegro") == 1
    assert check_round(entry1, "Montenegro") == 1
    assert check_round(entry1, "bosnian") == 1
    assert check_round(entry1, "spanish") == 0
    assert check_round(entry1, "mon tenegro") == 0
    assert check_round(entry1, "") == 0
    assert check_round(entry1, "russian") == 0

    assert check_round(entry2, "italy") == 1
    assert check_round(entry2, "ITALY") == 1
    assert check_round(entry2, "italian") == 1
    assert check_round(entry2, "ItaLIAn") == 1
    assert check_round(entry2, "swedish") == 0


def test_get_sample(): # Here we check the optional sample size feature. 
    # We check that if we don't specify anything, or we add invalid values, we get back the default value 5. We also check of course that
    # when we specify a valid value, the function returns it correctly (9).
    assert get_sample(5, ["project.py"]) == 5
    assert get_sample(5, ["project.py", "9"]) == 9
    assert get_sample(5, ["project.py", "cats and dogs"]) == 5
    assert get_sample(5, ["project.py", "-20"]) == 5
    

