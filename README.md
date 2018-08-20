# generate_1vs1_test pair
从gallery probe循环，前3000对为正样对，后3000对负样对，负样对选择是：从probe选取一张，循环计算与gallery的相似度，找到不是同一个人且相似度最大的图片做成
一对
