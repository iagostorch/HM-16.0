import os
qp=22
for row in xrange(1,17):
	for column in xrange(4,30):
		cmd = "./TAppEncoderStatic -c ../cfg/encoder_lowdelay_main.cfg -c ../cfg/per-sequence/BasketballDrive.cfg --TileUniformSpacing=0 --NumTileColumnsMinus1=1 --NumTileRowsMinus1=1 --TileColumnWidthArray=" + str(column) + " --TileRowHeightArray=" + str(row) +" --FramesToBeEncoded=2 --QP=" + str(qp)
		print cmd
		#os.system(cmd)

qp=27
for row in xrange(1,17):
	for column in xrange(4,30):
		cmd = "./TAppEncoderStatic -c ../cfg/encoder_lowdelay_main.cfg -c ../cfg/per-sequence/BasketballDrive.cfg --TileUniformSpacing=0 --NumTileColumnsMinus1=1 --NumTileRowsMinus1=1 --TileColumnWidthArray=" + str(column) + " --TileRowHeightArray=" + str(row) +" --FramesToBeEncoded=2 --QP="+str(qp)
		print cmd
		#os.system(cmd)

qp=32
for row in xrange(1,17):
	for column in xrange(4,30):
		cmd = "./TAppEncoderStatic -c ../cfg/encoder_lowdelay_main.cfg -c ../cfg/per-sequence/BasketballDrive.cfg --TileUniformSpacing=0 --NumTileColumnsMinus1=1 --NumTileRowsMinus1=1 --TileColumnWidthArray=" + str(column) + " --TileRowHeightArray=" + str(row) +" --FramesToBeEncoded=2 --QP="+str(qp)
		print cmd
		#os.system(cmd)

qp=37
for row in xrange(1,17):
	for column in xrange(4,30):
		cmd = "./TAppEncoderStatic -c ../cfg/encoder_lowdelay_main.cfg -c ../cfg/per-sequence/BasketballDrive.cfg --TileUniformSpacing=0 --NumTileColumnsMinus1=1 --NumTileRowsMinus1=1 --TileColumnWidthArray=" + str(column) + " --TileRowHeightArray=" + str(row) +" --FramesToBeEncoded=2 --QP="+str(qp)
		print cmd
		#os.system(cmd)

