import xml.etree.ElementTree as ET

#Es crea una funció que retorna un arxiu XML
def ArxiuXML():

    #Creem l'arxiu element amb el root students, el qual tindra 5 childs students amb atribut i 4 subchilds.
    RootXML = ET.Element('students')

    #Creem el primer child student amb el subchild name, surname, email i dni, i el seu atribut corresponent a nacionalitat.
    ChildsXml = ET.SubElement(RootXML, 'student')
    ChildsXml.set('Nacionalitat','Argentina')
    SubChild = ET.SubElement(ChildsXml, 'name')
    SubChild.text = " Talía " 
    SubChild = ET.SubElement(ChildsXml, 'surname')
    SubChild.text = " López "
    SubChild = ET.SubElement(ChildsXml, 'email')
    SubChild.text = " talialopezarias@gmail.com "
    SubChild = ET.SubElement(ChildsXml, 'dni')
    SubChild.text = " 43591348L "

    #Creem el segon child student amb el subchild name, surname, email i dni, i el seu atribut corresponent a nacionalitat.
    ChildsXml2 = ET.SubElement(RootXML, 'student')
    ChildsXml2.set('Nacionalitat','Espanyola')
    SubChild2 = ET.SubElement(ChildsXml2, 'name')
    SubChild2.text = " Ramón "
    SubChild2 = ET.SubElement(ChildsXml2, 'surname')
    SubChild2.text = " Font "
    SubChild2 = ET.SubElement(ChildsXml2, 'email')
    SubChild2.text = " ramonfont@gmail.com "
    SubChild2 = ET.SubElement(ChildsXml2, 'dni')
    SubChild2.text = " 42597156G "

    #Creem el tercer child student amb el subchild name, surname, email i dni, i el seu atribut corresponent a nacionalitat.
    ChildsXml3 = ET.SubElement(RootXML, 'student')
    ChildsXml3.set('Nacionalitat','Espanyola')
    SubChild3 = ET.SubElement(ChildsXml3, 'name')
    SubChild3.text = " Maria "
    SubChild3 = ET.SubElement(ChildsXml3, 'surname')
    SubChild3.text = " Palomeque "
    SubChild3 = ET.SubElement(ChildsXml3, 'email')
    SubChild3.text = " mariapalomeque@gmail.com "
    SubChild3 = ET.SubElement(ChildsXml3, 'dni')
    SubChild3 = " 45789216O "

    #Creem el quart child student amb el subchild name, surname, email i dni, i el seu atribut corresponent a nacionalitat.
    ChildsXml4 = ET.SubElement(RootXML, 'student')
    ChildsXml4.set('Nacionalitat','Xina')
    SubChild4 = ET.SubElement(ChildsXml4, 'name')
    SubChild4.text = " Aleksandra "
    SubChild4 = ET.SubElement(ChildsXml4, 'surname')
    SubChild4.text = " Arias "
    SubChild4 = ET.SubElement(ChildsXml4, 'email')
    SubChild4.text = " aleksandraarias@gmail.com "
    SubChild4 = ET.SubElement(ChildsXml4, 'dni')
    SubChild4.text = " 4235783X "

    #Creem el cinque child student amb el subchild name, surname, email i dni, i el seu atribut corresponent a nacionalitat.
    ChildsXml5 = ET.SubElement(RootXML, 'student')
    ChildsXml5.set('Nacionalitat','Italiana')
    SubChild5 = ET.SubElement(ChildsXml5, 'name')
    SubChild5.text = ' Oriol '
    SubChild5 = ET.SubElement(ChildsXml5, 'surname')
    SubChild5.text = ' Garcia '
    SubChild5 = ET.SubElement(ChildsXml5, 'email')
    SubChild5.text = ' oriolgarcia@gmail.com '
    SubChild5 = ET.SubElement(ChildsXml5, 'dni')
    SubChild5.text = ' 41569715A '
    
    #Guardem el nostre fitxer amb ElementTree
    FitxerXML = ET.ElementTree(RootXML)
    #L'escribim a un arxiu xml
    FitxerXML.write("Students.xml")

    #Fem identació dels elements
    ET.indent(RootXML)
    #Mostrem per consola
    ET.dump(RootXML)

