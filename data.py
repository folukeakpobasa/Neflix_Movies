import requests

# URL of the CSV file
url = "https://www.datacamp.com/datalab/w/cbb68350-11c2-4796-96e3-5b1a081c12b7/edit?emitCellOutputs=false&reducedMenuBar=true&showExploreMore=false&showLeftNavigation=false&showNavBar=false&showPublicationButton=false&showOnlyRelevantSampleIntegrationIds[]=89e17161-a224-4a8a-846b-0adc0fe7a4b1&showOnlyRelevantSampleIntegrationIds[]=e0c96696-ae0a-46fb-b6f9-1a43eb428ecb&showOnlyRelevantSampleIntegrationIds[]=b1fcb109-b4fe-4543-bc98-681df8c4dc6e&showOnlyRelevantSampleIntegrationIds[]=fcf37a0e-f8bd-4c85-95a5-201d3eebea48&showOnlyRelevantSampleIntegrationIds[]=db697c09-0402-4a02-b327-26018dc2ecce&showOnlyRelevantSampleIntegrationIds[]=7569175e-98be-4c89-9873-c20f699a9cc7&fetchUnlistedSampleIntegrationIds[]=7569175e-98be-4c89-9873-c20f699a9cc7#netflix_datacsv"


# Download the CSV file
response = requests.get(url)

# Save it to a file
with open("data.csv", "wb") as file:
    file.write(response.content)

print("Download complete: data.csv")
