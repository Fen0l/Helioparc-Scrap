#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request

import sys, re


contacts = []

contacted = []
MAIN_URL 	= "http://www.helioparc.com/fr/residents/themes/entreprises-et-autres-acteurs-de-linnovation"
PREFIXE 	= "http://www.helioparc.com%s"


def PagetoSoup(url): # Mise en beauté de la page
	try:
		response = urllib.request.urlopen( url )
	except urllib.error.HTTPError as e:
		print("HTTPError with: ", url, " as ", e)
		return None

	return BeautifulSoup(response.read())


def main():
	p = PagetoSoup(MAIN_URL)

	# a href="/fr/residents/la-creme-le-hollandais-volant-technopole-helioparc-galilee-pau">
	links = p.find_all('a', href = re.compile('/fr/residents/*'))

	for link in links:
		if not link.div : continue
		if link.div['class'][0] != 'img': continue

		link = PREFIXE % link['href']
		print("LINK - ", link)

		# Already scrapped ?
		if link in contacted: continue
		p = PagetoSoup(link)
		# <div class="presentation">
		#infos = p.find_all('div')
		infos = p.find("div", { "class" : "presentation" })
		if not infos: continue

		company = {
			'name': infos.find('h3').string,
			'emails': [],
			'contact': ''
		} 

		# Get emails present on the page
		emails = infos.find_all('a')
		for em in emails:
			if not em.string: continue
			if re.match("[^@]+@[^@]+\.[^@]+", em.string) and em.string not in company['emails']:
				company['emails'].append(em.string)


		# Get contact name
		elements = p.find_all(['span', 'li'])
		tmp = False
		for el in elements:
			# find <span>Contact :</span>
			if(el.string == "Contact :"):
				tmp = True
				continue

			if tmp:
				tmp = False
				company['contact'] = el.string

		if company['emails']:
			contacts.append(company)
		contacted.append(link)


	print(contacts)


if __name__ == '__main__':

	contacts = [{'name': ' APESA ', 'emails': ['contact@apesa.fr'], 'contact': 'Benoit De Guillebon'}, {'name': ' APITM ', 'emails': ['contact@apieh.fr'], 'contact': 'Rémi Giraudel et Aurélien Cuif'}, {'name': ' Artelia Région Sud-Ouest ', 'emails': ['pau@arteliagroup.com'], 'contact': 'Olivier TUCHAGUES'}, {'name': ' Artelia Bâtiment et Industrie ', 'emails': ['alain.lopez@arteliagroup.com'], 'contact': 'Alain LOPEZ'}, {'name': ' ASCOT ', 'emails': ['overdreau@ascot.fr'], 'contact': 'Olivier VERDREAU'}, {'name': ' ATI Services ', 'emails': ['h.bahurlet@ati-services.com'], 'contact': 'Hélène BAHURLET'}, {'name': ' Atos Worldgrid ', 'emails': ['jean-philippe.baron@atos.net'], 'contact': 'Jean-Philippe BARON'}, {'name': ' B2E Lapassade ', 'emails': ['l.lapassade@b2elapassade.com'], 'contact': 'Lydie LAPASSADE'}, {'name': ' BackPlan ', 'emails': ['sophie.bernier@backplan.fr'], 'contact': 'Sophie BERNIER'}, {'name': ' Belharra Conseil ', 'emails': ['belharraconseil@orange.fr'], 'contact': 'Marc PRIGENT'}, {'name': ' Bip Info ', 'emails': ['contact@bipinfo.com'], 'contact': 'Bip Info'}, {'name': ' DEEP Concept ', 'emails': ['info@deepconcept.fr'], 'contact': 'Cyrille DUCHESNE'}, {'name': ' E-city ', 'emails': ['contact@e-city.fr'], 'contact': 'Thierry CHARDY'}, {'name': ' ECO CEPS ', 'emails': ['rozisjf@club-internet.fr'], 'contact': 'Jean François ROZIS'}, {'name': ' Effitech ', 'emails': ['sylvain.paquet@effitech.eu'], 'contact': 'Sylvain PAQUET'}, {'name': ' Enesol Géothermie ', 'emails': ['cp.enesol.geo@gmail.com'], 'contact': 'Christophe PIQUEMAL'}, {'name': ' Euro Engineering ', 'emails': ['bruno.duc@euro-engineering.com'], 'contact': 'Bruno DUC'}, {'name': ' FD Topographie ', 'emails': ['nicolas.ferrer@fd-topographie.fr'], 'contact': 'Nicolas FERRER'}, {'name': " Feuille De Com' ", 'emails': ['valerie.thome@feuilledecom.fr'], 'contact': 'Valérie THOME'}, {'name': ' Formations & conseil UT2A ', 'emails': ['formation.ut2a@univ-pau.fr'], 'contact': 'Hugues PAUCOT'}, {'name': ' Foxyz ', 'emails': ['laurent.dalier@gmail.com'], 'contact': 'Laurent CASTANG'}, {'name': ' Go GeoEngineering ', 'emails': ['djamel.boukhelf@gogeo.biz'], 'contact': 'Djamel Boukhelf'}, {'name': ' GPC Solutions ', 'emails': ['contact@gpcsolutions.fr'], 'contact': 'Raphaël DOURSENAUD'}, {'name': ' INT ', 'emails': ['lionel.jeanson@int.com'], 'contact': 'Lionel JEANSON'}, {'name': ' Kerhis ', 'emails': ['kerhis@kerhis.com'], 'contact': 'Jo DREAU'}, {'name': ' Les Origines ', 'emails': ['c.roger@lesorigines.fr'], 'contact': 'Catherine ROGER'}, {'name': ' Mapotempo ', 'emails': ['contact@mapotempo.com'], 'contact': 'Mehdi JABRANE'}, {'name': ' MASE Sud-Ouest ', 'emails': ['gaelle.henault@maseso.fr'], 'contact': 'Nelly ALACOQUE'}, {'name': ' MEDIA Conseil ', 'emails': ['a.gayon@media-conseil.net'], 'contact': 'Alain GAYON'}, {'name': ' Median Conseil ', 'emails': ['benoit.thome@median-conseil.com'], 'contact': 'Benoît THOME'}, {'name': ' Mosart PME ', 'emails': ['mosart-pme@mosart-pme.org'], 'contact': 'Céline RICHARD'}, {'name': ' Neebtech ', 'emails': ['neebtech@gmail.com'], 'contact': 'Nour-Eddine EL BOUNIA'}, {'name': ' Novae Communication ', 'emails': ['contact@novae-communication.com'], 'contact': 'Didier LABORDE'}, {'name': ' Novaresa ', 'emails': ['contact@novaresa.fr'], 'contact': 'Didier LABORDE'}, {'name': ' Numérique 64 ', 'emails': ['numerique64@numerique64.fr'], 'contact': 'Thierry VENIN'}, {'name': ' Optinergie ', 'emails': ['contact@optinergie.fr'], 'contact': 'Lionel BARBE'}, {'name': ' Orthalis Sud ', 'emails': ['stephane.fourcade@orthalis.fr'], 'contact': 'Stéphane FOURCADE'}, {'name': ' PGS Geophysical ', 'emails': ['philip.ross@pgs.com'], 'contact': 'Philippe ROSS'}, {'name': ' Pricemetry ', 'emails': ['contact@pricemetry.com'], 'contact': 'Samuel ROY'}, {'name': ' Quasinil ', 'emails': ['benoit.chiron@quasinil.com'], 'contact': 'Benoit CHIRON'}, {'name': ' Naturabuy ', 'emails': ['olivier@naturabuy.fr'], 'contact': 'Olivier OCCELLI'}, {'name': ' Skills4 ', 'emails': ['arthur.boivin@skills4.io'], 'contact': 'Arthur BOIVIN'}, {'name': ' SMTB ', 'emails': ['smtb-lacq@wanadoo.fr'], 'contact': 'René VALTON'}, {'name': ' SOCOTEC France ', 'emails': ['bruno.sibers@socotec.com'], 'contact': 'Patrick Armando'}, {'name': ' SOPRA STERIA Group ', 'emails': ['steria.pau@soprasteria.com'], 'contact': 'SOPRA STERIA Group'}, {'name': ' STEP ', 'emails': ['kbertonazzi@step-sa.fr'], 'contact': 'Kenny BERTONAZZI'}, {'name': ' Studio Virtu ', 'emails': ['contact@studio-virtu.fr'], 'contact': 'Julien CHARRIERAS'}, {'name': ' Syndicat Intercommunal du Gave de Pau ', 'emails': ['si.gavedepau@heliantis.net'], 'contact': 'Henri PELLIZZARO'}, {'name': ' Syndicat Mixte du Gave de Pau ', 'emails': ['si.gavedepau@heliantis.net'], 'contact': 'Henri PELLIZZARO'}, {'name': " TECH'advantage ", 'emails': ['david.selleron@tech-advantage.com'], 'contact': 'David SELLERON'}, {'name': ' VERDI BATIMENT SUD OUEST ', 'emails': ['batimentsudouest@verdi-ingenierie.fr'], 'contact': 'VERDI BATIMENT SUD OUEST'}, {'name': ' EURO AIRSHIP ', 'emails': ['president@euroairship.com'], 'contact': 'Jean LESCAT'}, {'name': ' XAMEN Technologies ', 'emails': ['t.bleau@xamen.fr'], 'contact': 'Thierry BLEAU'}, {'name': ' FEBUS OPTICS ', 'emails': ['vincentlanticq@febus-optics.com'], 'contact': 'Vincent LANTICQ'}, {'name': ' INNOVSYSTEM SAS ', 'emails': ['contact@innovsystem.fr'], 'contact': 'Antoine Cascales'}, {'name': ' SYMALAB ', 'emails': ['contact@symalab.fr'], 'contact': 'Sylvain MALLET'}, {'name': ' BOURSO-BAT ', 'emails': ['contact@boursobat.com'], 'contact': 'Bourso-Bat'}, {'name': ' SURVEY GROUPE ', 'emails': ['contact@survey-groupe.fr'], 'contact': 'R. OLIVE'}, {'name': ' EXCELLENCE LOGGING (EXLOG) ', 'emails': ['ydouarin@exlog.com'], 'contact': 'Yann DOUARIN'}, {'name': ' LM ENTREPRISE ', 'emails': ['contact@lmentreprise.fr'], 'contact': 'Gabrielle MOUZE'}, {'name': ' Ease Engineering ', 'emails': ['adargelos@hotmail.com'], 'contact': 'Anne Dargelos'}, {'name': ' Real Time Seismic ', 'emails': ['claudio@fox-geoscience.com'], 'contact': 'Claudio Strobbia'}, {'name': ' PlaneteProfs ', 'emails': ['contact@planeteprofs.com'], 'contact': 'Paul Escudé'}, {'name': ' Refolded-Games ', 'emails': ['refoldedgames@gmail.com'], 'contact': 'Melvin REY'}, {'name': ' CiTO INFORMATIQUE ', 'emails': ['contact@citosav.com'], 'contact': 'Louis Lartigue'}, {'name': ' Urban&You; ', 'emails': ['digital-plu@urbanandyou.fr'], 'contact': 'Carine de BELMONT'}, {'name': ' EFFICIO ', 'emails': ['claude.valet@efficio.ovh'], 'contact': 'Claude Valet'}, {'name': ' WINUPS ', 'emails': ['contact@winups.fr'], 'contact': 'David Desclaux'}, {'name': ' INSPYR ÉNERGIES ENVIRONNEMENT ', 'emails': ['contact@inspyr-ee.com'], 'contact': 'INSPYR'}, {'name': ' Artfact ', 'emails': ['artfact64@gmail.com'], 'contact': 'Sébastien Loustau'}, {'name': ' DEEPI ', 'emails': ['deepi-sarl@wanadoo.fr'], 'contact': 'Christian LE GALL'}, {'name': ' ValoSys ', 'emails': ['l.debu@valosys.fr'], 'contact': 'Laurent Debû'}, {'name': ' LGM ', 'emails': ['Frederic.RIOS@lgm.fr'], 'contact': 'Frédéric RIOS - Responsable d’équipe Tarbes'}, {'name': ' KEIKO ', 'emails': ['contact@keiko-services.fr'], 'contact': 'Romain Mérisse-Toussaint'}, {'name': ' 360 Energia ', 'emails': ['e.pajot@360energia.fr'], 'contact': 'Emmanuel PAJOT'}, {'name': ' SERVICE ORGANISATION METHODES ', 'emails': ['mail.sud-ouest@som-industrie.com'], 'contact': 'Alexis BRUGEMAN'}, {'name': ' Fluent Data ', 'emails': ['yves.darmaillac@fluentdata.fr'], 'contact': 'Yves Darmaillac'}, {'name': ' SIMPLE & CORRECT FRANCE ', 'emails': ['rcascales@simpleandcorrect.com'], 'contact': 'Simple & Correct France'}, {'name': ' BS Digital ', 'emails': ['alexandre.stojanovic@bs.digital'], 'contact': 'Alexandre Stojanovic'}, {'name': ' SQUARE ACHAT ', 'emails': ['contact@square-achat.com'], 'contact': 'Accueil Square Achat'}, {'name': ' SKIPPER NDT ', 'emails': ['l.kassir@skipperndt.com'], 'contact': 'Luigi KASSIR'}, {'name': ' LA CREME/ LE HOLLANDAIS VOLANT ', 'emails': ['caroleanne.sowska@gmail.com'], 'contact': 'Carole-Anne SOWSKA'}, {'name': ' Petromanas Energy France ', 'emails': ['pascale.arangois@horizon-petroleum.com'], 'contact': 'Pascale ARANGOIS'}, {'name': ' GEOESPACE ', 'emails': ['a.mercier@geoespace.com'], 'contact': 'Anne Mercier'}]
	mails = []
	for contact in contacts:
		for mail in contact['emails']:
			mails.append(mail)

	print(', '.join(mails))

	sys.exit()

	main()