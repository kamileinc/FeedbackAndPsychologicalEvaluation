Feature: Vartotojas su statusu "darbuotojas" gali užpildyti anketą, kurią jam atsiuntė jo komandos vadovas.


  Background:
    Given Darbuotojui jo komandos vadovas atsiuntė anketą

  Scenario: Darbuotojas užpildo gautą anketą sėkmingai.
    Given Anketos pildymo langas
    When Darbuotojas pirmo klausimo atsakymui pasirenka reikšmę 3
    And antro klausimo atsakymui pasirenka reikšmę 4
    And trečio klausimo atsakymui pasirenka reikšmę 5
    And ketvirto klausimo atsakymui pasirenka reikšmę 6
    And penkto klausimo atsakymui pasirenka reikšmę 5
    And šešto klausimo atsakymui pasirenka reikšmę 4
    And septinto klausimo atsakymui pasirenka reikšmę 3
    And aštunto klausimo atsakymo lauke parašo “Viskas okay”
    And paspaudžia mygtuką “Išsaugoti”.
    Then Atidaromas pagrindinis darbuotojo paskyros langas
    And parodomas pranešimas “Anketa sėkmingai užpildyta”.

  Scenario: Darbuotojas užpildo gautą anketą nesėkmingai.
    Given Anketos pildymo langas
    When Darbuotojas pirmo klausimo atsakymui pasirenka reikšmę 3
    And antro klausimo atsakymui pasirenka reikšmę 4
    And trečio klausimo atsakymui pasirenka reikšmę 5
    And ketvirto klausimo atsakymui pasirenka reikšmę 6
    And penkto klausimo atsakymui pasirenka reikšmę 5
    And šešto klausimo atsakymui pasirenka reikšmę 4
    And septinto klausimo atsakymui pasirenka reikšmę 3
    And aštunto klausimo atsakymo lauke parašo “Kaip žmogus tu, vadove mano, gal ir esi gan normalus, bet ir tai yra didelis bet, kaip vadovas tu man nepatinki. Tikriausia dabar kyla klausimas kodėl? Na aš tau atsakysiu į šį klausimą daugiau netemdamas laiko. Manau, kad tu manęs, kaip darbuotojo, visai nevertini. Kaip tai pasireiškia? Į šį klausimą yra labai lengvas atsakymas. Aš žinau, kad tu prisimeni, kaip prieš apytiksliai 3 mėnesius, o tiksliai prieš 97 dienas, kaip aš tau atnešiau savo darbo ataskaitą tu man nepasakei ačiū. Ar taip galima elgti? Ne...”.
    And paspaudžia mygtuką “Išsaugoti”.
    Then Perkraunamas tas pats anketos pildymo puslapis
    And parodomas klaidos pranešimas “Atvirame lauke viršytas simbolių limitas”.
