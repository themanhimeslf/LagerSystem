# Intro
Dette er et lagersystem som bruker Pythom som hoved kode, og json for lagring & henting av lagret data.
Meste parten av koden er forklart via "#"

men i prinsippet lar det bruker
Registrere nye varer med informasjon som varenummer, navn, kategori, pris og antall.

Redigere og slette varer fra lageret.

Søke etter varer og vise lagerstatus.

Lagre og hente data fra en fil (output.json) slik at dataene ikke går tapt mellom kjøringer.


# Hvord




## Data
# Når data lagres:
Hver gang en vare registreres eller slettes, oppdateres lagersystem["vareliste"].

Etter oppdatering, brukes json.dump() for å skrive de nye dataene tilbake til output.json.

Dette gjør at dataene er permanente og ikke forsvinner når programmet avsluttes.

#  Når data lastes:
Når programmet starter, sjekker det om output.json finnes.

Hvis filen finnes, leses innholdet inn i variabelen lagersystem ved hjelp av json.load().

Hvis filen ikke finnes, starter programmet med et tomt lager.


