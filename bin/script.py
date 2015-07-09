import os
qps=[22, 27, 32, 37]

for qp in qps:
	for row in xrange(1,17):
		for column in xrange(4,30):
			cmd = "./TAppEncoderStatic -c ../cfg/encoder_lowdelay_main.cfg -c ../cfg/per-sequence/BasketballDrive.cfg --TileUniformSpacing=0 --NumTileColumnsMinus1=1 --NumTileRowsMinus1=1 --TileColumnWidthArray=" + str(column) + " --TileRowHeightArray=" + str(row) +" --FramesToBeEncoded=2 --QP=" + str(qp) + "--InputFile=/home/iagostorch/CIC2015/BasketballDrive_1920x1080_50.yuv"
			print cmd
			os.system(cmd)

