# import class from module

# from Indonesian_Address_Parser import Indonesian_Address_Parser
from Indonesian_Address_Parser import Indonesian_Address_Parser

indonesianParser = Indonesian_Address_Parser()

result = indonesianParser.getKodePos({"urban": "Srijaya"})
if result:
    for res in result:
        print(res)
        print()


