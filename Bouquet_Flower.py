class Flower:
    def __init__(self, name, freshness, colour, stem_length, price, expiration_date):
        self.name = name
        self.freshness = freshness
        self.colour = colour
        self.stem_length = stem_length
        self.price = price
        self.expiration_date = expiration_date


class FlowerBouquet:
    def __init__(self, bouquet=None):
        if bouquet is None:
            bouquet = []
        self.bouquet = bouquet

    def bouquet_price(self):
        p = Narcissist.price + Tulip.price + Orchid.price + Pion.price + Lily.price
        return f"The price of bouquet {p} $"

    def bouquet_term_life(self):
        l = (Narcissist.expiration_date + Tulip.expiration_date + \
             Orchid.expiration_date + Pion.expiration_date + Lily.expiration_date) / 5
        return f"The lifetime of the bouquet {l} days"

    def freshness_sort(self):
        fs = [(Narcissist.freshness, "days, Narcissist"),
              (Tulip.freshness, "days, Tulip"),
              (Orchid.freshness, "days, Orchid"),
              (Pion.freshness, "days, Pion"),
              (Lily.freshness, "days, Lily")
              ]
        fs.sort()
        return f"Sorting the bouquet by freshness {fs}"

    def colour_sort(self):
        cs = [Narcissist.colour, Tulip.colour, Orchid.colour, Pion.colour, Lily.colour]
        sorted_cs = sorted(cs)
        return f"Sorting flowers in a bouquet by color alphabetically {sorted_cs}"

    def stem_length_sort(self):
        sl = [(Narcissist.stem_length, "cm, Narcissist"),
              (Tulip.stem_length, "cm, Tulip"),
              (Orchid.stem_length, "cm, Orchid"),
              (Pion.stem_length, "cm, Pion"),
              (Lily.stem_length, "cm, Lily")
              ]
        sl.sort()
        return f"Sorting flowers in a bouquet by stem length {sl}"

    def price_sort(self):
        ps = [Narcissist.price, Tulip.price, Orchid.price, Pion.price, Lily.price]
        ps.sort()
        return f"Sorting flowers in a bouquet by price (cheap->expensive) {ps} $"

    def flower_in_bouquet(self):
        flower_list = "Narcissist", "Tulip", "Orchid", "Pion", "Lily"
        flower_1 = "Narcissist"
        flower_2 = "Tulip"
        flower_3 = "Orchid"
        flower_4 = "Pion"
        flower_5 = "Lily"

        if flower_1 in self.bouquet:
            print("The flower bouquet has", flower_1)
        if flower_2 in flower_list:
            print("The flower bouquet has", flower_2)
        if flower_3 in flower_list:
            print("The flower bouquet has", flower_3)
        if flower_4 in flower_list:
            print("The flower bouquet has", flower_4)
        if flower_5 in flower_list:
            print("The flower bouquet has", flower_5)
        else:
            print("The flower bouquet has not")


Narcissist = Flower("Narcissist", 2, "orange", 20, 8, 5)
Tulip = Flower("Tulip", 3, "yellow", 20, 5, 6)
Orchid = Flower("Orchid", 4, "white", 100, 15, 4)
Pion = Flower("Pion", 2, "pink", 50, 10, 3)
Lily = Flower("Lily", 1, "white", 25, 18, 2)

B = FlowerBouquet()
print(B.bouquet_price())  # output price for all bouquet
print(B.bouquet_term_life())  # output the time when bouquet will die
print()
print(B.freshness_sort())  # sort flowers in bouquet by freshness
print(B.colour_sort())  # sort flowers in bouquet by colour alphabetically
print(B.stem_length_sort())  # sort flowers in bouquet by stem length
print(B.price_sort())  # sort flowers in bouquet by price (cheap->expensive)
print()
print(Narcissist.price, "$")  # output flowers for their parameters
print(Pion.colour)
print(Orchid.stem_length, "cm")
print(Pion.freshness, "days")
print(Lily.expiration_date, "days")
print()
print(B.flower_in_bouquet())  # output what flowers has the bouquet
