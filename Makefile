all: overview.png mlil.png mlilssa.png commonil_call.png commonil_insn.png

overview.png: overview.gv
	dot -T png $< -o $@

mlil.png: mlil.gv
	dot -T png $< -o $@

mlilssa.png: mlilssa.gv
	dot -T png $< -o $@

commonil_call.png: commonil_call.gv
	dot -T png $< -o $@

commonil_insn.png: commonil_insn.gv
	dot -T png $< -o $@
