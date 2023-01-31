# --- EMISSION TYPES ---
VALID_VALUE_SELECTIONS: list[str] = [
    "Coal", "Oil", "Gas", "Cement", "Flaring", "Other",
    "Per Capita", "Total"
]

# --- AMERICAS ---

CARIBBEAN: list[str] = [
    "Anguilla", "Antigua and Barbuda", "Aruba", "Bahamas",
    "Barbados", "Bermuda", "British Virgin Islands",
    "Cuba", "Curaçao", "Dominica", "Dominican Republic",
    "Grenada", "Guadeloupe", "Haiti", "Jamaica", "Martinique",
    "Montserrat", "Puerto Rico", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent and the Grenadines",
    "Trinidad and Tobago"
]

CENTRAL_AMERICA: list[str] = [
    "Belize", "Costa Rica", "El Salvador", "Guatemala",
    "Honduras", "Nicaragua", "Panama"
]

SOUTH_AMERICA: list[str] = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia",
    "Ecuador", "French Guiana", "Guyana", "Paraguay", "Peru",
    "Suriname", "Uruguay", "Venezuela"
]

# --- EUROPE ---

NORTHERN_EUROPE: list[str] = [
    "Denmark", "Estonia", "Finland", "Greenland",
    "Iceland", "Ireland", "Latvia", "Lithuania",
    "Norway", "Sweden", "United Kingdom"
]

WESTERN_EUROPE: list[str] = [
    "Austria", "Belgium", "France", "Germany",
    "Liechtenstein", "Luxembourg", "Netherlands",
    "Switzerland"
]

EASTERN_EUROPE: list[str] = [
    "Belarus", "Bulgaria", "Hungary", "Moldova",
    "Poland", "Romania", "Russia", "Slovakia",
    "Ukraine"
]

SOUTHERN_EUROPE: list[str] = [
    "Albania", "Andorra", "Bosnia and Herzegovina",
    "Croatia", "Cyprus", "Greece", "Italy", "Kosovo",
    "North Macedonia", "Malta", "Monaco", "Montenegro",
    "Portugal", "Serbia", "Slovenia", "Spain", "Turkey"
]

# --- ASIA ---

WESTERN_ASIA: list[str] = [
    "Armenia", "Azerbaijan", "Bahrain", "Cyprus",
    "Georgia", "Iran", "Iraq", "Israel", "Jordan",
    'Kuwait', "Lebanon", "Oman", "Qatar", "Saudi Arabia",
    "Syria", "Turkey", "United Arab Emirates", "Yemen"
]

CENTRAL_ASIA: list[str] = [
    "Afghanistan", "Kazakhstan", "Kyrgyzstan",
    "Tajikistan", "Turkmenistan", "Uzbekistan"
]

EAST_ASIA: list[str] = [
    "China", "Japan", "North Korea", "South Korea",
    "Mongolia", "Taiwan"
]

SOUTH_ASIA: list[str] = [
    "Bangladesh", "Bhutan", "India", "Maldives",
    "Nepal", "Pakistan", "Sri Lanka"
]

SOUTHEAST_ASIA: list[str] = [
    "Brunei Darussalam", "Cambodia", "Indonesia",
    "Malaysia", "Myanmar", "Philippines", "Singapore",
    "Thailand"
]

# --- AFRICA ---

NORTH_AFRICA: list[str] = [
    "Algeria", "Egypt", "Libya", "Morocco", "Sudan",
    "Tunisia"
]

WESTERN_AFRICA: list[str] = [
    "Benin", "Burkina Faso", "Cape Verde", "Côte d'Ivoire",
    "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Liberia",
    "Mali", "Mauritania", "Niger", "Nigeria",
    "Saint Helena", "Senegal", "Sierra Leone", "Togo"
]

CENTRAL_AFRICA: list[str] = [
    "Angola", "Cameroon", "Central African Republic", "Chad",
    "Congo", "Equatorial Guinea", "Gabon", "Sao Tome and Principe"
]

EAST_AFRICA: list[str] = [
    "Burundi", "Comoros", "Djibouti", "Eritrea",
    "Ethiopia", "Kenya", "Madagascar", "Malawi",
    "Mauritius", "Mozambique", "Réunion", "Rwanda",
    "Seychelles", "Somalia", "South Sudan", "Tanzania",
    "Uganda", "Zambia", "Zimbabwe"
]

SOUTHERN_AFRICA: list[str] = [
    "Botswana", "Lesotho", "Namibia", "South Africa",
    "Swaziland"
]

# --- STREAMLIT SLIDER ---
YEAR_DOUBLE_SELECT_SLIDER_DEFAULT = (1850, 2021)
