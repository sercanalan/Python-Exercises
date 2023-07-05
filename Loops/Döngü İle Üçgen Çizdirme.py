"""
Örneğin üçgen limiti 6 ise;

   Triangle 1:                Triangle 2:              Triangle 3:                   Triangle 4: 
    x       (1*)             xxxxxx  (6*)             xxxxxxxxxxx  (11*)                  x       (5 space, 1* , 5 space)  

    xx      (2*)             xxxxx   (5*)             xxxxxxxxx    (9*)                  xxx      (4 space, 3* , 4 space)

    xxx     (3*)             xxxx    (4*)             xxxxxxx      (7*)                 xxxxx     (3 space, 5* , 3 space)

    xxxx    (4*)             xxx     (3*)             xxxxx        (5*)                xxxxxxx    (2 space, 7* , 2 space)

    xxxxx   (5*)             xx      (2*)             xxx          (3*)               xxxxxxxxx   (1 space, 9* , 1 space)

    xxxxxx  (6*)             x       (1*)             x            (1*)              xxxxxxxxxxx  (0 space, 11* , 0 space)    
"""

limit = int(input("Üçgen Limiti: "))

# --- Triangle 1 ---
print("\n--- Triangle 1 ---")
for i in range(1,limit+1):
    print(i * "*")

# --- Triangle 2 ---
print("\n--- Triangle 2 ---")
for i in range(1,limit+1):
    print((limit+1-i) *  "*")

# --- Triangle 3 ---
print("\n--- Triangle 3 ---")
for i in range(limit,0,-1):
    print((2*i-1) * "*")

# --- Triangle 4 ---
print("\n--- Triangle 4 ---")
for i in range(1,limit+1):
    print((limit-i) * " " + (2*i-1) * "*" + (limit-i) * " ")