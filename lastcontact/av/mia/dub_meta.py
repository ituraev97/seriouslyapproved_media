import json, os
SRC_URLS = [
 "https://www.ntsb.gov/investigations/Documents/DCA26MA352%20Prelim.pdf",
 "https://www.ntsb.gov/news/press-releases/Pages/NR20260909.aspx",
 "https://www.ntsb.gov/investigations/Pages/DCA26MA352.aspx",
 "https://www.airnav.com/airport/KMIA",
 None,
 "https://www.faa.gov/airports/runways/emas",
 None, None]
TC = ["0:00","0:57","1:21","2:55","3:32","5:10","6:07","7:33","8:17","9:31","10:40","11:15","12:06","13:03","13:29","14:16"]
L = {}
L["es"] = dict(
title="767 de Amazon se sale de pista en Miami: lo que muestra el NTSB",
intro="Salida de pista de un Boeing 767 de Amazon en Miami (vuelo 7598 de 21 Air, 6 de septiembre de 2026), explicada con datos preliminares del NTSB: registrador de datos de vuelo, cronología de la grabadora de voz de cabina, meteorología, control aéreo y hallazgos en los restos.",
p2="El carguero Boeing 767 tocó tierra a unos 3.750 pies de la cabecera de la pista 30, salió del final de la pista a 113 nudos y cruzó una vía pública. Murieron cinco personas en tierra. Esto es un análisis de lo que el NTSB ha publicado hasta ahora, no una conclusión sobre la causa. El NTSB no ha determinado una causa probable.",
ch_h="Capítulos", ch=["Qué pasó","La investigación","El avión y el vuelo","Aeropuerto Internacional de Miami, pista 30","El tiempo","Control de tráfico aéreo","Cronología de la grabadora de voz","Qué es una aproximación estabilizada","El aterrizaje, según los datos de vuelo","Cómo se detiene un avión así","Repetición: la parte final del aterrizaje","Más allá de la pista","Lo que encontraron los investigadores","EMAS","Lo que aún se desconoce","Próximos pasos"],
src_h="Fuentes", src=["Informe preliminar del NTSB DCA26MA352","Actualización de la investigación del NTSB, 9 de septiembre de 2026","Página de la investigación del NTSB","Datos de aeropuerto de la FAA (pista 12/30, umbral desplazado)","Nota informativa ALAR de la Flight Safety Foundation (aproximación estabilizada)","FAA — EMAS","Imágenes de archivo: DVIDS (Departamento de Defensa de EE. UU.), KC-46A (avión cisterna basado en el Boeing 767), no es el avión del accidente","Imágenes aéreas: USGS The National Map. La reconstrucción 3D es ilustrativa; el movimiento entre puntos de datos del NTSB está interpolado. Las componentes del viento son cálculo propio a partir del viento reportado."],
prelim="Toda la información es preliminar y puede cambiar.",
indep="LAST CONTACT es un canal independiente y no está afiliado ni respaldado por el NTSB, la FAA ni ninguna aerolínea. Documentos e imágenes oficiales: obras del Gobierno de EE. UU. (dominio público). La música y los efectos de sonido son originales.",
tags="#accidenteaereo #aviacion #NTSB #seguridadaerea #Miami")
L["pt"] = dict(
title="767 da Amazon sai da pista em Miami: o que mostram os dados do NTSB",
intro="Saída de pista de um Boeing 767 da Amazon em Miami (voo 7598 da 21 Air, 6 de setembro de 2026), explicada com dados preliminares do NTSB: gravador de dados de voo, cronologia do gravador de voz da cabine, meteorologia, controle de tráfego aéreo e achados nos destroços.",
p2="O cargueiro Boeing 767 tocou a pista a cerca de 3.750 pés da cabeceira da pista 30, saiu pelo fim da pista a 113 nós e atravessou uma via pública. Cinco pessoas em solo morreram. Esta é uma análise do que o NTSB publicou até agora, não uma conclusão sobre a causa. O NTSB não determinou uma causa provável.",
ch_h="Capítulos", ch=["O que aconteceu","A investigação","O avião e o voo","Aeroporto Internacional de Miami, pista 30","O tempo","Controle de tráfego aéreo","Cronologia do gravador de voz","O que é uma aproximação estabilizada","O pouso, pelos dados de voo","Como um jato assim para","Replay: a parte final do pouso","Além da pista","O que os investigadores encontraram","EMAS","O que ainda não se sabe","Próximos passos"],
src_h="Fontes", src=["Relatório preliminar do NTSB DCA26MA352","Atualização da investigação do NTSB, 9 de setembro de 2026","Página da investigação do NTSB","Dados de aeroporto da FAA (pista 12/30, cabeceira deslocada)","Nota ALAR da Flight Safety Foundation (aproximação estabilizada)","FAA — EMAS","Imagens de arquivo: DVIDS (Departamento de Defesa dos EUA), KC-46A (avião-tanque baseado no Boeing 767), não é a aeronave do acidente","Imagens aéreas: USGS The National Map. A reconstrução 3D é ilustrativa; o movimento entre pontos de dados do NTSB é interpolado. As componentes do vento são cálculo nosso a partir do vento reportado."],
prelim="Todas as informações são preliminares e podem mudar.",
indep="LAST CONTACT é um canal independente, sem afiliação ou endosso do NTSB, da FAA ou de qualquer companhia aérea. Documentos e imagens oficiais: obras do governo dos EUA (domínio público). Música e efeitos sonoros são originais.",
tags="#acidenteaereo #aviacao #NTSB #segurancadevoo #Miami")
L["fr"] = dict(
title="Sortie de piste d'un 767 d'Amazon à Miami : les données du NTSB",
intro="Sortie de piste d'un Boeing 767 d'Amazon à Miami (vol 7598 de 21 Air, 6 septembre 2026), expliquée avec les données préliminaires du NTSB : enregistreur de paramètres, chronologie de l'enregistreur phonique, météo, contrôle aérien et constatations sur l'épave.",
p2="Le Boeing 767 cargo a touché la piste 30 à environ 3 750 pieds du seuil, a quitté le bout de piste à 113 nœuds et a traversé une voie publique. Cinq personnes au sol ont été tuées. Ceci est une analyse de ce que le NTSB a publié jusqu'ici, pas une conclusion sur la cause. Le NTSB n'a pas déterminé de cause probable.",
ch_h="Chapitres", ch=["Ce qui s'est passé","L'enquête","L'avion et le vol","Aéroport international de Miami, piste 30","La météo","Le contrôle aérien","Chronologie de l'enregistreur phonique","Qu'est-ce qu'une approche stabilisée","L'atterrissage, d'après les données de vol","Comment un tel avion s'arrête","Revoyons : la fin de l'atterrissage","Au-delà de la piste","Ce qu'ont trouvé les enquêteurs","EMAS","Ce qu'on ignore encore","La suite"],
src_h="Sources", src=["Rapport préliminaire du NTSB DCA26MA352","Point d'étape de l'enquête du NTSB, 9 septembre 2026","Page de l'enquête du NTSB","Données aéroport de la FAA (piste 12/30, seuil décalé)","Note ALAR de la Flight Safety Foundation (approche stabilisée)","FAA — EMAS","Images d'archives : DVIDS (Département de la Défense des États-Unis), KC-46A (ravitailleur dérivé du Boeing 767), pas l'avion de l'accident","Images aériennes : USGS The National Map. La reconstitution 3D est illustrative ; le mouvement entre les points de données du NTSB est interpolé. Les composantes de vent sont notre propre calcul à partir du vent rapporté."],
prelim="Toutes les informations sont préliminaires et susceptibles de changer.",
indep="LAST CONTACT est une chaîne indépendante, sans lien avec le NTSB, la FAA ou une compagnie aérienne, ni approuvée par eux. Documents et images officiels : œuvres du gouvernement américain (domaine public). Musique et effets sonores originaux.",
tags="#accidentaerien #aviation #NTSB #securiteaerienne #Miami")
L["it"] = dict(
title="Uscita di pista del 767 di Amazon a Miami: cosa mostrano i dati NTSB",
intro="Uscita di pista di un Boeing 767 di Amazon a Miami (volo 7598 di 21 Air, 6 settembre 2026), spiegata con i dati preliminari dell'NTSB: registratore dei dati di volo, cronologia del registratore vocale di cabina, meteo, controllo del traffico aereo e rilievi sul relitto.",
p2="Il cargo Boeing 767 ha toccato la pista 30 a circa 3.750 piedi dalla soglia, è uscito dal fondo pista a 113 nodi e ha attraversato una strada pubblica. Cinque persone a terra sono morte. Questa è un'analisi di ciò che l'NTSB ha pubblicato finora, non una conclusione sulla causa. L'NTSB non ha stabilito una causa probabile.",
ch_h="Capitoli", ch=["Cosa è successo","L'indagine","L'aereo e il volo","Aeroporto internazionale di Miami, pista 30","Il meteo","Controllo del traffico aereo","Cronologia del registratore vocale","Cos'è un avvicinamento stabilizzato","L'atterraggio, dai dati di volo","Come si ferma un jet così","Replay: la parte finale dell'atterraggio","Oltre la pista","Cosa hanno trovato gli investigatori","EMAS","Cosa non si sa ancora","Prossimi passi"],
src_h="Fonti", src=["Rapporto preliminare NTSB DCA26MA352","Aggiornamento dell'indagine NTSB, 9 settembre 2026","Pagina dell'indagine NTSB","Dati aeroportuali FAA (pista 12/30, soglia spostata)","Nota ALAR della Flight Safety Foundation (avvicinamento stabilizzato)","FAA — EMAS","Filmati d'archivio: DVIDS (Dipartimento della Difesa USA), KC-46A (aerocisterna derivata dal Boeing 767), non è l'aereo dell'incidente","Immagini aeree: USGS The National Map. La ricostruzione 3D è illustrativa; il movimento tra i punti dati NTSB è interpolato. Le componenti del vento sono un nostro calcolo dal vento riportato."],
prelim="Tutte le informazioni sono preliminari e possono cambiare.",
indep="LAST CONTACT è un canale indipendente, non affiliato né approvato da NTSB, FAA o compagnie aeree. Documenti e immagini ufficiali: opere del governo USA (pubblico dominio). Musica ed effetti sonori originali.",
tags="#incidenteaereo #aviazione #NTSB #sicurezzavolo #Miami")
L["de"] = dict(
title="Amazon-767 schießt in Miami über die Piste: Was die NTSB-Daten zeigen",
intro="Pistenüberrollung einer Amazon-Boeing-767 in Miami (21 Air Flug 7598, 6. September 2026), erklärt mit vorläufigen NTSB-Daten: Flugdatenschreiber, Ablauf laut Cockpit-Stimmenrekorder, Wetter, Flugsicherung und Befunde am Wrack.",
p2="Der Boeing-767-Frachter setzte etwa 3.750 Fuß hinter der Schwelle von Piste 30 auf, verließ das Pistenende mit 113 Knoten und überquerte eine öffentliche Straße. Fünf Menschen am Boden kamen ums Leben. Dies ist eine Aufbereitung dessen, was das NTSB bisher veröffentlicht hat, keine Feststellung zur Ursache. Das NTSB hat noch keine wahrscheinliche Ursache bestimmt.",
ch_h="Kapitel", ch=["Was geschah","Die Untersuchung","Das Flugzeug und der Flug","Miami International, Piste 30","Das Wetter","Flugsicherung","Ablauf laut Stimmenrekorder","Was ein stabilisierter Anflug ist","Die Landung, laut Flugdaten","Wie ein solcher Jet anhält","Wiederholung: der letzte Teil der Landung","Hinter der Piste","Was die Ermittler fanden","EMAS","Was noch unbekannt ist","Wie es weitergeht"],
src_h="Quellen", src=["Vorläufiger NTSB-Bericht DCA26MA352","NTSB-Untersuchungsupdate, 9. September 2026","NTSB-Untersuchungsseite","FAA-Flughafendaten (Piste 12/30, versetzte Schwelle)","ALAR-Briefing der Flight Safety Foundation (stabilisierter Anflug)","FAA — EMAS","Archivaufnahmen: DVIDS (US-Verteidigungsministerium), KC-46A (Tanker auf Basis der Boeing 767), nicht das Unfallflugzeug","Luftbilder: USGS The National Map. Die 3D-Rekonstruktion ist illustrativ; Bewegungen zwischen NTSB-Datenpunkten sind interpoliert. Windkomponenten sind unsere eigene Berechnung aus dem gemeldeten Wind."],
prelim="Alle Informationen sind vorläufig und können sich ändern.",
indep="LAST CONTACT ist ein unabhängiger Kanal und steht in keiner Verbindung zum NTSB, zur FAA oder zu einer Fluggesellschaft. Offizielle Dokumente und Bilder: Werke der US-Regierung (gemeinfrei). Musik und Soundeffekte sind original.",
tags="#Flugunfall #Luftfahrt #NTSB #Flugsicherheit #Miami")
L["ru"] = dict(
title="Выкатывание Boeing 767 Amazon в Майами: что показывают данные NTSB",
intro="Выкатывание за пределы полосы грузового Boeing 767 Amazon в Майами (рейс 7598 авиакомпании 21 Air, 6 сентября 2026 года) — разбор по предварительным данным NTSB: бортовой самописец, хронология речевого самописца, погода, работа диспетчеров и находки на месте.",
p2="Грузовой Boeing 767 коснулся полосы 30 примерно в 3750 футах от торца, сошёл с конца полосы на скорости 113 узлов и пересёк дорогу общего пользования. На земле погибли пять человек. Это разбор того, что NTSB опубликовал на данный момент, а не вывод о причине. NTSB пока не установил вероятную причину.",
ch_h="Главы", ch=["Что произошло","Расследование","Самолёт и рейс","Международный аэропорт Майами, полоса 30","Погода","Управление воздушным движением","Хронология речевого самописца","Что такое стабилизированный заход","Посадка по полётным данным","Как останавливается такой самолёт","Повтор: последняя часть посадки","За пределами полосы","Что нашли следователи","EMAS","Что пока неизвестно","Что дальше"],
src_h="Источники", src=["Предварительный отчёт NTSB DCA26MA352","Обновление расследования NTSB, 9 сентября 2026 года","Страница расследования NTSB","Данные FAA по аэропорту (полоса 12/30, смещённый порог)","Справка ALAR от Flight Safety Foundation (стабилизированный заход)","FAA — EMAS","Архивные кадры: DVIDS (Министерство обороны США), KC-46A (заправщик на базе Boeing 767), это не самолёт, попавший в аварию","Аэрофотоснимки: USGS The National Map. 3D-реконструкция иллюстративна; движение между точками данных NTSB интерполировано. Составляющие ветра — наш собственный расчёт по сообщённому ветру."],
prelim="Вся информация предварительная и может измениться.",
indep="LAST CONTACT — независимый канал, не связанный с NTSB, FAA или какой-либо авиакомпанией и не одобренный ими. Официальные документы и изображения — произведения правительства США (общественное достояние). Музыка и звуковые эффекты оригинальные.",
tags="#авиакатастрофа #авиация #NTSB #безопасностьполетов #Майами")
L["hi"] = dict(
title="मियामी में Amazon 767 रनवे से आगे निकला: NTSB डेटा क्या दिखाता है",
intro="मियामी में Amazon के Boeing 767 का रनवे ओवररन (21 Air फ़्लाइट 7598, 6 सितंबर 2026), NTSB के प्रारंभिक डेटा से समझाया गया: फ़्लाइट डेटा रिकॉर्डर, कॉकपिट वॉइस रिकॉर्डर टाइमलाइन, मौसम, एयर ट्रैफ़िक कंट्रोल और मलबे से मिली जानकारी।",
p2="Boeing 767 मालवाहक विमान रनवे 30 की दहलीज़ से लगभग 3,750 फ़ुट आगे उतरा, 113 नॉट पर रनवे के अंत से निकला और एक सार्वजनिक सड़क पार कर गया। ज़मीन पर पाँच लोगों की मौत हुई। यह NTSB द्वारा अब तक जारी जानकारी का विश्लेषण है, कारण का निष्कर्ष नहीं। NTSB ने अभी संभावित कारण तय नहीं किया है।",
ch_h="अध्याय", ch=["क्या हुआ","जाँच","विमान और उड़ान","मियामी इंटरनेशनल, रनवे 30","मौसम","एयर ट्रैफ़िक कंट्रोल","कॉकपिट वॉइस रिकॉर्डर टाइमलाइन","स्टेबलाइज़्ड अप्रोच क्या है","फ़्लाइट डेटा से लैंडिंग","ऐसा जेट कैसे रुकता है","रीप्ले: लैंडिंग का आखिरी हिस्सा","रनवे के आगे","जाँचकर्ताओं को क्या मिला","EMAS","अभी क्या अज्ञात है","आगे क्या"],
src_h="स्रोत", src=["NTSB प्रारंभिक रिपोर्ट DCA26MA352","NTSB जाँच अपडेट, 9 सितंबर 2026","NTSB जाँच पेज","FAA एयरपोर्ट डेटा (रनवे 12/30, विस्थापित दहलीज़)","Flight Safety Foundation ALAR ब्रीफ़िंग नोट (स्टेबलाइज़्ड अप्रोच)","FAA — EMAS","फ़ाइल फ़ुटेज: DVIDS (अमेरिकी रक्षा विभाग), KC-46A (Boeing 767 आधारित टैंकर), यह हादसे वाला विमान नहीं है","हवाई तस्वीरें: USGS The National Map। 3D पुनर्निर्माण केवल चित्रण है; NTSB डेटा बिंदुओं के बीच की गति अनुमानित है। हवा के घटक रिपोर्ट की गई हवा से हमारी अपनी गणना हैं।"],
prelim="सारी जानकारी प्रारंभिक है और बदल सकती है।",
indep="LAST CONTACT एक स्वतंत्र चैनल है और NTSB, FAA या किसी एयरलाइन से संबद्ध या उनके द्वारा समर्थित नहीं है। आधिकारिक दस्तावेज़ और तस्वीरें: अमेरिकी सरकारी कार्य (पब्लिक डोमेन)। संगीत और साउंड इफ़ेक्ट मौलिक हैं।",
tags="#विमानहादसा #aviation #NTSB #हवाईसुरक्षा #Miami")
for code,d in L.items():
    assert len(d["title"])<=70, (code,len(d["title"]))
    out=[d["intro"],"",d["p2"],"",d["ch_h"]]
    out+= [f"{t} {c}" for t,c in zip(TC,d["ch"])]
    out+=["",d["src_h"]]
    for s,u in zip(d["src"],SRC_URLS):
        out.append(f"• {s}: {u}" if u else f"• {s}")
    out+=["",d["prelim"],"",d["indep"],"",d["tags"]]
    os.makedirs(f"dub/{code}",exist_ok=True)
    open(f"dub/{code}/title.txt","w").write(d["title"]+"\n")
    open(f"dub/{code}/description.txt","w").write("\n".join(out)+"\n")
    print(code,len(d["title"]),len("\n".join(out)))
