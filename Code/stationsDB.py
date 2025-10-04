# made a stationsDB, just add like every unique city in the 2nd column
# probably run this once then imma copy the output and hardcode it
# but bcs wrote this code im keeping the deadcode effort credit thx
"""
import connections
testfile = "smol.csv"
file = "eu_rail_network.csv"
uniquecity = []
data = connections.csvDB(file)
for row in data:
    if row[1] not in uniquecity:
        uniquecity.append(row[1])
print(uniquecity)
"""

stations = ['A CoruÃ±a', 'Aalborg', 'Aarhus', 'Alicante', 'AlmerÃ\xada',
            'Amiens', 'Amsterdam', 'Ancona', 'Angers', 'Annecy',
            'Antwerp', 'Arezzo', 'Ashford', 'Augsburg', 'Avignon',
            'Badajoz', 'Barcelona', 'Bari', 'Basel', 'Belgrade',
            'Bergamo', 'Bergen', 'Berlin', 'Bern', 'BesanÃ§on', 'Bilbao',
            'Birmingham', 'Bochum', 'Bologna', 'Bolzano', 'Bonn',
            'Bordeaux', 'Bratislava', 'BraÈ™ov', 'Bremen', 'Brescia',
            'Brest', 'Brighton', 'Brindisi', 'Bristol', 'Brno', 'Bruges',
            'Brussels', 'Bucharest', 'Budapest', 'Burgas', 'Burgos',
            'Calais', 'Cambridge', 'Cardiff', 'Cartagena', 'Catania',
            'ChambÃ©ry', 'Clermont-Ferrand', 'Cluj-Napoca', 'Cologne',
            'Como', 'Copenhagen', 'Cork', 'Cuenca', 'CÃ¡diz', 'CÃ³rdoba',
            'Debrecen', 'Derby', 'Dijon', 'Dortmund', 'Drammen',
            'Dresden', 'Dublin', 'DÃ¼sseldorf',
            'Edinburgh', 'Eindhoven', 'Essen', 'Exeter',
            'Ferrara', 'Florence', 'ForlÃ¬', 'Frankfurt',
            'Galway', 'GdaÅ„sk', 'Gdynia', 'Geneva', 'Genoa', 'Ghent',
            'Glasgow', 'Gothenburg', 'Granada', 'Graz', 'Grenoble',
            'Hamburg', 'Hannover', 'Heidelberg', 'Helsingborg', 'Helsinki',
            'IaÈ™i', 'Innsbruck',
            'Karlsruhe', 'Katowice', 'Kiel', 'KoÅ¡ice', 'Krakow',
            "L'Aquila", 'La Rochelle', 'La Spezia', 'Lausanne',
            'Le Mans', 'Leeds', 'Leicester', 'Leipzig', 'Lille',
            'Limerick', 'Limoges', 'LinkÃ¶ping', 'Linz', 'Lisbon',
            'Liverpool', 'Livorno', 'LiÃ¨ge', 'Ljubljana', 'LogroÃ±o',
            'London', 'Lublin', 'Lucerne', 'Lugano', 'Lund', 'Lyon',
            'Madrid', 'MalmÃ¶', 'Manchester', 'Mannheim', 'Maribor',
            'Marseille', 'Messina', 'Metz', 'Milan', 'Modena', 'Montpellier',
            'Mostar', 'Mulhouse', 'Munich', 'Murcia', 'MÃ¡laga',
            'Nancy', 'Nantes', 'Naples', 'Narbonne', 'Newcastle', 'Nice', 'NiÅ¡',
            'NorrkÃ¶ping', 'Nottingham', 'Novi Sad', 'Nuremberg', 'NÃ®mes',
            'Odense', 'Oslo', 'Ostrava', 'Oulu', 'Oviedo', 'Oxford',
            'Padua', 'Palermo', 'Pamplona', 'Paris', 'Parma', 'Perpignan',
            'Perugia', 'Piacenza', 'Pisa', 'Plovdiv', 'Plymouth', 'PlzeÅˆ',
            'Poitiers', 'Porto', 'Portsmouth', 'Potsdam', 'PoznaÅ„', 'Prague', 'PÃ©cs',
            'Ravenna', 'Reading', 'Regensburg', 'Reggio Calabria', 'Reggio Emilia', 'Reims',
            'Rennes', 'Rijeka', 'Rimini', 'Rome', 'Rostock', 'Rotterdam', 'Rouen',
            'Salamanca', 'Salerno', 'Salzburg', 'San SebastiÃ¡n', 'Santander',
            'Santiago de Compostela', 'Sarajevo', 'Seville', 'Sheffield', 'Sofia',
            'Sopot', 'Southampton', 'Split', 'St. Gallen', 'Stavanger',
            'Stockholm', 'Strasbourg', 'Stuttgart', 'Swansea', 'Szeged',
            'Tampere', 'Taranto', 'Terni', 'The Hague', 'Thessaloniki',
            'TimiÈ™oara', 'Toledo', 'Toulouse', 'Tours', 'Trento', 'Trieste',
            'Trondheim', 'Turin', 'Turku',
            'Uppsala', 'Utrecht',
            'Valencia', 'Valladolid', 'Varna', 'Venice', 'Verona',
            'Versailles', 'Vicenza', 'Vienna', 'Vigo', 'VÃ¤sterÃ¥s',
            'Warsaw', 'WrocÅ‚aw', 'WÃ¼rzburg',
            'York',
            'Zagreb', 'Zaragoza', 'Zurich',
            'Ã–rebro', 'ÄŒeskÃ© BudÄ›jovice', 'ÅÃ³dÅº']
