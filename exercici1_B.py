import json
#Declarem la funcio amb una variable datas que conte la informació de 4 llibres
def imprimir():
    datas = {"book":
            [{"title":"Tirant lo blanc",
            "cover":"Si",
            "year":"1932",
            "pages":"354"
            },

            {"title":"L'ocell de foc",
                "cover":"Si",
                "year":"1932",
                "pages":"354"
            },

            {"title":"La plaça del diamant",
                "cover":"Si",
                "year":"1932",
                "pages":"354"
            },
            
            {"title":"Terra baixa",
                "cover":"Si",
                "year":"1932",
                "pages":"354"
            }]
        }

    #Obrim example.json si existeix i sino el creem i li escribim datas
    with open("exemple.json", 'w') as llibres:
        json.dump(datas, llibres)

    #Printejem datas amb un indent 2 perque es pugui veure bé i no en una linia
    print(json.dumps(datas, indent=2))

#Obrim exemple i el copiem i el fem print
def copiar():
    with open("exemple.json", 'r') as llibres:
        result = json.load(llibres)
        print(json.dumps(result,indent=2))
