from elements.base import Element

element1 = Element(1)
element1.addElements([
    (0, 0), (0, 1),
            (1, 1),
            (2, 1),
            (3, 1)
])

element2 = Element(2)
element2.addElements([
    (0, 0), (0, 1), (0, 2),
                    (1, 2),
                    (2, 2)
])

element3 = Element(3)
element3.addElements([
    (0, 0),
    (1, 0), (1, 1),
    (2, 0),
    (3, 0)
])

element4 = Element(4)
element4.addElements([
            (0, 1),
            (1, 1), (1, 2),
    (2, 0), (2, 1)
])

element5 = Element(5)
element5.addElements([
    (0, 0), (0, 1),
    (1, 0), (1, 1),
    (2, 0)
])

element6 = Element(6)
element6.addElements([
    (0, 0),        (0, 2), 
    (1, 0), (1,1), (1, 2)
])

element7 = Element(7)
element7.addElements([
    (0, 0),
    (1, 0), (1, 1),
    (2, 0),
    (3, 0)
])

element8 = Element(8)
element8.addElements([
    (0, 0),
    (1, 0), (1, 1),
            (2, 1), 
            (3, 1)
])

element9 = Element(9)
element9.addElements([
    (0, 0), 
    (1, 0),(1, 1),
    (2, 0),
])

element10 = Element(10)
element10.addElements([
    (0, 0), 
    (1, 0), (1, 1),
            (2, 1), (2, 2)
])

element11 = Element(11)
element11.addElements([
            (0, 1),
    (1, 0), (1, 1),
    (2, 0),
])

element12 = Element(12)
element12.addElements([
    (0, 1),
    (1, 0), (1, 1),
])

element13 = Element(13)
element13.addElements([
    (0, 0),(1, 1), 
    (1, 0),
    (2, 0),
])

allElements = [
    element1,
    element2,
    element3,
    element4,
    element5,
    element6,
    element7,
    element8,
    element9,
    element10,
    element11,
    element12,
    element13
]
