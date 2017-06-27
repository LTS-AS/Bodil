import webbrowser


url = 'https://www.doffin.no/Notice?query=&PageNumber=1&PageSize=10&OrderingType=0&OrderingDirection=1&RegionId=6&CountyId=&MunicipalityId=&IsAdvancedSearch=false&location=6&NoticeType=&PublicationType=&IncludeExpired=false&Cpvs='
cpvs=['34970000',
      '34990000',
      '35125000',
      '48921000', # Automasjonssystemer
      '98395000',
      '98363000']

url2 = "&EpsReferenceNr=&DeadlineFromDate=&DeadlineToDate=&PublishedFromDate=&PublishedToDate="
url = url + '+'.join(cpvs) + url2



# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)
