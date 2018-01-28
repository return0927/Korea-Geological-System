import shapefile

fpath = "Resources/Daejeon/F_FAC_BUILDING_30_201801"

print("Reading file")
sh = shapefile.Reader(fpath)
print("Fetching records...")
records = sh.records()
print("Fetched all records ({})".format(len(records)))

rev = input()
for rec in records:
    if rec[19] == rev:
        print(rec)