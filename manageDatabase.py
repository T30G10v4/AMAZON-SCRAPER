import database

link = "https://www.amazon.it/gp/product/B074G5Z1PQ?pf_rd_r=1AG96W2A91G4K4NW0QRZ&pf_rd_p=33a234b0-b2e1-4fd7-9ea3-f5dca6c7be9c&pd_rd_r=2fafba21-4626-4fee-a7f2-89e26b4a23a7&pd_rd_w=9iatx&pd_rd_wg=Nj6hQ&ref_=pd_gw_unk"

database.writeOnDatabase(link, database.getTitleAmazon(link), database.getPriceAmazonFloat(link))

input()