Feature: Vartotojas su statusu "vadovas" gali pakeisti darbuotojo informaciją.
	Background: Kompanijos vadovas, kurio kompanija yra priregistruota prie sistemos ir darbuotojas Jonas Jonaitis, bei kompanijos vadovas nori pakeisti jo asmeninę informaciją.

	Scenario: Kompanijos vadovas sėkmingai pakeičia darbuotojo vardą.
		Given puslapis pavadinimu "Jonasss Jonaitis profilis".
		When kompanijos vadovas lauke „Vardas“ pakeičia vartotojo vardą iš „Jonasss“ į „Jonas“
		And paspaudžia mygtuką „Atnaujinti informaciją“
		Then kompanijos vadovas patenka į darbuotojų sąrašo puslapį ir pamato, kad darbuotojo vardas yra pakeistas į "Jonas", bei viršuje atsiranda pranešimas „Sėkmingai atnaujinta informacija“.

	Scenario: Kompanijos vadovui nepavyksta pakeisti darbuotojo el.pašto, nes naujas įvestas el.paštas neatitinka reikiamos struktūros
		Given puslapis pavadinimu "Jonas Jonaitis profilis".
		When kompanijos vadovas lauke „El.paštas“ pakeičia vartotojo paštą iš „jonas.jonaitis@gmail.com“ į „j.jonaitisgmail.com“
		And paspaudžia mygtuką „Atnaujinti informaciją“
		Then kompanijos vadovui užkraunamas tas pats "Jonas Jonaitis profilis" puslapis iš naujo ir po lauko “El.paštas” atsiranda pranešimas “El.pašto adresas neatitinka reikiamos struktūros”.

	Scenario: Kompanijos vadovui nepavyksta pakeisti darbuotojo vardo, nes palieka tuščią vardo lauką.
		Given puslapis pavadinimu "Jonas Jonaitis profilis".
		When kompanijos vadovas lauke „Vardas” ištrina seną vardą ir paskui pamiršta užpildyti vardo lauką
		And paspaudžia mygtuką „Atnaujinti informaciją“
		Then kompanijos vadovui užkraunamas tas pats "Jonas Jonaitis profilis" puslapis iš naujo ir po lauko “Vardas” atsiranda pranešimas “Vardas turi susidaryti iš 1-60 simbolių”.









