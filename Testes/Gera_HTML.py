clientes = """ADDM
AMD
APAE
ASSESCOM
ASTRO - HYPER-V
ASTRO CIGAM
ASTRO TS
ATN - TS
ATN - VIRTUAL
AUTOGERADORA
AUTOGERADORA - CIGAM
AUTOGERADORA - HYPER-V
AÇOS LEO HYPER-V
AÇOS LEO SISTEMA
BANDEIRA CONSTRUÇÕES
BCM
BELLGLASS
BORGES
CACHOEIRINHA CONTABIL
CACHOEIRINHA CONTABIL - HYPE
CEG
CORPORATIVE ATN
DAJAVA
DAJAVA VM
DEPIZZOL
DEPIZZOL - HYPER-V
DIFFERENCIAL
DIFFERENCIAL - HYPER-V
DISTRITO ENERGY
DISTRITO ENERGY - HYPER-V
EMBAFLUX
EMBAFLUX - HYPER-V
ENDOTECH
ENDOTECH - HYPERV
ESCRITASUL HYPER-V
FAC CONTABIL
FAC CONTABIL - HYPER-V
FERCOPI
FERCOPI - HYPER-V
FFS FILMES
FIBERMEYER
FISCONTARH HYPER-V
FISCONTARH TS
HERFE
HERFE HYPER-V
HESCH
HIDRABRASIL
JAS
JOG ANDAIMES
JOG ANDAIMES - HYPER-V
KONIG & HERZOG
LANES
LANES HYPER-V
MABY BALANCAS
MABY BI
MABY HYPER-V
MABY SRVDADOS
MAD.BORGES RONDON
METALRING - HYPER-V
METALRING - TS
METALRING DADOS
MKSINTER
MKSINTER HYPER-V
PNSV
POMIER
POMIER - HYPER-V
PREVINE
PREVINE HYPER-V
PROCONTABIL
PROCONTABIL PROSOFT
R2 ENGENHARIA
RAUPP
RAUPP HYPER-V
RAUTER
RAUTER -  REPLICA
RAUTER -  VM
SG CORTE&DOBRA
SHOPPING DO VALE
SHOPPING DO VALE - HYPER-V
SUCADV
SUCADV - HYPER-V
SUL ANDAIMES
SULCARGO
SULFER
SULFER VM
TECENGE
TECENGE HYPER-V
TOJOQUIM
URANO
VANCOSTY
VANCOSTY - HYPER-V
VIDROBOX
VIDROBOX - HYPER-V
VITARIM
YUDEVAN
YUDEVAN HYPER-V"""

lista = clientes.split('\n')
print(lista)
listanova = []
for c in range(0, 71):
    if lista[c].find("HYPER-V") == -1:
        listanova.append(lista[c])
print(listanova)

for item in listanova:
    print(f'<option value="{item}">{item}</option>')
