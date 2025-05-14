#[22,27,16,2,18,6] -> Insertion Sort

#Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

[22, 27, 16, 2, 18, 6]

27 zaten yerinde → [22, 27, 16, 2, 18, 6]

16, 27’den küçük → 27 kaydırılır, 16, 22’den küçük → 22 kaydırılır → [16, 22, 27, 2, 18, 6]

2, 27-22-16’dan küçük → tamamı sağa kaydırılır → [2, 16, 22, 27, 18, 6]

18, 27’den küçük → 27 kaydırılır, 18, 22’den küçük → 22 kaydırılır → [2, 16, 18, 22, 27, 6]

6, 27-22-18-16’den küçük → hepsi sağa kaydırılır → [2, 6, 16, 18, 22, 27]

#Big-O gösterimini yazınız.

#Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız

#Average case: Aradığımız sayının ortada olması
#Worst case: Aradığımız sayının sonda olması
#Best case: Aradığımız sayının dizinin en başında olması.

Best Case: O(n) → Dizi zaten sıralıysa

Average Case: O(n²)

Worst Case: O(n²) → Dizi ters sıralıysa
Bu dizide: Ortalama karmaşıklıkta işlemler uygulanıyor.
 Big-O: O(n²)
.
Sıralanmış dizi: [2, 6, 16, 18, 22, 27]
18 → tam ortada bulunuyor.
 Cevap: Average Case



#[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.

Selection Sort İlk 4 Adım:

[2, 3, 5, 8, 7, 9, 4, 15, 6]

[2, 3, 5, 8, 7, 9, 4, 15, 6]

[2, 3, 4, 8, 7, 9, 5, 15, 6]

[2, 3, 4, 5, 7, 9, 8, 15, 6]