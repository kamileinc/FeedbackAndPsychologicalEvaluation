Feature: Kompanija/HR gali panaikinti vartotoją iš visų darbuotojų sąrašo
  Background: 
  Given Darbuotojas paliko įmonę arba buvo atleistas ir jo priėjimas prie sistemos turi būti panaikintas
  And sisteoje prisijungta kaip kompanija
  
  Scenario: Kompanija/Hr panaikina Vartotoją sėkmingai
    Given įmonės darbuotojų sąrašo puslapis
    When Surandamas Vartotojas, kuris nėra vadovas, kuris turi būti panaikintas
    And paspaudžiamas mygtukas “DELETE”
    And patvirtinimo langle paspaudžiamas mygtukas “OK”
    Then Parodomas Darbuotojų sąrašo puslapis su pranešimu kad vartotojas buvo sėkmingai panaikintas
		
  Scenario: Kompanija/Hr naikinant vartotoją apsigalvoja ir nusprendžia nepanaikinti
    Given įmonės darbuotojų sąrašo puslapis
    When Surandamas Vartotojas kuris turi būti panaikintas
    And paspaudžiamas mygtukas “DELETE”
    And patvirtinimo langle paspaudžiamas mygtukas “Cancel”
    Then Perkraunamas Darbuotojų sąrašo puslapis be jokių pakeitimų
		
  Scenario: Kompanija/HR bando panaikinti vadovą
    Given įmonės darbuotojų sąrašo puslapis
    When Surandamas Vartotojas su vadovo statusu, kuris turi būti panaikintas
    And paspaudžiamas mygtukas “DELETE”
    And patvirtinimo langle paspaudžiamas mygtukas “OK”
    Then Parodomas Darbuotojų sąrašo puslapis su pranešimu “Darbuotojas turi pavaldinių, todėl jo negalima ištrinti”