Feature: Vartotojas su statusu "darbuotojas" gali pakeisti savo slaptažodį.
	Background: Jei sistemoje yra priregistruotas vartotojas Antanas Antanaitis ir jis yra prisijungęs prie sistemos su el.paštu “antanas.antanaitis@email.com” ir slaptažodžiu “antanas123”.

	Scenario: Darbuotojas sėkmingai pakeičia savo slaptažodį.
		Given slaptažodžio keitimo puslapis pavadinimu "Keisti slaptažodį".
		When Antanas lauke “Dabartinis slaptažodis” įveda dabar egzistuojantį slaptažodį
		And lauke „Naujas slaptažodis“ jis įveda naują, sugalvotą slaptažodį,
		And lauke „Pakartokite naują slaptažodį“ Antanas pakartoja naują slaptažodį
		And paspaudžia mygtuką "Pakeisti slaptažodį"
		Then užkraunamas prisijungimo puslapis ir darbuotojas yra raginamas vėl prisijungti su nauju, pakeistu slaptažodžiu, bei virš prisijungimo formos yra pranešimas „Slaptažodis sėkmingai pakeistas, prisijunkite iš naujo“.

	Scenario: Antanui nepavyksta pakeisti slaptažodžio, nes jis lauke „Dabartinis slaptažodis“ įveda neteisingą slaptažodį.
		Given slaptažodžio keitimo puslapis pavadinimu "Keisti slaptažodį".
		When Antanas lauke “Dabartinis slaptažodis” įveda dabar egzistuojantį, bet neteisingą slaptažodį
		And lauke „Naujas slaptažodis“ jis įveda naują, sugalvotą slaptažodį
		And lauke „Pakartokite naują slaptažodį“ Antanas pakartoja naują slaptažodį
		And paspaudžia mygtuką "Pakeisti slaptažodį"
		Then Antanas pasilieka tame pačiame puslapyje „Keisti slaptažodį“ ir nėra peradresuojamas į prisijungimo puslapį, bei atsiranda pranešimas „Slaptažodis įvestas neteisingai“.

	Scenario: Antanui nepavyksta pakeisti slaptažodžio, nes jis lauke „Pakartokite naują slaptažodį“ įveda neteisingą slaptažodį.
		Given: slaptažodžio keitimo puslapis pavadinimu "Keisti slaptažodį".
		When Antanas lauke “Dabartinis slaptažodis” įveda dabar egzistuojantį slaptažodį
		And lauke „Naujas slaptažodis“ jis įveda naują, sugalvotą slaptažodį
		And lauke „Pakartokite naują slaptažodį“ Antanas neteisingai pakartoja naują slaptažodį
		And paspaudžia mygtuką "Pakeisti slaptažodį"
		Then Antanas pasilieka tame pačiame puslapyje „Keisti slaptažodį“ ir nėra peradresuojamas į prisijungimo puslapį, bei atsiranda pranešimas „Slaptažodis įvestas neteisingai“.

	Scenario: Antanui nepavyksta pakeisti slaptažodžio, nes jis lauke „Naujas slaptažodis“ įveda slaptažodį, kuris susideda iš mažiau negu 6 simbolių.
		Given slaptažodžio keitimo puslapis pavadinimu "Keisti slaptažodį".
		When Antanas lauke “Dabartinis slaptažodis” įveda dabar egzistuojantį slaptažodį
		And lauke „Naujas slaptažodis“ jis įveda naują, sugalvotą slaptažodį, bet slaptažodyje nepasiektas minimalus slaptažodžio simbolių kiekis
		And lauke „Pakartokite naują slaptažodį“ Antanas pakartoja naują slaptažodį
		And paspaudžia mygtuką "Pakeisti slaptažodį"
		Then Antanas pasilieka tame pačiame puslapyje „Keisti slaptažodį“ ir nėra peradresuojamas į prisijungimo puslapį, bei atsiranda pranešimas „Slaptažodis įvestas neteisingai“.





