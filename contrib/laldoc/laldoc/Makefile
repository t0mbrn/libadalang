run:
	#RST generation (IMPORTANT: give all files)
	python3 generate_rst.py -P ../../../../muen/components/libmuchannel/libmuchannel.gpr \
	../../../../muen/components/libmuchannel/src/muchannel.ads \
	../../../../muen/components/libmuchannel/src/muchannel_constants.ads \
	../../../../muen/components/libmuchannel/src/muchannel-writer.ads \
	../../../../muen/components/libmuchannel/src/muchannel-readers.ads \
	../../../../muen/components/libmuchannel/src/minstance-read.ads \
	../../../../muen/components/libmuchannel/src/minstance-write.ads \
	../../../../muen/components/libmuchannel/src/minstance.ads \
	-O ../../../../out/muchannel/rst/

	# HTML
	# Colleting RSTs for TOC in index.rst
	python3 collectRSTs.py -P ../../../../out/muchannel/rst/

	#HTML generation
	sphinx-build -b html ../../../../ ../../../../out/muchannel/html