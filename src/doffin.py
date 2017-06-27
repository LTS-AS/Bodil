import webbrowser

cpvs=[
    '30200000', #Datautstyr og -materiell
####34=Transportutstyr og hjelpeprodukter til transport
    '34970000', #Trafikkovervåkningssystem
    '34990000', #Kontroll-, sikkerhets- signal- og lysutstyr
####35=Sikkerhets-, brannslukkings-, politi- og forsvarsutstyr
    '35125000', #Overvåkingssystemer
####42=Diverse maskineri til generelt og spesielt bruk
    '42122220', #Avløpspumper
    '42500000', # Kjøle- og ventilasjonsutstyr
    '42520000', #Ventilasjonsutstyr
    '42961000', #Adgangskontrollsystemer
    '42961200', #Scada eller lignende system
    '45331000', #Installasjon av varme-, ventilasjons- og klimaanlegg
    '45331210', #Arbeid i forbindelse med ventilasjonsanlegg
    '48921000', #Automasjonssystemer
    '71315410', #Inspeksjon av ventilasjonssystemer
####98=Andre kommunale, sosiale og personlige tjenester
    '98395000', #Låsesmedtjenester
    '98363000', #Dykking
    ]
    
url = 'https://www.doffin.no/Notice?query='
url = url + '&PageNumber=1'
url = url + '&PageSize=100'# elementer per side. 10, 25, 50 eller 100
url = url + '&OrderingType=2' #sorter på 0=relevans, 1=kunngjøringsdato, 2=tilbudsfrist
url = url + '&OrderingDirection=1'#0=stigende, 1=synkende
url = url + '&RegionId=6' # ''=alle, 6=Trøndelag, 12=Østfold
url = url + '&CountyId='
url = url + '&MunicipalityId='
url = url + '&IsAdvancedSearch=true' #ser ut som dette er flagget "inkluder overliggende"
url = url + '&location=6' #Samme som region??
url = url + '&NoticeType=2'#Kunngjøringstype ''=alle, 2=kunngjøring av konkurranse
url = url + '&PublicationType='
url = url + '&IncludeExpired=false'
url = url + '&Cpvs='  + '+'.join(cpvs)
url = url + '&EpsReferenceNr='
url = url + '&DeadlineFromDate='
url = url + '&DeadlineToDate='
url = url + '&PublishedFromDate='
url = url + '&PublishedToDate='

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)
