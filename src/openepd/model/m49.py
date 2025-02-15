#
#  Copyright 2025 by C Change Labs Inc. www.c-change-labs.com
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
M49_CODE_WORLD = "001"
M49_CODE_AFRICA = "002"
M49_CODE_NORTH_AMERICA = "003"
M49_CODE_SOUTH_AMERICA = "005"
M49_CODE_OCEANIA = "009"
M49_CODE_CENTRAL_AMERICA = "013"
M49_CODE_ASIA = "142"
M49_CODE_EUROPE = "150"

NORTHERN_AFRICA = {
    "DZ",  # 012 Algeria
    "EG",  # 818 Egypt
    "LY",  # 434 Libya
    "MA",  # 504 Morocco
    "SD",  # 729 Sudan
    "TN",  # 788 Tunisia
    "EH",  # 732 Western Sahara
}
EASTERN_AFRICA = {
    "IO",  # 086 British Indian Ocean Territory
    "BI",  # 108 Burundi
    "KM",  # 174 Comoros
    "DJ",  # 262 Djibouti
    "ER",  # 232 Eritrea
    "ET",  # 231 Ethiopia
    "TF",  # 260 French Southern Territories
    "KE",  # 404 Kenya
    "MG",  # 450 Madagascar
    "MW",  # 454 Malawi
    "MU",  # 480 Mauritius
    "YT",  # 175 Mayotte
    "MZ",  # 508 Mozambique
    "RW",  # 646 Rwanda
    "RE",  # 638 Réunion
    "SC",  # 690 Seychelles
    "SO",  # 706 Somalia
    "SS",  # 728 South Sudan
    "UG",  # 800 Uganda
    "TZ",  # 834 United Republic of Tanzania
    "ZM",  # 894 Zambia
    "ZW",  # 716 Zimbabwe
}
MIDDLE_AFRICA = {
    "AO",  # 024 Angola
    "CM",  # 120 Cameroon
    "CF",  # 140 Central African Republic
    "TD",  # 148 Chad
    "CG",  # 178 Congo
    "CD",  # 180 Democratic Republic of the Congo
    "GQ",  # 226 Equatorial Guinea
    "GA",  # 266 Gabon
    "ST",  # 678 Sao Tome and Principe
}
SOUTHERN_AFRICA = {
    "BW",  # 072 Botswana
    "SZ",  # 748 Eswatini
    "LS",  # 426 Lesotho
    "NA",  # 516 Namibia
    "ZA",  # 710 South Africa
}
WESTERN_AFRICA = {
    "BJ",  # 204 Benin
    "BF",  # 854 Burkina Faso
    "CV",  # 132 Cabo Verde
    "CI",  # 384 Côte d’Ivoire
    "GM",  # 270 Gambia
    "GH",  # 288 Ghana
    "GN",  # 324 Guinea
    "GW",  # 624 Guinea-Bissau
    "LR",  # 430 Liberia
    "ML",  # 466 Mali
    "MR",  # 478 Mauritania
    "NE",  # 562 Niger
    "NG",  # 566 Nigeria
    "SH",  # 654 Saint Helena
    "SN",  # 686 Senegal
    "SL",  # 694 Sierra Leone
    "TG",  # 768 Togo
}
SUB_SAHARAN_AFRICA = {
    *EASTERN_AFRICA,
    *MIDDLE_AFRICA,
    *SOUTHERN_AFRICA,
    *WESTERN_AFRICA,
}
AFRICA = {
    *NORTHERN_AFRICA,
    *SUB_SAHARAN_AFRICA,
}
CARIBBEAN = {
    "AI",  # 660 Anguilla
    "AG",  # 028 Antigua and Barbuda
    "AW",  # 533 Aruba
    "BS",  # 044 Bahamas
    "BB",  # 052 Barbados
    "BQ",  # 535 Bonaire, Sint Eustatius and Saba
    "VG",  # 092 British Virgin Islands
    "KY",  # 136 Cayman Islands
    "CU",  # 192 Cuba
    "CW",  # 531 Curaçao
    "DM",  # 212 Dominica
    "DO",  # 214 Dominican Republic
    "GD",  # 308 Grenada
    "GP",  # 312 Guadeloupe
    "HT",  # 332 Haiti
    "JM",  # 388 Jamaica
    "MQ",  # 474 Martinique
    "MS",  # 500 Montserrat
    "PR",  # 630 Puerto Rico
    "BL",  # 652 Saint Barthélemy
    "KN",  # 659 Saint Kitts and Nevis
    "LC",  # 662 Saint Lucia
    "MF",  # 663 Saint Martin (French Part)
    "VC",  # 670 Saint Vincent and the Grenadines
    "SX",  # 534 Sint Maarten (Dutch part)
    "TT",  # 780 Trinidad and Tobago
    "TC",  # 796 Turks and Caicos Islands
    "VI",  # 850 United States Virgin Islands
}
CENTRAL_AMERICA = {
    "BZ",  # 084 Belize
    "CR",  # 188 Costa Rica
    "SV",  # 222 El Salvador
    "GT",  # 320 Guatemala
    "HN",  # 340 Honduras
    "MX",  # 484 Mexico
    "NI",  # 558 Nicaragua
    "PA",  # 591 Panama
}
SOUTH_AMERICA = {
    "AR",  # 032 Argentina
    "BO",  # 068 Bolivia (Plurinational State of)
    "BV",  # 074 Bouvet Island
    "BR",  # 076 Brazil
    "CL",  # 152 Chile
    "CO",  # 170 Colombia
    "EC",  # 218 Ecuador
    "FK",  # 238 Falkland Islands (Malvinas)
    "GF",  # 254 French Guiana
    "GY",  # 328 Guyana
    "PY",  # 600 Paraguay
    "PE",  # 604 Peru
    "GS",  # 239 South Georgia and the South Sandwich Islands
    "SR",  # 740 Suriname
    "UY",  # 858 Uruguay
    "VE",  # 862 Venezuela (Bolivarian Republic of)
}
LATIN_AMERICA_AND_THE_CARIBBEAN = {
    *CARIBBEAN,
    *CENTRAL_AMERICA,
    *SOUTH_AMERICA,
}
NORTHERN_AMERICA = {
    "BM",  # 060 Bermuda
    "CA",  # 124 Canada
    "GL",  # 304 Greenland
    "PM",  # 666 Saint Pierre and Miquelon
    "US",  # 840 United States of America
}
NORTH_AMERICA = {
    *CARIBBEAN,
    *CENTRAL_AMERICA,
    *NORTHERN_AMERICA,
}
AMERICAS = {
    *LATIN_AMERICA_AND_THE_CARIBBEAN,
    *NORTHERN_AMERICA,
    *NORTH_AMERICA,
}
CENTRAL_ASIA = {
    "KZ",  # 398 Kazakhstan
    "KG",  # 417 Kyrgyzstan
    "TJ",  # 762 Tajikistan
    "TM",  # 795 Turkmenistan
    "UZ",  # 860 Uzbekistan
}
EASTERN_ASIA = {
    "CN",  # 156 China
    "HK",  # 344 China, Hong Kong Special Administrative Region
    "MO",  # 446 China, Macao Special Administrative Region
    "KP",  # 408 Democratic People's Republic of Korea
    "JP",  # 392 Japan
    "MN",  # 496 Mongolia
    "KR",  # 410 Republic of Korea
}
SOUTH_EASTERN_ASIA = {
    "BN",  # 096 Brunei Darussalam
    "KH",  # 116 Cambodia
    "ID",  # 360 Indonesia
    "LA",  # 418 Lao People's Democratic Republic
    "MY",  # 458 Malaysia
    "MM",  # 104 Myanmar
    "PH",  # 608 Philippines
    "SG",  # 702 Singapore
    "TH",  # 764 Thailand
    "TL",  # 626 Timor-Leste
    "VN",  # 704 Viet Nam
}
SOUTHERN_ASIA = {
    "AF",  # 004 Afghanistan
    "BD",  # 050 Bangladesh
    "BT",  # 064 Bhutan
    "IN",  # 356 India
    "IR",  # 364 Iran (Islamic Republic of)
    "MV",  # 462 Maldives
    "NP",  # 524 Nepal
    "PK",  # 586 Pakistan
    "LK",  # 144 Sri Lanka
}
WESTERN_ASIA = {
    "AM",  # 051 Armenia
    "AZ",  # 031 Azerbaijan
    "BH",  # 048 Bahrain
    "CY",  # 196 Cyprus
    "GE",  # 268 Georgia
    "IQ",  # 368 Iraq
    "IL",  # 376 Israel
    "JO",  # 400 Jordan
    "KW",  # 414 Kuwait
    "LB",  # 422 Lebanon
    "OM",  # 512 Oman
    "QA",  # 634 Qatar
    "SA",  # 682 Saudi Arabia
    "PS",  # 275 State of Palestine
    "SY",  # 760 Syrian Arab Republic
    "TR",  # 792 Turkey
    "AE",  # 784 United Arab Emirates
    "YE",  # 887 Yemen
}
ASIA = {
    *CENTRAL_ASIA,
    *EASTERN_ASIA,
    *SOUTH_EASTERN_ASIA,
    *SOUTHERN_ASIA,
    *WESTERN_ASIA,
}
EASTERN_EUROPE = {
    "BY",  # 112 Belarus
    "BG",  # 100 Bulgaria
    "CZ",  # 203 Czechia
    "HU",  # 348 Hungary
    "PL",  # 616 Poland
    "MD",  # 498 Republic of Moldova
    "RO",  # 642 Romania
    "RU",  # 643 Russian Federation
    "SK",  # 703 Slovakia
    "UA",  # 804 Ukraine
}
CHANNEL_ISLANDS = {
    "GG",  # 831 Guernsey
    "JE",  # 832 Jersey
}
NORTHERN_EUROPE = {
    *CHANNEL_ISLANDS,
    "DK",  # 208 Denmark
    "EE",  # 233 Estonia
    "FO",  # 234 Faroe Islands
    "FI",  # 246 Finland
    "IS",  # 352 Iceland
    "IE",  # 372 Ireland
    "IM",  # 833 Isle of Man
    "LV",  # 428 Latvia
    "LT",  # 440 Lithuania
    "NO",  # 578 Norway
    "SJ",  # 744 Svalbard and Jan Mayen Islands
    "SE",  # 752 Sweden
    "GB",  # 826 United Kingdom of Great Britain and Northern Ireland
    "AX",  # 248 Åland Islands
}
SOUTHERN_EUROPE = {
    "AL",  # 008 Albania
    "AD",  # 020 Andorra
    "BA",  # 070 Bosnia and Herzegovina
    "HR",  # 191 Croatia
    "GI",  # 292 Gibraltar
    "GR",  # 300 Greece
    "VA",  # 336 Holy See
    "IT",  # 380 Italy
    "MT",  # 470 Malta
    "ME",  # 499 Montenegro
    "MK",  # 807 North Macedonia
    "PT",  # 620 Portugal
    "SM",  # 674 San Marino
    "RS",  # 688 Serbia
    "SI",  # 705 Slovenia
    "ES",  # 724 Spain
}
WESTERN_EUROPE = {
    "AT",  # 040 Austria
    "BE",  # 056 Belgium
    "FR",  # 250 France
    "DE",  # 276 Germany
    "LI",  # 438 Liechtenstein
    "LU",  # 442 Luxembourg
    "MC",  # 492 Monaco
    "NL",  # 528 Netherlands
    "CH",  # 756 Switzerland
}
EUROPE = {
    *EASTERN_EUROPE,
    *NORTHERN_EUROPE,
    *SOUTHERN_EUROPE,
    *WESTERN_EUROPE,
}
AUSTRALIA_AND_NEW_ZEALAND = {
    "AU",  # 036 Australia
    "CX",  # 162 Christmas Island
    "CC",  # 166 Cocos (Keeling) Islands
    "HM",  # 334 Heard Island and McDonald Islands
    "NZ",  # 554 New Zealand
    "NF",  # 574 Norfolk Island
}
MELANESIA = {
    "FJ",  # 242 Fiji
    "NC",  # 540 New Caledonia
    "PG",  # 598 Papua New Guinea
    "SB",  # 090 Solomon Islands
    "VU",  # 548 Vanuatu
}
MICRONESIA = {
    "GU",  # 316 Guam
    "KI",  # 296 Kiribati
    "MH",  # 584 Marshall Islands
    "FM",  # 583 Micronesia (Federated States of)
    "NR",  # 520 Nauru
    "MP",  # 580 Northern Mariana Islands
    "PW",  # 585 Palau
    "UM",  # 581 United States Minor Outlying Islands
}
POLYNESIA = {
    "AS",  # 016 American Samoa
    "CK",  # 184 Cook Islands
    "PF",  # 258 French Polynesia
    "NU",  # 570 Niue
    "PN",  # 612 Pitcairn
    "WS",  # 882 Samoa
    "TK",  # 772 Tokelau
    "TO",  # 776 Tonga
    "TV",  # 798 Tuvalu
    "WF",  # 876 Wallis and Futuna Islands
}
OCEANIA = {
    *AUSTRALIA_AND_NEW_ZEALAND,
    *MELANESIA,
    *MICRONESIA,
    *POLYNESIA,
}
WORLD = {
    *AFRICA,
    *AMERICAS,
    *ASIA,
    *EUROPE,
    *OCEANIA,
    "AQ",  # 010 Antarctica
}

M49_AREAS = {
    M49_CODE_WORLD: WORLD,
    M49_CODE_AFRICA: AFRICA,
    M49_CODE_NORTH_AMERICA: NORTH_AMERICA,
    M49_CODE_SOUTH_AMERICA: SOUTH_AMERICA,
    M49_CODE_OCEANIA: OCEANIA,
    "011": WESTERN_AFRICA,
    M49_CODE_CENTRAL_AMERICA: CENTRAL_AMERICA,
    "014": EASTERN_AFRICA,
    "015": NORTHERN_AFRICA,
    "017": MIDDLE_AFRICA,
    "018": SOUTHERN_AFRICA,
    "019": AMERICAS,
    "021": NORTHERN_AMERICA,
    "029": CARIBBEAN,
    "030": EASTERN_ASIA,
    "034": SOUTHERN_ASIA,
    "035": SOUTH_EASTERN_ASIA,
    "039": SOUTHERN_EUROPE,
    "053": AUSTRALIA_AND_NEW_ZEALAND,
    "054": MELANESIA,
    "057": MICRONESIA,
    "061": POLYNESIA,
    M49_CODE_ASIA: ASIA,
    "143": CENTRAL_ASIA,
    "145": WESTERN_ASIA,
    M49_CODE_EUROPE: EUROPE,
    "151": EASTERN_EUROPE,
    "154": NORTHERN_EUROPE,
    "155": WESTERN_EUROPE,
    "202": SUB_SAHARAN_AFRICA,
    "419": LATIN_AMERICA_AND_THE_CARIBBEAN,
    "830": CHANNEL_ISLANDS,
}

M49_TO_ISO3166_ALPHA2 = {
    "004": "AF",  # Afghanistan
    "008": "AL",  # Albania
    "010": "AQ",  # Antarctica
    "012": "DZ",  # Algeria
    "016": "AS",  # American Samoa
    "020": "AD",  # Andorra
    "024": "AO",  # Angola
    "028": "AG",  # Antigua and Barbuda
    "031": "AZ",  # Azerbaijan
    "032": "AR",  # Argentina
    "036": "AU",  # Australia
    "040": "AT",  # Austria
    "044": "BS",  # Bahamas
    "048": "BH",  # Bahrain
    "050": "BD",  # Bangladesh
    "051": "AM",  # Armenia
    "052": "BB",  # Barbados
    "056": "BE",  # Belgium
    "060": "BM",  # Bermuda
    "064": "BT",  # Bhutan
    "068": "BO",  # Bolivia (Plurinational State of)
    "070": "BA",  # Bosnia and Herzegovina
    "072": "BW",  # Botswana
    "074": "BV",  # Bouvet Island
    "076": "BR",  # Brazil
    "084": "BZ",  # Belize
    "086": "IO",  # British Indian Ocean Territory
    "090": "SB",  # Solomon Islands
    "092": "VG",  # British Virgin Islands
    "096": "BN",  # Brunei Darussalam
    "100": "BG",  # Bulgaria
    "104": "MM",  # Myanmar
    "108": "BI",  # Burundi
    "112": "BY",  # Belarus
    "116": "KH",  # Cambodia
    "120": "CM",  # Cameroon
    "124": "CA",  # Canada
    "132": "CV",  # Cabo Verde
    "136": "KY",  # Cayman Islands
    "140": "CF",  # Central African Republic
    "144": "LK",  # Sri Lanka
    "148": "TD",  # Chad
    "152": "CL",  # Chile
    "156": "CN",  # China
    "162": "CX",  # Christmas Island
    "166": "CC",  # Cocos (Keeling) Islands
    "170": "CO",  # Colombia
    "174": "KM",  # Comoros
    "175": "YT",  # Mayotte
    "178": "CG",  # Congo
    "180": "CD",  # Democratic Republic of the Congo
    "184": "CK",  # Cook Islands
    "188": "CR",  # Costa Rica
    "191": "HR",  # Croatia
    "192": "CU",  # Cuba
    "196": "CY",  # Cyprus
    "203": "CZ",  # Czechia
    "204": "BJ",  # Benin
    "208": "DK",  # Denmark
    "212": "DM",  # Dominica
    "214": "DO",  # Dominican Republic
    "218": "EC",  # Ecuador
    "222": "SV",  # El Salvador
    "226": "GQ",  # Equatorial Guinea
    "231": "ET",  # Ethiopia
    "232": "ER",  # Eritrea
    "233": "EE",  # Estonia
    "234": "FO",  # Faroe Islands
    "238": "FK",  # Falkland Islands (Malvinas)
    "239": "GS",  # South Georgia and the South Sandwich Islands
    "242": "FJ",  # Fiji
    "246": "FI",  # Finland
    "248": "AX",  # Åland Islands
    "250": "FR",  # France
    "254": "GF",  # French Guiana
    "258": "PF",  # French Polynesia
    "260": "TF",  # French Southern Territories
    "262": "DJ",  # Djibouti
    "266": "GA",  # Gabon
    "268": "GE",  # Georgia
    "270": "GM",  # Gambia
    "275": "PS",  # State of Palestine
    "276": "DE",  # Germany
    "288": "GH",  # Ghana
    "292": "GI",  # Gibraltar
    "296": "KI",  # Kiribati
    "300": "GR",  # Greece
    "304": "GL",  # Greenland
    "308": "GD",  # Grenada
    "312": "GP",  # Guadeloupe
    "316": "GU",  # Guam
    "320": "GT",  # Guatemala
    "324": "GN",  # Guinea
    "328": "GY",  # Guyana
    "332": "HT",  # Haiti
    "334": "HM",  # Heard Island and McDonald Islands
    "336": "VA",  # Holy See
    "340": "HN",  # Honduras
    "344": "HK",  # China, Hong Kong Special Administrative Region
    "348": "HU",  # Hungary
    "352": "IS",  # Iceland
    "356": "IN",  # India
    "360": "ID",  # Indonesia
    "364": "IR",  # Iran (Islamic Republic of)
    "368": "IQ",  # Iraq
    "372": "IE",  # Ireland
    "376": "IL",  # Israel
    "380": "IT",  # Italy
    "384": "CI",  # Côte d’Ivoire
    "388": "JM",  # Jamaica
    "392": "JP",  # Japan
    "398": "KZ",  # Kazakhstan
    "400": "JO",  # Jordan
    "404": "KE",  # Kenya
    "408": "KP",  # Democratic People's Republic of Korea
    "410": "KR",  # Republic of Korea
    "414": "KW",  # Kuwait
    "417": "KG",  # Kyrgyzstan
    "418": "LA",  # Lao People's Democratic Republic
    "422": "LB",  # Lebanon
    "426": "LS",  # Lesotho
    "428": "LV",  # Latvia
    "430": "LR",  # Liberia
    "434": "LY",  # Libya
    "438": "LI",  # Liechtenstein
    "440": "LT",  # Lithuania
    "442": "LU",  # Luxembourg
    "446": "MO",  # China, Macao Special Administrative Region
    "450": "MG",  # Madagascar
    "454": "MW",  # Malawi
    "458": "MY",  # Malaysia
    "462": "MV",  # Maldives
    "466": "ML",  # Mali
    "470": "MT",  # Malta
    "474": "MQ",  # Martinique
    "478": "MR",  # Mauritania
    "480": "MU",  # Mauritius
    "484": "MX",  # Mexico
    "492": "MC",  # Monaco
    "496": "MN",  # Mongolia
    "498": "MD",  # Republic of Moldova
    "499": "ME",  # Montenegro
    "500": "MS",  # Montserrat
    "504": "MA",  # Morocco
    "508": "MZ",  # Mozambique
    "512": "OM",  # Oman
    "516": "NA",  # Namibia
    "520": "NR",  # Nauru
    "524": "NP",  # Nepal
    "528": "NL",  # Netherlands
    "531": "CW",  # Curaçao
    "533": "AW",  # Aruba
    "534": "SX",  # Sint Maarten (Dutch part)
    "535": "BQ",  # Bonaire, Sint Eustatius and Saba
    "540": "NC",  # New Caledonia
    "548": "VU",  # Vanuatu
    "554": "NZ",  # New Zealand
    "558": "NI",  # Nicaragua
    "562": "NE",  # Niger
    "566": "NG",  # Nigeria
    "570": "NU",  # Niue
    "574": "NF",  # Norfolk Island
    "578": "NO",  # Norway
    "580": "MP",  # Northern Mariana Islands
    "581": "UM",  # United States Minor Outlying Islands
    "583": "FM",  # Micronesia (Federated States of)
    "584": "MH",  # Marshall Islands
    "585": "PW",  # Palau
    "586": "PK",  # Pakistan
    "591": "PA",  # Panama
    "598": "PG",  # Papua New Guinea
    "600": "PY",  # Paraguay
    "604": "PE",  # Peru
    "608": "PH",  # Philippines
    "612": "PN",  # Pitcairn
    "616": "PL",  # Poland
    "620": "PT",  # Portugal
    "624": "GW",  # Guinea-Bissau
    "626": "TL",  # Timor-Leste
    "630": "PR",  # Puerto Rico
    "634": "QA",  # Qatar
    "638": "RE",  # Réunion
    "642": "RO",  # Romania
    "643": "RU",  # Russian Federation
    "646": "RW",  # Rwanda
    "652": "BL",  # Saint Barthélemy
    "654": "SH",  # Saint Helena
    "659": "KN",  # Saint Kitts and Nevis
    "660": "AI",  # Anguilla
    "662": "LC",  # Saint Lucia
    "663": "MF",  # Saint Martin (French Part)
    "666": "PM",  # Saint Pierre and Miquelon
    "670": "VC",  # Saint Vincent and the Grenadines
    "674": "SM",  # San Marino
    "678": "ST",  # Sao Tome and Principe
    "682": "SA",  # Saudi Arabia
    "686": "SN",  # Senegal
    "688": "RS",  # Serbia
    "690": "SC",  # Seychelles
    "694": "SL",  # Sierra Leone
    "702": "SG",  # Singapore
    "703": "SK",  # Slovakia
    "704": "VN",  # Viet Nam
    "705": "SI",  # Slovenia
    "706": "SO",  # Somalia
    "710": "ZA",  # South Africa
    "716": "ZW",  # Zimbabwe
    "724": "ES",  # Spain
    "728": "SS",  # South Sudan
    "729": "SD",  # Sudan
    "732": "EH",  # Western Sahara
    "740": "SR",  # Suriname
    "744": "SJ",  # Svalbard and Jan Mayen Islands
    "748": "SZ",  # Eswatini
    "752": "SE",  # Sweden
    "756": "CH",  # Switzerland
    "760": "SY",  # Syrian Arab Republic
    "762": "TJ",  # Tajikistan
    "764": "TH",  # Thailand
    "768": "TG",  # Togo
    "772": "TK",  # Tokelau
    "776": "TO",  # Tonga
    "780": "TT",  # Trinidad and Tobago
    "784": "AE",  # United Arab Emirates
    "788": "TN",  # Tunisia
    "792": "TR",  # Turkey
    "795": "TM",  # Turkmenistan
    "796": "TC",  # Turks and Caicos Islands
    "798": "TV",  # Tuvalu
    "800": "UG",  # Uganda
    "804": "UA",  # Ukraine
    "807": "MK",  # North Macedonia
    "818": "EG",  # Egypt
    "826": "GB",  # United Kingdom of Great Britain and Northern Ireland
    "831": "GG",  # Guernsey
    "832": "JE",  # Jersey
    "833": "IM",  # Isle of Man
    "834": "TZ",  # United Republic of Tanzania
    "840": "US",  # United States of America
    "850": "VI",  # United States Virgin Islands
    "854": "BF",  # Burkina Faso
    "858": "UY",  # Uruguay
    "860": "UZ",  # Uzbekistan
    "862": "VE",  # Venezuela (Bolivarian Republic of)
    "876": "WF",  # Wallis and Futuna Islands
    "882": "WS",  # Samoa
    "887": "YE",  # Yemen
    "894": "ZM",  # Zambia
}


def is_m49_code(to_check: str) -> bool:
    """
    :param to_check: any string
    :return: `True` if passed string is M49 code, `False` otherwise
    """
    return to_check in M49_AREAS or to_check in M49_TO_ISO3166_ALPHA2
