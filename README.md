[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/yYjnxW8g)
# Domácí úkol č. 5

> **Upravujte pouze soubor `assignment_5_1.py` a v něm pouze nahraďte `...` podle zadání!**

### Problém optimálního vrácení mincí
Mějme peněžní částku `money`, kterou musíme vrátit zákazníkovi. Dále mějme sadu mincí o různé nominální hodnotě, 
ze kterých můžeme částku `money` poskládat. Program vrátí zákazníkovi částku tak, aby k tomu využil co 
nejmenší počet mincí. Program bude splňovat následující požadavky:

* Peněžní částka (proměnná `money`) bude získána pomocí uživatelského vstupu (to je již předprogramováno)
  a program ověří, že vstupem je přirozené číslo. Pokud vstupem nebude přirozené číslo, 
  program vypíše chybovou hlášku a proměnnou `returned_coins` nastaví na prázdný seznam.
  > Pozn.: V rámci předprogramovaného souboru můžete otestovat pouze odpověď na záporné celé (a tedy ne přirozené) číslo.
  Nemůžete otestovat ověření, pokud by uživatel zadal text nebo desetinné číslo, protože program nepřijme jiný vstup než
  `integer`. Přesto ověřujte, že vstup zadaný uživatelem je typu `integer`.)
* Seznam dostupných mincí (proměnná `denominations`) se může měnit a vy dopředu nevíte, jaké mince budou k dispozici. 
* Mince jsou k dispozici v neomezeném množství.
* Program vytvoří proměnnou `returned_coins` typu `list`, která bude obsahovat vrácené mince seřazené sestupně.

__Nápověda:__ Pro řešení problému existuje celá řada algoritmů. Intuitivně lze snadno přijít na implementačně jednoduché
řešení pomocí hladového (Greedy) algoritmu, které by šlo popsat následujícím postupem (klidně však zvolte vlastní 
řešení):

1. Vezmi minci s nejvyšší nominální hodnotou.
2. Vracej minci tak dlouho, dokud jejich součet nepřekročí celkovou částku `money`.
3. Přesuň se na minci s nižší nominální hodnotou.
4. Opakuj krok 2 a 3, dokud nebude vrácena celá částka.

Tento postup nebude fungovat vždy optimálně. Uvažujme, že by celková vracená částka byla `13` a dostupné mince by byly
`[1, 5, 8, 9]`. Výše zmíněný hladový algoritmus vrátí nejprve minci o hodnotě `9`, ke vrácení zbyde hodnota `4`. 
Program tedy vrátí čtyřikrát minci o hodnotě `1`. Celkem tedy vrátí pět mincí. Optimální vrácení by ale byly dvě mince s 
hodnotami `5` a `8`. Z tohoto důvodu se optimální vracení mincí bude ověřovat jenom, pokud budou dostupné mince 
`[1, 2, 5, 10, 20, 50]`, v tomto případě funguje výše uvedený hladový algoritmus bezchybně. U jiného seznamu dostupných
mincí musí program vrátit správně, ale nemusí vracet co nejméně mincí.

Pro řešení se může hodit příkaz na seřazení čísel v seznamu dle velikosti:
```python
denominations.sort()  # serazeni cisel v seznamu denominations vzestupne
denominations.sort(reverse=True)  # serazeni cisel v seznamu denominations sestupne
```
