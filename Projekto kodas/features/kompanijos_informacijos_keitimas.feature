Feature: vartotojas su statusu “kompanija” gali keisti kompanijos informaciją.
  Background: 
    Given sistemoje priregistruota kompanija su pavadinimu “test” 
	And el. pašto adresu “test@email.com” 
	And slaptažodžiu “123456”
	And atnaujino informaciją
	And paspaudė mygtuką “Atnaujinti informaciją” 
	
  Scenario: Kompanijos darbuotojas prisijungęs su kompanijos el. paštu ir slaptažodžiu atnaujina informaciją nekeičiant nei vieno lauko
    Given profilio keitimo langas
    When vartojas palieka nekeistą kompanijos pavadinimo lauką
    And palieka nekeistą el. pašto lauką
    And paspaudžia mygtuką “Atnaujinti informaciją”
    Then perkraunamas profilio keitimo puslapis su pranešimu “Duomenys išliko tokie pat”

  Scenario: Kompanijos darbuotojas prisijungęs su kompanijos el. paštu ir slaptažodžiu atnaujina informaciją pakeičiant kompanijos pavadinimą į “test1”
    Given profilio keitimo langas
    When vartotojas pakeičia kompanijos pavadinimą į “test1”
    And palieka nekeistą el. pašto lauką
    And paspaudžia mygtuką “Atnaujinti informaciją”
    Then užkraunamas prisijungimo puslapis su pranešimu “Sėkmingai atnaujinta informacija, prisijunkite iš naujo”.

  Scenario: Kompanijos darbuotojas prisijungęs su kompanijos el. paštu ir slaptažodžiu atnaujina informaciją pakeičiant kompanijos pavadinimo ir el. pašto lauką.
    Given profilio keitimo langas.
    When vartotojas pakeičia kompanijos pavadinimą į “test1”
    And pakeičia el. paštą į “test1@gmail.com”
    And paspaudžia mygtuką “Atnaujinti informaciją”
    Then užkraunamas prisijungimo puslapis su pranešimu “Sėkmingai atnaujinta informacija, prisijunkite iš naujo”

  Scenario: Kompanijos darbuotojas prisijungęs su kompanijos el. paštu ir slaptažodžiu atnaujina informaciją pakeičiant kompanijos slaptažodį į “supersecret”
    Given slaptažodžio keitimo langas.
    When vartotojas suveda dabartinį slaptažodį “123456”.
    And suveda naują slaptažodį “supersecret”.
    And pakartoja slaptažodį “supersecret”
    And paspaudžia mygtuką “Pakeisti slaptažodį”.
    Then užkraunamas prisijungimo puslapis su pranešimu “Slaptažodis sėkmingai pakeistas, prisijunkite iš naujo”
        
  Scenario: kompanijos darbuotojas prisijungęs su kompanijos el. paštu ir slaptažodžiu nurodo netinkamą el. pašto formatą
    Given profilio keitimo langas
    When vartotojas nekeičia kompanijos pavadinimo lauko
    And nurodo el. pašto adresą pavadinimu “testČgmail.com”
    And paspaudžia mygtuką “Atnaujinti informaciją”
    Then po el. pašto lauku atsiranda pranešimas “El. pašto adresas neatitinka reikiamos struktūros”

        
  Scenario: kompanijos darbuotojas prisijungęs su kompanijos el. paštu ir slaptažodžiu nurodo jau egzistuojantį kompanijos pavadinimą “egzistuojantis”
    Given profilio keitimo langas
    When vartotojas pakeičia kompanijos pavadinimą į “egzistuojantis”
    And nekeičia el. pašto lauko
    And paspaudžia mygtuką “Atnaujinti informaciją”
    Then Profilio keitimo lange atsiranda klaidos pranešimas “Kompanija su tokiu pavadinimu jau yra užregistruota”
