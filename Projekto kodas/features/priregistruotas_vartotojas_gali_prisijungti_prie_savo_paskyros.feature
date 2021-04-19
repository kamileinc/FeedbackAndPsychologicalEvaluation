Feature: Priregistruotas vartotojas gali prisijungti prie savo paskyros.


  Background:
    Given Darbuotojas Antanas yra priregistruotas vartotojas
    And jo el. pašto adresas yra “antanas.antanaitis@email.com”
    And slaptažodis yra “antanas123”

  Scenario: Vartotojas prisijungia prie savo paskyros sėkmingai
    Given Prisijungimo langas
    When Antanas el. pašto lauke įrašo “antanas.antanaitis@email.com”
    And Antanas slaptažodžio lauke įrašo “antanas123”
    And paspaudžia mygtuką “prisijungti”.
    Then Antanas prisijungia prie sistemos
    And mato darbuotojo paskyros pagrindinį puslapį.

  Scenario: Vartotojas bando prisijungti prie sistemos naudojant neteisingus prisijungimo duomenis ir jam nepavyksta.
    Given Prisijungimo langas
    When Antanas el. pašto lauke įrašo “antanas.antanaitis@email.com”
    And Antanas slaptažodžio lauke įrašo “juozas123”
    And paspaudžia mygtuką “prisijungti”.
    Then užkraunamas tas pats prisijungimo puslapis iš naujo
    And parodomas klaidos pranešimas “Neteisingas prisijungimas”.

  Scenario: Vartotojas bando prisijungti prie sistemos neužpildęs el. pašto adreso lauko ir jam nepavyksta.
    Given Prisijungimo langas
    When Antanas el. pašto lauką palieka tuščią
    And Antanas slaptažodžio lauke įrašo “antanas123”
    And paspaudžia mygtuką “prisijungti”.
    Then Antanui parodomas pranešimas „El. paštas laukas yra neužpildytas“.

  Scenario: Vartotojas bando prisijungti prie sistemos neužpildęs slaptažodžio lauko ir jam nepavyksta.
    Given Prisijungimo langas
    When Antanas el. pašto lauke įrašo “antanas.antanaitis@email.com”
    And Antanas slaptažodžio lauką palieka tuščią
    And paspaudžia mygtuką “prisijungti”.
    Then Antanui parodomas pranešimas „Slaptažodis laukas yra neužpildytas“.
