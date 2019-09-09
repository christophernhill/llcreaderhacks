from xmitgcm import llcreader
model = llcreader.ECCOPortalLLC4320Model()
ds1 = model.get_dataset(varnames=['Eta'])
phi=ds1.Eta[1,1,1:4320,1:4320]
phi.to_netcdf('foo.nc')
