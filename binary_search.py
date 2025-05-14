[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] 
#dizisinin Binary-Search-Tree aşamalarını yazınız.

#Örnek: root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.

1. Root 7'dir.
2. 5, 7'nin soluna eklenir.
3. 1, 5'in soluna eklenir.
4. 8, 7'nin sağına eklenir.
5. 3, 1'in sağına eklenir.
6. 6, 5'in sağına eklenir.
7. 0, 1'in soluna eklenir.
8. 9, 8'in sağına eklenir.
9. 4, 3'ün sağına eklenir.
10. 2, 3'ün soluna eklenir.

Ağaç Yapısı:
               7
             /   \
           5       8
         /   \       \
       1      6       9
      / \
     0   3
        / \
       2   4

Açıklama:
- Root 7'dir.
- 7'nin solunda 5 bulunur.
  - 5'in solunda 1 bulunur.
    - 1'in solunda 0 bulunur.
    - 1'in sağında 3 bulunur.
      - 3'ün solunda 2 bulunur.
      - 3'ün sağında 4 bulunur.
  - 5'in sağında 6 bulunur.
- 7'nin sağında 8 bulunur.
  - 8'in sağında 9 bulunur.