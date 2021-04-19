# encoding: UTF-8
import unittest
from actionwords import Actionwords
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

class TestPkpWebsite(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_kompanijos_darbuotojas_prisijunges_su_kompanijos_el_pastu_ir_slaptazodziu_atnaujina_informacija_nekeiciant_nei_vieno_lauko(self):
        # Given profilio keitimo langas
        self.actionwords.profilio_keitimo_langas()
        # When vartojas palieka nekeistą kompanijos pavadinimo lauką
        self.actionwords.vartojas_palieka_nekeista_kompanijos_pavadinimo_lauka()
        # And palieka nekeistą el. pašto lauką
        self.actionwords.palieka_nekeista_el_pasto_lauka()
        # And paspaudžia mygtuką “Atnaujinti informaciją”
        self.actionwords.paspaudzia_mygtuka_atnaujinti_informacija()
        # Then perkraunamas profilio keitimo puslapis su pranešimu “Duomenys išliko tokie pat”
        self.actionwords.perkraunamas_profilio_keitimo_puslapis_su_pranesimu_duomenys_isliko_tokie_pat()

    def test_kompanijos_darbuotojas_prisijunges_su_kompanijos_el_pastu_ir_slaptazodziu_atnaujina_informacija_pakeiciant_kompanijos_pavadinima_i_test1(self):
        # Given profilio keitimo langas
        self.actionwords.profilio_keitimo_langas()
        # When vartotojas pakeičia kompanijos pavadinimą į “test1”
        self.actionwords.vartotojas_pakeicia_kompanijos_pavadinima_i_test1()
        # And palieka nekeistą el. pašto lauką
        self.actionwords.palieka_nekeista_el_pasto_lauka()
        # And paspaudžia mygtuką “Atnaujinti informaciją”
        self.actionwords.paspaudzia_mygtuka_atnaujinti_informacija()
        # Then užkraunamas prisijungimo puslapis su pranešimu “Sėkmingai atnaujinta informacija, prisijunkite iš naujo”.
        self.actionwords.uzkraunamas_prisijungimo_puslapis_su_pranesimu_sekmingai_atnaujinta_informacija_prisijunkite_is_naujo()

    def test_kompanijos_darbuotojas_prisijunges_su_kompanijos_el_pastu_ir_slaptazodziu_atnaujina_informacija_pakeiciant_kompanijos_pavadinimo_ir_el_pasto_lauka(self):
        # Given profilio keitimo langas.
        self.actionwords.profilio_keitimo_langas()
        # When vartotojas pakeičia kompanijos pavadinimą į “test1”
        self.actionwords.vartotojas_pakeicia_kompanijos_pavadinima_i_test1()
        # And pakeičia el. paštą į “test1@gmail.com”
        self.actionwords.pakeicia_el_pasta_i_test1gmailcom()
        # And paspaudžia mygtuką “Atnaujinti informaciją”
        self.actionwords.paspaudzia_mygtuka_atnaujinti_informacija()
        # Then užkraunamas prisijungimo puslapis su pranešimu “Sėkmingai atnaujinta informacija, prisijunkite iš naujo”
        self.actionwords.uzkraunamas_prisijungimo_puslapis_su_pranesimu_sekmingai_atnaujinta_informacija_prisijunkite_is_naujo()

    def test_kompanijos_darbuotojas_prisijunges_su_kompanijos_el_pastu_ir_slaptazodziu_atnaujina_informacija_pakeiciant_kompanijos_slaptazodi_i_supersecret(self):
        # Given slaptažodžio keitimo langas.
        self.actionwords.slaptazodzio_keitimo_langas()
        # When vartotojas suveda dabartinį slaptažodį “123456”.
        self.actionwords.vartotojas_suveda_dabartini_slaptazodi_123456()
        # And suveda naują slaptažodį “supersecret”.
        self.actionwords.suveda_nauja_slaptazodi_supersecret()
        # And pakartoja slaptažodį “supersecret”
        self.actionwords.pakartoja_slaptazodi_supersecret()
        # And paspaudžia mygtuką “Pakeisti slaptažodį”.
        self.actionwords.paspaudzia_mygtuka_pakeisti_slaptazodi()
        # Then užkraunamas prisijungimo puslapis su pranešimu “Slaptažodis sėkmingai pakeistas, prisijunkite iš naujo”
        self.actionwords.uzkraunamas_prisijungimo_puslapis_su_pranesimu_slaptazodis_sekmingai_pakeistas_prisijunkite_is_naujo()

    def test_kompanijos_darbuotojas_prisijunges_su_kompanijos_el_pastu_ir_slaptazodziu_nurodo_netinkama_el_pasto_formata(self):
        # Given profilio keitimo langas
        self.actionwords.profilio_keitimo_langas()
        # When vartotojas nekeičia kompanijos pavadinimo lauko
        self.actionwords.vartotojas_nekeicia_kompanijos_pavadinimo_lauko()
        # And nurodo el. pašto adresą pavadinimu “testČgmail.com”
        self.actionwords.nurodo_el_pasto_adresa_pavadinimu_test_cgmailcom()
        # And paspaudžia mygtuką “Atnaujinti informaciją”
        self.actionwords.paspaudzia_mygtuka_atnaujinti_informacija()
        # Then po el. pašto lauku atsiranda pranešimas “El. pašto adresas neatitinka reikiamos struktūros”
        self.actionwords.po_el_pasto_lauku_atsiranda_pranesimas_el_pasto_adresas_neatitinka_reikiamos_strukturos()

    def test_kompanijos_darbuotojas_prisijunges_su_kompanijos_el_pastu_ir_slaptazodziu_nurodo_jau_egzistuojanti_kompanijos_pavadinima_egzistuojantis(self):
        # Given profilio keitimo langas
        self.actionwords.profilio_keitimo_langas()
        # When vartotojas pakeičia kompanijos pavadinimą į “egzistuojantis”
        self.actionwords.vartotojas_pakeicia_kompanijos_pavadinima_i_egzistuojantis()
        # And nekeičia el. pašto lauko
        self.actionwords.nekeicia_el_pasto_lauko()
        # And paspaudžia mygtuką “Atnaujinti informaciją”
        self.actionwords.paspaudzia_mygtuka_atnaujinti_informacija()
        # Then Profilio keitimo lange atsiranda klaidos pranešimas “Kompanija su tokiu pavadinimu jau yra užregistruota”
        self.actionwords.profilio_keitimo_lange_atsiranda_klaidos_pranesimas_kompanija_su_tokiu_pavadinimu_jau_yra_uzregistruota()

    def test_lina_uzpildo_gauta_anketa_sekmingai(self):
        # Given vadovo anketos pildymo langas
        self.actionwords.vadovo_anketos_pildymo_langas()
        # When Lina parenka pirmam laukui reikšmę 5
        self.actionwords.lina_parenka_pirmam_laukui_reiksme_5()
        # And antram laukui reikšmę 6
        self.actionwords.antram_laukui_reiksme_6()
        # And trečiam lauke parašo “Nuostabūs šios savaitės pasiekimai”
        self.actionwords.treciam_lauke_paraso_nuostabus_sios_savaites_pasiekimai()
        # And paspaudžia mygtuką “Išsaugoti”
        self.actionwords.paspaudzia_mygtuka_issaugoti()
        # Then užkraunamas pagrindinis vadovo paskyros puslapis ir parašomas pranešimas “Anketa sėkmingai užpildyta”
        self.actionwords.uzkraunamas_pagrindinis_vadovo_paskyros_puslapis_ir_parasomas_pranesimas_anketa_sekmingai_uzpildyta()

    def test_lina_uzpildo_gauta_anketa_nesekmingai_ir_gauna_klaidos_pranesima(self):
        # Given vadovo anketos pildymo langas
        self.actionwords.vadovo_anketos_pildymo_langas()
        # When Lina parenka pirmam laukui reikšmę 5
        self.actionwords.lina_parenka_pirmam_laukui_reiksme_5()
        # And antram laukui reikšmę 6
        self.actionwords.antram_laukui_reiksme_6()
        # And trečiam lauke parašo “Nuostabūs šios savaitės pasiekimai. Ypač patiko tavo pasiūlymas pakeisti mūsų firmos darbų atlikimo tvarką. Net mano vadovė tai pastebėjo ir labai pagyrė iniciatyvą. Jei kils dar kokių minčių visad lauksim tavo idėjų ir bandysim jas įgyvendint. Taip pat labai noriu pagirti dėl gerų klientų įvertinimo. Esi vienas iš mylimiausių darbuotojų klientų akyse. Būtų gerai, jei sutartume, kada galėtum papasakoti apie tai savo kolegoms. Tačiau tikiuosi iš tavęs geresnės darbo etikos. Dėl to norėčiau pasikalbėti gyvai. Planuokime susitikimą antradienį 15:30 mano kabinete. Jei kas keisis ar netinka mano pasiūlytas laikas, tuomet galime gyvai susitart dėl kito tinkamesnio laiko. Jei tinka, tai tuomet susitiksime antradienį nutartu laiku.”
        self.actionwords.treciam_lauke_paraso_nuostabus_sios_savaites_pasiekimai_ypac_patiko_tavo_pasiulymas_pakeisti_musu_firmos_darbu_atlikimo_tvarka_net_mano_vadove_tai_pastebejo_ir_labai_pagyre_iniciatyva_jei_kils_dar_kokiu_minciu_visad_lauksim_tavo_ideju_ir_bandysim_jas_igyvendint_taip_pat_labai_noriu_pagirti_del_geru_klientu_ivertinimo_esi_vienas_is_mylimiausiu_darbuotoju_klientu_akyse_butu_gerai_jei_sutartume_kada_galetum_papasakoti_apie_tai_savo_kolegoms_taciau_tikiuosi_is_taves_geresnes_darbo_etikos_del_to_noreciau_pasikalbeti_gyvai_planuokime_susitikima_antradieni_1530_mano_kabinete_jei_kas_keisis_ar_netinka_mano_pasiulytas_laikas_tuomet_galime_gyvai_susitart_del_kito_tinkamesnio_laiko_jei_tinka_tai_tuomet_susitiksime_antradieni_nutartu_laiku()
        # And paspaudžia mygtuką “Išsaugoti”
        self.actionwords.paspaudzia_mygtuka_issaugoti()
        # Then perkraunamas tas pats anketos pildymo puslapis ir parašomas klaidos pranešimas “Atvirame lauke viršytas simbolių limitas”
        self.actionwords.perkraunamas_tas_pats_anketos_pildymo_puslapis_ir_parasomas_klaidos_pranesimas_atvirame_lauke_virsytas_simboliu_limitas()

    def test_kompanija_uzsiregistruoja_sistemoje_sekmingai(self):
        # Given registracijos langas.
        self.actionwords.registracijos_langas()
        # When Kompaniją bandantis priregistruoti žmogus prie Kompanijos pavadinimo lauko įrašo “Kompanija A”
        self.actionwords.kompanija_bandantis_priregistruoti_zmogus_prie_kompanijos_pavadinimo_lauko_iraso_kompanija_a()
        # And prie kompanijos el. pašto lauko įrašo “kompanija_a@email.com”
        self.actionwords.prie_kompanijos_el_pasto_lauko_iraso_kompanija_aemailcom()
        # And prie slaptažodžio lauko įrašo “kompanijaa123”
        self.actionwords.prie_slaptazodzio_lauko_iraso_kompanijaa123()
        # And prie pakartokite slaptažodį lauko įrašo “kompanijaa123”
        self.actionwords.prie_pakartokite_slaptazodi_lauko_iraso_kompanijaa123()
        # And paspaudžia mygtuką “užsiregistruoti”
        self.actionwords.paspaudzia_mygtuka_uzsiregistruoti()
        # Then užkraunamas prisijungimo puslapis ir parašomas pranešimas “Užsiregistravote, galite prisijungti”.
        self.actionwords.uzkraunamas_prisijungimo_puslapis_ir_parasomas_pranesimas_uzsiregistravote_galite_prisijungti()

    def test_kompanijai_nepavyksta_uzsiregistruoti_sistemoje_nes_suklysta_atkartojant_slaptazodi(self):
        # Given registracijos langas.
        self.actionwords.registracijos_langas()
        # When Kompaniją bandantis priregistruoti žmogus prie Kompanijos pavadinimo lauko įrašo “Kompanija A”
        self.actionwords.kompanija_bandantis_priregistruoti_zmogus_prie_kompanijos_pavadinimo_lauko_iraso_kompanija_a()
        # And prie kompanijos el. pašto lauko įrašo “kompanija_a@email.com”
        self.actionwords.prie_kompanijos_el_pasto_lauko_iraso_kompanija_aemailcom()
        # And prie slaptažodžio lauko įrašo “kompanijaa123”
        self.actionwords.prie_slaptazodzio_lauko_iraso_kompanijaa123()
        # And prie pakartokite slaptažodį lauko įrašo “kompanijaa12”
        self.actionwords.prie_pakartokite_slaptazodi_lauko_iraso_kompanijaa12()
        # And paspaudžia mygtuką “užsiregistruoti”
        self.actionwords.paspaudzia_mygtuka_uzsiregistruoti()
        # Then užkraunamas tas pats registracijos puslapis iš naujo ir parašomas pranešimas “Slaptažodžiai nesutampa”.
        self.actionwords.uzkraunamas_tas_pats_registracijos_puslapis_is_naujo_ir_parasomas_pranesimas_slaptazodziai_nesutampa()

    def test_kompanijai_nepavyksta_uzsiregistruoti_sistemoje_nes_iraso_jau_sistemoje_issaugota_kompanijos_pavadinima(self):
        # Given registracijos langas.
        self.actionwords.registracijos_langas()
        # When Kompaniją bandantis priregistruoti žmogus prie Kompanijos pavadinimo lauko įrašo “Pavyzdys”
        self.actionwords.kompanija_bandantis_priregistruoti_zmogus_prie_kompanijos_pavadinimo_lauko_iraso_pavyzdys()
        # And prie kompanijos el. pašto lauko įrašo “kompanija_a@email.com”
        self.actionwords.prie_kompanijos_el_pasto_lauko_iraso_kompanija_aemailcom()
        # And prie slaptažodžio lauko įrašo “kompanijaa123”
        self.actionwords.prie_slaptazodzio_lauko_iraso_kompanijaa123()
        # And prie pakartokite slaptažodį lauko įrašo “kompanijaa123”
        self.actionwords.prie_pakartokite_slaptazodi_lauko_iraso_kompanijaa123()
        # And paspaudžia mygtuką “užsiregistruoti”
        self.actionwords.paspaudzia_mygtuka_uzsiregistruoti()
        # Then užkraunamas tas pats registracijos puslapis iš naujo ir parašomas pranešimas “Kompanija su tokiu pavadinimu jau yra užregistruota.”.
        self.actionwords.uzkraunamas_tas_pats_registracijos_puslapis_is_naujo_ir_parasomas_pranesimas_kompanija_su_tokiu_pavadinimu_jau_yra_uzregistruota()

    def test_kompanijai_nepavyksta_uzsiregistruoti_sistemoje_nes_iraso_jau_sistemoje_issaugota_kompanijos_el_pasta(self):
        # Given registracijos langas.
        self.actionwords.registracijos_langas()
        # When Kompaniją bandantis priregistruoti žmogus prie Kompanijos pavadinimo lauko įrašo “Kompanija A”
        self.actionwords.kompanija_bandantis_priregistruoti_zmogus_prie_kompanijos_pavadinimo_lauko_iraso_kompanija_a()
        # And prie kompanijos el. pašto lauko įrašo “pvz@pvz.lt“
        self.actionwords.prie_kompanijos_el_pasto_lauko_iraso_pvzpvzlt()
        # And prie slaptažodžio lauko įrašo “kompanijaa123”
        self.actionwords.prie_slaptazodzio_lauko_iraso_kompanijaa123()
        # And prie pakartokite slaptažodį lauko įrašo “kompanijaa123”
        self.actionwords.prie_pakartokite_slaptazodi_lauko_iraso_kompanijaa123()
        # And paspaudžia mygtuką “užsiregistruoti”
        self.actionwords.paspaudzia_mygtuka_uzsiregistruoti()
        # Then užkraunamas tas pats registracijos puslapis iš naujo ir parašomas pranešimas “Toks el. paštas jau yra naudojamas.”.
        self.actionwords.uzkraunamas_tas_pats_registracijos_puslapis_is_naujo_ir_parasomas_pranesimas_toks_el_pastas_jau_yra_naudojamas()

    def test_kompanijai_nepavyksta_uzsiregistruoti_sistemoje_nes_palieka_tuscia_kompanijos_pavadinimo_lauka(self):
        # Given registracijos langas.
        self.actionwords.registracijos_langas()
        # When Kompaniją bandantis priregistruoti žmogus Kompanijos pavadinimo lauką palieka tuščią
        self.actionwords.kompanija_bandantis_priregistruoti_zmogus_kompanijos_pavadinimo_lauka_palieka_tuscia()
        # And prie kompanijos el. pašto lauko įrašo “kompanija_a@email.com“
        self.actionwords.prie_kompanijos_el_pasto_lauko_iraso_kompanija_aemailcom()
        # And prie slaptažodžio lauko įrašo “kompanijaa123”
        self.actionwords.prie_slaptazodzio_lauko_iraso_kompanijaa123()
        # And prie pakartokite slaptažodį lauko įrašo “kompanijaa123”
        self.actionwords.prie_pakartokite_slaptazodi_lauko_iraso_kompanijaa123()
        # And paspaudžia mygtuką “užsiregistruoti”
        self.actionwords.paspaudzia_mygtuka_uzsiregistruoti()
        # Then užkraunamas tas pats registracijos puslapis iš naujo ir parašomas pranešimas “Kompanijos pavadinimas yra privalomas laukas.”.
        self.actionwords.uzkraunamas_tas_pats_registracijos_puslapis_is_naujo_ir_parasomas_pranesimas_kompanijos_pavadinimas_yra_privalomas_laukas()

    def test_kompanijai_nepavyksta_uzsiregistruoti_sistemoje_nes_palieka_tuscia_kompanijos_el_pasto_lauka(self):
        # Given registracijos langas.
        self.actionwords.registracijos_langas()
        # When Kompaniją bandantis priregistruoti žmogus prie Kompanijos pavadinimo lauko įrašo “Kompanija A”
        self.actionwords.kompanija_bandantis_priregistruoti_zmogus_prie_kompanijos_pavadinimo_lauko_iraso_kompanija_a()
        # And kompanijos el. pašto lauką palieka tuščią
        self.actionwords.kompanijos_el_pasto_lauka_palieka_tuscia()
        # And prie slaptažodžio lauko įrašo “kompanijaa123”
        self.actionwords.prie_slaptazodzio_lauko_iraso_kompanijaa123()
        # And prie pakartokite slaptažodį lauko įrašo “kompanijaa123”
        self.actionwords.prie_pakartokite_slaptazodi_lauko_iraso_kompanijaa123()
        # And paspaudžia mygtuką “užsiregistruoti”
        self.actionwords.paspaudzia_mygtuka_uzsiregistruoti()
        # Then užkraunamas tas pats registracijos puslapis iš naujo ir parašomas pranešimas “El. paštas yra privalomas laukas. El. pašto adresas turi susidaryti iš 6-50 simbolių. El. pašto adresas neatitinka reikiamos struktūros”.
        self.actionwords.uzkraunamas_tas_pats_registracijos_puslapis_is_naujo_ir_parasomas_pranesimas_el_pastas_yra_privalomas_laukas_el_pasto_adresas_turi_susidaryti_is_650_simboliu_el_pasto_adresas_neatitinka_reikiamos_strukturos()

    def test_vartotojas_prisijungia_prie_savo_paskyros_sekmingai(self):
        # Given Prisijungimo langas
        self.actionwords.prisijungimo_langas()
        # When Antanas el. pašto lauke įrašo “antanas.antanaitis@email.com”
        self.actionwords.antanas_el_pasto_lauke_iraso_antanasantanaitisemailcom()
        # And Antanas slaptažodžio lauke įrašo “antanas123”
        self.actionwords.antanas_slaptazodzio_lauke_iraso_antanas123()
        # And paspaudžia mygtuką “prisijungti”.
        self.actionwords.paspaudzia_mygtuka_prisijungti()
        # Then Antanas prisijungia prie sistemos
        self.actionwords.antanas_prisijungia_prie_sistemos()
        # And mato darbuotojo paskyros pagrindinį puslapį.
        self.actionwords.mato_darbuotojo_paskyros_pagrindini_puslapi()

    def test_vartotojas_bando_prisijungti_prie_sistemos_naudojant_neteisingus_prisijungimo_duomenis_ir_jam_nepavyksta(self):
        # Given Prisijungimo langas
        self.actionwords.prisijungimo_langas()
        # When Antanas el. pašto lauke įrašo “antanas.antanaitis@email.com”
        self.actionwords.antanas_el_pasto_lauke_iraso_antanasantanaitisemailcom()
        # And Antanas slaptažodžio lauke įrašo “juozas123”
        self.actionwords.antanas_slaptazodzio_lauke_iraso_juozas123()
        # And paspaudžia mygtuką “prisijungti”.
        self.actionwords.paspaudzia_mygtuka_prisijungti()
        # Then užkraunamas tas pats prisijungimo puslapis iš naujo
        self.actionwords.uzkraunamas_tas_pats_prisijungimo_puslapis_is_naujo()
        # And parodomas klaidos pranešimas “Neteisingas prisijungimas”.
        self.actionwords.parodomas_klaidos_pranesimas_neteisingas_prisijungimas()

    def test_vartotojas_bando_prisijungti_prie_sistemos_neuzpildes_el_pasto_adreso_lauko_ir_jam_nepavyksta(self):
        # Given Prisijungimo langas
        self.actionwords.prisijungimo_langas()
        # When Antanas el. pašto lauką palieka tuščią
        self.actionwords.antanas_el_pasto_lauka_palieka_tuscia()
        # And Antanas slaptažodžio lauke įrašo “antanas123”
        self.actionwords.antanas_slaptazodzio_lauke_iraso_antanas123()
        # And paspaudžia mygtuką “prisijungti”.
        self.actionwords.paspaudzia_mygtuka_prisijungti()
        # Then Antanui parodomas pranešimas „El. paštas laukas yra neužpildytas“.
        self.actionwords.antanui_parodomas_pranesimas_el_pastas_laukas_yra_neuzpildytas()

    def test_vartotojas_bando_prisijungti_prie_sistemos_neuzpildes_slaptazodzio_lauko_ir_jam_nepavyksta(self):
        # Given Prisijungimo langas
        self.actionwords.prisijungimo_langas()
        # When Antanas el. pašto lauke įrašo “antanas.antanaitis@email.com”
        self.actionwords.antanas_el_pasto_lauke_iraso_antanasantanaitisemailcom()
        # And Antanas slaptažodžio lauką palieka tuščią
        self.actionwords.antanas_slaptazodzio_lauka_palieka_tuscia()
        # And paspaudžia mygtuką “prisijungti”.
        self.actionwords.paspaudzia_mygtuka_prisijungti()
        # Then Antanui parodomas pranešimas „Slaptažodis laukas yra neužpildytas“.
        self.actionwords.antanui_parodomas_pranesimas_slaptazodis_laukas_yra_neuzpildytas()

    def test_darbuotojas_uzpildo_gauta_anketa_sekmingai(self):
        # Given Anketos pildymo langas
        self.actionwords.anketos_pildymo_langas()
        # When Darbuotojas pirmo klausimo atsakymui pasirenka reikšmę 3
        self.actionwords.darbuotojas_pirmo_klausimo_atsakymui_pasirenka_reiksme_3()
        # And antro klausimo atsakymui pasirenka reikšmę 4
        self.actionwords.antro_klausimo_atsakymui_pasirenka_reiksme_4()
        # And trečio klausimo atsakymui pasirenka reikšmę 5
        self.actionwords.trecio_klausimo_atsakymui_pasirenka_reiksme_5()
        # And ketvirto klausimo atsakymui pasirenka reikšmę 6
        self.actionwords.ketvirto_klausimo_atsakymui_pasirenka_reiksme_6()
        # And penkto klausimo atsakymui pasirenka reikšmę 5
        self.actionwords.penkto_klausimo_atsakymui_pasirenka_reiksme_5()
        # And šešto klausimo atsakymui pasirenka reikšmę 4
        self.actionwords.sesto_klausimo_atsakymui_pasirenka_reiksme_4()
        # And septinto klausimo atsakymui pasirenka reikšmę 3
        self.actionwords.septinto_klausimo_atsakymui_pasirenka_reiksme_3()
        # And aštunto klausimo atsakymo lauke parašo “Viskas okay”
        self.actionwords.astunto_klausimo_atsakymo_lauke_paraso_viskas_okay()
        # And paspaudžia mygtuką “Išsaugoti”.
        self.actionwords.paspaudzia_mygtuka_issaugoti()
        # Then Atidaromas pagrindinis darbuotojo paskyros langas
        self.actionwords.atidaromas_pagrindinis_darbuotojo_paskyros_langas()
        # And parodomas pranešimas “Anketa sėkmingai užpildyta”.
        self.actionwords.parodomas_pranesimas_anketa_sekmingai_uzpildyta()

    def test_darbuotojas_uzpildo_gauta_anketa_nesekmingai(self):
        # Given Anketos pildymo langas
        self.actionwords.anketos_pildymo_langas()
        # When Darbuotojas pirmo klausimo atsakymui pasirenka reikšmę 3
        self.actionwords.darbuotojas_pirmo_klausimo_atsakymui_pasirenka_reiksme_3()
        # And antro klausimo atsakymui pasirenka reikšmę 4
        self.actionwords.antro_klausimo_atsakymui_pasirenka_reiksme_4()
        # And trečio klausimo atsakymui pasirenka reikšmę 5
        self.actionwords.trecio_klausimo_atsakymui_pasirenka_reiksme_5()
        # And ketvirto klausimo atsakymui pasirenka reikšmę 6
        self.actionwords.ketvirto_klausimo_atsakymui_pasirenka_reiksme_6()
        # And penkto klausimo atsakymui pasirenka reikšmę 5
        self.actionwords.penkto_klausimo_atsakymui_pasirenka_reiksme_5()
        # And šešto klausimo atsakymui pasirenka reikšmę 4
        self.actionwords.sesto_klausimo_atsakymui_pasirenka_reiksme_4()
        # And septinto klausimo atsakymui pasirenka reikšmę 3
        self.actionwords.septinto_klausimo_atsakymui_pasirenka_reiksme_3()
        # And aštunto klausimo atsakymo lauke parašo “Kaip žmogus tu, vadove mano, gal ir esi gan normalus, bet ir tai yra didelis bet, kaip vadovas tu man nepatinki. Tikriausia dabar kyla klausimas kodėl? Na aš tau atsakysiu į šį klausimą daugiau netemdamas laiko. Manau, kad tu manęs, kaip darbuotojo, visai nevertini. Kaip tai pasireiškia? Į šį klausimą yra labai lengvas atsakymas. Aš žinau, kad tu prisimeni, kaip prieš apytiksliai 3 mėnesius, o tiksliai prieš 97 dienas, kaip aš tau atnešiau savo darbo ataskaitą tu man nepasakei ačiū. Ar taip galima elgti? Ne...”.
        self.actionwords.astunto_klausimo_atsakymo_lauke_paraso_kaip_zmogus_tu_vadove_mano_gal_ir_esi_gan_normalus_bet_ir_tai_yra_didelis_bet_kaip_vadovas_tu_man_nepatinki_tikriausia_dabar_kyla_klausimas_kodel_na_as_tau_atsakysiu_i_si_klausima_daugiau_netemdamas_laiko_manau_kad_tu_manes_kaip_darbuotojo_visai_nevertini_kaip_tai_pasireiskia_i_si_klausima_yra_labai_lengvas_atsakymas_as_zinau_kad_tu_prisimeni_kaip_pries_apytiksliai_3_menesius_o_tiksliai_pries_97_dienas_kaip_as_tau_atnesiau_savo_darbo_ataskaita_tu_man_nepasakei_aciu_ar_taip_galima_elgti_ne()
        # And paspaudžia mygtuką “Išsaugoti”.
        self.actionwords.paspaudzia_mygtuka_issaugoti()
        # Then Perkraunamas tas pats anketos pildymo puslapis
        self.actionwords.perkraunamas_tas_pats_anketos_pildymo_puslapis()
        # And parodomas klaidos pranešimas “Atvirame lauke viršytas simbolių limitas”.
        self.actionwords.parodomas_klaidos_pranesimas_atvirame_lauke_virsytas_simboliu_limitas()

    def test_kompanijahr_panaikina_vartotoja_sekmingai(self):
        # Given įmonės darbuotojų sąrašo puslapis
        self.actionwords.imones_darbuotoju_saraso_puslapis()
        # When Surandamas Vartotojas, kuris nėra vadovas, kuris turi būti panaikintas
        self.actionwords.surandamas_vartotojas_kuris_nera_vadovas_kuris_turi_buti_panaikintas()
        # And paspaudžiamas mygtukas “DELETE”
        self.actionwords.paspaudziamas_mygtukas_delete()
        # And patvirtinimo langle paspaudžiamas mygtukas “OK”
        self.actionwords.patvirtinimo_langle_paspaudziamas_mygtukas_ok()
        # Then Parodomas Darbuotojų sąrašo puslapis su pranešimu kad vartotojas buvo sėkmingai panaikintas
        self.actionwords.parodomas_darbuotoju_saraso_puslapis_su_pranesimu_kad_vartotojas_buvo_sekmingai_panaikintas()

    def test_kompanijahr_naikinant_vartotoja_apsigalvoja_ir_nusprendzia_nepanaikinti(self):
        # Given įmonės darbuotojų sąrašo puslapis
        self.actionwords.imones_darbuotoju_saraso_puslapis()
        # When Surandamas Vartotojas kuris turi būti panaikintas
        self.actionwords.surandamas_vartotojas_kuris_turi_buti_panaikintas()
        # And paspaudžiamas mygtukas “DELETE”
        self.actionwords.paspaudziamas_mygtukas_delete()
        # And patvirtinimo langle paspaudžiamas mygtukas “Cancel”
        self.actionwords.patvirtinimo_langle_paspaudziamas_mygtukas_cancel()
        # Then Perkraunamas Darbuotojų sąrašo puslapis be jokių pakeitimų
        self.actionwords.perkraunamas_darbuotoju_saraso_puslapis_be_jokiu_pakeitimu()

    def test_kompanijahr_bando_panaikinti_vadova(self):
        # Given įmonės darbuotojų sąrašo puslapis
        self.actionwords.imones_darbuotoju_saraso_puslapis()
        # When Surandamas Vartotojas su vadovo statusu, kuris turi būti panaikintas
        self.actionwords.surandamas_vartotojas_su_vadovo_statusu_kuris_turi_buti_panaikintas()
        # And paspaudžiamas mygtukas “DELETE”
        self.actionwords.paspaudziamas_mygtukas_delete()
        # And patvirtinimo langle paspaudžiamas mygtukas “OK”
        self.actionwords.patvirtinimo_langle_paspaudziamas_mygtukas_ok()
        # Then Parodomas Darbuotojų sąrašo puslapis su pranešimu “Darbuotojas turi pavaldinių, todėl jo negalima ištrinti”
        self.actionwords.parodomas_darbuotoju_saraso_puslapis_su_pranesimu_darbuotojas_turi_pavaldiniu_todel_jo_negalima_istrinti()

    def test_darbuotojas_sekmingai_pakeicia_savo_slaptazodi(self):
        # Given slaptažodžio keitimo puslapis pavadinimu "Keisti slaptažodį".
        self.actionwords.slaptazodzio_keitimo_puslapis_pavadinimu_p1(p1 = "Keisti slaptažodį")
        # When Antanas lauke “Dabartinis slaptažodis” įveda dabar egzistuojantį slaptažodį
        self.actionwords.antanas_lauke_dabartinis_slaptazodis_iveda_dabar_egzistuojanti_slaptazodi()
        # And lauke „Naujas slaptažodis“ jis įveda naują, sugalvotą slaptažodį,
        self.actionwords.lauke_naujas_slaptazodis_jis_iveda_nauja_sugalvota_slaptazodi()
        # And lauke „Pakartokite naują slaptažodį“ Antanas pakartoja naują slaptažodį
        self.actionwords.lauke_pakartokite_nauja_slaptazodi_antanas_pakartoja_nauja_slaptazodi()
        # And paspaudžia mygtuką "Pakeisti slaptažodį"
        self.actionwords.paspaudzia_mygtuka_p1(p1 = "Pakeisti slaptažodį")
        # Then užkraunamas prisijungimo puslapis ir darbuotojas yra raginamas vėl prisijungti su nauju, pakeistu slaptažodžiu, bei virš prisijungimo formos yra pranešimas „Slaptažodis sėkmingai pakeistas, prisijunkite iš naujo“.
        self.actionwords.uzkraunamas_prisijungimo_puslapis_ir_darbuotojas_yra_raginamas_vel_prisijungti_su_nauju_pakeistu_slaptazodziu_bei_virs_prisijungimo_formos_yra_pranesimas_slaptazodis_sekmingai_pakeistas_prisijunkite_is_naujo()

    def test_antanui_nepavyksta_pakeisti_slaptazodzio_nes_jis_lauke_dabartinis_slaptazodis_iveda_neteisinga_slaptazodi(self):
        # Given slaptažodžio keitimo puslapis pavadinimu "Keisti slaptažodį".
        self.actionwords.slaptazodzio_keitimo_puslapis_pavadinimu_p1(p1 = "Keisti slaptažodį")
        # When Antanas lauke “Dabartinis slaptažodis” įveda dabar egzistuojantį, bet neteisingą slaptažodį
        self.actionwords.antanas_lauke_dabartinis_slaptazodis_iveda_dabar_egzistuojanti_bet_neteisinga_slaptazodi()
        # And lauke „Naujas slaptažodis“ jis įveda naują, sugalvotą slaptažodį
        self.actionwords.lauke_naujas_slaptazodis_jis_iveda_nauja_sugalvota_slaptazodi()
        # And lauke „Pakartokite naują slaptažodį“ Antanas pakartoja naują slaptažodį
        self.actionwords.lauke_pakartokite_nauja_slaptazodi_antanas_pakartoja_nauja_slaptazodi()
        # And paspaudžia mygtuką "Pakeisti slaptažodį"
        self.actionwords.paspaudzia_mygtuka_p1(p1 = "Pakeisti slaptažodį")
        # Then Antanas pasilieka tame pačiame puslapyje „Keisti slaptažodį“ ir nėra peradresuojamas į prisijungimo puslapį, bei atsiranda pranešimas „Slaptažodis įvestas neteisingai“.
        self.actionwords.antanas_pasilieka_tame_paciame_puslapyje_keisti_slaptazodi_ir_nera_peradresuojamas_i_prisijungimo_puslapi_bei_atsiranda_pranesimas_slaptazodis_ivestas_neteisingai()

    def test_antanui_nepavyksta_pakeisti_slaptazodzio_nes_jis_lauke_pakartokite_nauja_slaptazodi_iveda_neteisinga_slaptazodi(self):
        # Given: slaptažodžio keitimo puslapis pavadinimu "Keisti slaptažodį".
        # When Antanas lauke “Dabartinis slaptažodis” įveda dabar egzistuojantį slaptažodį
        self.actionwords.antanas_lauke_dabartinis_slaptazodis_iveda_dabar_egzistuojanti_slaptazodi()
        # And lauke „Naujas slaptažodis“ jis įveda naują, sugalvotą slaptažodį
        self.actionwords.lauke_naujas_slaptazodis_jis_iveda_nauja_sugalvota_slaptazodi()
        # And lauke „Pakartokite naują slaptažodį“ Antanas neteisingai pakartoja naują slaptažodį
        self.actionwords.lauke_pakartokite_nauja_slaptazodi_antanas_neteisingai_pakartoja_nauja_slaptazodi()
        # And paspaudžia mygtuką "Pakeisti slaptažodį"
        self.actionwords.paspaudzia_mygtuka_p1(p1 = "Pakeisti slaptažodį")
        # Then Antanas pasilieka tame pačiame puslapyje „Keisti slaptažodį“ ir nėra peradresuojamas į prisijungimo puslapį, bei atsiranda pranešimas „Slaptažodis įvestas neteisingai“.
        self.actionwords.antanas_pasilieka_tame_paciame_puslapyje_keisti_slaptazodi_ir_nera_peradresuojamas_i_prisijungimo_puslapi_bei_atsiranda_pranesimas_slaptazodis_ivestas_neteisingai()

    def test_antanui_nepavyksta_pakeisti_slaptazodzio_nes_jis_lauke_naujas_slaptazodis_iveda_slaptazodi_kuris_susideda_is_maziau_negu_6_simboliu(self):
        # Given slaptažodžio keitimo puslapis pavadinimu "Keisti slaptažodį".
        self.actionwords.slaptazodzio_keitimo_puslapis_pavadinimu_p1(p1 = "Keisti slaptažodį")
        # When Antanas lauke “Dabartinis slaptažodis” įveda dabar egzistuojantį slaptažodį
        self.actionwords.antanas_lauke_dabartinis_slaptazodis_iveda_dabar_egzistuojanti_slaptazodi()
        # And lauke „Naujas slaptažodis“ jis įveda naują, sugalvotą slaptažodį, bet slaptažodyje nepasiektas minimalus slaptažodžio simbolių kiekis
        self.actionwords.lauke_naujas_slaptazodis_jis_iveda_nauja_sugalvota_slaptazodi_bet_slaptazodyje_nepasiektas_minimalus_slaptazodzio_simboliu_kiekis()
        # And lauke „Pakartokite naują slaptažodį“ Antanas pakartoja naują slaptažodį
        self.actionwords.lauke_pakartokite_nauja_slaptazodi_antanas_pakartoja_nauja_slaptazodi()
        # And paspaudžia mygtuką "Pakeisti slaptažodį"
        self.actionwords.paspaudzia_mygtuka_p1(p1 = "Pakeisti slaptažodį")
        # Then Antanas pasilieka tame pačiame puslapyje „Keisti slaptažodį“ ir nėra peradresuojamas į prisijungimo puslapį, bei atsiranda pranešimas „Slaptažodis įvestas neteisingai“.
        self.actionwords.antanas_pasilieka_tame_paciame_puslapyje_keisti_slaptazodi_ir_nera_peradresuojamas_i_prisijungimo_puslapi_bei_atsiranda_pranesimas_slaptazodis_ivestas_neteisingai()

    def test_kompanijos_vadovas_sekmingai_pakeicia_darbuotojo_varda(self):
        # Given puslapis pavadinimu "Jonasss Jonaitis profilis".
        self.actionwords.puslapis_pavadinimu_p1(p1 = "Jonasss Jonaitis profilis")
        # When kompanijos vadovas lauke „Vardas“ pakeičia vartotojo vardą iš „Jonasss“ į „Jonas“
        self.actionwords.kompanijos_vadovas_lauke_vardas_pakeicia_vartotojo_varda_is_jonasss_i_jonas()
        # And paspaudžia mygtuką "„Atnaujinti informaciją“"
        self.actionwords.paspaudzia_mygtuka_p1(p1 = "„Atnaujinti informaciją“")
        # Then kompanijos vadovas patenka į darbuotojų sąrašo puslapį ir pamato, kad darbuotojo vardas yra pakeistas į "Jonas", bei viršuje atsiranda pranešimas „Sėkmingai atnaujinta informacija“.
        self.actionwords.kompanijos_vadovas_patenka_i_darbuotoju_saraso_puslapi_ir_pamato_kad_darbuotojo_vardas_yra_pakeistas_i_p1_bei_virsuje_atsiranda_pranesimas_sekmingai_atnaujinta_informacija(p1 = "Jonas")

    def test_kompanijos_vadovui_nepavyksta_pakeisti_darbuotojo_elpasto_nes_naujas_ivestas_elpastas_neatitinka_reikiamos_strukturos(self):
        # Given puslapis pavadinimu "Jonas Jonaitis profilis".
        self.actionwords.puslapis_pavadinimu_p1(p1 = "Jonas Jonaitis profilis")
        # When kompanijos vadovas lauke „El.paštas“ pakeičia vartotojo paštą iš „jonas.jonaitis@gmail.com“ į „j.jonaitisgmail.com“
        self.actionwords.kompanijos_vadovas_lauke_elpastas_pakeicia_vartotojo_pasta_is_jonasjonaitisgmailcom_i_jjonaitisgmailcom()
        # And paspaudžia mygtuką "„Atnaujinti informaciją“"
        self.actionwords.paspaudzia_mygtuka_p1(p1 = "„Atnaujinti informaciją“")
        # Then kompanijos vadovui užkraunamas tas pats "Jonas Jonaitis profilis" puslapis iš naujo ir po lauko “El.paštas” atsiranda pranešimas “El.pašto adresas neatitinka reikiamos struktūros”.
        self.actionwords.kompanijos_vadovui_uzkraunamas_tas_pats_p1_puslapis_is_naujo_ir_po_lauko_elpastas_atsiranda_pranesimas_elpasto_adresas_neatitinka_reikiamos_strukturos(p1 = "Jonas Jonaitis profilis")

    def test_kompanijos_vadovui_nepavyksta_pakeisti_darbuotojo_vardo_nes_palieka_tuscia_vardo_lauka(self):
        # Given puslapis pavadinimu "Jonas Jonaitis profilis".
        self.actionwords.puslapis_pavadinimu_p1(p1 = "Jonas Jonaitis profilis")
        # When kompanijos vadovas lauke „Vardas” ištrina seną vardą ir paskui pamiršta užpildyti vardo lauką
        self.actionwords.kompanijos_vadovas_lauke_vardas_istrina_sena_varda_ir_paskui_pamirsta_uzpildyti_vardo_lauka()
        # And paspaudžia mygtuką "„Atnaujinti informaciją“"
        self.actionwords.paspaudzia_mygtuka_p1(p1 = "„Atnaujinti informaciją“")
        # Then kompanijos vadovui užkraunamas tas pats "Jonas Jonaitis profilis" puslapis iš naujo ir po lauko “Vardas” atsiranda pranešimas “Vardas turi susidaryti iš 1-60 simbolių”.
        self.actionwords.kompanijos_vadovui_uzkraunamas_tas_pats_p1_puslapis_is_naujo_ir_po_lauko_vardas_atsiranda_pranesimas_vardas_turi_susidaryti_is_160_simboliu(p1 = "Jonas Jonaitis profilis")
		
if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)