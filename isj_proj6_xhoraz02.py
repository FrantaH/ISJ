#!/usr/bin/env python3



class Polynomial:
    """zavolá se po inicializaci.
    může přijmout buďto jakýkoli počet integerů, nebo list integerů nebo zadané argumenty pomocí x0 kde 0 je libovolné číslo reprezentující mocninu
    nelze kombinovat
    """
    def __init__(self,*x,**xs):
        self.poly = list()
        if len(x) != 0 and len(xs) != 0:
            print("error")
        elif len(xs) == 0 and len(x) == 1 and type(x[0]) is list:
            self.poly = x[0]
        elif len(xs) == 0:
            for val in x:
                if isinstance(val, int):
                    self.poly.append(val)
                else:
                    print("wrong arguments!")
                    exit(1)
        elif len(x) == 0 and len(xs) != 0:
            my_keys = list(xs.keys())
            leng = 0
            for item in my_keys:
                if item[0] != "x":
                    print("wrong keywords!")
                    exit(1)
                item = item[1:]
                try:
                    item = int(item)
                except:
                    print("wrong keywords!")
                    exit(1)
                if item > leng:
                    leng = item
                    
            self.poly = [0] * (leng+1)
            
            for key, value in xs.items():
                self.poly[int(key[1:])] = value
        else:
            print("can combine args and kwargs!")
            exit(1)
            
        while len(self.poly)>1 and self.poly[-1] == 0:
            del self.poly[-1]

    """funkce pro převod na string
    pokud index obsahuje 0 nevypíše tento index (výjimkou je list, který obsahuje jednu položku = 0
    pokud index obsahuje 1 nevypíše 1 ale pouze x
    pokud index obsahuje jiná čísla N, vypíše je ho jako "O Nx^index "
    kde O je buďto + nebo - (výjimka je nejvyšší řád, kde se vypíše pouze pokud je N záporné"""
    def __str__(self):
        tmplist = list(self.poly)
        if len(tmplist) == 1:
            return str(self.poly[0])
            
        for index, item in enumerate(tmplist):
            if item == 0:
                tmplist[index] = ""
            else:
                if index == 0:
                    if item < 0:
                        tmplist[index] = "- " + str(item)[1:]
                    elif item > 0:
                        tmplist[index] = "+ " + str(item)

                elif index == 1:
                    if item < 0:
                        if item == -1:
                            item = ""
                        tmplist[index] = "- " + str(item)[1:] + "x"
                    elif item > 0:
                        if item == 1:
                            item = ""
                        tmplist[index] = "+ " + str(item) + "x"

                else:
                    if item < 0:
                        if item == -1:
                            item = ""
                        tmplist[index] = "- " + str(item)[1:] + "x^" + str(index)
                    elif item > 0:
                        if item == 1:
                            item = ""
                        tmplist[index] = "+ " + str(item) + "x^" + str(index)

        tmplist = tmplist[::-1]

        if tmplist[0][0] == "+":
            tmplist[0] = tmplist[0][2:]
        
        tmplist = filter(lambda a: a != "", tmplist)
        return ' '.join(tmplist)
    """porovná 2 polynomy (jejich interní listy)"""
    def __eq__(self, other):
            return self.poly == other.poly

    """sečte 2 polynomy (jejich interní listy prodlouží na stejnou velikost a pak sečte"""
    def __add__(self, other):
        if len(self.poly) < len(other.poly):
            helplist = self.poly
            helplist = helplist + [0]*(len(other.poly) - len(self.poly))
            return Polynomial(list(map(lambda x,y:x+y,helplist,other.poly)))

        else:
            helplist = other.poly
            helplist = helplist + [0]*(len(self.poly) - len(other.poly))
            return Polynomial(list(map(lambda x,y:x+y,self.poly,helplist)))

    """umocní polynom zadaným argumentem power"""
    def __pow__(self, power):
        if power == 1:
            return Polynomial(self.poly)
        elif power == 0:
            return Polynomial(1)
        else:
            result_new = self.poly + [0] * (len(self.poly)-1)
            
            while power > 1:
                result_old = result_new
                result_new = [0] * (len(self.poly)+len(result_new))
                    
                for inda,a in enumerate(self.poly):
                    for indb, b in enumerate(result_old):
                        result_new[indb+inda] = result_new[indb+inda] + (a*b)

                power -= 1

            return Polynomial(result_new)

    """derivuje polynom (odřízne první index a posléze každou hodnotu sečte s jejím indexem)"""
    def derivative(self):
        if len(self.poly)==1:
            return Polynomial(0)
        return Polynomial([(item*(index+1)) for index, item in enumerate(self.poly[1:])])

    """dosadí do polynomu číslo tak, že index se vynásobí tímto číslem a dohromady se tyto prvky sečtou,
    pokud jsou zadané 2 parametry, tak se první odečítá a druhý přičítá (v rámci zadání to takto bylo, logičtější pro mě by bylo první přičítá druhý odečítá, pak by odpadla nutnost "swapowat" argumenty"""
    def at_value(self,val1,val2 = None):
        if val2 != None:
            val1, val2 = val2, val1
        result = 0
        for index, item in enumerate(self.poly):
            result = result + (item*(val1**index))
            if val2 != None:
                result = result - (item*(val2**index))
        return result


"""Do souboru, nazvaného podle konvence isj_proj6_xnovak00.py, implementujte třídu Polynomial, která bude pracovat s polynomy reprezentovanými pomocí seznamů. Například 2x^3 - 3x + 1 
bude  reprezentováno jako [1,-3,0,2] (seznam začíná nejnižším řádem, i když se polynomy většinou zapisují opačně).

Instance třídy bude možné vytvářet několika různými způsoby:
pol1 = Polynomial([1,-3,0,2])
pol2 = Polynomial(1,-3,0,2)
pol3 = Polynomial(x0=1,x3=2,x1=-3)

Volání funkce print() vypíše polynom v obvyklém formátu:
>>> print(pol2)
2x^3 - 3x + 1

Bude možné porovnávat vektory porovnávat:
>>> pol1 == pol2
True

Polynomy bude možné sčítat a umocňovat nezápornými celými čísly:
>>> print(Polynomial(1,-3,0,2) + Polynomial(0, 2, 1))
2x^3 + x^2 - x + 1
>>> print(Polynomial(-1, 1) ** 2)
x^2 - 2x  + 1

A budou fungovat metody derivative() - derivace a at_value() - hodnota polynomu pro zadané x - obě pouze vrací výsledek, nemění samotný polynom:
>>> print(pol1.derivative())
6x^2 - 3
>>> print(pol1.at_value(2))
11
>>> print(pol1.at_value(2,3))
35
(pokud jsou zadány 2 hodnoty, je výsledkem rozdíl mezi hodnotou at_value() druhého a prvního parametru - může sloužit pro výpočet určitého integrálu, ale ten nemá být implementován)

Maximální hodnocení bude vyžadovat, abyste:
- uvedli "shebang" jako v předchozích projektech
- důsledně používali dokumentační řetězce a komentovali kód
- nevypisovali žádné ladicí/testovací informace při běžném "import isj_proj05_xnovak00" 


- zajistili, že následující platí:"""
def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()