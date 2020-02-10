# In jupyter/datascience-notebook add
# conda install zarr
# conda install holoviews
# conda install hdatashader
# conda install datashader
# pip install git+https://github.com/MITgcm/xmitgcm.git ( tested with commit 876786c413488f6be0cb0b479064a9cd2f68b6b5 )

import xmitgcm.llcreader as llcreader
import numpy as np
import matplotlib.pyplot as plt

model = llcreader.ECCOPortalLLC4320Model()
ds_sst = model.get_dataset(varnames=['Theta'], k_levels=[0], type='latlon')
th=ds_sst.Theta.isel(k=0).astype('f4')
tv=th[720:744,9000:11000,500:1800].  # Get Gulf of Cadiz for 24 1 hour snapshots
phi=tv.values

plt.figure(figsize=(30,40))
# plt.imshow(phi[4900:5300,500:1000],origin='lower',cmap='jet',interpolation='spline16',vmin=14,vmax=17)
cm='jet'
cm='gist_ncar'
# cm='prism'
cmap = plt.cm.get_cmap(cm)
cmap.set_bad(color='grey')
plt.imshow(phi[1,:,:],origin='lower',cmap=cmap,vmin=17,vmax=23)
plt.colorbar()
plt.show()
