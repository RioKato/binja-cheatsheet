all: overview.png mlil.png mlilssa.png

overview.png: overview.gv
	dot -T png $< -o $@

mlil.png: mlil.gv
	dot -T png $< -o $@

mlilssa.png: mlilssa.gv
	dot -T png $< -o $@
