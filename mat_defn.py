from pyne.material import Material, from_atom_frac

hea1 = from_atom_frac({'ta':1,'ti':1,'v':1,'zr':1}, density=7.2)
hea2 = from_atom_frac({'nb':1,'ti':1,'v':1,'zr':1}, density=6.5)
hea3 = from_atom_frac({'nb':1,'ta':1,'ti':1,'v':1,'zr':1}, density=6.9)
hea4 = from_atom_frac({'cr':0.66,'fe':1,'mn':1,'ni':1}, density=7.2)

print(hea1.expand_elements().mcnp())
print(hea2.expand_elements().mcnp())
print(hea3.expand_elements().mcnp())
print(hea4.expand_elements().mcnp())

