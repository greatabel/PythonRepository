#-*- coding: utf-8 -*-
from  vec import Vec


D = {'metal','concrete','plastic','water','electricity'}
v_gnome = Vec(D,{'concrete':1.3,'plastic':.2,'water':.8,'electricity':.4})
v_hoop = Vec(D, {'plastic':1.5, 'water':.4, 'electricity':.3})
v_slinky = Vec(D, {'metal':.25, 'water':.2, 'electricity':.7})
v_putty = Vec(D, {'plastic':.3, 'water':.7, 'electricity':.5})
v_shooter = Vec(D, {'metal':.15, 'plastic':.5, 'water':.4,'electricity':.8})

print(240*v_gnome + 55*v_hoop + 150*v_slinky + 133*v_putty + 90*v_shooter)