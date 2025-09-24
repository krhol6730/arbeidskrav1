"""
Sammenlikning av årlige kostnader for elbil og bensinbil
Kristian Holmås (krhol6730@usn.no)
Oppdatert 2025 09 24
"""

lengde = 10000  # [km/år]

forsikringelbil = 5000  # [kr/år]
forsikringbensinbil = 7500  # [kr/år]

trafikkforsikring = 8.38 * 365  # [kr/år]

elforbruk = 0.2  #[kWh/km]
elpris = 2.00  # [kr/kWh]
elkostnad = elforbruk*elpris*lengde # [kr/år]

bensinpris = 1.00  #[kr/km]
bensinkostnad = bensinpris * lengde  # [kr/år]

elbompris = 0.1  # [kr/km]
elbomkostnad = elbompris * lengde  # [kr/år]

bensinbompris = 0.3  # [kr/km]
bensinbomkostnad = bensinbompris * lengde  # [kr/år]

elbilkostnad = forsikringelbil + trafikkforsikring + elkostnad + elbomkostnad  # [kr/år]
bensinbilkostnad = forsikringbensinbil + trafikkforsikring + bensinkostnad + bensinbomkostnad  # [kr/år]
kostnadsdifferanse = elbilkostnad - bensinbilkostnad  # [kr/år]

print('Elbilkostnad = ', elbilkostnad)
print('Bensinbilkostnad = ', bensinbilkostnad)
print('Kostnadsdifferense = ', kostnadsdifferanse)