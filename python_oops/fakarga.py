def get_data(engine,*queries,**proprtties):
	print engine,queries,proprtties
get_data('google','python',"flask","Django",limit=10,verbose=True)
