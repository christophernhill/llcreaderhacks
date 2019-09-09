from xmitgcm import llcreader
model = llcreader.ECCOPortalLLC4320Model()
ds1 = model.get_dataset(varnames=['Eta'])
tsLo=1
tsHi=1
fLo=1
fHi=1
jLo=1
jHi=1
iLo=1
iHi=4320
phi=ds1.Eta[tsLo:tsHi,fLo:fHi,jLo:jHi,iLo:iHi]
phi.to_netcdf('eta.nc')
