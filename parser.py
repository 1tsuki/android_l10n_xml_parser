import csv
import xml.etree.ElementTree as ET


class L10nParser:
    def __init__(self, path):
        self.path = path
        tree = ET.parse(self.path)
        self.root = tree.getroot()

    def parse(self):
        words = {}
        for child in self.root:
            words[child.attrib['name']] = child.text
        return words


dict_en = L10nParser('./input/en.xml').parse()
dict_ja = L10nParser('./input/ja.xml').parse()
dict_th = L10nParser('./input/th.xml').parse()
dict_zhrCN = L10nParser('./input/zh-rCN.xml').parse()
dict_zhrTW = L10nParser('./input/zh-rTW.xml').parse()

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    for key in dict_en:
        en = dict_en[key] if key in dict_en else ''
        ja = dict_ja[key] if key in dict_ja else ''
        th = dict_th[key] if key in dict_th else ''
        zhrTW = dict_zhrTW[key] if key in dict_zhrTW else ''
        zhrCN = dict_zhrCN[key] if key in dict_zhrCN else ''
        writer.writerow([key, ja, en, th, zhrCN, zhrTW])
