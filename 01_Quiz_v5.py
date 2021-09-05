"""Program that runs a quiz based on capitals. It asks the users what the capital of a certain country is.
This version uses the full/final list of capitals that will be used in the overall program/game.
Jung Woo Yi
Version 5 – 03/08/2021
"""

# Importing
import random

# List that contains capitals and countries
capitals = [['Wellington', 'New Zealand'], ['Canberra', 'Australia'],
            ['Washington, D.C.', 'the United States of America'], ['Seoul', 'the Republic of Korea'],
            ['Ottawa', 'Canada'], ['Kabul', 'Afghanistan'], ['Tirana', 'Albania'], ['Algiers', 'Algeria'],
            ['Andorra la Vella', 'Andorra'], ['Luanda', 'Angola'], ["St John's", 'Antigua and Barbuda'],
            ['Buenos Aires', 'Argentina'], ['Yerevan', 'Armenia'], ['Vienna', 'Austria'], ['Baku', 'Azerbaijan'],
            ['Nassau', 'the Bahamas'], ['Manama', 'Bahrain'], ['Dhaka', 'Bangladesh'], ['Bridgetown', 'Barbados'],
            ['Minsk', 'Belarus'], ['Brussels', 'Belgium'], ['Belmopan', 'Belize'], ['Porto Novo', 'Benin'],
            ['Thimphu', 'Bhutan'], ['La Paz', 'Bolivia'], ['Sarajevo', 'Bosnia and Herzegovina'],
            ['Gaborone', 'Botswana'], ['Brasilia', 'Brazil'], ['Bandar Seri Begawan', 'Brunei'], ['Sofia', 'Bulgaria'],
            ['Ouagadougou', 'Burkina Faso'], ['Bujumbura', 'Burundi'], ['Praia', 'Cabo Verde'],
            ['Phnom Penh', 'Cambodia'], ['Yaounde', 'Cameroon'], ['Bangui', 'the Central African Republic'],
            ["N'Djamena", 'Chad'], ['Santiago', 'Chile'], ['Beijing', 'China'], ['Bogotá', 'Colombia'],
            ['Moroni', 'Comoros'], ['Kinshasa', 'the Democratic Republic of the Congo'], ['San José', 'Costa Rica'],
            ['Yamoussoukro', "Côte d'Ivoire"], ['Zagreb', 'Croatia'], ['Havana', 'Cuba'], ['Nicosia', 'Cyprus'],
            ['Prague', 'Czech Republic'], ['Copenhagen', 'Denmark'], ['Djibouti', 'Djibouti'], ['Roseau', 'Dominica'],
            ['Santo Domingo', 'Dominican Republic'], ['Dili', 'East Timor'], ['Quito', 'Ecuador'], ['Cairo', 'Egypt'],
            ['San Salvador', 'El Salvador'], ['Malabo', 'Equatorial Guinea'], ['Asmara', 'Eritrea'],
            ['Tallinn', 'Estonia'], ['Mbabane', 'eSwatini'], ['Addis Ababa', 'Ethiopia'], ['Suva', 'Fiji'],
            ['Helsinki', 'Finland'], ['Paris', 'France'], ['Libreville', 'Gabon'], ['Banjul', 'the Gambia'],
            ['Tbilisi', 'Georgia'], ['Berlin', 'Germany'], ['Accra', 'Ghana'], ['Athens', 'Greece'],
            ["St George's", 'Grenada'], ['Guatemala City', 'Guatemala'], ['Conakry', 'Guinea'],
            ['Bissau', 'Guinea-Bissau'], ['Georgetown', 'Guyana'], ['Port-au-Prince', 'Haiti'],
            ['Tegucigalpa', 'Honduras'], ['Budapest', 'Hungary'], ['Reykjavik', 'Iceland'], ['New Delhi', 'India'],
            ['Jakarta', 'Indonesia'], ['Tehran', 'Iran'], ['Baghdad', 'Iraq'], ['Dublin', 'the Republic of Ireland'],
            ['Jerusalem', 'Israel'], ['Rome', 'Italy'], ['Kingston', 'Jamaica'], ['Tokyo', 'Japan'],
            ['Amman', 'Jordan'], ['Astana', 'Kazakhstan'], ['Nairobi', 'Kenya'], ['Bairiki', 'Kiribati'],
            ['Pyongyang', 'North Korea'], ['Priština', 'Kosovo'], ['Kuwait City', 'Kuwait'], ['Bishkek', 'Kyrgyzstan'],
            ['Vientiane', 'Laos'], ['Riga', 'Latvia'], ['Beirut', 'Lebanon'], ['Maseru', 'Lesotho'],
            ['Monrovia', 'Liberia'], ['Tripoli', 'Libya'], ['Vaduz', 'Liechtenstein'], ['Vilnius', 'Lithuania'],
            ['Luxembourg', 'Luxembourg'], ['Antananarivo', 'Madagascar'], ['Lilongwe', 'Malawi'],
            ['Kuala Lumpur', 'Malaysia'], ['Male', 'Maldives'], ['Bamako', 'Mali'], ['Valletta', 'Malta'],
            ['Majuro', 'the Marshall Islands'], ['Nouakchott', 'Mauritania'], ['Port Louis', 'Mauritius'],
            ['Mexico City', 'Mexico'], ['Palikir', 'the Federated States of Micronesia'], ['Chişinău', 'Moldova'],
            ['Ulaanbaatar', 'Mongolia'], ['Podgorica', 'Montenegro'], ['Rabat', 'Morocco'], ['Maputo', 'Mozambique'],
            ['Naypyidaw', 'Union of Myanmar'], ['Windhoek', 'Namibia'], ['Kathmandu', 'Nepal'],
            ['Amsterdam', 'Netherlands'], ['Managua', 'Nicaragua'], ['Niamey', 'Niger'], ['Abuja', 'Nigeria'],
            ['Skopje', 'North Macedonia'], ['Oslo', 'Norway'], ['Muscat', 'Oman'], ['Islamabad', 'Pakistan'],
            ['Ngerulmud', 'Palau'], ['Panama City', 'Panama'], ['Port Moresby', 'Papua New Guinea'],
            ['Asunción', 'Paraguay'], ['Lima', 'Peru'], ['Manila', 'the Philippines'], ['Warsaw', 'Poland'],
            ['Lisbon', 'Portugal'], ['Bucharest', 'Romania'], ['Moscow', 'Russia'], ['Kigali', 'Rwanda'],
            ['Basseterre', 'St Kitts and Nevis'], ['Castries', 'St Lucia'],
            ['Kingstown', 'St Vincent and the Grenadines'], ['Apia', 'Samoa'], ['San Marino', 'San Marino'],
            ['São Tomé', 'São Tomé and Príncipe'], ['Riyadh', 'Saudi Arabia'], ['Dakar', 'Senegal'],
            ['Belgrade', 'Serbia'], ['Victoria', 'Seychelles'], ['Freetown', 'Sierra Leone'],
            ['Singapore City', 'Singapore'], ['Bratislava', 'Slovakia'], ['Ljubljana', 'Slovenia'],
            ['Honiara', 'the Solomon Islands'], ['Mogadishu', 'Somalia'], ['Pretoria', 'South Africa'],
            ['Madrid', 'Spain'], ['Colombo', 'Sri Lanka'], ['Khartoum', 'Sudan'], ['Juba', 'South Sudan'],
            ['Paramaribo', 'Suriname'], ['Stockholm', 'Sweden'], ['Berne', 'Switzerland'], ['Damascus', 'Syria'],
            ['Taipei', 'Taiwan'], ['Dushanbe', 'Tajikistan'], ['Dodoma', 'Tanzania'], ['Bangkok', 'Thailand'],
            ['Lomé', 'Togo'], ["Nuku'alofa", 'Tonga'], ['Port-of-Spain', 'Trinidad and Tobago'], ['Tunis', 'Tunisia'],
            ['Ankara', 'Turkey'], ['Ashgabat', 'Turkmenistan'], ['Funafuti', 'Tuvalu'], ['Kampala', 'Uganda'],
            ['Kiev', 'Ukraine'], ['Abu Dhabi', 'the United Arab Emirates'], ['London', 'the United Kingdom'],
            ['Montevideo', 'Uruguay'], ['Tashkent', 'Uzbekistan'], ['Vila', 'Vanuatu'], ['Caracas', 'Venezuela'],
            ['Hanoi', 'Vietnam'], ["Sana'a", 'Yemen'], ['Lusaka', 'Zambia'], ['Harare', 'Zimbabwe']]

get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
country = capitals[get_country][1]  # This gets the country from the list
capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above

question = ""
while question != "Q":
    # Asks the user the capital of the country
    question = input("What is the capital of {}? ".format(country))
    if question == capital:
        print("Correct")
        if len(capitals) > 0:
            capitals.pop(get_country)
        if len(capitals) > 0:
            get_country = random.randint(0, len(capitals) - 1)  # This gets a list from within the whole list
            country = capitals[get_country][1]  # This gets the country from the list
            capital = capitals[get_country][0]  # This gets the respective capital for the country in the line above
        else:
            print("Finished")
            break
    elif question == "Q" or question == "q":
        break
    else:
        print("Incorrect\n"
              "The correct answer was {}".format(capital))
