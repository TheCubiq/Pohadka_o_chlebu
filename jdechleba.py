

doplnky = [ 
  #s/se
  "",
  "máslem",
  "salámem",
  "kečupem",
  #"lučinou",
  #"marmeládou",
  #"nutelou"
]

potraviny = [
  #  jde     povídá   potkají  
  ["chleba","chlebe"],                    #chleba
  ["rohlík","rohlíku"],                   #rohlík
  ["houska","housko","housku"],           #houska  
  ["veka","veko","veku"],                 #veka
  ["loupák","loupáku"],                   #loupák
  ["dalamánek","dalamánku"],              #dalamánek
  ["mazanec","mazanče"],                  #mazanec
  ["vánočka","vánočko","vánočku"],        #vánočka
  ["pletýnka","pletýnko","pletýnku"],     #pletýnka
  ["toust","touste"],                     #toust
  ["preclík","preclíku"],                 #preclík
  ["tyčinka","tyčinko","tyčinku"],        #tyčka
  ["bulka","bulko","bulku"],              #bulka
  ["brioška","brioško","briošku"],        #brioška
  ["bageta","bageto","bagetu"],           #bageta
  ["beránek","beránku","beránka"],        #beránek
  ["buchta","buchto","buchtu"],           #buchta
  ["langoš","langoši"],                   #langoš
  ["trdelník","trdelníku"],               #trdelník
  ["kobliha","kobliho","koblihu"],        #kobliha
  ["krosant","krosante"],                 #krosant
  ["donat","donate"],                     #donat
  ["koláček","koláčku"],                  #koláček
  ["krutónek","krutónku"],                #krutónky
  ["krekr","krekře"],                     #krekry
  ["čokorolka","čokorolko","čokorolku"],  #čokorolka
  ["sušenka","sušenko","sušenku"],        #sušenky
  ["perníček","perníčku"],                #perníček
  ["očičko","očičko"],                    #očičko
  ["piškot","piškote"],                   #piškot
  ["zemlbába","zemlbábo","zemlbábu"],     #zemlbába
  ["roláda","roládo","roládu"],           #roláda
  ["drdol","drdole"],                     #drdol
  ["dukáta","dukátko","dukátku"],         #dukátky
  ["šáteček","šátečku"],                  #šáteček
  ["mafin","mafine"],                     #mafin
  ["bochánek","bochánku"],                #bochánek
  ["kaiserka","kaiserko","kaiserku"],     #keiserka
  ["vdolek","vdolku"],                    #vdolek
  ["placka","placko","placku"],           #placka
  ["cebetka","cebetko","cebetku"],        #cebetka
  ["cizrnka","cizrnko","cizrnku"],        #cizrnka
  ["raženka","raženko","raženku"],        #raženka
  ["uzel","uzle"],                        #uzel
  ["štrůdl","štrůdle"],                   #štrůdl
  ["řepánek","řepánku"],                  #řepánek
  ["bábovka","bábovko","bábovku"],        #bábovka
  ["makovec","makovče"],                  #makovec
  ["frgál","frgále"],                     #frgál
  ["hvězdička","hvězdičko","hvězdičku"],  #hvězdička
]

def se(s):
  if len(s) != 0:
    if s[:1] == "s":
        return(f"se {s}")
    else:
        return(f"s {s}")
  else:
    return("")

def potrdopl(pozice,typ):
  #potravina
  pt = ""
  d = potraviny[int(pozice/len(doplnky))]
  if (typ == 2 and len(d) != 3):
      pt = d[0]
  else:
      pt = d[typ]
  
  #doplněk
  dp = ""
  for i in range(int(pozice%(len(doplnky)))+1):
    dp = f"{dp}{se(doplnky[i])} "
  
  b = f"{pt}{dp}"
  b = b[:len(b)-1]
  return(b)

def kdovsechnojde(kolik,typ):
  sezn = ""
  for kdojde in range(kolik+1):
      c = ""
      if kdojde != kolik:
        c=", "
      sezn = sezn + (potrdopl(kdojde,typ)+c)
  return(sezn)
      
def skymjdu(kolik,jeden,vic):
  skym = ""
  if kolik == 0:
    skym = jeden
  else:
    skym = vic
  return(skym)

def bezmez(text, filename, write = False,):
  if write:
    f = open(filename, 'a', encoding='utf-8')
  for radek in text:
    if write:
      f.write(radek+" ")
    else:
      print(radek,end=' ') #'\n'

def pohadka(write = False, filename = "demofile.txt"):
  if write:
    f = open(filename, "w")
    f.write("") # vytvoří a přepíše soubor
    print("vytvořen nový soubor")
      
  for i in range(len(potraviny)*len(doplnky)-1):
    texty =[
      "jde",
      kdovsechnojde(i,0),
      f"a {skymjdu(i,'potká','potkají')}",
      potrdopl(i+1,2)+".",
      "A",
      potrdopl(i+1,0),
      "povídá:",
      kdovsechnojde(i,1),
      f"můžu jít s {skymjdu(i,'tebou','vámi')}?",
      "Přičemž",
      kdovsechnojde(i,0),
      "odpoví:",
    ]
    if i != len(potraviny)*len(doplnky)-2 :
      texty.append("jo, můžeš. Takže")
    else:
      texty.append("Ne. Čas na smích:")
    bezmez(texty,filename,write)
  

 
# poví pohádku, argumenty:
#     [(bool) zapsat do souboru] - Default : False
#     [(string) jméno souboru včetně přípony] - Default : "demofile.txt"
pohadka(True,"sampleOutput.txt")




