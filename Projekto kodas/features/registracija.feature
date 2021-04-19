Feature: Vartotojas su statusu "kompanija" gali priregistruoti kompaniją prie sistemos.
	Background: Dar sistemoje nepriregistruota kompanija bando priregistruoti savo kompaniją prie sistemos.

	Scenario: Kompanija užsiregistruoja sistemoje sėkmingai
		Given registracijos langas.
		When Kompaniją bandantis priregistruoti žmogus prie Kompanijos pavadinimo lauko įrašo “Kompanija A”
		And prie kompanijos el. pašto lauko įrašo “kompanija_a@email.com”
		And prie slaptažodžio lauko įrašo “kompanijaa123”
		And prie pakartokite slaptažodį lauko įrašo “kompanijaa123”
		And paspaudžia mygtuką “užsiregistruoti”
		Then užkraunamas prisijungimo puslapis ir parašomas pranešimas “Užsiregistravote, galite prisijungti”.

	Scenario: Kompanijai nepavyksta užsiregistruoti sistemoje, nes suklysta atkartojant slaptažodį.
		Given registracijos langas.
		When Kompaniją bandantis priregistruoti žmogus prie Kompanijos pavadinimo lauko įrašo “Kompanija A”
		And prie kompanijos el. pašto lauko įrašo “kompanija_a@email.com”
		And prie slaptažodžio lauko įrašo “kompanijaa123”
		And prie pakartokite slaptažodį lauko įrašo “kompanijaa12”
		And paspaudžia mygtuką “užsiregistruoti”
		Then užkraunamas tas pats registracijos puslapis iš naujo ir parašomas pranešimas “Slaptažodžiai nesutampa”.
	
	Scenario: Kompanijai nepavyksta užsiregistruoti sistemoje, nes įrašo jau sistemoje išsaugotą kompanijos pavadinimą
		Given registracijos langas.
		When Kompaniją bandantis priregistruoti žmogus prie Kompanijos pavadinimo lauko įrašo “Pavyzdys”
		And prie kompanijos el. pašto lauko įrašo “kompanija_a@email.com”
		And prie slaptažodžio lauko įrašo “kompanijaa123”
		And prie pakartokite slaptažodį lauko įrašo “kompanijaa123”
		And paspaudžia mygtuką “užsiregistruoti”
		Then užkraunamas tas pats registracijos puslapis iš naujo ir parašomas pranešimas “Kompanija su tokiu pavadinimu jau yra užregistruota.”.
		
	Scenario: Kompanijai nepavyksta užsiregistruoti sistemoje, nes įrašo jau sistemoje išsaugotą kompanijos el. paštą
		Given registracijos langas.
		When Kompaniją bandantis priregistruoti žmogus prie Kompanijos pavadinimo lauko įrašo “Kompanija A”
		And prie kompanijos el. pašto lauko įrašo “pvz@pvz.lt“
		And prie slaptažodžio lauko įrašo “kompanijaa123”
		And prie pakartokite slaptažodį lauko įrašo “kompanijaa123”
		And paspaudžia mygtuką “užsiregistruoti”
		Then užkraunamas tas pats registracijos puslapis iš naujo ir parašomas pranešimas “Toks el. paštas jau yra naudojamas.”.
		
	Scenario: Kompanijai nepavyksta užsiregistruoti sistemoje, nes palieka tuščią kompanijos pavadinimo lauką
		Given registracijos langas.
		When Kompaniją bandantis priregistruoti žmogus Kompanijos pavadinimo lauką palieka tuščią
		And prie kompanijos el. pašto lauko įrašo “kompanija_a@email.com“
		And prie slaptažodžio lauko įrašo “kompanijaa123”
		And prie pakartokite slaptažodį lauko įrašo “kompanijaa123”
		And paspaudžia mygtuką “užsiregistruoti”
		Then užkraunamas tas pats registracijos puslapis iš naujo ir parašomas pranešimas “Kompanijos pavadinimas yra privalomas laukas.”.
		
	Scenario: Kompanijai nepavyksta užsiregistruoti sistemoje, nes palieka tuščią kompanijos el. pašto lauką
		Given registracijos langas.
		When Kompaniją bandantis priregistruoti žmogus prie Kompanijos pavadinimo lauko įrašo “Kompanija A”
		And kompanijos el. pašto lauką palieka tuščią
		And prie slaptažodžio lauko įrašo “kompanijaa123”
		And prie pakartokite slaptažodį lauko įrašo “kompanijaa123”
		And paspaudžia mygtuką “užsiregistruoti”
		Then užkraunamas tas pats registracijos puslapis iš naujo ir parašomas pranešimas “El. paštas yra privalomas laukas. El. pašto adresas turi susidaryti iš 6-50 simbolių. El. pašto adresas neatitinka reikiamos struktūros”.
