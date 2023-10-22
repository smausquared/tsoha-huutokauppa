# Huutokauppasovellus
Sovelluksella voi seurata nopeita kahden minuutin huutokauppoja. Ylläpitäjä voi lisätä huutokaupattavia esineitä, joita käyttäjät voivat huutaa.

Sovelluksella on seuraavanlaisia ominaisuuksia:
* Käyttäjä voi luoda uuden tunnuksen ja kirjautua sisään. ✓
* Käyttäjä näkee etusivulla nykyisen (✓), edellisen ja seuraavan huutokaupattavan esineen. Hän voi nähdä edellisen esineen voittajan ja myyntiajankohdan ja -hinnan.
* Käyttäjä näkee, miten pitkään nykyinen huutokauppa kestää ✓.
* Käyttäjä voi myös huutaa nykyistä esinettä mielivaltaisella korotuksella tai ennalta valituilla korotuksilla, esim. 5e, 10e, 20e (✓).
* Ylläpitäjä voi lisätä huudettavia esineitä.
* Ylläpitäjä voi peruuttaa nykyisen huutokaupan.

## Asennus
Aktivoi virtuaaliympäristö:
```bash
python3 -m venv venv
souce venv/bin/activate
```

Asenna riippuvuudet:
```bash
pip install -r requirements.txt
```

Alusta tietokanta:
```bash
psql < schema.sql
```

Käynnistä sovellus:
```bash
flask run
```
