Feature: Vartotojas su statusu "vadovas" gali užpildyti anketą, kuri jau yra užpildytą iš darbuotojo pusės.
	Background: Darbuotojas Antanas užpildė anketą
		And ji buvo išsiųsta vadovei Linai.

	Scenario: Lina užpildo gautą anketą sėkmingai
		Given vadovo anketos pildymo langas
		When Lina parenka pirmam laukui reikšmę 5
		And antram laukui reikšmę 6
		And trečiam lauke parašo “Nuostabūs šios savaitės pasiekimai”
		And paspaudžia mygtuką “Išsaugoti”
		Then užkraunamas pagrindinis vadovo paskyros puslapis ir parašomas pranešimas “Anketa sėkmingai užpildyta”

	Scenario: Lina užpildo gautą anketą nesėkmingai ir gauna klaidos pranešimą
		Given vadovo anketos pildymo langas
		When Lina parenka pirmam laukui reikšmę 5
		And antram laukui reikšmę 6
		And trečiam lauke parašo “Nuostabūs šios savaitės pasiekimai. Ypač patiko tavo pasiūlymas pakeisti mūsų firmos darbų atlikimo tvarką. Net mano vadovė tai pastebėjo ir labai pagyrė iniciatyvą. Jei kils dar kokių minčių visad lauksim tavo idėjų ir bandysim jas įgyvendint. Taip pat labai noriu pagirti dėl gerų klientų įvertinimo. Esi vienas iš mylimiausių darbuotojų klientų akyse. Būtų gerai, jei sutartume, kada galėtum papasakoti apie tai savo kolegoms. Tačiau tikiuosi iš tavęs geresnės darbo etikos. Dėl to norėčiau pasikalbėti gyvai. Planuokime susitikimą antradienį 15:30 mano kabinete. Jei kas keisis ar netinka mano pasiūlytas laikas, tuomet galime gyvai susitart dėl kito tinkamesnio laiko. Jei tinka, tai tuomet susitiksime antradienį nutartu laiku.”
		And paspaudžia mygtuką “Išsaugoti”
		Then perkraunamas tas pats anketos pildymo puslapis ir parašomas klaidos pranešimas “Atvirame lauke viršytas simbolių limitas”
