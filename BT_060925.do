* BÀI TẬP
* Tỷ lệ người dân trong độ tuổi từ 50-60 bị bệnh nặng trong 12 tháng qua

* Tỷ lệ người dân trong độ tuổi từ 50-60 bị bệnh nặng trong 12 tháng qua phân theo giới

* Tỷ lệ người dân ở ĐBSCL trong độ tuổi từ 50-60 bị bệnh nặng trong 12 tháng qua
	
* Ước lượng mô hình logit để xem xét ảnh hưởng của tuổi, giới, dân tộc (Kinh/Hoa-1), học vấn bị bệnh nặng trong 12 tháng qua	
	
*********************************************************
*********************************************************

use "D:\Thanh Vy\CT7- PYTHON\VHLSS 2020v2\VHLSS 2020\MUC3A.dta", clear
count
tab m3c1a
des tinh huyen xa diaban hoso m3ma
gen matv = m3ma
move matv m3ma
sort tinh huyen xa diaban hoso matv
save "D:\Thanh Vy\CT7- PYTHON\THỰC HÀNH VHLSS\muc3a.dta",  replace

*  Nối file muc3a.dta vời file muc1_2v.dta
use "D:\Thanh Vy\CT7- PYTHON\THỰC HÀNH VHLSS\muc1_2v.dta", clear
sort tinh huyen xa diaban hoso matv

merge 1:1 tinh huyen xa diaban hoso matv using "D:\Thanh Vy\CT7- PYTHON\THỰC HÀNH VHLSS\muc3a.dta"

tab _merge
tab _merge, nol

keep if _merge==3
drop _merge 

save "D:\Thanh Vy\CT7- PYTHON\THỰC HÀNH VHLSS\muc1_muc2v_muc3a.dta", replace

************* TRẢ LỜI CÂU HỎI *************

*1 Tỷ lệ người dân trong độ tuổi từ 50-60 bị bệnh nặng trong 12 tháng qua

tab m3c1a if m1ac5 >= 50 & m1ac5 <= 60

*2 Tỷ lệ người dân trong độ tuổi từ 50-60 bị bệnh nặng trong 12 tháng qua phân theo giới

tab m1ac2 m3c1a if m1ac5 >= 50 & m1ac5 <= 60

*3 Tỷ lệ người dân ở ĐBSCL trong độ tuổi từ 50-60 bị bệnh nặng trong 12 tháng qua
gen dbscl=0
replace dbscl=1 if tinh==80|tinh==82|tinh==83|tinh==84|tinh==86|tinh==87|tinh==89|tinh==91|tinh==94|tinh==95|tinh==96
	
tab dbscl m3c1a if m1ac5 >= 50 & m1ac5 <= 60
	
*4 Ước lượng mô hình logit để xem xét ảnh hưởng của tuổi, giới, dân tộc (Kinh/Hoa-1), học vấn bị bệnh nặng trong 12 tháng qua